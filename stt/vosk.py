import queue
import sounddevice as sd
import vosk
import json

q = queue.Queue()
model = vosk.Model('vosk-stt-model')
device = sd.default.device = 0, 4
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])


def callback(indata, frames, time, status):
    q.put(bytes(indata))

def Listen():
    rec = vosk.KaldiRecognizer(model, samplerate)

    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, channels=1, device=device[0], dtype='int16',
                               callback=callback):
        print("Слухаємо...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if 'text' in result:
                    recognized_text= result['text']
                    return recognized_text

