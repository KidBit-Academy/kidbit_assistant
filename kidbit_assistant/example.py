from main import *

def get_time(voice):
    time_in_ist = ""
    
    try:
        code = "ist"
        time_in_gst = get_time_in_gst()
        time_in_ist = convert_time(time_in_gst, code)
    except Exception as e:
        print("Cannot get time")
        print(e)
    
    return time_in_ist

def check_for_phrase(voice):
    if "where are we" in voice:
        return get_response("where are we")
    elif "who am i" in voice:
        return get_response("who am i")
    elif "where do i study" in voice:
        return get_response("where do i study")
    elif "what is my hobby" in voice:
        return get_response("what is my hobby")
    else:
        return ""

def add_custom_responses_to_assistant():
    save_response("where are we", "We are in a session with D A V teachers. They are liking it.")
    save_response("who am i", "I am KidBo.")
    save_response("where do i study", "I study in D A V.")
    save_response("what is my hobby", "I love to play cricket.")

def tell_about(voice_input):
    try:
        interest = erase_phrase_from_sentence(voice_input, "tell me about")
        info = wikipedia.summary(interest, 1)
        speak(info)
    except:
        speak("Cannot find relevant information. Please try again later.")

add_custom_responses_to_assistant()
add_exit_phrases("quit")
add_exit_phrases("exit")
add_exit_phrases("bye")
assistant_name = "alexa"
    
while True:
    voice = take_voice_input_begininng_with(assistant_name)
    
    if assistant_name in voice:
        voice_filtered = erase_from_voice(voice, assistant_name)
    
        if "news for today" in voice_filtered:
            news = get_google_news()
            speak(news)

        elif "current time" in voice_filtered:
            time = get_time(voice)
            speak(time)

        elif "joke" in voice_filtered:
            joke = get_joke()
            speak(joke)

        elif "play song" in voice_filtered:
            song = identify_song(voice_filtered)
            speak("Playing song ", song)
            play_on_youtube(song)

        elif "where are we" in voice_filtered:
            saved_response = get_response("where are we")
            speak(saved_response)

        elif contains_exit_phrase(voice_filtered):
            speak("Goodbye! Have a great day!")
            break
        
        else:
            custom_response = check_for_phrase(voice_filtered)
            speak(custom_response)

    else:
        speak("Did you wish to ask something? Try saying something with " + assistant_name + " in it.")