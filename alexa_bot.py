"This is a 'smart' Alexa bot  program"
import datetime
import pyttsx3
import pywhatkit
import wikipedia
import speech_recognition as sr


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(text):
    """Alexa talks."""
    engine.say(text)
    engine.runAndWait()


def take_command():
    """Alexa takes the command."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
    except ValueError:
        pass
    return command


def run_alexa():
    """Runs alexa."""
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("Current time is " + time)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    else:
        talk("Say it again")


if __name__ == "__main__":
    run_alexa()
