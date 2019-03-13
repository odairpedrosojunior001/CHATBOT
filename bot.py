#-*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer #importar 2 bibliotecas ( lista treinamento ; bot)
from chatterbot import ChatBot

bot = ChatBot('Test') 

convImei=[
            "oi",
            "olá,em que posso ajudar?",
            "olá",
            "bom dia",
            "como faturar um pedido de celular no mobile?",
            "realizar a separação no mobile,coletar IMEI e finalizar",
            "muito obrigado","de nada."
]

bot.set_trainer(ListTrainer) #iniciar a lista com bot
bot.train(convImei) #treinar a lista com Machine Learning

while True: # laço para a interação de perguntas e respostas do bot 
    quest = input("Você:")
    response = bot.get_response(quest)

print("Bot:",response) # print com o retorno da resposta do bot se estiver dentro do laço e da variavel de lista.


