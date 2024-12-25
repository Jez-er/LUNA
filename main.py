import json
from stt.listen import Listen
from stt.wakeword import wakeword
from tts.gtts import gtts
from utils.greeting import greeting_based_on_time
import skills
# import threading
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def speak(text):
    gtts(text)

with open('commands.json', 'r', encoding='utf-8') as f:
    commands_data = json.load(f)

def recognize(data):
    # reset_timeout()
    data = ' '.join([word for word in data.split()])
    handle_command(data.strip())

def handle_command(command):
    # timeout_timer.cancel()

    best_match = None
    best_similarity = 0
    similarity_threshold = 0.5

    vectorizer = TfidfVectorizer().fit(
        [trigger for cmd in commands_data["commands"] for trigger in cmd['triggers']])
    command_vector = vectorizer.transform([command])

    for cmd in commands_data["commands"]:
        trigger_vectors = vectorizer.transform(cmd['triggers'])
        similarities = cosine_similarity(command_vector, trigger_vectors).flatten()
        max_similarity = similarities.max()

        # print(f"Команда: '{command}', Лучшая схожесть для команды '{cmd['command']}': {max_similarity}")

        if max_similarity > best_similarity:
            best_similarity = max_similarity
            best_match = cmd

    print(f"Лучшая команда: '{best_match['command'] if best_match else 'None'}', Лучшая схожесть: {best_similarity}")

    if best_match and best_similarity >= similarity_threshold:
        func_to_call = getattr(skills, best_match['make'], None)
        if func_to_call and callable(func_to_call):
            func_to_call(best_match, command)

        response = best_match.get('say', "Команда выполнена.")
        print(f"Отвечаем: {response}")

        speak(response)
    else:
        print("Команда не распознана.")
        speak(response)

def main():
    greeting_based_on_time()
    while True:
        wakeWord = wakeword()
        if wakeWord:
            text = Listen()
            if text:
                recognize(text)
            else:
                speak("Повторіть ще раз")
                

if __name__ == "__main__":
	main()