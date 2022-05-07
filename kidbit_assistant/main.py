import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import random
from gnewsclient import gnewsclient

__custom_joke = []
__engine = pyttsx3.init()
__voices = __engine.getProperty("voices")
__engine.setProperty("voice", __voices[0].id) # 40 is for en_IN, Female voice

def stop():
  __engine.stop()

def get_voice_id(voice_num):
  global __engine, __voices
  num_to_name = {
    0: 'Alex',
    7: 'Daniel',
    10: 'Fiona',
    11: 'Fred',
    17: 'Karen',
    28: 'Moira',
    32: 'Rishi',
    33: 'Samantha',
    37: 'Tessa',
    40: 'Veena',
    41: 'Victoria'
  }

  i = 0
  for voice in __voices:
    if voice_num in num_to_name and voice.name == num_to_name[voice_num]:
      return i
    elif voice_num not in num_to_name and 'en_IN' in voice.languages:
      return i
    i += 1

  return 1 # default value.

def set_voice(voice_num):
  global __engine, __voices

  v_id = 1
  try:
    v_id = get_voice_id(voice_num)
  except:
    pass
  __engine.setProperty("voice", __voices[v_id].id)


def add_custom_joke(joke):
  global __custom_joke
  if joke == None or joke.strip() == '' or joke in __custom_joke:
    return
  __custom_joke.append(joke)

############# Misc Functions #################
def erase_from_voice(voice, *phrases, debug = False):
  if voice == None or voice.strip() == '':
    return ""

  if phrases == None:
    return ""

  voice_filtered = voice.strip()

  for arg in phrases:
    voice_filtered = voice_filtered.replace(arg,"").strip()

  if debug:
    print("Voice:", voice)
    print("Phrase:", phrase)
    print("Voice filtered:", voice_filtered)

  return voice_filtered

def get_joke():
  return pyjokes.get_joke()

def get_custom_joke():
  global __custom_joke
  return random.choice(__custom_joke)

############# Speaking #################
def speak(phrase, *args, debug = True):
  if phrase == None:
    return
  phrase = str(phrase).strip()
  if phrase == '':
    return

  if "\n" in phrase:
    [speak_single(curr, debug) for curr in phrase.split("\n")]
  else:
    speak_single(phrase)

  for curr in args:
    if curr == None:
      return
    curr = str(curr).strip()
    if curr == '':
      return
    if "\n" in curr:
      [speak_single(curr_, debug) for curr_ in curr.split("\n")]
    else:
      speak_single(curr)



def speak_single(phrase, debug = True):
  if phrase == None or phrase.strip() == '':
    return
  phrase = phrase.strip()

  if debug:
    print(phrase)
  __engine.say(phrase)
  __engine.runAndWait()
############# Listening #################
def listen():
  r = sr.Recognizer()
  voice_input = ""
  try:
    print("Listening...")
    r.pause_threshold = 1
    with sr.Microphone() as source:
      voice = r.listen(source)
      voice_input = r.recognize_google(voice, language ='en-in')
      voice_input = voice_input.lower()
  except Exception as e:
    print("Error in taking voice input", e)
  return voice_input

############# Google News #################
def get_google_news(debug = False):
  client = gnewsclient.NewsClient(language = 'english',
                  location = 'India',
                  max_results=3)
  news_to_str = ''
  for news in client.get_news():
    news_to_str += (news['title'] + ".\n")

  if debug:
    print("News To Str: ", news_to_str)
  return news_to_str

############# Time Functions #################
def get_time_in_gmt(debug = False):
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
