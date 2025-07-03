import openai
import speech_recognition as sr
import pygame
import csv
import os
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 🔐 OpenAI API anahtarını buraya yaz
client = openai.OpenAI(api_key="⚠️ API Key Not Included
For security reasons, the OpenAI API key has been removed from the source code.
To run the application, please insert your own key in the appropriate location in the script.")

# 🔑 Google Calendar izin kapsamı
SCOPES = ['https://www.googleapis.com/auth/calendar']

def speak(text):
    print("🔊 Generating voice reply...")
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=text
        )

        filename = "reply.mp3"
        with open(filename, "wb") as f:
            f.write(response.content)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

    except Exception as e:
        print(f"TTS Error: {e}")

def record_and_transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=10)

    print("🔁 Converting to text using Whisper API...")

    try:
        with open("temp.wav", "wb") as f:
            f.write(audio.get_wav_data())

        with open("temp.wav", "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )

        print("✅ Transcription:", transcription.text)
        return transcription.text

    except Exception as e:
        print(f"Transcription Error: {e}")
        return None

def log_call(user_input, gpt_response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("call_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, user_input, gpt_response])

def create_calendar_event(summary, date_str, time_str, duration_minutes=30):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    start_datetime = datetime.datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    end_datetime = start_datetime + datetime.timedelta(minutes=duration_minutes)

    event = {
        'summary': summary,
        'start': {
            'dateTime': start_datetime.isoformat(),
            'timeZone': 'Europe/London',
        },
        'end': {
            'dateTime': end_datetime.isoformat(),
            'timeZone': 'Europe/London',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"📅 Appointment created: {event.get('htmlLink')}")

def check_and_create_appointment(user_input):
    print("📘 Checking if it's an appointment...")
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=200,
            messages=[
                {"role": "system", "content": "If user input contains appointment info, reply in format: yes|summary text|YYYY-MM-DD|HH:MM. If not, reply: no."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content.strip()
        print("📘 GPT Appointment Check:", reply)

        if reply.lower().startswith("yes|"):
            _, summary, date_str, time_str = reply.split("|")
            create_calendar_event(summary.strip(), date_str.strip(), time_str.strip())
        else:
            print("🟡 No appointment found in message.")

    except Exception as e:
        print(f"Appointment parse error: {e}")

def ask_gpt(text):
    print("🤖 Asking GPT-4o...")
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=200,
            messages=[
                {"role": "system", "content": "You are a helpful and polite receptionist AI for a medical clinic. Keep replies short and clear."},
                {"role": "user", "content": text}
            ]
        )
        reply = response.choices[0].message.content
        print("🧠 GPT-4o says:", reply)
        speak(reply)
        log_call(text, reply)
        check_and_create_appointment(text)
        return reply

    except Exception as e:
        print(f"GPT Error: {e}")
        return None

if __name__ == "__main__":
    transcribed_text = record_and_transcribe()
    if transcribed_text:
        ask_gpt(transcribed_text)
