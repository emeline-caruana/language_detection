import glob

""" Cette classe nous permet de lire les fichiers textes """

listText = []

def getTexts(inputUser) :
    """Cette fonction sert à récupérer tous les textes se trouvant dans Train
        Le sous-dossier de Train est maintenant choisis automatiquement
    """

    mypath = "DataSet/Train/" + inputUser + "/*.txt"
    listText = glob.glob(mypath)

    count = 0
    for text in listText :
        textSplit = text.split("/")
        listText[count] = textSplit[3]
        count += 1

    return listText, inputUser
