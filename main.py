import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speak(text):
    """Make JARVIS speak text out loud"""
    print(f"🤖 JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to voice input from microphone and convert to text"""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        audio = recognizer.listen(source)

    try:
        print("🧠 Processing voice...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"👤 You said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Sorry, my speech recognition service is currently unavailable.")
        return ""

def process_command(command):
    """Execute action based on user command"""
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "open youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")

    elif "stop" in command or "exit" in command or "bye" in command:
        speak("Goodbye Rachit! Powering down.")
        return False
        
    elif command != "":
        speak("I heard you, but I don't have a feature for that yet.")
        
    return True

if __name__ == "__main__":
    speak("JARVIS system online. How can I help you?")
    
    running = True
    while running:
        user_command = listen()
        if user_command:
            running = process_command(user_command)