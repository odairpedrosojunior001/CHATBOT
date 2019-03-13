#-*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot('Célula Implantação')

#bot = ChatBot(
    #'Célula Implantação',
    #storage_adapter='chatterbot.storage.SQLStorageAdapter',
    #logic_adapters=[
        #'chatterbot.logic.MathematicalEvaluation',
        #'chatterbot.logic.TimeLogicAdapter'
    #],
    #database_uri='sqlite:///database.sqlite3'
#)

while True:  # laço para a interação de perguntas e respostas do bot
    quest = input("Você:")
    response = bot.get_response(quest)

# print com o retorno da resposta do bot se estiver dentro do laço e da variavel de lista.
print("Bot:", response)


trainer = ListTrainer(bot)

trainer.train([
    'Ola',
    'Ola,em que posso ajudar?',
    'Como posso faturar um pedido de celular no mobile?',
    'Primeiro realize a separação no mobile, coletando o IMEI, logo em seguida, finalize',
    'Quanto tempo demora para faturar?',
    'Cerca de 10 a 30 segundos'
])



