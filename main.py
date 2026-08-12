import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Set voice properties (Optional: speed up or slow down speech)
engine.setProperty('rate', 180)  # Speed of speech

def speak(text):
    """Function to make JARVIS speak and print text"""
    print(f"🤖 JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello Rachit! I am JARVIS, online and ready to assist you.")
