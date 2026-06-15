import speech_recognition as sr
import pyttsx3 


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:

    try:

        with sr.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")
            speak(f"You said: {text}")

    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue

    except sr.RequestError as e:
        print(f"API error: {e}")
        break

