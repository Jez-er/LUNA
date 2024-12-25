import pygame
from gtts import gTTS
import io

def gtts(text):
	tts = gTTS(text=text, lang='uk', slow=False)

	# Створення аудіо в пам'яті
	audio_stream = io.BytesIO()
	tts.write_to_fp(audio_stream)
	audio_stream.seek(0)

	# Ініціалізація pygame
	pygame.mixer.init()

	# Завантаження та програвання з потоку
	pygame.mixer.music.load(audio_stream, 'mp3')
	pygame.mixer.music.play()

	# Очікуємо завершення відтворення
	while pygame.mixer.music.get_busy():
			pygame.time.Clock().tick(10)

def gtts_local(file):
	pygame.mixer.init()

	# Завантаження та програвання з потоку
	pygame.mixer.music.load(file, 'mp3')
	pygame.mixer.music.play()

	# Очікуємо завершення відтворення
	while pygame.mixer.music.get_busy():
			pygame.time.Clock().tick(10)