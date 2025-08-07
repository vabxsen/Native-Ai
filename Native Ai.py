# External Libraries / Modules -

import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install SpeechRecognition
import wikipedia  #pip install wikipedia
import webbrowser

# Text-to-Speech Function Setup -

def speak(audio):
    print(f"Speaking: {audio}")
    try:
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.setProperty("rate", 190)
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speak(): {e}")

# Greeting function -

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Boy!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Boy!")
    else:
        speak("Good Evening Boy!")
    speak("I Am Your Native AI. How can I assist you?")

# Voice input / command function -

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("Timeout while listening")
            return "none"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "none"
    except sr.RequestError:
        print("Network error")
        return "none"

    return query.lower()

# Main Program Entry Point -

if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand()
# Exit Commands -
        if query == "none":
            continue

        elif "close" in query or "exit" in query or "stop" in query:
            speak("Goodbye Boy! Stopping the program.")
            break
            
# Program for  Wikipedia Search -
        
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                print(f"Wikipedia Summary: {results}")
                speak("According to Wikipedia")
                speak(results[:300])
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find anything on that topic.")
                
# Progran To Open Websites You Want -
        
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "open spotify" in query or "play music" in query:
            webbrowser.open("https://spotify.com")
        elif "open amazon" in query:
            webbrowser.open("https://amazon.in")
        elif "open instagram" in query:
            webbrowser.open("https://instagram.com")
        elif "open steam" in query:
            webbrowser.open("https://store.steampowered.com")



# -------------------------------------------------------
# Thank you for using this voice assistant!
# Created with passion and Python by Vaibhav Sen.
# -------------------------------------------------------

