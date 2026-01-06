from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    # Il faut 4 espaces ici pour être DANS la fonction
    return "Hello, DevOps!"

if __name__ == "__main__":
    # Il faut 4 espaces ici pour être DANS la condition if
    app.run(host="0.0.0.0", port=5000)