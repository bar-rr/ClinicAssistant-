# ClinicBot_v9 – Android + Realtime Bridge (September 2025)

This version introduces **mobile-first realtime integration** with OpenAI Realtime API, designed to run directly on Android for universal plug-and-play deployment.

## ✨ Features
- 📱 Android integration for call auto-answer & realtime voice assistant
- 🔌 WebSocket bridge for tool calls (availability, booking, reschedule, cancel)
- 🧠 GPT-4o Realtime session management with natural conversation
- 📅 Google Calendar full sync (create, update, cancel)
- 🎤 Natural speech interaction (English, en-GB tone)

## 📂 Files
- `openai-realtime-client.js` → connects to OpenAI Realtime API  
- `rt-ws-bridge.js` → forwards tool calls to calendar  
- `ws_tool_bridge_snippet.js` → handles tool definitions  
- `calendar.js` → Google Calendar helper functions  
- `.env.example` → environment config template  

## 🚀 How to Run
1. Install dependencies:
   ```bash
   npm install
   ```
2. Configure `.env` with:
   - `OPENAI_API_KEY`
   - `GOOGLE_CLIENT_EMAIL`
   - `GOOGLE_PRIVATE_KEY`
   - `CALENDAR_ID=primary`
   - `TZ=Europe/London`
3. Start bridge:
   ```bash
   node rt-ws-bridge.js
   ```
4. Start realtime client:
   ```bash
   node openai-realtime-client.js
   ```

## 📸 Demo
Screenshots available in `screenshots/`.

## 🛠️ Status
This version marks the transition to **mobile-first deployment**.  
Next steps: Android APK packaging & audio streaming integration.

---
© 2025 Baris Yurttas
