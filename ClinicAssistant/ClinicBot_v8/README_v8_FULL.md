# 🧠 Clinic Assistant v8 – Plug-and-Play Voice Modem Integration

This is version 8 of the AI-powered voice assistant for healthcare clinics, designed for plug-and-play use with landline phone systems. It automatically detects and answers incoming landline calls using a USB voice modem, then launches a natural AI conversation to handle appointment bookings via Google Calendar.

---

## 🚀 What’s New in v8

- ☎️ **Plug-and-Play USB Voice Modem Support**
- 🔔 Automatically detects incoming landline calls (via modem)
- 🧠 Launches AI assistant automatically when call is detected
- 🧠 GPT-4o with persistent memory and contextual conversation
- 🗣️ Text-to-Speech (Nova voice) playback via ffplay
- 🗖️ Automatic appointment creation with Google Calendar
- ✅ Fully standalone executable option (`call_listener.exe`)

---

## ⚙️ Tech Stack

- Python
- OpenAI Whisper, GPT-4o, TTS
- Google Calendar API
- `SpeechRecognition`
- `subprocess` + `ffplay`
- `pyserial` (for USB modem communication)

---

## 📂 File Structure

```
ClinicBot_v8/
├── call_listener.py             # NEW: Listens to USB voice modem
├── call_listener.exe            # Executable version (optional)
├── clinic_assistant_v7.py       # Main AI assistant logic
├── appointments.csv             # Appointment logs (optional)
├── credentials.json / token.json # Google API credentials
├── voice.mp3                    # Sample voice reply
├── README.txt                   # Installation instructions
```

---

## 🧠 How It Works

1. `call_listener.py` listens to the USB modem on available COM ports
2. When an incoming call is detected (RING), it sends `ATA` to answer
3. Automatically launches `clinic_assistant_v7.py`
4. The assistant greets the caller and records their voice
5. GPT-4o replies with natural, step-by-step prompts
6. Extracts name, date, and time → books on Google Calendar
7. Ends the session with a polite voice confirmation

---

## 💬 Sample Conversation

> 👤 **User**: Hi, I’d like to book a PRP appointment.  
> 🤖 **Assistant**: Sure, may I have your full name?  
> 👤 **User**: Jack Barn  
> 🤖 **Assistant**: Thank you Jack. What day and time works best for you?  
> 👤 **User**: Wednesday at 3 PM  
> 🤖 **Assistant**: Great, I’ve booked your appointment for Wednesday at 3 PM. Goodbye!

---

## 🔀 Key Code Snippets

### 🔌 Call Listener Script (Modem integration)
```python
import serial
...
if "RING" in line:
    ser.write(b'ATA\r')  # Answer
    subprocess.Popen(["python", "clinic_assistant_v7.py"])
```

### 🧠 GPT-4o Conversation
```python
def ask_gpt(prompt):
    chat_history.append({"role": "user", "content": prompt})
    ...
```

### 📤 Detail Extraction
```python
# Extract name, date, and time from conversation context
```

### 🗖️ Calendar Integration
```python
# Uses Google Calendar API to schedule 30-minute appointment
```

### 🔊 Text-to-Speech
```python
# Converts GPT response to voice and plays with ffplay
```

---

## 🗼 Screenshots

| Call Detected | Conversation | Calendar Event | Final Voice |
|---------------|--------------|----------------|--------------|
| ![](screenshots/v8_call.png) | ![](screenshots/v8_conversation.png) | ![](screenshots/v8_calendar.png) | ![](screenshots/v8_voice.png) |

> 📝 Add screenshots in `screenshots/` folder with matching names

---

## 🎥 Demo Video

[▶️ Watch the live demo](https://drive.google.com/file/d/1fSnoXweF3DPscOMT_REZauueIymp6N_P/view?usp=sharing)

---

## 📌 Notes

- Requires `ffplay` to be installed and accessible from command line
- Fully compatible with Windows 10+ systems
- Tested with Hiro H50113 USB Voice Modem
- AI features depend on stable internet connection
- Designed for use in UK-based clinics

