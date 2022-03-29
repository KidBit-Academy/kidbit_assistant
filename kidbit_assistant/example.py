from main import *

def get_time(voice):
    time_in_ist = "" 
    try:
        code = "ist"
        time_in_gmt = get_time_in_gmt()
        time_in_ist = convert_time(time_in_gmt, code)
    except:
        print("Cannot get time")
    
    return time_in_ist

add_custom_joke("Joke 1")
add_custom_joke("Joke 2")

while True:
    voice = listen()
    set_voice(40)
    print(voice)
    try:
        if "alexa" in voice:
            if "news" in voice:
                speak("Fetching Live News")
                news = get_google_news()
                speak(news)

            elif "time" in voice:
                time = get_time(voice)
                speak(time)

            elif "joke" in voice:
                joke = get_custom_joke()
                speak(joke)

            elif "play song" in voice:
                speak("Playing song")
                song = erase_from_voice(voice, "alexa", "play song")
                play_on_youtube(song)
                print("Enjoy")

            elif "where are we" in voice:
                speak("We are in India")

            elif "quit" in voice or "exit" in voice:
                speak("Goodbye! Have a great day!")
                stop()
                break
            
            elif "calculate" in voice:
                speak("What do you want to do?")
                voice2 = listen()
                if "add" in voice2:
                    speak("Speak number 1")
                    n1 = int(listen())
                    speak("Number 1 is ", n1)
                    speak("Speak number 2")
                    n2 = int(listen())
                    speak("Number 2 is ", n1)
                    speak("Addition of two numbers is ", n1 + n2)

                elif "subtract" in voice2:
                    speak("Speak number 1")
                    n1 = int(listen())
                    print("Number 1 is:", n1)
                    speak("Speak number 2")
                    n2 = int(listen())
                    print("Number 2 is:", n2)
                    speak("Subtraction of two numbers is ", n1 - n2)

            else:
                speak("I don't understand. Please try again.")
        else:
            speak("Did you wish to ask something? Try saying something with alexa in it.")
    except:
        speak("There was a fatal error. GoodBye")


