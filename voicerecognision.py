import random
import sys

import speech_recognition # packages speechrecognition
import pyttsx3
import os
import webbrowser
import winsound
confirm = ''

r = speech_recognition.Recognizer()
dir = os.path.dirname(os.path.abspath(sys.argv[0]))

def speak(text): # text = parametros h opoia tha kathorizei ti tha leei h sinartisi speak
    engine = pyttsx3.init() # arxikopoihsh vivliothikis

    # taxitita omilias
    rate = engine.getProperty('rate') # etsi pairnoume tin idiotita
    engine.setProperty('rate', 170) # etsi rithmizoume tin idiotita

    # male or female voice, 0 = male, female = 1
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # volume tis fonis, min = 0, max = 1
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 0.8)

#a = engine.getProperty('')

    engine.say(text)
    engine.runAndWait()


def confirmation():
    global confirm
    with speech_recognition.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=1)  # ignore background noise
        speak("please confirm this is what you meant")
        audio2 = r.listen(source2)
        try:  # an katalavei ti tou eipame
            yesno = r.recognize_google(audio2)  # metafrazei auto pou eipame (audio2) se keimeno (myText)
        except:  # an den katalavei ti tou eipame
            speak("Didn't recognize what you said")
            speak("Is that what you meant?")
            listen()
            return
        if yesno.lower() == 'yes' or yesno.lower() == 'confirm' or yesno.lower == myText: confirm = True
        elif yesno.lower() == 'no' or yesno.lower() == 'cancel': confirm = False
        else: confirm = False
def listen():
    global myText
    with (speech_recognition.Microphone() as source2):
        r.adjust_for_ambient_noise(source2, duration=1) # ignore background noise
        speak("Say something")
        audio2 = r.listen(source2)
        try: # an katalavei ti tou eipame
            myText = r.recognize_google(audio2) # metafrazei auto pou eipame (audio2) se keimeno (myText)
        except: # an den katalavei ti tou eipame
            speak("Didn't recognize what you said")
            speak("Try again")
            listen()
            return
        print(myText)
        myText = myText.lower()
        speak("You said "+myText)

        if myText == "shut down":
            speak('Authorising distraction protocol')
            speak('in 3')
            speak('2')
            speak('1')
            speak('distraction protocol')
            #os.system('shutdown -s')
        if myText == 'youtube':
            with speech_recognition.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=1)  # ignore background noise
                speak("what video should i search?")
                audio3 = r.listen(source2)
                try:
                    searchyt = r.recognize_google(audio3)
                except:
                    speak("Didn't recognize what you said")
                    speak("Try again")
                    listen()
                    return
                searchyt = searchyt.lower()
                speak(searchyt)
                webbrowser.open("https://www.youtube.com/results?search_query="+searchyt)
        if myText == 'smells like teen spirit' or myText == 'song':
            speak('playing default song')
            winsound.PlaySound(dir + '/Nirvana - Smells Like Teen Spirit.wav', winsound.SND_FILENAME)
        if myText == 'game':
            speak('lets play rock paper scissors')
            def rps():
                with speech_recognition.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2, duration=1)  # ignore background noise
                    speak("what's your choice?")
                    audio4 = r.listen(source2)
                    try:
                        rpsme = r.recognize_google(audio4)
                    except:
                        speak("Didn't recognize what you said")
                        speak("Try again")
                        listen()
                        return
                    rpsme1 = rpsme.lower()
                    import random
                    rps_choises = ['paper', 'scissors', 'rock']
                    rps_system = random.choice(rps_choises)
                    if 'caesar' in rpsme or 'Caesar' in rpsme :
                        rpsme1 = 'scissors'

                    if (rpsme1 != "paper") and (rpsme1 != "scissors") and (rpsme1 != "rock"):
                        speak('Sorry, something went wrong.')
                        speak("Let's try again")
                        rps()
                    else:
                        speak('i chose' + str(rps_system))
                        if (rps_system == "rock" and rpsme1 == "rock") or (rps_system == "paper" and rpsme1 == "paper") or (rps_system == "scissors" and rpsme1 == "scissors"):
                            speak('we tied')
                        elif (rps_system == "rock" and rpsme1 == "scissors") or (rps_system == "paper" and rpsme1 == "rock") or (rps_system == "scissors" and rpsme1 == "paper"):
                            speak('i won')
                        elif (rpsme1 == "rock" and rps_system == "scissors") or (rpsme1 == "paper" and rps_system == "rock") or (rpsme1 == "scissors" and rps_system == "paper"):
                            speak('you won')
            rps()
        if myText == 'open ai':
            speak('opening ai platform')
            speak('recommended: chat GPT')
            webbrowser.open("https://chatgpt.com/")
        if myText == 'google this' or myText == 'google' or myText == 'search':
            with speech_recognition.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=1)  # ignore background noise
                speak("what should i google?")
                audio5 = r.listen(source2)
                try:
                    search = r.recognize_google(audio5)
                except:
                    speak("Didn't recognize what you said")
                    speak("Try again")
                    listen()
                    return
                search = search.lower()
                speak(search)
                webbrowser.open("https://www.google.com/search?q="+search+'&rlz=1C1GCEB_enGR967GR967&oq=bbbbb&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDExMzlqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8')




listen()