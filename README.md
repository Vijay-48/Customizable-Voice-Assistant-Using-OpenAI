# Customizable-Voice-Assistant-Using-OpenAI

This project implements a voice-controlled assistant that can be personalized by setting a custom name, allowing users to interact with the assistant in a more natural and engaging way. The assistant listens to user commands, processes them using OpenAI's GPT-3.5, and responds with synthesized speech through Google Text-to-Speech (gTTS).

# Features:

***Custom Assistant Name:*** Users can dynamically set their preferred name for the assistant, making interactions more personalized.
***Voice Command Recognition:*** The assistant listens for commands using Google Speech Recognition and responds when the user calls its name.
***AI-Powered Responses:*** User commands are processed by OpenAI’s GPT-3.5 model to generate intelligent responses.
***Text-to-Speech:*** Responses are vocalized using the gTTS library, providing real-time feedback with an Australian accent.
***Stop Command:*** Users can end the session by simply saying "stop".

# Technologies Used:

- Python
- OpenAI API (GPT-3.5)
- Google Text-to-Speech (gTTS)
- SpeechRecognition
- PyAudio
- Playsound

# Setup Instructions:

1. Clone the repository.
2. Install the required Python packages:

  pip install openai SpeechRecognition pyaudio playsound gtts

3. Replace the placeholder api_key with your OpenAI API key.
4. Run the script and set your custom assistant name via voice input.

# Usage:

- Start the assistant, set a custom name by speaking into the microphone, and call it by that name to issue voice commands.
- The assistant responds with a synthesized voice based on GPT-3.5's response to your command.
- Say "stop" to end the session.

