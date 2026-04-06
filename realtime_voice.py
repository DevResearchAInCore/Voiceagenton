import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
from rag_engine import get_answer
from tts_engine import speak

model = WhisperModel("base")

sd.default.samplerate = 16000
sd.default.channels = 1


def record_audio(filename="input.wav", duration=8):

    print("Listening...")

    recording = sd.rec(int(duration * 16000),
                       samplerate=16000,
                       channels=1)

    sd.wait()

    write(filename, 16000, recording)


def speech_to_text(file):

    segments, _ = model.transcribe(file)

    text = ""

    for segment in segments:
        text += segment.text

    return text


def start_voice_agent():

    print("Voice AI Assistant Started")
    print("Say 'stop assistant' to exit")

    while True:

        record_audio()

        text = speech_to_text("input.wav")

        print("User:", text)

        if "stop assistant" in text.lower():
            speak("Goodbye")
            break

        answer = get_answer(text)

        print("AI:", answer)

        speak(answer)
