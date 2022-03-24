import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import gnewsclient
from gnewsclient import gnewsclient

__listener = sr.Recognizer()
__engine = pyttsx3.init()
__voices = __engine.getProperty("voices")
__engine.setProperty("voice", __voices[40].id) # 40 is for en_IN, Female voice
__ext_responses = {}
__ext_phrases = []

def __listen_all_voices__():
    index = 0
    for voice in __voices:
        print(i, voice, voice.id)
        __engine.setProperty("voice", voice.id)
        __engine.say("Hello World!")
        __engine.runAndWait()
        index += 1

############# Misc Functions #################
def erase_from_voice(voice, phrase, debug = False):
    if voice == None or voice.strip() == '': 
        return ""

    if phrase == None or phrase.strip() == '': 
        return ""

    voice = voice.strip()
    phrase = phrase.strip()
    
    if debug:
        print("Voice:", voice)
        print("Phrase:", phrase)
    
    return voice.replace(phrase, "").strip()

def get_joke():
    return pyjokes.get_joke()

############# Speaking #################
def speak(phrase, debug = True):
    if phrase == None or phrase.strip() == '': 
        return

    phrase = phrase.strip()
    if debug:
        print(phrase)
    __engine.say(phrase)
    __engine.runAndWait()

############# Listening #################
def take_voice_input_begininng_with(assistant_name = "alexa"):
    voice_input = ""
    try:
        print("Listening...")
        with sr.Microphone() as source:
            voice = __listener.listen(source)
            voice_input = __listener.recognize_google(voice)
            voice_input = erase_from_voice(voice_input, assistant_name)
            voice_input = voice_input.lower()
    except:
        print("Error in taking voice input")
    return voice_input

############# Google News #################
def get_google_news(debug=False):
    speak("Fetching Live News")
    client = gnewsclient.NewsClient(language = 'english',
                                    location = 'India',
                                    max_results=10)
    for news in client.get_news():
        speak(news['title'])

############# Time Functions #################
def get_time_in_gst(debug = False):
    time = datetime.datetime.now(datetime.timezone.utc)
    if debug:
        print(time)
    return time

def get_delta_time(hours, minutes):
    return datetime.timedelta(0, (hours * 60 + minutes) * 60)

def convert_time(utc_time, code, debug = False):
    hours = 5
    minutes = 30

    if "ist" in code:
        pass
    elif "aedt" in code:
        hours = 11
        minutes = 0
    
    elif "pdt" in code:
        hours = -7
        minutes = 0

    elif "gmt" in code or "utc" in code:
        hours = 0
        minutes = 0

    elif "cst" in code:
        hours = -6
        minutes = 0

    elif "brt" in code or "brst" in code:
        hours = -3
        minutes = 0

    elif "sast" in code:
        hours = 2
        minutes = 0 

    elif "jst" in code:
        hours = 9
        minutes = 0
    else:
        print("hours: ", hours)
        print("minutes: ", minutes)
        print("code: ", code)
        print("utc_time: ", utc_time)
        raise Exception("Conversion not found to the required code")

    if debug == True:
        print("hours: ", hours)
        print("minutes: ", minutes)
        print("code: ", code)
        print("utc_time: ", utc_time)

    time_new = (utc_time + get_delta_time(hours, minutes))
    return time_new.strftime("%I:%M %p")

############# Playing Song #################
def play_on_youtube(song):
    speak("playing " + song)
    pywhatkit.playonyt(song)

def identify_song(voice):
    if voice == None or voice.strip() == '': 
        return ""
    
    voice = voice.strip()
    filtered = erase_from_voice(voice, "play song")
    filtered = erase_from_voice(filtered, "play")
    filtered = erase_from_voice(filtered, "song")
    return filtered

############# Custom Response #################
def save_response(phrase, response, debug = False):
    global __ext_responses
    
    if phrase == None or phrase.strip() == '': 
        return
    
    __ext_responses[phrase.strip()] = response.strip()


def __contains_response(phrase, debug = False):
    global __ext_responses

    if phrase == None or phrase.strip() == '': 
        return False
    
    phrase = phrase.strip()
    return (phrase in __ext_responses)
    
def get_response(phrase, debug = False):
    global __ext_responses

    if phrase == None or phrase.strip() == '': 
        return ""
    
    phrase = phrase.strip()
    if __contains_response(phrase, debug):
        if debug:
            print("Response: ", __ext_responses[phrase])
        return __ext_responses[phrase]
    else:
        if debug:
            print("Does not contain phrases")
        return ""

############# Exit #################
def add_exit_phrases(phrase):
    global __ext_phrases
    
    __ext_phrases.append(phrase)

def contains_exit_phrase(phrase):
    global __ext_phrases

    if phrase == None or phrase.strip() == '': 
        return False
    
    phrase = phrase.strip()
    if phrase in __ext_phrases:
        return True
    return False



# def tell_time():
#     time = datetime.datetime.now().strftime("%I:%M %p")
#     talk("Current time is " + time)

# def play_song(voice_input):
#     filtered = erase_phrase_from_sentence(voice, "play song")
#     pywhatkit.playonyt(filtered)

# def tell_about(voice_input):
#     try:
#         interest = erase_phrase_from_sentence(voice_input, "tell me about")
#         info = wikipedia.summary(interest, 1)
#         talk(info)
#     except:
#         talk("Cannot find relevant information. Please try again later.")
# while True:
#     voice_input = take_voice_input()
#     print(voice_input)

#     if "time" in voice_input:
#         tell_time()

#     elif "news for today" in voice_input:
#         tell_news()
    
#     elif "play" in voice_input:
#         play_song(voice_input)
    
#     elif "tell me about" in voice_input:
#         tell_about(voice_input)
    
#     elif "joke" in voice_input:
#         talk(pyjokes.get_joke())

#     elif "where are we" in voice_input:
#         talk("We are in a session with D A V teachers. They are liking it.")
    
#     elif "quit" in voice_input or "exit" in voice_input:
#         talk("Goodbye! Have a great day!")
#         break
    
#     else:
#         talk("Sorry! I did not follow. Can you repeat?")
