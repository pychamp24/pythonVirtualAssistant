import textToSpeech
import speechToText
import datetime
import sys
import webbrowser
import weather
from calculateNumbers import calculate_query

def Action(data):
    dataBy_user = data.lower()

    if"what is your name" in dataBy_user:
        textToSpeech.text_to_speech('I am MORRIS how can i help you??')
        return 'I am MORRIS how can i help you??'

    elif "hello" in dataBy_user or "Hi" in dataBy_user:
        textToSpeech.text_to_speech("hi ,sir how can i help you")
        return "hi ,sir how can i help you"

    elif "good morning" in dataBy_user:
        textToSpeech.text_to_speech("very good morning sir")
        return "very good morning sir"
        
    elif "time now" in dataBy_user:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :", (str)(current_time.minute) + "minute"
        return Time

    elif "bye" in dataBy_user or "off" in dataBy_user or "see you soon" in dataBy_user:
        textToSpeech.text_to_speech("ok sir shutting down see you soon!!")
        sys.exit("User ended the session.")

    elif "play music" in dataBy_user or "music" in dataBy_user:
        webbrowser.open("https://open.spotify.com/")
        textToSpeech.text_to_speech("spotify is opened")
        return "spotify is opened"

    elif "open youtube" in dataBy_user:
        webbrowser.open("https://www.youtube.com/")
        textToSpeech.text_to_speech("youtube is opened")
        return "youtube is opened"

    elif "open google" in dataBy_user:
        webbrowser.open("https://www.google.co.in/")
        textToSpeech.text_to_speech("google is opened")
        return "google is opened"
    
    elif "weather" in dataBy_user or "weather today" in dataBy_user:
        res = weather.weather()
        textToSpeech.text_to_speech(res)
        return res
    
    elif "calculate" in dataBy_user:
        query = dataBy_user.replace("calculate", "").strip()
        result = calculate_query(query)
        textToSpeech.text_to_speech(result)
        return result

    
    else:
        textToSpeech.text_to_speech("I'm not able to understand give command again")
        return "I'm not able to understand give command again"