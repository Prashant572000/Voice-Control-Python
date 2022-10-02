from os import system
import speech_recognition as sr
from pyttsx3 import speak
from webbrowser import open_new
from pywhatkit import search
from time import sleep
import datetime

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
     speak("Good Morning Sir ...")
elif hour >= 12 and hour < 18:
     speak("Good Afternoon Sir ...")
else:
     speak("Good Evening Sir ...")

speak("Welcome To Voice Assistant Tool")

while True:
	speak("Tell me how can i  help you")
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Start Saying")
		audio = r.listen(source)
		print("Speak Done")
	p = r.recognize_google(audio)
	print(p)

	if (("open" in p) and ("this PC"  in p)):
		speak(" I Understand I am opening This Pc program")
		system("explorer")
		sleep(10)
	elif (("open windows" in p) and ("c drive"  in p)):
		speak(" I Understand I am opening This Pc c drive for you")
		system("explorer c:")
		sleep(10)
	elif (("open windows" in p) and ("d drive"  in p)):
		speak(" I Understand I am opening This Pc d drive for you")
		system("explorer d: ")
		sleep(10)
	elif (("open windows" in p) and ("e drive"  in p)):
		speak(" I Understand I am opening This Pc e drive for you")
		system("explorer e: ")
		sleep(10)
	elif ((("run" in p) or ("execute" in p) or ("open" in p)) and (("chrome" in p) or ("browser" in p))):
		speak(" I Understand i am opening Chrome browser")
		system("chrome")
		sleep(10)
	elif (("close" in p)  and (("chrome" in p) or ("browser" in p))):
		speak(" I Understand i am closing Chrome browser")
		system("taskkill/im chrome.exe")
	
	elif (( ("run" in p) or ("execute" in p) or ("open" in p)) and (("Youtube" in p) or ("video" in p))):
		speak(" I Understand i am opening youtube")
		system("start www.youtube.com")

	elif (( ("execute" in p) or ("open" in p)) and (("linkdin" in p) or ("linkedin" in p) or ("my profile" in p))):
		speak("  I Understand i am opening your profile on linkdin")
		system("start https://www.linkedin.com/feed/")
	elif ((("open" in p)) and (("github" in p) or ("github account" in p) or ("my github account" in p))):
		speak("  I Understand i am opening your github account")
		system("start https://github.com/")
	elif (( ("execute" in p) or ("open" in p)) and (("gmail" in p) or ("mail" in p))):
		speak("  I Understand i am opening gmail")
		system("start https://mail.google.com/mail/u/0/#inbox")
	elif (( ("execute" in p) or ("open" in p)) and (("google" in p) or ("drive" in p))):
		speak("  I Understand i am opening google drive")
		system("start https://drive.google.com/drive/u/0/my-drive")
	elif ((("run" in p) or ("execute" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p))):
		speak("  I Understand i am opening Notepad text editor")
		system("notepad")
	elif (("close" in p)  and (("notepad" in p) or ("editor" in p))):
		speak(" I Understand i am closing Notepad browser")
		system("taskkill/im notepad.exe")

	elif ((("run" in p) or ("execute" in p) or ("open" in p)) and (("VLC" in p) or ("media player" in p))):
		speak("  I Understand i am opening VLC media Player")
		system("vlc")
	elif (("close" in p)  and (("vlc" in p) or ("media player" in p))):
		speak(" I Understand i am closing VLC")
		system("taskkill/im vlc.exe")

	elif ((("run" in p) or ("execute" in p) or ("open" in p)) and (("Visual" in p) or ("Studio Code" in p))):
		speak("  I Understand i am opening Visual Studio code")
		system("code .")
	elif (("close" in p)  and (("Visual" in p) or ("studio code" in p))):
		speak(" I Understand i am closing Chrome browser")
		system("taskkill/im Code.exe")

	elif ((("run" in p) or ("execute" in p) or ("open" in p)) and (("Command" in p) or ("CMD" in p))):
		speak("  I Understand i am opening CMD")
		open_new("cmd")
		sleep(10)
	elif (("close" in p)  and (("Command" in p) or ("CMD" in p))):
		speak(" I Understand i am closing Chrome browser")
		system("taskkill/im cmd.exe")

	elif ((("run" in p) or ("execute" in p) or ("open" in p)) and (("Camera" in p) or ("Khamera" in p) or ("image" in p))):
		speak(" I Understand i am opening Camera")
		system("start microsoft.windows.camera:")
		sleep(10)

	elif (("close" in p)  and (("camera" in p) or ("image" in p))):
		speak(" I Understand i am closing Chrome browser")
		system("taskkill/im WindowsCamera.exe")

	elif ((("run" in p) or ("open" in p)) and (("Microsoft Word" in p) or ("word" in p) or ("ms word" in p))):
		speak(" I Understand i am opening MS office Word")
		system("winword")
		sleep(10)
	elif ((("run" in p) or ("open" in p)) and (("Microsoft Excel" in p) or ("Excel" in p) or ("ms excel" in p) or ("excel" in p))):
		speak(" I Understand i am opening MS office Excel")
		system("excel")
		sleep(10)
	elif (("close" in p)  and (("Excel" in p) or ("ms excel" in p))):
		speak(" I Understand i am closing Ms Excel")
		system("taskkill/im EXCEL.exe")
	elif ((("run" in p) or ("open" in p)) and (("Microsoft Excel" in p) or ("Powerpoint" in p) or ("powerpoint" in p))):
		speak(" I Understand i am opening MS office Powerpoint")
		system("powerpnt")
		sleep(10)
	elif ("Show" in p) or ("list" in p) or ("all" in p) or ("Virual" in p) or ("Machine" in p):
		speak("I Understand what do you want you want to see all virual machines in virtualbox")
		system("vboxmanage list vms")
		sleep(10)
	elif (("open" in p) and ("Machine" in p)) or (("Redhat 8.4" in p) and ("Devops" in p)):
		speak(" I Understand i am opening Redhat 8.4 Devops machine")
		system("vboxmanage startvm 0406fd44-4c2b-4469-b697-ace8fc78ac8b")
		sleep(10)
	elif (("open" in p) and ("Machine" in p)) or (("Redhat latest" in p) or ("Redhat 8.0" in p)):
		speak(" I Understand i am opening Redhat 8.0 machine ")
		system("vboxmanage startvm 2964cb1c-078f-4508-aaff-60c48bc4951d")
		sleep(10)
	elif (("open" in p) and ("machine" in p)) or (("Minicube" in p) or ("Kubenetes" in p) or ("docker" in p)):
		speak(" I Understand i am opening Kubenetes machine ")
		system("vboxmanage startvm 8d7ee1a5-7b76-4436-b158-df77dc393106")
		sleep(10)
	elif (("okay Google" in p) or ("ok Google" in p) or ("Ok Google" in p) or ("Hii Google" in p) or ("hey Google" in p) or ("hi Google" in p) ):
		speak("What you want to Search tell me")
		with sr.Microphone() as source:
			print("Start Saying")
			audio = r.listen(source)
			print("Speak Done")
			target = r.recognize_google(audio)
			finalsearch = target.replace("Search", "")
		print("Got it You want to {0}".format(finalsearch))
		speak("Here is your result")
		search(finalsearch)
		sleep(20)
	elif (("exit" in p) or ("quit" in p) or ("go to hell" in p)):
		speak("Ok I understand thanks for using me see you next time by")
		exit()	
	else:
		speak("OOPS I am sorry couldn't Understand Please try again ")
