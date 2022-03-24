# KidBit Assistant
Use this python package to create your own alexa assistant. Enjoy!

## Installation

`pip install kidbit_assistant`

## List of Methods

#### listen()
Listens to the input from the user.

#### speak(text)
Speaks out whatever input you provide.

#### set_voice(number)
Pass an integer value to get different voices.

Set of valid numbers:
```
0  Alex, 'en_US'
7  Daniel, 'en_GB'
10 Fiona, 'en-scotland'
11 Fred, 'en_US'
17 Karen, 'en_AU'
28 Moira, 'en_IE'
32 Rishi, 'en_IN'
33 Samantha, 'en_US'
37 Tessa, 'en_ZA'
40 Veena, 'en_IN'
41 Victoria, 'en_US'
```

### get_google_news()
Fetches live Google News to you.

### get_joke()
Fetches a random computer science joke.

### identify_song(voice)
Identifies the song from the `voice`. Assumes either `play` or `song` or both present in the `voice`.

### play_on_youtube(song)
Plays song on YouTube.

### get_time_in_gmt()
Gets the current time in GMT.

### convert_time(utc_time, code)
Converts the `utc_time` provided to the timezone with the `code` provided. 

List of acceptable codes:
```
ist
aedt
pdt
gmt
utc
cst
brt
brst
sast
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
