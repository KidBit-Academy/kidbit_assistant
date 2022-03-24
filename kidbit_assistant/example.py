from main import *

def get_time(voice):
    time_in_ist = "" 
    try:
        code = "ist"
        time_in_gst = get_time_in_gst()
        time_in_ist = convert_time(time_in_gst, code)
    except:
        print("Cannot get time")
    
    return time_in_ist
    
while True:
    voice = listen_voice()
    if "alexa" in voice:
    
        if "news for today" in voice:
            news = get_google_news()
            speak(news)

        elif "current time" in voice:
            time = get_time(voice)
            speak(time)

        elif "joke" in voice:
            joke = get_joke()
            speak(joke)

        elif "play song" in voice:
            song = identify_song(voice)
            speak("Playing song ")
            play_on_youtube(song)

        elif "where are we" in voice:
            speak("We are in India")

        elif "quit" in voice or "exit" in voice:
            speak("Goodbye! Have a great day!")
            break
        
        else:
            speak("I don't understand. Please try again.")

    else:
        speak("Did you wish to ask something? Try saying something with alexa in it.")