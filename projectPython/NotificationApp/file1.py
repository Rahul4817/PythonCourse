import speech_recognition as sr

import pyaudio


def main():
     # the recognizer
    recognizer = sr.Recognizer()

    #microphone instance
    microphone = sr.Microphone()

    print("Say something...")
    with microphone as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio)
    f=open("text.txt","w")
    print(f.write(text))
if __name__ == "__main__":
    main()
