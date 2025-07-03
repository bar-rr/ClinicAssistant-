import openai
import speech_recognition as sr
import pygame
import csv
import os
import pandas as pd
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

# OpenAI setup
client = openai.OpenAI(api_key=" Note: For security purposes, API keys have been removed from the uploaded .py files.")  # Replace with your real key

# Calendar setup
SCOPES = ['https://www.googleapis.com/auth/calendar']
calendar_id = 'primary'

def get_calendar_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)

def speak(text):
    print("🔊 Generating voice with OpenAI TTS...")
    try:
        response = client.audio.speech.create(model="tts-1", voice="nova", input=text)
        with open("reply.mp3", "wb") as f:
            f.write(response.content)
        pygame.mixer.init()
        pygame.mixer.music.load("reply.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"TTS Error: {e}")

def record_and_transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now... (you have 7 seconds to start talking)")
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=7)
    try:
        with open("temp.wav", "wb") as f:
            f.write(audio.get_wav_data())
        with open("temp.wav", "rb") as audio_file:
            transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
        print("✅ Transcription:", transcription.text)
        return transcription.text
    except Exception as e:
        print(f"❌ Transcription Error: {e}")
        return None

def record_name():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("👤 Please say your full name...")
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=5)
    try:
        with open("temp_name.wav", "wb") as f:
            f.write(audio.get_wav_data())
        with open("temp_name.wav", "rb") as audio_file:
            transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file, language="en")
        name_raw = transcription.text.strip()
        print("📝 Name Transcription:", name_raw)

        # Confirm with GPT
        confirmation = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Extract only the person's full name from the sentence."},
                {"role": "user", "content": name_raw}
            ]
        )
        name_clean = confirmation.choices[0].message.content.strip()
        return name_clean
    except Exception as e:
        print(f"❌ Name Transcription Error: {e}")
        return "Unknown"

def create_appointment(summary="General Appointment"):
    try:
        service = get_calendar_service()
        start = datetime.now() + timedelta(days=2)
        end = start + timedelta(minutes=30)
        event = {
            'summary': summary,
            'start': {'dateTime': start.isoformat(), 'timeZone': 'Europe/London'},
            'end': {'dateTime': end.isoformat(), 'timeZone': 'Europe/London'}
        }
        created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
        print("✅ Appointment created:", created_event.get('htmlLink'))
    except Exception as e:
        print(f"❌ Appointment Creation Error: {e}")

def update_latest_appointment(summary="Updated Appointment"):
    try:
        service = get_calendar_service()
        events_result = service.events().list(calendarId=calendar_id, maxResults=1, orderBy='startTime', singleEvents=True).execute()
        events = events_result.get('items', [])
        if events:
            event = events[0]
            event['summary'] = summary
            updated_event = service.events().update(calendarId=calendar_id, eventId=event['id'], body=event).execute()
            print("✏️ Appointment updated:", updated_event.get('htmlLink'))
    except Exception as e:
        print(f"❌ Update Error: {e}")

def cancel_latest_appointment():
    try:
        service = get_calendar_service()
        events_result = service.events().list(calendarId=calendar_id, maxResults=1, orderBy='startTime', singleEvents=True).execute()
        events = events_result.get('items', [])
        if events:
            service.events().delete(calendarId=calendar_id, eventId=events[0]['id']).execute()
            print("❌ Latest appointment cancelled.")
    except Exception as e:
        print(f"❌ Cancellation Error: {e}")

def save_appointment_info(user_input):
    print("📋 Checking for appointment intent...")
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": (
                    "You are a classification assistant. Based on the user input, classify the intent strictly into one of the following:\n"
                    "- booking\n- reschedule\n- cancel\n- info\n- wrong_call\nReply with only the category label."
                )},
                {"role": "user", "content": user_input}
            ]
        )
        intent = response.choices[0].message.content.strip().lower()
        print(f"🧠 Detected intent: {intent}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if intent == "booking":
            create_appointment(user_input)
            with open("appointments.csv", mode="a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, user_input, "NEW"])

        elif intent == "reschedule":
            update_latest_appointment(user_input)

        elif intent == "cancel":
            cancel_latest_appointment()

        elif intent == "info":
            speak("Thanks for your interest. May I have your full name so our team can follow up with you?")
            name = record_name()
            with open("followup_requests.csv", mode="a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, user_input, name])
            speak("Thank you. I’ve noted your request. One of our team members will contact you shortly.")

        elif intent == "wrong_call":
            with open("wrong_calls.csv", mode="a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, user_input])
            speak("This is My Health and Wellbeing Clinic, a private clinic in Whitechapel London. It seems this might be the wrong number. Thank you.")

        else:
            print("⚠️ Unknown intent.")
    except Exception as e:
        print(f"❌ Appointment Detection Error: {e}")

def log_call(user_input, response):
    with open("call_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input, response])

def ask_gpt(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=200,
            messages=[
                {"role": "system", "content": "You are a helpful assistant at a private clinic. Keep replies short."},
                {"role": "user", "content": text}
            ]
        )
        reply = response.choices[0].message.content
        print("🧠 GPT-4o says:", reply)
        speak(reply)
        log_call(text, reply)
        return reply
    except Exception as e:
        print(f"❌ GPT Error: {e}")
        return None

if __name__ == "__main__":
    speak("Hi, this is My Health and Wellbeing Clinic, a private medical center in Whitechapel London. How can I help you?")
    transcribed = record_and_transcribe()
    if transcribed:
        save_appointment_info(transcribed)
