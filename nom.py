import random 
mots = ["chat", "maison", "ecole", "python", "soleil"]

mot = random.choice(mots)
lettres_trouvees = []
tentatives = 6

def afficher_mot():
    affichage = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    print(affichage)

def dessiner_pendu(tentatives):
    dessins = [
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """
        ]
    print(dessins[tentatives])

print("Bienvenue dans le jeu du pendu !")

while tentatives > 0:
    dessiner_pendu(tentatives)
    afficher_mot()
    print("Tentatives restantes :", tentatives)

    lettre = input("Entre une lettre : ")

    if lettre in mot:
        print("Bonne réponse !")
        if lettre not in lettres_trouvees:
            lettres_trouvees.append(lettre)
    else:
        print("Mauvaise réponse !")
        tentatives -= 1

    gagne = True
    for lettre in mot:
        if lettre not in lettres_trouvees:
            gagne = False

    if gagne == True:
        afficher_mot()
        print("Bravo, tu as gagné !")
        print("Le mot était :", mot)
        break

if tentatives == 0:
    dessiner_pendu(tentatives)
    print("Perdu !")
    print("Le mot était :", mot)
