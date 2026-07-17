import requests


short_memory = []


def ask_ollama(user_input):
    short_memory.append({"role": "user", "content": user_input})
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={"model": "llama3.2:3b",
        "message": short_memory,
        "stream": False,
        }
    )
    reply = response.json()["message"]["content"]
    short_memory.append({"role": "assistant", "content": reply})
    return reply


