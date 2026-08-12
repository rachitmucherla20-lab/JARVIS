import speech_recognition as sr
import pyttsx3

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
        # Adjust for background noise
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        audio = recognizer.listen(source)

    try:
        print("🧠 Processing voice...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"👤 You said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat?")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech recognition service is currently unavailable.")
        return ""

if __name__ == "__main__":
    speak("Hello Rachit! Listening for your command.")
    command = listen()
    
    if command:
        speak(f"I heard you say: {command}")
        
