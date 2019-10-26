from datetime import datetime
import pyttsx3 
import win32com.client 
import speech_recognition as sr  
import os

#Use female voice
converter = pyttsx3.init()
voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0" 
converter.setProperty('voice', voice_id) 
converter.runAndWait()

i=0
while (i==0):
    ch=str(input("What's your command: "))
    if ch=="hey friday":
        print("What's up Boss")
        mytext="What's up Boss"
    elif ch=="hey buddy":
        print("Yes Boss")
        mytext="Yes Boss"
    elif ch=="hey bud":
        print("Good to see you too sir")
        mytext="Good to see you too sir"
    elif ch=="fri":
        time = datetime.now().time()
        print("Current time is:",time)
        mytext="Current time is:",time
    elif ch=="day":
        today=datetime.today()
        print("Today's date is: ",today)
        mytext="Today's date is: ",today
    elif ch=="stop":
        i=1
        print("Bye Sir")
        mytext="Bye Sir"
    elif ch=="i said stop it":
        i=1
        print("Okay Sir")
        mytext="Okay Sir"
    elif ch=="would you stop":
        i=1
        print("Aye aye Captain!!")
        mytext="Aye,aye,Captain!!"
    elif ch=="can you stop":
        print("But I don't want to    ಥ_ಥ")
        mytext="But I don't want to"
    elif ch=="glad to have you back buddy":
        print("That's my Pleasure Boss")
        mytext="That's my Pleasure Boss"
    elif ch=="open":
        print("Apps that I can open are:")
        mytext="Apps that I can open are"
        print("")
    
    converter.say(mytext)
    converter.runAndWait()
