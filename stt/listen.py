import speech_recognition as sr
from tts.gtts import gtts_local
from pathlib import Path

# Ініціалізація розпізнавача
recognizer = sr.Recognizer()

# Використання мікрофона
def Listen():

	current_directory = Path(__file__).parent

	# Створюємо відносний шлях до файлу
	file_path = current_directory / '..' / 'assets' / 'active.mp3'

	# Перетворюємо шлях на абсолютний
	file_path = file_path.resolve()

	with sr.Microphone() as source:
			gtts_local(file_path)
			print("Скажіть щось українською...")
			recognizer.adjust_for_ambient_noise(source)  # Налаштування на шум
			audio = recognizer.listen(source)  # Запис звуку
			
			try:
					# Розпізнавання
					text = recognizer.recognize_google(audio, language="uk-UA")
					return text
			except sr.UnknownValueError:
					return False
			except sr.RequestError as e:
					print(f"Помилка сервісу: {e}")