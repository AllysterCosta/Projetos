#  Importando as bibliotecas necessárias


from services.clima_service import buscar_clima
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/clima")
def api_clima():
    clima = buscar_clima()
    return jsonify(clima)


if __name__ == "__main__":
    app.run(debug=True)
