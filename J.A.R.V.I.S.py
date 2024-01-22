# Python program to translate
# Speech to text and text to speech
import os
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv


load_dotenv()
OPEN_API_KEY = os.getenv("OPENAPI_KEY")


from openai import OpenAI


def speak_text(command):
    # Function to convert text to speech.
    # Initialize the engine.
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Initialize the recognizer.
r = sr.Recognizer()


def record_text():
    # Loop in case of errors.
    while(1):
        try:
            # Use the mic as source for input.
            with sr.Microphone() as mic:
                # Prepare recognizer to receive input.
                r.adjust_for_ambient_noise(mic, duration=0.2)

                print("I'm listening")

                # Listen for user's voice input.
                audio = r.listen(mic)

                # Using Google to recognize audio.
                reg_text = r.recognize_google(audio)
                return reg_text
        except sr.RequestError as e:
            print("Could not request result; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred.")


def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
    client = OpenAI(api_key=OPEN_API_KEY)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message


messages = [{"role": "user", "content": "You are Jarvis from Iron Man."}]
while(1):
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    speak_text(response)

    print(response)
