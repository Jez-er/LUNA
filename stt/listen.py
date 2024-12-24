import speech_recognition as sr

# Ініціалізація розпізнавача
recognizer = sr.Recognizer()

# Використання мікрофона
def Listen():
	with sr.Microphone() as source:
			print("Скажіть щось українською...")
			recognizer.adjust_for_ambient_noise(source)  # Налаштування на шум
			audio = recognizer.listen(source)  # Запис звуку
			
			try:
					# Розпізнавання
					text = recognizer.recognize_google(audio, language="uk-UA")
					return text
			except sr.UnknownValueError:
					print("Не вдалося розпізнати мову.")
			except sr.RequestError as e:
					print(f"Помилка сервісу: {e}")