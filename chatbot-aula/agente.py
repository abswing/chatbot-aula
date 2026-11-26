import truststore
truststore.inject_into_ssl()

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODELO = "gemini-3.5-flash-lite"

PERSONA = "Voce recebe os pedidos de uma pizzaria"

conversar = {}

def responder(usuario, mensagem):
    if usuario not in conversar:
        conversar[usuario] = client.chats.create(
            model= MODELO,
            config= types.GenerateContentConfig(system_instruction=PERSONA)
        )
    responder = conversar[usuario].send_message(mensagem)
    return responder.text

if __name__ == "__main__":
    while True:
        msg = input("Voce: ")
        if msg == "sair":
            break
        print("bot: ", responder("terminal", msg))