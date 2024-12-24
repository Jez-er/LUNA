import os
import struct

import pvporcupine
import pyaudio


def wakeword():
    porcupine = None
    pa = None
    audio_stream = None
    keyword_path = os.path.abspath("D:/work/LUNA/wake-word/wakeword.ppn")  # На Windows
    try:
        porcupine = pvporcupine.create(keyword_paths=[keyword_path], access_key='ZbO+y+/8iVAfWax6eHLXgANnHvfDhCfzf3MPBDmaulqeC+4uWJGpww==')
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("Прослушивание активационного слова...")

        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Активационное слово обнаружено!")
                return True
    except Exception as e:
        print(f"Ошибка в wakeword: {e}")
    finally:
        if audio_stream:
            audio_stream.stop_stream()
            audio_stream.close()
        if pa:
            pa.terminate()
        if porcupine:
            porcupine.delete()