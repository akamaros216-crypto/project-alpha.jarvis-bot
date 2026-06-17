import speech_recognition as sr
import pyttsx3 


recognizer = sr.Recognizer()
talk = pyttsx3.init()

def speak(text):
    talk.say(text)
    talk.runAndWait()

def listen():
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.3)
        audio = recognizer .listen(mic)
    
    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}")


while True:
    print("Jarvis is sleeping...")
    text = listen()

    if "jarvis" in text:
        break
speak("Hello sir, what can i do for you?")
print("Awake and ready for help")
while True:
    command = listen()  # listen fresh every iteration
    if command == "":
        print("Didn't catch that")
        continue
    print(f"Command recived: {command}")
    speak(f"You gave me command to: {command}")

    if "sleep" in command:
        break

speak("Goodnight sir")
print("Jarvis is sleeping...")








