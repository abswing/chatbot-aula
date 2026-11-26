# Servidor web do chatbot. A página (templates/index.html) já está pronta.
from flask import Flask, render_template, request, jsonify
#from agente import responder   # <- vamos ligar o cérebro aqui

from agente import responder

app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    dados = request.get_json()
    resposta = responder(dados["usuario"], dados["mensagem"])

    return jsonify({"resposta": resposta})


@app.route("/")
def pagina():
    return render_template("index.html")


# A página manda: POST /api/chat  com  {"usuario": "...", "mensagem": "..."}
# e espera de volta:                  {"resposta": "..."}
#
# TODO (juntos em aula): criar a rota /api/chat


if __name__ == "__main__":
    app.run(debug=True, port=5000)
