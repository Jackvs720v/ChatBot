# Codigo a aplicaçao principal transformando a LLM em uma API

#Importa as bibliotecas
from fastapi import FastAPI, Body
from pydantic import BaseModel
from serenatto_bot import SerenattoBot

# inicia a api

app = FastAPI(title="Serenato Chatbot API")

#Instancia o bot

bot = SerenattoBot()

class MensagemRequest(BaseModel):
    mensagem: str

class MensagemResponse(BaseModel):
    resposta:str

#Criando as rotas

@app.post("/conversar", response_model=MensagemResponse)
def conversar(request: MensagemRequest):
     resposta = bot.responder(request.mensagem)
     return MensagemResponse(resposta=resposta)

@app.post("/resetar")
def resetar():
    bot.resetar()
    return {"Status":"Chat resetado com sucesso !"}


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
