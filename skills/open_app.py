import subprocess

app_short = {
    "google": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "code": "C:\\Users\\Hcc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "thinking": "C:\\Users\\Hcc\\AppData\\Local\\AnthropicClaude\\claude.exe",
    "discord": ("C:\\Users\\Hcc\\AppData\\Local\\Discord\\Update.exe", "--processStart", "Discord.exe"),
    "spotify": "Spotify",
    "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
}

def run(command, speak):
    words = command.split()

    for i, word in enumerate(words):
        if word in ("open", "start"):
            if i + 1 < len(words):
                app_key = " ".join(words[i + 1:])
                app = app_short.get(app_key)

                if app is None:
                    print(f"'{app_key}' not found in known apps")
                    speak(f"I don't know how to open {app_key}")
                    return

                try:
                    if isinstance(app, tuple):
                        subprocess.Popen(list(app))
                    elif app.endswith(".exe") and "\\" in app:
                        subprocess.Popen(app)
                    else:
                        subprocess.Popen(f'start "" "{app}"', shell=True)

                    print("App successfully opened")
                    speak(f"Opening {app_key}")

                except Exception as e:
                    print(f"There was an error finding the app: {e}")
                return