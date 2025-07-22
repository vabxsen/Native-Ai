import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip inatall wikipedia
import webbrowser

# Text-to-Speech Setup
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

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Boy!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Boy!")
    else:
        speak("Good Evening Boy!")

    speak("Myself Jill. How can i assist you?")

def takeCommand():
    """Takes voice input and returns string output."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("Timeout while listening")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except sr.RequestError:
        print("Network error")
        return "None"

    return query

# MAIN PROGRAM
if __name__ == "__main__":
    wishme()

    if 1:
        query = takeCommand().lower()

        if query == "none":
           
         if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                print(f"Wikipedia Summary: {results}")
                speak("According to Wikipedia")
                speak(results[:300])  # Prevents long or problematic strings
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find anything on that topic.")

        elif 'open youtube' in query:
                webbrowser.open("youtube.com")
        elif'open google' in query:
                webbrowser.open("google.com")
        elif'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is{strTime}")
        elif"open spotify" in query:
            webbrowser.open("spotify.com")
        elif"play music" in query:
            webbrowser.open("spotify.com")
        elif"open amazon" in query:
            webbrowser.open("amazon.in")
        elif"open instagram" in query:
            webbrowser.open("instagram.com")
        elif"open steam" in query:
            webbrowser.open("store.steampowered.com")


          # That's all with my small Ai program. 
                  # Myself Vaibhav Sen



            


       




























































































































