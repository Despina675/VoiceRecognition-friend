
# Voice Assistant in Python 🎙️🤖

This is a fun, voice-activated Python assistant that listens, understands, and responds to your voice commands using the power of speech recognition and text-to-speech technologies. It's like having a mini-JARVIS on your machine!
Ideal for when you get bored. It also plays my favorite song! 😇

## Features 🚀

- 🔊 Speaks back to you using `pyttsx3`
- 🎧 Listens to your voice using `SpeechRecognition`
- 🌐 Opens YouTube and searches for videos
- 🔍 Googles your queries
- 🎵 Plays a local `.wav` song
- ✌️ Plays Rock-Paper-Scissors with you
- 🤖 Opens ChatGPT
- 💻 Can (theoretically) initiate system shutdown

## How It Works 🛠️

The assistant:
1. Listens for your command.
2. Responds or acts accordingly:
   - Says back what you said
   - Asks for clarification if needed
   - Executes special voice commands like:
     - `youtube` → Search YouTube
     - `game` → Play rock-paper-scissors
     - `song` → Play "Smells Like Teen Spirit"
     - `google` or `search` → Google something
     - `open ai` → Open ChatGPT
     - `shut down` → (Mocked) shutdown command

## Requirements 📦

Make sure you have these Python packages installed:

```bash
pip install SpeechRecognition pyttsx3
```

On Windows, also ensure:
- `pyaudio` is installed properly.
- You have access to a microphone.

## Fun Commands to Try 🎮

- `"youtube"` → Voice search for videos
- `"game"` → Voice-based rock-paper-scissors
- `"google"` or `"search"` → Voice-search Google
- `"open ai"` → Opens ChatGPT in your browser
- `"song"` → Plays a preset song (make sure the WAV file exists!)
- `"shut down"` → Triggers a mocked shutdown protocol

## Notes 📝

- The voice recognition may not be perfect — if it fails to hear you, it’ll ask you to repeat.
- You can customize the wake words and actions easily in the script.
- It currently uses `recognize_google()` for voice input translation.

---

🗣️ Give it a go and feel the power of voice-controlled Python!
