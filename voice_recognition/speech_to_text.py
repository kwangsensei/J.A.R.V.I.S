import speech_recognition as sr


def record_text():
    # Initialize the recognizer.
    r = sr.Recognizer()
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


def output_text(text):
    f = open("./voice_recognition/output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()


while(1):
    text = record_text()
    output_text(text)

    print("Wrote Text")
