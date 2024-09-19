import os
import time
import pyaudio
import speech_recognition as sr
import playsound
from gtts import gTTS
import openai
import uuid

api_key = "CHANGE THIS"
lang = 'en'

openai.api_key = api_key

guy = ""
assistant_name = "Honey"

def set_assistant_name():
    global assistant_name
    print("Please say the name you'd like to call your assistant.")
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
        try:
            assistant_name = r.recognize_google(audio)
            print(f"Assistant name set to: {assistant_name}")
        except Exception as e:
            print(f"Could not recognize the name. Exception: {str(e)}")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
            global guy
            guy = said

            if assistant_name in said:
                new_string = said.replace(assistant_name, "")
                new_string = new_string.strip()
                print(new_string)
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", 
                    messages=[{"role": "user", "content": new_string}]
                )
                text = completion.choices[0].message.content
                speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                file_name = f"response_{str(uuid.uuid4())}.mp3"
                speech.save(file_name)
                playsound.playsound(file_name, block=False)

        except Exception as e:
            print(f"Exception: {str(e)}")

    return said

# Main Program
set_assistant_name()

while True:
    if "stop" in guy:
        break
    get_audio()
