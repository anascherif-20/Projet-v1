from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

mots = ["chat", "maison", "ecole", "python", "soleil"]

mot = random.choice(mots)
lettres_trouvees = []
tentatives = 6
message = ""

dessins = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
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

@app.route("/", methods=["GET", "POST"])
def accueil():
    global mot, lettres_trouvees, tentatives, message

    if request.method == "POST":
        lettre = request.form["lettre"].lower()

        if lettre in mot:
            message = "Bonne réponse !"
            if lettre not in lettres_trouvees:
                lettres_trouvees.append(lettre)
        else:
            message = "Mauvaise réponse !"
            tentatives -= 1

    affichage = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "

    gagne = True
    for lettre in mot:
        if lettre not in lettres_trouvees:
            gagne = False

    if tentatives == 0:
        message = "Perdu ! Le mot était : " + mot

    if gagne == True:
        message = "Bravo, tu as gagné ! Le mot était : " + mot

    return render_template(
        "index.html",
        affichage=affichage,
        tentatives=tentatives,
        message=message,
        dessin=dessins[tentatives]
    )

@app.route("/restart")
def restart():
    global mot, lettres_trouvees, tentatives, message

    mot = random.choice(mots)
    lettres_trouvees = []
    tentatives = 6
    message = ""

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)