import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def main():
    speak("Hello! I am your Python Voice Assistant.")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {current_date}")

        elif "search" in command:
            speak("What do you want me to search?")
            query = listen()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Searching Google for {query}")

        elif "bye" in command or "exit" in command:
            speak("Goodbye! Have a nice day.")
            break

        elif command != "":
            speak("Sorry, I don't know that command.")

if __name__ == "__main__":
    main()