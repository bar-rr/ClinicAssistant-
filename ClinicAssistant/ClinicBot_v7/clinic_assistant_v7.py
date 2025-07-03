import openai
import speech_recognition as sr
import subprocess
import os
import csv
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# OpenAI API
client = openai.OpenAI(api_key=" Note: For security purposes, API keys have been removed from the uploaded .py files.")

# Google Calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']
calendar_id = 'primary'

# GLOBAL MEMORY
chat_history = []
user_name = None
appointment_date = None
appointment_time = None

def speak(text):
    print(f"🤖 {text}")
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=text
        )
        with open("voice.mp3", "wb") as f:
            f.write(response.content)
        subprocess.run(["ffplay", "-nodisp", "-autoexit", "voice.mp3"],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"🔊 Error in TTS: {e}")

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
    try:
        with open("temp.wav", "wb") as f:
            f.write(audio.get_wav_data())
        with open("temp.wav", "rb") as file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=file
            )
        return transcription.text.strip()
    except Exception as e:
        print(f"❌ Transcription Error: {e}")
        return ""

def get_calendar_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("calendar", "v3", credentials=creds)

def create_calendar_event(name, date_str, time_str):
    try:
        service = get_calendar_service()
        start_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        end_time = start_time + timedelta(minutes=30)
        event = {
            "summary": f"PRP Appointment - {name}",
            "start": {"dateTime": start_time.isoformat(), "timeZone": "Europe/London"},
            "end": {"dateTime": end_time.isoformat(), "timeZone": "Europe/London"},
        }
        created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
        print("✅ Appointment created:", created_event.get("htmlLink"))
        return True
    except Exception as e:
        print(f"❌ Calendar Error: {e}")
        return False

def ask_gpt(prompt):
    global chat_history
    chat_history.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": (
                "You're a helpful and friendly clinic assistant. Ask the caller for their full name, preferred date "
                "and time if not already provided. Confirm appointment once all info is available. End politely."
            )}
        ] + chat_history,
        temperature=0.4,
        max_tokens=300
    )
    reply = response.choices[0].message.content.strip()
    chat_history.append({"role": "assistant", "content": reply})
    return reply

def extract_details():
    global user_name, appointment_date, appointment_time

    latest_context = "\n".join([msg["content"] for msg in chat_history if msg["role"] == "user"])
    extract_prompt = f"""
From the following conversation, extract:
1. Full name (first + last),
2. Appointment date in YYYY-MM-DD format,
3. Appointment time in HH:MM format.

Reply in format: name|date|time

Conversation:
{latest_context}
"""

    result = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": extract_prompt}]
    ).choices[0].message.content.strip()

    if "|" in result:
        parts = result.split("|")
        if len(parts) == 3:
            user_name = parts[0].strip()
            appointment_date = parts[1].strip()
            appointment_time = parts[2].strip()

def main():
    speak("Hi, this is My Health and Wellbeing Clinic, how can I help you?")
    while True:
        user_input = record_audio()
        if not user_input:
            continue
        reply = ask_gpt(user_input)
        speak(reply)

        extract_details()
        if user_name and appointment_date and appointment_time:
            if create_calendar_event(user_name, appointment_date, appointment_time):
                speak(f"Thank you {user_name}. Your appointment has been scheduled for {appointment_date} at {appointment_time}. Goodbye.")
                break
            else:
                speak("Sorry, there was a problem scheduling your appointment.")
                break

if __name__ == "__main__":
    main()
