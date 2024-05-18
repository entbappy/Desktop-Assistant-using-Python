import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


# Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


#speak function
def speak(text):
    """This function takes text and returns voice

    Args:
        text (_type_): string
    """
    engine.say(text)
    engine.runAndWait()


# speech recognition function
def takeCommand():
    """this function will recognize voice & return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query




if __name__ == "__main__":
    
    query = takeCommand().lower()

    if "wikipedia" in query:
        speak("Searching wikipedia")
        query = query.replace('wikipedia', "")
        results = wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    
    elif "youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("youtube.com")

    
    elif "google" in query:
        speak("Opening google")
        webbrowser.open("google.com")


    elif "github" in query:
        speak("Opening github")
        webbrowser.open("github.com")





