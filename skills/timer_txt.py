import time
import threading
import winsound

def run(command, speak):
    words = command.split()
    seconds = None
    number = None
    unit = None

    for i, word in enumerate(words):
        if word.isdigit():
            number = int(word)
            if i + 1 < len(words):
                unit = words[i +1]
                if "hours" in unit:
                    seconds = number * 3600
                elif "minutes" in unit:
                    seconds = number * 60
                elif "seconds" in unit:
                    seconds = number 
            break

    if seconds is None:
        speak("Sorry didnt catch that")
        return
    speak(f"You gave me a command to: {command}")
    speak(f"Setting a timer for {number} {unit}")
    t = threading.Thread(target=_countdown, args=(seconds, speak))
    t.daemon = True
    t.start()

def _countdown(seconds, speak):
    time.sleep(seconds)
    winsound.Beep(1000, 500)
    speak("The timer is done")
    print("Timer done!")



