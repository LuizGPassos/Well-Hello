from openai import OpenAI
from speech_to_text import SpeechToText
from tts_response import text_to_speech_file
import pygame
import os

client = OpenAI()

AI_ROLE = """You are a helpful assistant."""


def AiTalk():
    user_prompt = SpeechToText()

    print(f'User Prompt: {user_prompt}')
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": AI_ROLE},
            {"role": "user", "content": user_prompt},
        ]
    )
    ai_response = response.choices[0].message.content
    print(f'\n Ai Response: {ai_response}')
    last_message = user_prompt
    return ai_response



if __name__ == "__main__":
    while True:
        text_to_speech_file(AiTalk())
    


