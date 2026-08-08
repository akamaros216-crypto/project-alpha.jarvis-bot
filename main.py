
import speech_recognition as sr
import pyttsx3 
import time
from skills import timer, open_app, close_app
from ai_brain import ask_ollama as ask_ollama_run
from faster_whisper import WhisperModel
import os
import uuid
import threading


running = True
model_size = "small"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

speak_lock = threading.Lock()


def trans(speech): # function that turns audio into text
    segments, _ = model.transcribe(speech)
    text = " ".join(seg.text for seg in segments).strip()
    return text

def speak(text): # function that makes it talk
    with speak_lock:
        talk = pyttsx3.init()
        talk.setProperty("rate", 150)
        talk.say(text)
        talk.runAndWait()
        time.sleep(0.3)
        


def listen(): #function that inputs what you say
    time.sleep(0.5)
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.3)
        try:
            audio = recognizer.listen(mic, timeout=5)
        except sr.WaitTimeoutError:
            return ""
    
    try: # inputs my speech to whisper
        filename = f"temp_{uuid.uuid4().hex}.wav"
        with open(filename, "wb") as f:
            f.write(audio.get_wav_data())
        segments, _ = model.transcribe(filename)
        segments = list(segments)
        text = " ".join(seg.text for seg in segments).strip()
        try:
            os.remove(filename)
        except PermissionError:
            pass
        return text.lower()

    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""         


while True: #inactive
    print("Jarvis is sleeping...")
    text = listen()

    if "jarvis" in text: #wake word
        break
speak("Hello sir, what can i do for you?")
print("Awake and ready for help")

while running: # giving tasks to do


    command = listen()
    if not command:
        print("Didn't catch that")
        continue

    if "timer" in command: #timer task
        timer.run(command, speak)
    
    elif "open" in command: #opening app task
        open_app.run(command, speak)
    
    elif "close" in command: #closing app task
        close_app.run(command, speak)
    
    elif "sleep" in command: #shutting off
        running = False

    else:
        ask_ollama_run(command, speak)
        
        

speak("Goodnight sir")
print("Jarvis is sleeping...")
