## Language Detection / Détection de langue

Le but de ce projet est d'avoir un programme capable de détecter la langue d'un texte.

## Organisation du projet
Notre projet s'organise simplement :
```
La racine
  |__________ DataSet
  |             |_______ Evaluation -> Fichiers texts qui nous permettent de tester notre programmes après l'avoir entraîné
  |             |_______ Test -> Fichiers texts qui nous permettent de tester notre programme en démonstration
  |             |_______ Train -> Fichiers texts qui entraînent notre programmes à construire les dictionnaires des langues
  | 
  |__________ LangDetection
  |             |___________ Final.py
  |             |___________ ReadFiles.py
  |             |___________ Token.py
  |             |___________ Vect.py
  |
  |____ Main.py
  |____ README.md
```

## Faire tourner le programme

Dans un terminal il suffit d'entrer la commande `python3 Main.py`
Vous verrez une fenêtre apparaître dans laquelle vous pourrez choisir entre lire ce README ou bien ouvrir une autre fenêtre sur laquelle vous avez la détection de langue.

### Fenêtre "Détecteur de langue"

Dans cette fenêtre vous pourrez :

### 1. Cliquer sur le bouton `fichier` 
Celui-ci permet d'aller cherche un fichier avec une extension .txt dans votre ordinateur.
Une fois le fichier récupéré, cliquez sur `Détecter la langue` et le résultat s'affiche en bas de la fenêtre.

### 2. Ecrire du texte dans la zone dédiée
Cette zone de texte est utilisée par le programme pour identifier la langue de ce que vous avez tapé.
Une fois le ou les mots entrés, cliquez sur `Détecter la langue` et le résultat s'affiche en bas de la fenêtre.

### Précautions d'utilisation
Vous ne devez pas choisir un texte et entrer des mots dans la zone de texte, choisissez seulement un des deux moyens de détection.  
Vous ne pouvez pas entrer de numéros dans la zone de texte.
Vous ne pouvez pas lire de fichier dans un autre format que .txt

## Fermer le programme
Si vous souhaitez fermer le programme, vous pouvez appuyer à tout moment sur le bouton `Quitter`

