#  Importando as bibliotecas necessárias
from services.moedas_service import buscar_moedas
from services.clima_service import buscar_clima
from services.noticias_service import buscar_noticias
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

# Rotas da aplicação


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/clima")
def api_clima():
    clima = buscar_clima()
    return jsonify(clima)


@app.route("/api/moedas")
def api_moedas():
    try:
        return buscar_moedas()
    except Exception as e:
        return {"error": str(e)}, 500


@app.route("/api/noticias")
def api_noticias():
    return buscar_noticias()


if __name__ == "__main__":
    app.run(debug=True)
