# KidBit Assistant
Use this python package to create your own talking assistant.

## Installation

`pip install kidbit_assistant`

## How to use?
After installing the `kidbit_assistant` package, import the package into your program by typing:

`from kidbit_assistant import *`

## List of Methods
The `kidbit_assistant` package provides you with a list of in-built methods which can be leveraged to make your own customized assistant. All the methods are defined below.
#### listen()
Listens for the input from the microphone.

#### speak(text)
Speaks out `text` variable you provide as input.

#### set_voice(number)
Pass a `number` to set a specific voice for your assistant. Every `number` corresponds to a unique voice as defined below in the list.

**Set of valid `numbers`:**
```
NUMBER      PERSON        ACCENT
0           Alex        English US
7           Daniel      English Great Britain
10          Fiona       English Scotland
11          Fred        English US
17          Karen       English Australia
28          Moira       English Ireland
32          Rishi       English India
33          Samantha    English US
37          Tessa       English South Africa
40          Veena       English India
41          Victoria    English US
```

### get_google_news()
Fetches live Google News.

### get_joke()
Fetches a random computer science joke.

### play_on_youtube(song)
Plays `song` on YouTube.

### get_time_in_gmt()
Gets the current time in GMT.

### erase_from_voice(voice, phrase_1, phrase_2, ...)
Erases all the occurences of `phrase_1`, `phrase_2` and subsequent phrases from `voice` and returns it.

### convert_time(utc_time, code)
Converts the `utc_time` provided to the timezone with the `code` provided.
**List of acceptable codes:**
```
CODES       TIMEZONE
ist         Indian Standard Time
aedt        Australian Eastern Daylight Time
pdt         Pacific Daylight Time
gmt         Greenwich Mean Time
utc         Coordinated Universal Time
cst         Central Standard Time
brt         Brasilia Time
brst        Brasília Summer Time
sast        South African Standard Time
```

## Sample Code

```
from kidbit_assistant import *
voice = listen()

if "alexa" in voice:  
  if "joke" in voice:
      joke = get_joke()
      speak(joke)
  
  elif "news" in voice:
      news = get_google_news()
      speak(news)
  
  elif "where are we" in voice:
      speak("We live on Earth")

  elif "see you later" in voice or "quit" in voice or "exit" in voice:
      speak("Goodbye! Have a great day!")
  
  else:
      speak("I don't understand.")
else:
    speak("Are you saying something? Say with alexa in it.")
```
