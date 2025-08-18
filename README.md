# Clinic Assistant – AI Voice Receptionist  
[![Build](https://img.shields.io/github/actions/workflow/status/bar-rr/ClinicAssistant-/ci.yml)](../../actions)
[![Release](https://img.shields.io/github/v/release/bar-rr/ClinicAssistant-)](../../releases)
[![License](https://img.shields.io/github/license/bar-rr/ClinicAssistant-)](LICENSE)
![Issues](https://img.shields.io/github/issues/bar-rr/ClinicAssistant-)

> **One-man unicorn project**: An AI-powered call assistant that answers clinic phones, books/reschedules appointments via Google Calendar, and speaks naturally with patients.  
> Built in Python, extended to Android & USB modem integration.

![Social Preview]<img width="1280" height="640" alt="social_preview_white_signature" src="https://github.com/user-attachments/assets/b7ea6898-8a20-4945-8272-05b4839b9933" />


---

## 🚀 Overview
The **Clinic Assistant** is a plug-and-play voice receptionist for healthcare clinics.  
It connects to landline phones (via USB voice modem) or mobile devices and handles:

- Answering calls  
- Understanding appointment requests (book / reschedule / cancel)  
- Confirming details in natural speech  
- Creating Google Calendar events automatically  

Designed to run **fully offline on a clinic PC** (no cloud hosting required).

---

## ✨ Features
- 🎤 **Speech I/O**: Whisper speech-to-text + Nova TTS voice replies  
- 🧠 **GPT-4o intent recognition** with multi-turn memory  
- 📅 **Google Calendar integration** for scheduling  
- ☎️ **USB voice modem plug-and-play** (v8)  
- 📟 **Executable mode** (`call_listener.exe`) for Windows  
- 📊 **CSV logs** for human follow-up  
- 📱 **Android beta** for mobile reception  

---

## 📂 Versions
Each version is documented in its own folder:

- [ClinicBot_v1](./ClinicAssistant/ClinicBot_v1/) – first prototype (voice → calendar) – first prototype (voice → calendar)  
- [ClinicBot_v2](./ClinicAssistant/ClinicBot_v2/) – natural conversation + rescheduling  
- [ClinicBot_v7](./ClinicAssistant/ClinicBot_v7/) – full confirmation loop, professional demo  
- [ClinicBot_v8](./ClinicAssistant/ClinicBot_v8/) – USB modem plug-and-play  

---

## ⚡ Quick Start

### Python (v7/v8)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python clinic_assistant_v7.py


Android (beta)

Install Android Studio (SDK 33 or higher).

Open the /android folder as a project.

Build & run on an Android device or emulator.

For details, see /android/README.md.

🎥 Demo

📹 Watch Demo Video

📸 Screenshots available in the /screenshots folder

🛣️ Roadmap

 Finalize v8 mobile flow

 Add call recording + consent handling

 Enable multi-clinic routing support

 Build admin dashboard for appointment management

📖 Documentation

See the /docs folder for detailed documentation:

Architecture.md – high-level system design

API.md – API usage and integration notes

FAQ.md – frequently asked questions

Changelog.md – version history

🤝 Contributing

Contributions are welcome!

Please read CONTRIBUTING.md before submitting PRs.

Bug reports and feature requests → GitHub Issues.

🔒 Security

If you discover a security vulnerability, please report it responsibly.
See SECURITY.md for guidelines.

📜 License

This project is licensed under the Apache-2.0 License.
© 2025 Baris Yurttas

⭐ Acknowledgements

This project was built as a solo founder journey, with GPT acting as CTO.
Special thanks to clinicians who tested the assistant in real-world environments and provided invaluable feedback.

## Quick Start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python clinic_assistant_v7.py
