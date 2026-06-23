import subprocess


def run(command, speak):
    words = command.split()
    

    for i, word in enumerate(words):
        if "open" == word or "start" == word:
            if i + 1 < len(words):
                app = " ".join(words[i +1:])

                try: 
                    subprocess.Popen(f'start "" "{app}"', shell=True)
                    print("App succesfully opened")
                    speak(f"Opening {app}")

                except Exception as e:
                    print(f"There was an error finding the app: {e}")


