import requests
import threading


short_memory = []
def output(prints):
    print(prints)

def ask_ollama(command, speak):
    user_input = command
    try:
        short_memory.append({"role": "user", "content": user_input})
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": "llama3.2:3b",
            "messages": short_memory,
            "stream": False,
            }
        )
        reply = response.json()["message"]["content"]
        short_memory.append({"role": "assistant", "content": reply})
    except Exception:
        print("Sorry i couldnt think properly")
        speak("Sorry i couldnt think properly")
        return
    thread1 = threading.Thread(target=speak, args=(reply,))
    thread2 = threading.Thread(target=output, args=(reply,))

    thread1.start()
    thread2.start()


