import os
import speech_recognition as sr
import pyttsx3
pyttsx3.speak("Welcome To Voice Assistant Tool using python")
pyttsx3.speak("What Software you want to open")
r = sr.Recognizer()
print("Please say what Command Do you want to run : ", end='')
with sr.Microphone() as source:
	print("Start Saying")
	audio = r.listen(source)
	print("Speak Done")
p = r.recognize_google(audio)
#p = input("Run any gui program using chat with me : ")
#while True:
if ((("run" in p) or ("execute" in p) or ("open" in p)) and (("chrome" in p) or ("browser" in p))):
	pyttsx3.speak(" I Understand what do you want you want to open Chrome browser")
	os.system("chrome")
elif ((("run" in p) or ("execute" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p))):
	pyttsx3.speak(" I Understand what do you want you want to open Notepad text editor")
	os.system("notepad")
elif ((("run" in p) or ("execute" in p) or ("open" in p)) and (("VLC" in p) or ("media player" in p))):
	pyttsx3.speak(" I Understand what do you want you want to open VLC media Player")
	os.system("vlc")
elif ((("run" in p) or ("execute" in p) or ("open" in p)) and (("Visual" in p) or ("Studio Code" in p))):
	pyttsx3.speak(" I Understand what do you want you want to open Visual Studio code")
	os.system("code .")
elif ((("run" in p) or ("execute" in p) or ("open" in p)) and (("Command" in p) or ("CMD" in p))):
	pyttsx3.speak(" I Understand what do you want you want to open CMD")
	os.system("cmd")
elif ((("run" in p) or ("execute" in p) or ("open" in p)) and (("Camera" in p) or ("Khamera" in p) or ("image" in p))):
	pyttsx3.speak("I Understand what do you want you want to open Camera")
	os.system("start microsoft.windows.camera:")
elif ("Show" in p) or ("list" in p) or ("all" in p) or ("Virual" in p) or ("Machine" in p):
	pyttsx3.speak("I Understand what do you want you want to see all virual machines in virtualbox")
	os.system("vboxmanage list vms")
elif ("open" in p) or ("Machine" in p) or ("Redhat 8.4" in p) or ("Devops" in p):
	pyttsx3.speak("I Understand what do you want you want to Open Redhat 8.4 Devops machine")
	os.system("vboxmanage startvm 0406fd44-4c2b-4469-b697-ace8fc78ac8b")
elif ("open" in p) or ("Machine" in p) or ("Redhat latest" in p) or ("Redhat 8.0" in p):
	pyttsx3.speak("I Understand what do you want you want to Open Redhat 8.0 machine ")
	os.system("vboxmanage startvm 2964cb1c-078f-4508-aaff-60c48bc4951d")
elif ("open" in p) or ("machine" in p) or ("Minicube" in p) or ("Kubenetes" in p) or ("docker" in p):
	pyttsx3.speak("I Understand what do you want you want to Open Kubenetes machine ")
	os.system("vboxmanage startvm 8d7ee1a5-7b76-4436-b158-df77dc393106")
elif (("exit" in p) or ("quit" in p)):
	pyttsx3.speak(" Ok I am exiting")
	exit()	
else:
    	pyttsx3.speak("Not Listen proper")