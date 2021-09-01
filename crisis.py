# salut je me sens seul go créé un pote
# inspiration Charlie Code youtube

# import library

from urlib.request import urlopen			# for working with url
from googletrans import Translator			# for traduction
from random import choice					# for taking a random element
import speech_recognition as sortie			# for voice recognition
import pyttsx3								# convert text in audio 
import subprocess							# for openning application
import wolframalpha							# API of wall fram for counting
import webbrowser							# for open link
import wikipedia							# for database


# voice management
def assistant_voix(sortie):
	if sortie != None:
		voix = pyttsx3.init()
		print("A.I : " + sortie)
		voix.say(sortie)
		voix.runAndWait()

# cheking if we are connected
def internet():
	try:
		urlopen("https://www.google.com", timeout = 1)
		return True
	except:
		return False

#voice recognition
def reconnaissance():
	r = sr.Recognizer()
	pas_compris = "Désolé, je n'ai pas compris ."
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		r.pause_threshold = 0.7
		print("....")
		ausio = r.listen(source)
		if ineternet()
			try:
				vocal = recognize_google(audio, language = "fr-FR")
				print(vocal)
			except:
				assistant_voix(pas_compris)
		else:
			try:
				vocal = r.recognize_sphinx(audio, language = "fr-fr")
				print(vocal)
			except:
				assistant_voix(pas_compris)

def application(entree):
	if entree != None:
		dico-apps = {
		"note" : ["notepad","note pad"],
		"sublime" : ["sunlime text", "sublime texte"],
		"obs" : ["obs","obs capture","capture l'ecran"],
		"edge" : ["microsoft edge","edge"]
		}
		fini = False
		while not fini:
			for x in dico_apps["note"]:
				if x in entree.lower():
					assistant_voix("Ouverture de Notepad .")
					subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
					fini = True
			for x in dico_apps["sublime"]:
				if x in entree.lower():
					assistant_voix("Ouverture de sublime texte .")
					subprocess.Popen("")
					fini = True
			for x in dico_apps["obs"]:
				if x in entree.lower():
					assistant_voix("Ouverture de obs .")
					subprocess.Popen("")
					fini = True
			for x in dico_apps["edge"]:
				if x in entree.lower():
					assistant_voix("Ouverture de edge .")
					subprocess.Popen("")
					fini = True

	def calcul (entree):
		if entree != None 
				