from flask import Flask

app = Flask(__name__)

@app.route("/")
def accueil():
    return "Bonjour Anas ! Flask fonctionne."

if __name__ == "__main__":
    app.run(debug=True)