
# Well, Hello!

Welcome to **Well, Hello!** – a Python-based AI project that combines OpenAI's Whisper for speech recognition and transcription with ElevenLabs' text-to-speech (TTS) technology. This application allows you to interact with an AI as if you're having a conversation on platforms like Discord or Skype. Depending on how you configure it, the AI can be your friend or your virtual assistant, and it supports multiple languages.

**Note:** To use this project, you must have accounts on both OpenAI and ElevenLabs platforms.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Versioning](#versioning)
- [License](#license)

## Features
- **Voice Recognition:** Uses OpenAI's Whisper to transcribe spoken words into text.
- **Text-to-Speech:** Converts AI-generated text responses back into speech using ElevenLabs' TTS technology.
- **Interactive Conversations:** Engage in real-time conversations with the AI.
- **Customizable AI Behavior:** Define the AI's role and personality to suit your needs.
- **Multi-Language Support:** Communicate with the AI in various languages.

## Technologies Used
- **Python**: The core programming language for the project.
- **OpenAI Whisper**: For speech recognition and transcription.
- **ElevenLabs TTS**: For converting text responses into speech.
- **PyAudio**: For handling audio recording.
- **Pygame**: For playing back the audio responses.
- **dotenv**: For managing environment variables securely.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/LuizGPassos/well-hello.git
   cd well-hello
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   - Create a `.env` file in the root directory of the project.
   - Add your OpenAI and ElevenLabs API keys to the `.env` file:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key_here
     ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
     ```

## Usage
1. **Run the application:**
   ```bash
   python openai_request.py
   ```

2. **Interact with the AI:**
   - Press `V` to start recording your voice.
   - Speak your prompt.
   - The AI will process your speech, generate a response, and play it back to you.

## Configuration
- **AI Role Configuration:**
  Modify the `AI_ROLE` variable in `openai_request.py` to change the AI's personality and behavior. For example:
  ```python
  AI_ROLE = """You are a friendly assistant who loves to help with daily tasks."""
  ```
  
- **Voice Settings:**
  Adjust the parameters in `tts_response.py` to customize the voice settings (e.g., stability, similarity_boost).

## Versioning
### Version 1.0
- Initial release with the following features:
  - Voice Recognition
  - Text-to-Speech
  - Interactive Conversations
  - Customizable AI Behavior
  - Multi-Language Support

### Version 1.1
- Added image recognition functionality.
  - The AI can recognize images if the user says "what do you see?" at the ending of the audio recording.
  - Utilizes OpenAI's image processing capabilities.
  - Takes a screenshot of the screen and sends it along with the voice prompt to the AI for a more detailed response based on the screenshot.

### Version 1.2
- Added Conversation Memory with JSON.
  - Implemented a session-based memory feature using JSON files to store the conversation history.
  - The stored history is used to provide context for the AI's responses, enabling it to refer to previous interactions within the same session.
  - The history file is deleted at the end of the session to reset the memory for the next session.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
