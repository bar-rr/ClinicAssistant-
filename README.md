# Clinic Assistant – AI Voice Receptionist  
[![Build](https://img.shields.io/github/actions/workflow/status/bar-rr/ClinicAssistant-/ci.yml)](../../actions)
[![Release](https://img.shields.io/github/v/release/bar-rr/ClinicAssistant-)](../../releases)
[![License](https://img.shields.io/github/license/bar-rr/ClinicAssistant-)](LICENSE)
![Issues](https://img.shields.io/github/issues/bar-rr/ClinicAssistant-)

> **One-man unicorn project**: An AI-powered call assistant that answers clinic phones, books/reschedules appointments via Google Calendar, and speaks naturally with patients.  
> Built in Python, extended to Android & USB modem integration.

![Social Preview](docs/social_preview_white_signature.png)

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

- [ClinicBot_v1](./ClinicBot_v1) – first prototype (voice → calendar)  
- [ClinicBot_v2](./ClinicBot_v2) – natural conversation + rescheduling  
- [ClinicBot_v7](./ClinicBot_v7) – full confirmation loop, professional demo  
- [ClinicBot_v8](./ClinicBot_v8) – USB modem plug-and-play  

---

## ⚡ Quick Start

### Python (v7/v8)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python clinic_assistant_v7.py



# ClinicAssistant (v8 → Mobile)
Scalable AI-powered voice assistant that automates clinic appointment handling through landline integration, enabling natural GPT-4 conversations without cloud telephony.
## Overview
Kısa özet + 1 görsel/gif.

## Features
- Landline/USB modem entegrasyonu
- Android “plug-and-play” arama karşılama
- Google Calendar entegrasyonu
- …

## Quick Start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python clinic_assistant_v7.py
