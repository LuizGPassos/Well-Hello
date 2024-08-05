from openai import OpenAI
import pyaudio
import wave
import keyboard
import os

client = OpenAI()

audio = pyaudio.PyAudio()

def RecordAudio():
    stream = audio.open(
        input=True,
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        frames_per_buffer=1024,
    )
  
    print("Recording...")

    frames = []

    while keyboard.is_pressed('v'):
        data = stream.read(1024)
        frames.append(data)

    print("Finish recording.")
    
    stream.stop_stream()
    stream.close()

    wf = wave.open("Speech.wav", "wb")
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

def SpeechToText():
    print("Press 'V' to record.")
    keyboard.wait('v')
    RecordAudio()

    audio_file = open("Speech.wav", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    audio_file.close()
    os.remove("Speech.wav")
    return transcription.text

if __name__ == "__main__":
    print(SpeechToText())
    audio.terminate()
    