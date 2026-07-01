import subprocess

app_short= {"google": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "code": "C:\\Users\\Hcc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
            "thinking": "C:\\Users\\Hcc\\AppData\\Local\\AnthropicClaude\\claude.exe",
            "discord": "C:\\Users\\Hcc\AppData\\Local\\Discord\\app-1.0.9243\\Discord.exe",
            "spotify": "Spotify",
            "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
            "excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
            }
def run(command, speak):
    words = command.split()
    

    for i, word in enumerate(words):
        if "open" == word or "start" == word:
            if i + 1 < len(words):
                app =" ".join(words[i +1:])
                original = app
                if app in app_short:
                    app = app_short[app]
                    if app.endswith(".exe") and "\\" in app:
                        subprocess.Popen(app)
                    else:
                        subprocess.Popen(f'start "" "{app}"', shell=True)

                    try: 
                        subprocess.Popen(f'start "" "{app}"', shell=True)
                        print("App succesfully opened")
                        speak(f"Opening {original}")

                    except Exception as e:
                        print(f"There was an error finding the app: {e}")


