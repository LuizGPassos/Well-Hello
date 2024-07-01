from openai import OpenAI
from speech_to_text import SpeechToText
from tts_response import text_to_speech_file
from screenshot import ShotAndSave
import pygame
import os


client = OpenAI()

AI_ROLE = """You are a helpful assistant."""


def AiTalk():
    user_prompt = SpeechToText()

    if user_prompt.startswith("Capture this."):

        image = ShotAndSave()
        print(f'User Prompt: {user_prompt}')
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": AI_ROLE},
                {"role": "user", "content": [{"type" : "text", "text" : user_prompt},
                                             {"type" : "image_url", "image_url" : {"url": f"data:image/jpeg;base64,{image}"}}]},
            ]
        )
        ai_response = response.choices[0].message.content
        print(f'\n Ai Response: {ai_response}')
        
    else:
        print(f'User Prompt: {user_prompt}')
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": AI_ROLE},
                {"role": "user", "content": user_prompt},
            ]
        )
        ai_response = response.choices[0].message.content
        print(f'\n Ai Response: {ai_response}')
    
    return ai_response



if __name__ == "__main__":
    while True:
        text_to_speech_file(AiTalk())    



