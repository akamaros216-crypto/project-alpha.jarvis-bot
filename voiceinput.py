import speech_recognition as sr
import pyttsx3 
import time





def speak(text):
    talk = pyttsx3.init()
    talk.setProperty("rate", 150)
    talk.say(text)
    talk.runAndWait()
    time.sleep(0.3)


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.3)
        try:
            audio = recognizer.listen(mic, timeout=5)
        except sr.WaitTimeoutError:
            return ""
    
    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""         


while True:
    print("Jarvis is sleeping...")
    text = listen()

    if "jarvis" in text:
        break
speak("Hello sir, what can i do for you?")
print("Awake and ready for help")
while True:
    command = listen()
    if not command:
        print("Didn't catch that")
        continue
    print(f"Command received: {command}")
    speak(f"You gave me a command to: {command}")

    if "sleep" in command:
        break

speak("Goodnight sir")
print("Jarvis is sleeping...")








