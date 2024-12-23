from stt.vosk import Listen


def main():
	while True:
		text = Listen()
		print(text)

if __name__ == "__main__":
	main()