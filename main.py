import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from google import genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.runAndWait()
newsapi = "NEWS API KEY"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def OpenAI(command):
    client = genai.Client(api_key="GEMINI API KEY")
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=command
)
    return(response.text)


def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com/")
    elif "open instagram" in command.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open spotify" in command.lower():
        webbrowser.open("https://open.spotify.com")
    
    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            for article in data['articles']:
                speak(article['title'])

    else:
        output = OpenAI(command) 
        speak(output)   
   

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        r = sr.Recognizer()
        print("recognizing")

        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio1 = recognizer.listen(source,timeout=5)
                word =  recognizer.recognize_google(audio1)
            if(word.lower() == "jarvis"):
                speak("Yeah")
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio2 = recognizer.listen(source,timeout=5)
                    command = recognizer.recognize_google(audio2)
                    print(command) 
                
                processCommand(command)
        
        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand what was said.")
        except sr.RequestError as e:
            print(f"Could not request results: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
