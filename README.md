# 🎙️ Voice-Controlled AI Desktop Assistant (Python)

A Python-based voice-controlled AI assistant that performs real-time speech recognition and responds using text-to-speech. The assistant can search Wikipedia, open popular websites, tell the current time, and execute system tasks through natural voice commands. This project demonstrates practical implementation of speech processing, automation, and human-computer interaction.

---

## 🚀 Features

- 🎤 Real-time voice command recognition
- 🔊 Text-to-speech audio responses
- 🌐 Wikipedia search with spoken summary
- ⏰ Time announcement
- 🌍 Open websites via voice commands
- 🎵 Quick access to Spotify, YouTube, Google, Amazon, Instagram, Steam
- 🧠 Error handling for unclear speech or network issues
- 🖥️ Continuous assistant loop until exit command

---

## 🛠️ Technologies Used

- Python 3
- `pyttsx3` — offline text-to-speech engine
- `SpeechRecognition` — voice input processing
- `wikipedia` — information retrieval API
- `datetime` — system time handling
- `webbrowser` — browser automation

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/voice-ai-assistant.git
cd voice-ai-assistant
```

### 2. Install dependencies
```bash
pip install pyttsx3 SpeechRecognition wikipedia pyaudio
```

> Note: If PyAudio installation fails:
- Windows: install precompiled wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
- Then run:
```bash
pip install PyAudio-filename.whl
```

---

## ▶️ Usage

Run the assistant:

```bash
python assistant.py
```

Speak commands such as:

- “Wikipedia Albert Einstein”
- “Open YouTube”
- “Open Google”
- “What is the time?”
- “Open Spotify”
- “Exit”

The assistant will continue listening until you say **exit**, **close**, or **stop**.

---

## 🧠 How It Works

1. Microphone captures voice input
2. SpeechRecognition converts audio → text
3. Assistant processes the command
4. pyttsx3 converts response → speech
5. Program executes requested action

This loop runs continuously for real-time interaction.

---

## 🌍 Practical Applications

- Accessibility tools for visually impaired users
- Hands-free productivity assistant
- Smart home control prototype
- Voice-based kiosk systems
- Educational AI projects
- Automation assistant for everyday tasks

---

## 🔮 Future Improvements

- Add AI chatbot integration (LLMs)
- Voice authentication
- Desktop app launcher
- Weather/news API integration
- Smart home IoT control
- GUI interface
- Multi-language support
- Wake-word detection

---

## 📌 Learning Outcomes

This project helped develop skills in:

- Speech processing
- API integration
- Python automation
- Error handling
- Human-computer interaction
- Real-time system design

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Vaibhav Sen  
GitHub: https://github.com/vabxsen

---

⭐ If you like this project, consider giving it a star!
