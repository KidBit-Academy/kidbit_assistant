from main import *

while True:
    voice = listen()
    if "alexa" in voice:  
      if "joke" in voice:
          joke = get_joke()
          speak(joke)
      
      elif "news" in voice:
          news = get_google_news()
          speak(news)
      
      elif "where are we" in voice:
          speak("D A V")

      elif "see you later" in voice or "quit" in voice or "exit" in voice:
          speak("Goodbye! Have a great day!")
          break
      
      elif "calculate" in voice:
        speak("What do you want to do?")
        voice2 = listen()
        if "add" in voice2:
            speak("Speak number 1")
            n1 = int(listen())
            speak("Speak number 2")
            n2 = int(listen())
            speak("Addition of two numbers is ")
            speak(str(n1 + n2))

        elif "subtract" in voice2:
            speak("Speak number 1")
            n1 = int(listen())
            speak("Speak number 2")
            n2 = int(listen())
            speak("Addition of two numbers is ")
            speak(str(n1 - n2))
        else:
            speak("Sorry I don't understand.")

      else:
          speak("I don't understand.")
    else:
        speak("Are you saying something? Say with alexa in it.")
