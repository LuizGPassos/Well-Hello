from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import os
from dotenv import load_dotenv
import pygame
import time

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

VOICE_ID = "VU3GQXOzoenLZNZ84sCy"

def text_to_speech_file(text: str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id=VOICE_ID, 
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2", # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = "ai-response.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Initialize pygame mixer and load the audio file
    pygame.mixer.init()
    pygame.mixer.music.load(save_file_path)

    # Play the audio file
    pygame.mixer.music.play()
    print("Playing audio...")

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

   

    print("Audio finished playing.")

    pygame.mixer.music.stop()
    pygame.mixer.quit()

    os.remove("ai-response.mp3")

    # Return the path of the saved audio file
    return save_file_path
