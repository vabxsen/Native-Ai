# README.md


# 🎙️ Native AI

A modern desktop voice assistant built with Python, featuring speech recognition, text-to-speech, system monitoring, Claude AI integration, and a sleek Tkinter-based GUI.

---

# ✨ Preview

Native AI is a lightweight personal assistant capable of:

- 🎤 Voice interaction
- 🌐 Opening websites
- 🔎 Searching Google
- 📚 Wikipedia summaries
- 💻 System monitoring
- 🤖 AI-powered responses using Claude
- 🔊 Speech output with natural voice feedback

Built using Python 3.12 and designed with a clean cyber-style desktop interface.

---

# 🚀 Features

## 🎙️ Voice Recognition
- Real-time microphone input
- Speech-to-text using Google Speech Recognition
- Ambient noise adjustment
- Automatic listening status indicators

---

## 🔊 Text-to-Speech
- Natural voice responses using `pyttsx3`
- Fast local speech synthesis
- Offline TTS support

---

## 🤖 Claude AI Integration
- Uses Anthropic Claude API as an intelligent fallback
- Conversational responses
- Lightweight AI assistant behavior

---

## 💻 System Monitoring

Check:
- ⚡ CPU usage
- 🧠 RAM usage
- 💾 Disk space
- 🖥️ Operating system information

---

## 🧠 Smart Commands

Supports commands like:


Time
Date
Day
Open youtube
Open github
Search artificial intelligence
Wikipedia python programming
System info
Cpu usage
Disk space
Joke
Calculator



## 🖥️ Modern Desktop GUI
- 🌑 Dark-themed interface
- 📜 Live command logs
- 📡 Status indicators
- ⌨️ Keyboard shortcuts
- ⚙️ Multithreaded listening system

---

# 🛠️ Technologies Used

- 🐍 Python 3.12
- 🪟 Tkinter
- 🔊 pyttsx3
- 🎤 SpeechRecognition
- 📚 Wikipedia API
- 🤖 Anthropic Claude API
- 💻 psutil
- 🌐 requests

---

# 📦 Installation

## 1️⃣ Clone the Repository

~~
git clone https://github.com/vabxsen/Native-Ai.git
cd Native-Ai
~~

---

## 2️⃣ Install Dependencies

``
pip install pyttsx3 SpeechRecognition wikipedia requests psutil pyaudio

``

---

# 🎧 PyAudio Installation (Windows)

If PyAudio fails to install:

## ✅ Option 1 — Recommended

Download the correct `.whl` file for your Python version from:

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

Then install:

```bash
pip install PyAudio-<version>.whl
```

---

## ⚡ Option 2

```bash
pip install pipwin
pipwin install pyaudio
```

---

# 🔑 Claude API Setup

Open the source file and replace:

```python
ANTHROPIC_API_KEY = "YOUR_API_KEY_HERE"
```

with your actual API key:

```python
ANTHROPIC_API_KEY = "sk-ant-xxxxxxxx"
```

Get your API key from:

https://console.anthropic.com/

---

# ▶️ Run the Assistant

```bash
python Native_Ai.py
```

---

# 📁 Project Structure

```bash
Native-Ai/
│
├── Native_Ai.py
├── README.md
└── requirements.txt
```

---

# ⌨️ Keyboard Shortcuts

| Key | Action |
|------|---------|
| Space | 🎤 Start Listening |

---

# 🔮 Future Improvements

Planned upgrades:

- 🎧 Wake word detection
- 🧠 Offline AI mode
- 🖱️ Custom desktop automation
- 📂 File management commands
- 🎵 Spotify and Discord control
- 🧬 AI memory system
- 🤖 Better NLP intent detection
- 🌦️ Weather integration
- 📱 Mobile companion app

---

# 🔒 Security Note

⚠️ Never upload your real API keys publicly.

For production projects, use environment variables instead of hardcoded keys.

Example:

```python
import os

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
```

---

# 👨‍💻 Author

Developed by **Vaibhav Sen**

### 🌐 GitHub
https://github.com/vabxsen

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 🤝 Contributing

Pull requests and feature suggestions are welcome.

If you'd like to improve Native AI, feel free to fork the repository and submit a PR.

---

# 📸 Screenshots

Add screenshots of the GUI here.

Example:

Markdown

<img src="[https://github.com/user-attachments/assets/1367098e-49b4-4e94-8bf2-2b8cf1455648](https://github.com/user-attachments/assets/1367098e-49b4-4e94-8bf2-2b8cf1455648)" width="920" alt="Native AI Screenshot">



---

# ⭐ Support the Project

If you found this project useful, consider giving the repository a star on GitHub.

It helps the project grow and motivates future development 🚀
````
