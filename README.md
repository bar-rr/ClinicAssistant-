# Clinic Assistant – AI Voice Receptionist  
[![Build](https://img.shields.io/github/actions/workflow/status/bar-rr/ClinicAssistant-/ci.yml)](../../actions)
[![Release](https://img.shields.io/github/v/release/bar-rr/ClinicAssistant-)](../../releases)
[![License](https://img.shields.io/github/license/bar-rr/ClinicAssistant-)](LICENSE)
![Issues](https://img.shields.io/github/issues/bar-rr/ClinicAssistant-)

> **One-man unicorn project**: An AI-powered call assistant that answers clinic phones, books/reschedules appointments via Google Calendar, and speaks naturally with patients.  
> Built in Python, extended to Android & USB modem integration.

<img width="1280" height="640" alt="social_preview_white_signature" src="https://github.com/user-attachments/assets/b7ea6898-8a20-4945-8272-05b4839b9933" />

---

## 🚀 Overview
The **Clinic Assistant** is a plug-and-play AI receptionist for healthcare clinics.  
It connects to landline phones (via USB voice modem) or mobile devices and handles:

- Answering calls  
- Understanding appointment requests (book / reschedule / cancel)  
- Confirming details in natural speech  
- Creating Google Calendar events automatically  

Designed to run **fully offline on a clinic PC** – no cloud servers required.

---

## 🎯 Project Goal
To provide a **cost-effective, instantly deployable AI solution** that allows clinics to handle **24/7 appointment scheduling** with natural voice interaction, without needing cloud telephony or specialized IT infrastructure.

---

## ✨ Features
- 🎤 **Speech I/O**: Whisper speech-to-text + Nova TTS voice replies  
- 🧠 **GPT-4o intent recognition** with multi-turn memory  
- 📅 **Google Calendar integration** for scheduling  
- ☎️ **USB voice modem plug-and-play** (v8)  
- 📟 **Executable mode** (`call_listener.exe`) for Windows  
- 📊 **CSV logs** for receptionist follow-up  
- 📱 **Android beta** for mobile reception  

---

## 📂 Versions
Each version is documented in its own folder:

- [ClinicBot_v1](./ClinicAssistant/ClinicBot_v1/) – first prototype (voice → calendar)  
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
Android (planned)

🚧 The Android client is under development and not yet available.
It will provide a mobile version of the assistant for clinics that prefer smartphone deployment.
Stay tuned — progress will be shared in Roadmap.

🎥 Demo

📹 Watch Demo Video

📸 Screenshots available in the screenshots folder

🛣️ Roadmap

 Finalize v8 mobile flow

 Add call recording + consent handling

 Enable multi-clinic routing support

 Build admin dashboard for appointment management

📖 Documentation

Documentation is being prepared and will be added in future versions:

Architecture – high-level system design (coming soon)

API – API usage and integration notes (coming soon)

FAQ – frequently asked questions (coming soon)

Changelog – version history (coming soon)

📈 Why It Matters

No cloud telephony required – works with a basic landline and PC.

Ideal for clinics, legal offices, beauty salons, and other service providers.

Scalable, modular, and easy to deploy.

🤝 Contributing

Contributions are welcome!
Guidelines will be published soon.
Bug reports and feature requests can be shared via GitHub Issues.

🔒 Security

If you discover a security vulnerability, please report it responsibly.
A detailed security policy will be added soon.

📜 License

This project is licensed under the Apache-2.0 License.
© 2025 Baris Yurttas

⭐ Acknowledgements

This project was built as a solo founder journey, with GPT acting as CTO.
Special thanks to clinicians who tested the assistant in real-world environments and provided invaluable feedback.

☕ Support the Project

If you find this project useful, you can support my work here:
https://buymeacoffee.com/barisy
