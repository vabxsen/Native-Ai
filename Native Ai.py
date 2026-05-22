
# External Libraries / Modules -

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import threading
import tkinter as tk
from tkinter import scrolledtext
import requests
import platform
import psutil

# ─── CONFIG ───────────────────────────────────────────────────────────────────

ANTHROPIC_API_KEY = "YOUR_API_KEY_HERE"  # Replace with your key
ASSISTANT_NAME = "Native AI"

# ─── TTS ENGINE (initialized once) ────────────────────────────────────────────

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 185)

def speak(audio):
    log(f"🔊 {audio}")
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        log(f"[TTS Error] {e}")

# ─── GUI SETUP ────────────────────────────────────────────────────────────────

root = tk.Tk()
root.title("Native AI Assistant")
root.geometry("620x540")
root.configure(bg="#0f0f0f")
root.resizable(False, False)

# Header
header = tk.Label(root, text="🎙️  NATIVE AI", font=("Courier New", 22, "bold"),
                  bg="#0f0f0f", fg="#00ff88")
header.pack(pady=(18, 2))

subtitle = tk.Label(root, text="Voice Assistant  •  Python 3.12  •  Tkinter GUI",
                    font=("Courier New", 8), bg="#0f0f0f", fg="#333333")
subtitle.pack()

# Status indicator
status_var = tk.StringVar(value="● IDLE")
status_label = tk.Label(root, textvariable=status_var, font=("Courier New", 10),
                        bg="#0f0f0f", fg="#555555")
status_label.pack(pady=(4, 0))

# Log window
log_area = scrolledtext.ScrolledText(root, width=72, height=18,
                                     bg="#1a1a1a", fg="#cccccc",
                                     font=("Courier New", 10),
                                     insertbackground="white",
                                     borderwidth=0, relief="flat",
                                     wrap=tk.WORD)
log_area.pack(padx=20, pady=10)
log_area.config(state=tk.DISABLED)

# Buttons
btn_frame = tk.Frame(root, bg="#0f0f0f")
btn_frame.pack(pady=6)

def make_btn(parent, text, command, color="#00ff88"):
    return tk.Button(parent, text=text, command=command,
                     bg="#1a1a1a", fg=color,
                     font=("Courier New", 10, "bold"),
                     relief="flat", padx=15, pady=7,
                     activebackground="#2a2a2a", activeforeground=color,
                     cursor="hand2")

def log(message):
    log_area.config(state=tk.NORMAL)
    log_area.insert(tk.END, message + "\n")
    log_area.see(tk.END)
    log_area.config(state=tk.DISABLED)

def set_status(text, color="#00ff88"):
    status_var.set(f"● {text}")
    status_label.config(fg=color)

# ─── VOICE INPUT ──────────────────────────────────────────────────────────────

def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True
    with sr.Microphone() as source:
        set_status("LISTENING...", "#ffaa00")
        log("🎤 Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=7, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            set_status("IDLE", "#555555")
            log("⚠️  Timeout — no input detected.")
            return "none"
    try:
        set_status("RECOGNIZING...", "#00aaff")
        query = r.recognize_google(audio, language='en-in')
        log(f"🗣️  You said: {query}")
        set_status("PROCESSING...", "#aa00ff")
        return query.lower()
    except sr.UnknownValueError:
        log("⚠️  Could not understand. Try again.")
        set_status("IDLE", "#555555")
        return "none"
    except sr.RequestError:
        log("❌  Network error during recognition.")
        set_status("IDLE", "#555555")
        return "none"

# ─── CLAUDE API FALLBACK ──────────────────────────────────────────────────────

def ask_claude(query):
    if ANTHROPIC_API_KEY == "YOUR_API_KEY_HERE":
        return "Claude API key not configured. Please add your API key to use this feature."
    log("🤖 Asking Claude AI...")
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 200,
                "system": "You are a helpful voice assistant. Give SHORT answers — 2-3 sentences max. No markdown, no bullet points. Plain conversational text only.",
                "messages": [{"role": "user", "content": query}]
            },
            timeout=10
        )
        data = response.json()
        if response.status_code != 200:
            return f"API error {response.status_code}: {data.get('error', {}).get('message', 'Unknown error')}"
        return data["content"][0]["text"].strip()
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except Exception as e:
        return f"Could not reach Claude. Error: {str(e)}"

# ─── SYSTEM INFO ──────────────────────────────────────────────────────────────

def get_system_info():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    ram_used = round(ram.used / (1024**3), 1)
    ram_total = round(ram.total / (1024**3), 1)
    disk = psutil.disk_usage('/')
    disk_free = round(disk.free / (1024**3), 1)
    os_name = platform.system() + " " + platform.release()
    return (f"OS: {os_name}. CPU usage: {cpu}%. "
            f"RAM: {ram_used} GB used out of {ram_total} GB. "
            f"Free disk space: {disk_free} GB.")

# ─── COMMAND DISPATCH ─────────────────────────────────────────────────────────

WEBSITE_COMMANDS = {
    "youtube":    "https://youtube.com",
    "google":     "https://google.com",
    "spotify":    "https://spotify.com",
    "amazon":     "https://amazon.in",
    "instagram":  "https://instagram.com",
    "steam":      "https://store.steampowered.com",
    "github":     "https://github.com",
    "netflix":    "https://netflix.com",
    "twitter":    "https://twitter.com",
    "reddit":     "https://reddit.com",
    "whatsapp":   "https://web.whatsapp.com",
    "linkedin":   "https://linkedin.com",
    "chatgpt":    "https://chat.openai.com",
}

# Keywords that must match as whole words to avoid substring bugs (e.g. "ram" inside "instagram")
SYSTEM_INFO_TRIGGERS = ["system info", "system status", "cpu usage", "ram usage",
                        "memory usage", "check memory", "check cpu", "disk space"]

def handle_command(query):
    if query == "none":
        return

    # Exit
    if any(w in query for w in ["exit", "close", "stop", "bye", "goodbye", "shut down"]):
        speak("Goodbye! Have a great day.")
        root.after(1500, root.destroy)
        return

    # Time
    if "time" in query and "wikipedia" not in query:
        t = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {t}")
        return

    # Date
    if "date" in query and "wikipedia" not in query:
        d = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {d}")
        return

    # Day of week
    if "day" in query and "wikipedia" not in query:
        day = datetime.datetime.now().strftime("%A")
        speak(f"Today is {day}")
        return

    # Wikipedia — check before system info to avoid substring conflicts
    if "wikipedia" in query:
        topic = query.replace("wikipedia", "").strip()
        if not topic:
            speak("Please tell me what to search on Wikipedia.")
            return
        speak(f"Searching Wikipedia for {topic}...")
        try:
            result = wikipedia.summary(topic, sentences=2)
            log(f"📖 {result}")
            speak("According to Wikipedia, " + result[:300])
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Multiple results found. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak(f"Sorry, I couldn't find anything about {topic} on Wikipedia.")
        return

    # System info — use full phrase matching to avoid "ram" inside "instagram"
    if any(trigger in query for trigger in SYSTEM_INFO_TRIGGERS):
        info = get_system_info()
        log(f"💻 {info}")
        speak(info)
        return

    # Joke
    if "joke" in query:
        try:
            r = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
            joke = r.json()
            text = f"{joke['setup']} ... {joke['punchline']}"
            log(f"😄 {text}")
            speak(text)
        except:
            speak("Why don't scientists trust atoms? Because they make up everything!")
        return

    # Calculator — simple math
    if any(w in query for w in ["calculate", "what is", "how much is"]):
        math_query = query.replace("calculate", "").replace("what is", "").replace("how much is", "").strip()
        try:
            # Only evaluate if it looks like a math expression
            if any(op in math_query for op in ["+", "-", "x", "times", "divided", "/"]):
                math_query = math_query.replace("x", "*").replace("times", "*").replace("divided by", "/")
                result = eval(math_query)
                speak(f"The answer is {result}")
                return
        except:
            pass  # Fall through to Claude

    # Open websites — full word matching to avoid substring issues
    if "open" in query:
        matched = False
        for site, url in WEBSITE_COMMANDS.items():
            # Match site name as a whole word
            words = query.split()
            if site in words or any(site in w for w in words):
                speak(f"Opening {site}")
                webbrowser.open(url)
                matched = True
                break
        if not matched:
            speak("Sorry, I don't have that website. Try saying 'open YouTube' or 'open GitHub'.")
        return

    # Search Google by voice
    if "search" in query:
        search_term = query.replace("search", "").strip()
        if search_term:
            speak(f"Searching Google for {search_term}")
            webbrowser.open(f"https://google.com/search?q={search_term.replace(' ', '+')}")
        return

    # Claude fallback for everything else
    answer = ask_claude(query)
    log(f"🤖 Claude: {answer}")
    speak(answer)

# ─── LISTEN LOOP ──────────────────────────────────────────────────────────────

def listen_once():
    query = takeCommand()
    handle_command(query)
    set_status("IDLE", "#555555")

def start_listening():
    threading.Thread(target=listen_once, daemon=True).start()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    speak(f"{greeting}! I am {ASSISTANT_NAME}, your personal voice assistant. "
          f"Press the Listen button or hit Space to give me a command.")

# ─── BUTTON WIRING ────────────────────────────────────────────────────────────

listen_btn = make_btn(btn_frame, "🎤  LISTEN", start_listening, "#00ff88")
listen_btn.pack(side=tk.LEFT, padx=8)

clear_btn = make_btn(btn_frame, "🗑  CLEAR", lambda: (
    log_area.config(state=tk.NORMAL),
    log_area.delete(1.0, tk.END),
    log_area.config(state=tk.DISABLED)
), "#555555")
clear_btn.pack(side=tk.LEFT, padx=8)

quit_btn = make_btn(btn_frame, "✕  QUIT", root.destroy, "#ff4444")
quit_btn.pack(side=tk.LEFT, padx=8)

# Keyboard shortcut
root.bind("<space>", lambda e: start_listening())

# ─── LAUNCH ───────────────────────────────────────────────────────────────────

log(f"{'─'*60}")
log(f"  {ASSISTANT_NAME} — Initialized")
log(f"  Commands:")
log(f"    • time / date / day")
log(f"    • open <site>  (youtube, github, spotify...)")
log(f"    • search <anything>")
log(f"    • wikipedia <topic>")
log(f"    • system info / cpu usage / disk space")
log(f"    • joke")
log(f"    • calculate <expression>")
log(f"    • ask anything  →  Claude AI fallback")
log(f"{'─'*60}")

threading.Thread(target=greet, daemon=True).start()
root.mainloop()



# -------------------------------------------------------
# Thank you for using this voice assistant!
# Created with passion and Python by Vaibhav Sen.
# -------------------------------------------------------
