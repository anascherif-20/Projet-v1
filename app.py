from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "pendu_secret_v2_2024"

MOTS = [
    "elephant", "girafe", "crocodile", "pingouin", "hippopotame",
    "tigre", "leopard", "gorille", "dauphin", "requin",
    "python", "ordinateur", "algorithme", "programmation", "clavier",
    "javascript", "navigateur", "serveur", "microphone", "ecran",
    "volcan", "galaxie", "planete", "montagne", "cascade",
    "chocolat", "croissant", "baguette", "fromage", "croissant",
    "aventure", "mystere", "tresor", "pirate", "explorateur",
    "bibliotheque", "architecture", "intelligence", "universite", "laboratoire",
]

MAX_ERREURS = 6


def init_session():
    session["mot"] = random.choice(MOTS)
    session["correctes"] = []
    session["incorrectes"] = []
    session["message"] = ""
    session["message_type"] = ""


@app.route("/", methods=["GET", "POST"])
def accueil():
    if "mot" not in session:
        init_session()

    mot = session["mot"]
    correctes = list(session["correctes"])
    incorrectes = list(session["incorrectes"])
    erreurs = len(incorrectes)
    gagne = all(l in correctes for l in mot)
    perdu = erreurs >= MAX_ERREURS

    if request.method == "POST" and not gagne and not perdu:
        lettre = request.form.get("lettre", "").lower().strip()
        if len(lettre) == 1 and lettre.isalpha():
            if lettre in correctes or lettre in incorrectes:
                session["message"] = "Tu as déjà essayé cette lettre !"
                session["message_type"] = "warn"
            elif lettre in mot:
                correctes.append(lettre)
                session["correctes"] = correctes
                session["message"] = "Bonne réponse !"
                session["message_type"] = "good"
            else:
                incorrectes.append(lettre)
                session["incorrectes"] = incorrectes
                erreurs += 1
                session["message"] = "Mauvaise lettre..."
                session["message_type"] = "bad"

    gagne = all(l in correctes for l in mot)
    perdu = erreurs >= MAX_ERREURS

    if gagne:
        statut = "gagne"
        session["message"] = f'Bravo ! Tu as trouvé "{mot.upper()}" !'
        session["message_type"] = "win"
    elif perdu:
        statut = "perdu"
        session["message"] = f"Perdu ! Le mot était : {mot.upper()}"
        session["message_type"] = "lose"
    else:
        statut = "en_cours"

    affichage = [l if l in correctes else "_" for l in mot]

    return render_template(
        "index.html",
        affichage=affichage,
        mot=mot,
        erreurs=erreurs,
        max_erreurs=MAX_ERREURS,
        tentatives=MAX_ERREURS - erreurs,
        message=session.get("message", ""),
        message_type=session.get("message_type", ""),
        correctes=correctes,
        incorrectes=incorrectes,
        utilisees=correctes + incorrectes,
        statut=statut,
        alphabet="abcdefghijklmnopqrstuvwxyz",
    )


@app.route("/restart")
def restart():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
