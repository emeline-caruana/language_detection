# -*- coding: utf-8 -*-
#!usr/bin/env python3.6
import re
import os
import webbrowser
from Vecteur import *
from Token import *
from ReadFiles import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

#Variables globales
windowMenu = Tk()
progressBar = ttk.Progressbar(windowMenu, mode="determinate", length="300")
chemin = ""
phrase = StringVar()
global window
global i
i = 0

def startProg() :
    """Cette fonction va créer tous nos dictionnaires automatiquement en arrière plan"""

    langues = ["Eng","Fra","Esp","Dut","Ger","Ita"]
    for myFile in langues :
        myFile = myFile + "Dico.txt"
        if os.path.isfile(myFile) :
            os.remove(myFile)
            print("file ", myFile, "removed")

    count = 0


    for j in range(len(langues)):
        effacerOcc()
        inputUser = langues[j]
        listTexts, inputUser = ReadFiles.getTexts(inputUser)
        for name in listTexts :
            progressBar.step(count)
            count += 1
            windowMenu.update()
            path = "DataSet/Train/" + inputUser + "/" + name
            contenu = lireF(path)
            #occ_uni(contenu)
            occ_bi(contenu)
            ecrireDico("Dico.txt", inputUser)

    completeDico("FraDico.txt","EngDico.txt")
    completeDico("FraDico.txt","EspDico.txt")
    completeDico("FraDico.txt","ItaDico.txt")
    completeDico("FraDico.txt","DutDico.txt")
    completeDico("FraDico.txt","GerDico.txt")
    completeDico("EspDico.txt","EngDico.txt")
    completeDico("EspDico.txt","FraDico.txt")
    completeDico("EspDico.txt","ItaDico.txt")
    completeDico("EspDico.txt","GerDico.txt")
    completeDico("EspDico.txt","DutDico.txt")
    completeDico("EngDico.txt","FraDico.txt")
    completeDico("EngDico.txt","EspDico.txt")
    completeDico("EngDico.txt","DutDico.txt")
    completeDico("EngDico.txt","GerDico.txt")
    completeDico("EngDico.txt","ItaDico.txt")
    completeDico("GerDico.txt","FraDico.txt")
    completeDico("GerDico.txt","EspDico.txt")
    completeDico("GerDico.txt","DutDico.txt")
    completeDico("GerDico.txt","EngDico.txt")
    completeDico("GerDico.txt","ItaDico.txt")
    completeDico("DutDico.txt","FraDico.txt")
    completeDico("DutDico.txt","EspDico.txt")
    completeDico("DutDico.txt","EngDico.txt")
    completeDico("DutDico.txt","GerDico.txt")
    completeDico("DutDico.txt","ItaDico.txt")
    completeDico("ItaDico.txt","FraDico.txt")
    completeDico("ItaDico.txt","EspDico.txt")
    completeDico("ItaDico.txt","DutDico.txt")
    completeDico("ItaDico.txt","GerDico.txt")
    completeDico("ItaDico.txt","EngDico.txt")

def openFile() :
    """Cette fonction prend le chemin du fichier choisis dans la boite de dialogue une fois qu'on a cliqué sur le bouton "fichier"""
    filename = filedialog.askopenfilename(initialdir = "/",title = "Choisissez un fichier texte", filetypes = (("txt files","*.txt"),("all files","*.*")))
    global chemin
    chemin = filename

def checkString() :
    """ Cette fonction vérifie si les conditions de recherches sont bien remplies par l'utilisateur.
        Si l'utilisateur a choisis un texte il ne doit pas entrer de phrases et inversement.
    """

    if chemin != "" and phrase.get() == "" :
        choiceText(chemin)
    elif phrase.get() != "" and chemin == "" and not phrase.get().isdigit() :
        choicePh(phrase.get())
    elif chemin != "" and phrase.get() != "" :
        messagebox.showinfo(message="Vous ne devez choisir qu'un mode de détection")
    elif phrase.get().isdigit() :
        messagebox.showinfo(message="Vous ne devez entrer que des lettres")

def choiceText(fileTxt) :
    """ Cette fonction prend le chemin du fichier choisis et extrait seulement le nom du fichier puis appelle la fonction result()
        Elle est appelée si l'utilisateur a choisit un texte et qu'il a cliqué sur le boutton "Détecter la langue"
    """
    effacerOcc()
    global chemin
    contenu = lireF(chemin)
    chemin = chemin.split("/")
    chemin = chemin[len(chemin)-1].split(".")
    result(chemin[0], contenu)


def choicePh(words) :
    """ Cette fonction prend la phrase entrée par l'utilisateur et appelle la fonction result()
        Elle est appelée si l'utilisateur a choisit d'écrire une phrase et qu'il a cliqué sur le boutton "Détecter la langue"
    """
    effacerOcc()
    global i
    i += 1
    contenu = lireP(words)
    fichierTest = "phrase"+str(i)
    result(fichierTest, contenu)

def openWindow() :
    """ Cette fonction execute d'abord la fonction startProg() puis ouvre une nouvelle fenêtre """
    startProg()

    #Création de la fenêtre principale

    global window
    window = Toplevel(windowMenu)
    window.title("Detecteur de langue")
    window.geometry("2000x400")

    lF = LabelFrame(window, text="Choisissez un fichier texte", padx=20, pady=20)
    exitBtn = Button(window, text="Quitter", command=window.quit)
    findFile = Button(lF, text="Fichier", command=openFile)
    choiceTxt = Button(lF, text="Détecter la langue", command=checkString)

    #Ajout des widgets à la fenêtre
    expliLabel = Label(window, text="""\nPrécisions sur la similarité cosinus : \nComme la valeur cos θ est comprise dans "
        "l'intervalle [-1,1], la valeur -1 indiquera des vecteurs résolument opposés, 0 des vecteurs indépendants (orthogonaux) "
        "et 1 des vecteurs similaires.\nLes valeurs intermédiaires permettent d'évaluer le degré de similarité.\n""").pack()
    lF.pack(fill="both", expand="yes")
    findFile.pack()
    phraseBox = Entry(lF,textvariable=phrase).pack()
    choiceTxt.pack()

    exitBtn.pack()

def openReadMe() :
    """Cette fonction renvois sur la page web du README du github."""
    webbrowser.open('https://github.com/Tellarra/LanguageDetection/blob/master/README.md')

def result(fichierTest, contenu) :
    """ Cette fonction nous donne le résultat obtenus après le calcule des similaritées
        cosinus entre les dictionnaires créées précedemment et celui du texte ou de la phrase
    """
    occ_bi(contenu)
    ecrireDico("Dico.txt",fichierTest)
    file = fichierTest + "Dico.txt"
    dicoTest = recupVect(file)
    completeDico("EspDico.txt",file)
    completeDico("EngDico.txt",file)
    completeDico("FraDico.txt",file)
    completeDico("GerDico.txt",file)
    completeDico("DutDico.txt",file)
    completeDico("ItaDico.txt",file)

    normeTest = normeVect(file)
    simCosEng = simCosinus("EngDico.txt",file)
    simCosFra = simCosinus("FraDico.txt",file)
    simCosEsp = simCosinus("EspDico.txt",file)
    simCosDut = simCosinus("DutDico.txt",file)
    simCosGer = simCosinus("GerDico.txt",file)
    simCosIta = simCosinus("ItaDico.txt",file)

    if(simCosEng < 0) and (simCosEsp < 0) and (simCosFra < 0) and (simCosGer < 0):
        labelRes = Label(window, text="""Puisque tous les résultats des similarités cosinus sont inférieures à 0, alors le texte Test est un texte d'une langue ne faisant pas partie des langues de notre base de données.\nNous obtenons les résultats suivants pour les calculs de similarité avec l'anglais, le français, l'espagnol et l'allemend respectivement : \n"""+str(simCosEng)+", "+str(simCosFra)+", "+str(simCosEsp)+", "+str(simCosGer)+" .\n")
        labelRes.pack()
        #print("""Puisque tous les résultats des similarités cosinus sont inférieures à 0, alors le texte Test est un texte d'une langue ne faisant pas partie des langues de notre base de données.\nNous obtenons les résultats suivants pour les calculs de similarité avec l'anglais, le français et l'espagnol respectivement : \n"""+str(simCosEng)+", "+str(simCosFra)+", "+str(simCosEsp)+" .\n")
    elif(simCosEng == 1.0) or ((simCosEng > simCosFra >= simCosEsp >= simCosGer) or (simCosEng > simCosEsp >= simCosFra >= simCosGer) or (simCosEng > simCosFra >= simCosGer >= simCosEsp) or (simCosEng > simCosEsp >= simCosGer >= simCosFra) or (simCosEng > simCosGer >= simCosFra >= simCosEsp) or (simCosEng > simCosGer >= simCosEsp>= simCosFra)):
        labelRes = Label(window, text="Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour l'anglais, donc ce texte est un texte en anglais. Taux de similarité : "+str(simCosEng)+" .\n")
        labelRes.pack()
        #print("Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour l'anglais, donc ce texte est un texte en anglais. Taux de similarité : "+str(simCosEng)+" .\n")
    elif(simCosFra == 1.0) or ((simCosFra > simCosEng >= simCosEsp >= simCosGer) or (simCosFra > simCosEsp >= simCosEng >= simCosGer) or (simCosFra > simCosEng >= simCosGer >= simCosEsp) or (simCosFra > simCosEsp >= simCosGer >= simCosEng) or (simCosFra > simCosGer >= simCosEng >= simCosEsp) or (simCosFra > simCosGer >= simCosEsp>= simCosEng)):
        labelRes = Label(window, text="Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour le français, donc ce texte est un texte en français. Taux de similarité : "+str(simCosFra)+" .\n")
        labelRes.pack()
        #print("Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour le français, donc ce texte est un texte en français. Taux de similarité : "+str(simCosFra)+" .\n")
    elif(simCosEsp == 1.0) or ((simCosEsp > simCosEng >= simCosFra >= simCosGer) or (simCosEsp > simCosFra >= simCosEng >= simCosGer) or (simCosEsp > simCosEng >= simCosGer >= simCosFra) or (simCosEsp > simCosFra >= simCosGer >= simCosEng) or (simCosEsp > simCosGer >= simCosEng >= simCosFra) or (simCosEsp > simCosGer >= simCosFra >= simCosEng)):
        labelRes = Label(window, text="Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour l'espagnol, donc ce texte est un texte en espagnol. Taux de similarité : "+str(simCosEsp)+" .\n")
        labelRes.pack()
        #print("Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour l'espagnol, donc ce texte est un texte en espagnol. Taux de similarité : "+str(simCosEsp)+" .\n")
    elif(simCosGer == 1.0) or ((simCosGer > simCosEng >= simCosFra >= simCosEsp) or (simCosGer > simCosFra >= simCosEng >= simCosEsp) or (simCosGer > simCosEng >= simCosEsp >= simCosFra) or (simCosGer > simCosFra >= simCosEsp >= simCosEng) or (simCosGer > simCosEsp >= simCosEng >= simCosFra) or (simCosGer > simCosEsp >= simCosFra >= simCosEng)):
        labelRes = Label(window, text="Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour l'allemand, donc ce texte est un texte en allemand. Taux de similarité : "+str(simCosGer)+" .\n")
        labelRes.pack()

    global chemin
    chemin = ""

#Création de la fenêtre principale
windowMenu.title("Detecteur de langage")
windowMenu.geometry("2000x400")

#Création des widgets
introLabel = Label(windowMenu, text="Bienvenu sur notre programme de détection de la langue"
    "\nSi vous voulez détecter la langue d'un texte ou d'une phrase, cliquez sur le bouton Accéder au programme."
    "\nSi vous souhaitez en savoir plus sur l'utilisation du programme, cliquez sur ReadMe.")
exitBtn = Button(windowMenu, text="Quitter", command=windowMenu.quit)
detectBtn = Button(windowMenu, text="Accéder au programme", command=openWindow)
readmeBtn = Button(windowMenu, text="ReadMe", command=openReadMe)

#Ajout des widgets à la fenêtre
introLabel.pack()
detectBtn.pack()
readmeBtn.pack()
progressBar.pack()
exitBtn.pack()

#Affichage de la fenêtre
windowMenu.mainloop()
