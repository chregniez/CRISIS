# salut je me sens seul go créé un pote
# inspiration Charlie Code youtube

# import library

from urllib.request import urlopen			# for working with url
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
		audio = r.listen(source)
		if internet():
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
		"sublime" : ["sublime text", "sublime texte"],
		"vmware" : ["vm","vm ware","vm war"],
		"firefox" : ["mozzilla firefox","mozilla","firefox"]
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
			for x in dico_apps["firefox"]:
				if x in entree.lower():
					assistant_voix("Ouverture de firefox .")
					subprocess.Popen("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
					fini = True

def calcul (entree):
	if entree != None:
		traducteur = Translator()
		traduction = traducteur.translate(text = entree, dest = "en").text
		app_id ="PLACEZ VOTRE IDEZ ICI / YOUR ID TAKE PLACE HERE !!!"
		client = wolframalpha.Client(app_id)
		res = client.query(traduction)
		try:
			reponse= next(res.results).text
			traduction_reponse = traducteur.translate(text = reponse,dest = "fr").text
			assistant_voix("Le résultat est %d ." %(traduction_reponse))
		except:
			assistant_voix("Il y'a eu une erreur, désolé . ")

def sur_le_net(entree):
	if entree != None:
		if "youtube" in entree.lower():
			indx = entree.lower().split.index("youtube") # we maybe can delete this line ( test before ) 
			recherche = entree.lower()split()[indx + 1:]
		if len(recherche) != 0:
			assistant_voix("recherche sur Youtube .")
			webbrowser.open("http://www.youtube.com/results?search_query="+"+".join(recherche),new = 2)
		elif "wikipedia" in  entre.lower():
			wikipedia.set_lang("fr")
			try:
				indx = entree.lower().split.index("wikipedia")
				recherche = entre.lower().replace("cherche sur wiki")
				if len(recherche) != 0:
					resultat = wikipedia.summary(recherche, sentences = 1)
					assistant_voix("recherche sur Wikipédia .")
					assistant_voix(resultat)
			except:
				assistant_voix("Désoler, aucune page n'a été trouvée")
		else:
			if "google" in entre.lower():
				indx = entree.lower()split().index("google")
				recherche = entree.lower()split[indx + 1:]
				if len(recherche) != 0:
					assistant_voix("recherche sur Google .")
					webbrowser.open("http://www.google.com/results?search_query="+"+".join(recherche),new = 2)	
			elif "cherche" in entre.lower():
				indx = entree.lower()split().index("cherche")
				recherche = entree.lower()split[indx + 1:]
				if len(recherche) != 0:
					assistant_voix("recherche sur Google .")
					webbrowser.open("http://www.google.com/results?search_query="+"+".join(recherche),new = 2)
			if "recherche" in entre.lower():
				indx = entree.lower()split().index("recherche")
				recherche = entree.lower()split[indx + 1:]
				if len(recherche) != 0:
					assistant_voix("recherche sur Google .")
					webbrowser.open("http://www.google.com/results?search_query="+"+".join(recherche),new = 2)

def main():
	assistant_voix("Bonjour monsieur, je suis votre assistant de bureau. Dites-moi ce que je peux faire pour vous .")
	fermer = ["arrêtes-toi","tais-toi"]
	ouvrir = ["ouvrir","peut-tu ouvrir"]
	cherche  = ["cherche sur youtube","cherche sur google","cherche sur wikipedia","cherche","peut-tu faire cette recherche"]
	calculs = ["calcule la somme de","calcule la différence de","calcule le produit de","calcule le quotient de",]
	actif = True
	while actif:
		if (entree := reconnaissance()) is not None:
			for x in range(len(fermer)):
				if fermer[x] in entree.lower():
					assistant_voix("A la prochaine Monsieur .")
					actif = False
				for x in range(len(ouvrir)):
					if fermer[x] in entree.lower():
					application(entree)
					break
				for x in range(len(chercher)):
					if fermer[x] in entree.lower():
					application(entree)
					break
				for x in range(len(calcul)):
					if fermer[x] in entree.lower():
					application(entree)
					break


if __name__ == '__main__':
	main()