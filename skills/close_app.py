import subprocess

app_short = {
    "google": "chrome.exe",
    "chrome": "chrome.exe",
    "code": "Code.exe",
    "discord": "Discord.exe",
    "spotify": "Spotify.exe",
    "word": "WINWORD.EXE",
    "excel": "EXCEL.EXE",
    "thinking": "claude.exe"
}

def run(command, speak):
    words = command.split()

    for i, word in enumerate(words):
        if "close" in word:
            if i + 1 < len(words):
                app = " ".join(words[i + 1:])
                if app in app_short:
                    app = app_short[app]
                    try:
                        result = subprocess.run(f'taskkill /IM {app} /F', shell=True, capture_output=True, text=True)
                        if result.returncode == 0:
                            speak(f"You gave me a command to: {command}")
                            print(f"Successfully closed {app}")
                            speak(f"Closed {app}")
                        else:
                            print(f"App not running or not found: {result.stderr}")
                            speak("That app doesn't seem to be open")
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    speak(f"I don't know how to close {app}")