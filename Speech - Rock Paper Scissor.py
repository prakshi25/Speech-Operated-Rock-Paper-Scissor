import speech_recognition as sr
import pyttsx3
import random
r=sr.Recognizer()
text=""
possible_choices=["rock","paper","scissor"]

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[17].id)
text = ""

def speak(audio):
    engine.setProperty("rate", 180)
    engine.say(audio)
    engine.runAndWait()

speak("Hello! I am a Rock Paper Scissor Bot")
p1=""
while p1!="no" or text!="no":
    print("Please talk or say no to stop")
    with sr.Microphone() as source:
        speak("Do you wish to play Rock Paper Scissor?")
        print("Getting")
        audio_data=r.record(source,duration=6)
        text=r.recognize_google(audio_data)

        if text=="no" or p1=="no":
            print("Ok, Bye")
            speak("Ok, Bye")
            break

        speak("What is your name?")
        print("Getting")
        audio_data=r.record(source,duration=6)
        p1=r.recognize_google(audio_data)
        
        speak("Okay"+p1+"let's play Rock Paper Scissor")
        speak(p1+"you go first")
        print("Getting")
        audio_data=r.record(source,duration=6)
        user_choice=r.recognize_google(audio_data)
        print(p1," - ",user_choice)
        
        bot_choice=random.choice(possible_choices)
        speak(bot_choice)
        print("Bot - ",bot_choice)
        if user_choice == bot_choice:
            print("Bot     ",p1)
            print("1         1")
            speak("It's a tie. You both selected"+user_choice)
        elif user_choice == "rock":
            if bot_choice == "scissor":
                print("Bot     ",p1)
                print("0         1")
                speak("Rock smashes the scissor! You won")
            else:
                print("Bot     ",p1)
                print("1         0")
                speak("Paper covers the rock! You lost")
        elif user_choice == "paper":
            if bot_choice == "rock":
                print("Bot     ",p1)
                print("0         1")
                speak("Paper covers the rock! You won")
            else:
                print("Bot     ",p1)
                print("1         0")
                speak("Scissor cuts the paper! You lost")
        elif user_choice == "scissor":
            if bot_choice == "paper":
                print("Bot     ",p1)
                print("0         1")
                speak("Scissors cuts the paper! You won")
            else:
                print("Bot     ",p1)
                print("1         0")
                speak("Rock smashes the scissor! You lost")