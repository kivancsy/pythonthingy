from datetime import datetime
import speech_recognition
import pyttsx3
import webbrowser
import wikipedia



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
activationWord = "computer"


def speak(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


opera_path = r"C:\Users\kivan\AppData\Local\Programs\Opera GX\launcher.exe"
webbrowser.register("opera", None, webbrowser.BackgroundBrowser(opera_path))


def parseCommand():
    listener = speech_recognition.Recognizer()
    print("I am listening")

    with speech_recognition.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print("Recognizing speech...")
        query = listener.recognize_google(input_speech, language='en_gb')
        #print(f"the input speech was:  {query}")
        #speak(f"{query}")
    except Exception as exception:
        print("I couldn't hear that")
        speak("I couldn't hear that")
        print(exception)
        return "None"

    return query


def search_wikipedia(query=""):
    searchResults = wikipedia.search(query)
    if not searchResults:
        print("No results in the encyclopedia")
        return "No result received"
    try:
        wikiPage = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    print(f"{wikiSummary}")
    return wikiSummary


if __name__ == "__main__":
    speak("All systems nominal.")

    while True:
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            if query[0] == "say":
                if "hello" in query:
                    speak("Hello y'all!")
                else:
                    query.pop(0)
                    speech = " ".join(query)
                    speak(speech)

                    # Web'de geziyoz
            if query[0] == "go" and query[1] == "to":
                speak("Opening...")
                query = " ".join(query[2:])
                webbrowser.get("opera").open_new(query)

            if query[0] == "wikipedia":
                query = " ".join(query[1:])
                speak(f"Searching the encyclopedia for {query}")
                result = search_wikipedia(query)
                speak(result)
