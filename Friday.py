from datetime import datetime
import win32com.client 


speaker = win32com.client.Dispatch("SAPI.SpVoice")
i=0
while (i==0):
    ch=str(input("What's your command: "))
    if ch=="hey friday":
        print("What's up Boss")
        mytext="What's up Boss"
        speaker.Speak(mytext)
    elif ch=="hey buddy":
        print("Yes Boss")
    elif ch=="hey bud":
        print("Good to see you too sir")
    elif ch=="fri":
        time = datetime.now().time()
        print("Current time is:",time)
    elif ch=="day":
        today=datetime.today()
        print("Today's date is: ",today)
    elif ch=="stop":
        i=1
        print("Bye Sir")
    elif ch=="i said stop it":
        i=1
        print("Okay Sir")
    elif ch=="would you stop":
        i=1
        print("Aye aye Captain!!")
    elif ch=="can you stop":
        print("But I don't want to    ಥ_ಥ")
    elif ch=="glad to have you back buddy":
        print("That's my Pleasure Boss")
