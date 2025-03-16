import openai
from speech_to_text import SpeechToText
from tts_response import text_to_speech_file
from screenshot import ShotAndSave
import pygame
import os
import json
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

AI_ROLE = """You're an helpful assistant."""

def load_history():
    if os.path.exists("history.json"):
        with open("history.json", "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open("history.json", "w") as f:
        json.dump(history, f)

def AiTalk():
    history = load_history()
    user_prompt = SpeechToText()
    
    print(f'User Prompt: {user_prompt}')
    
    history.append({"role": "user", "content": user_prompt})

    if "what do you see?" in user_prompt.lower():
        image = ShotAndSave()
        print(f'Screen captured.')
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": AI_ROLE},
                *history, 
                {"role": "user", "content": user_prompt},
                {"role": "user", "content": [{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image}"}}]}
            ]
        )
        os.remove("screenshot.jpeg") 
    else:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": AI_ROLE},
                *history, 
                {"role": "user", "content": user_prompt},
            ]
        )

    ai_response = response.choices[0].message.content
    print(f'\nAi Response: {ai_response}')
    
    history.append({"role": "assistant", "content": ai_response})
    save_history(history)
    
    return ai_response

if __name__ == "__main__":
    try:
        while True:
            text_to_speech_file(AiTalk())  
    except KeyboardInterrupt:
        if os.path.exists("history.json"):
            os.remove("history.json")
