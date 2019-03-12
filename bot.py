#-*-coding: utf-8 -*-
from chatterbot.trainers import ListTrainer #importar 2 bibliotecas ( lista treinamento ; bot)
from chatterbot import chatterbot

bot=ChatBot('test') 

conv_Imei=["oi","olá","olá","bom dia","como faturar um pedido de celular no mobile?","realizar a separação no mobile,coletar IMEI e finalizar","muito obrigado","de nada"]

bot.set_trainer(ListTrainer) #iniciar a lista com bot
bot.train(conv_IMEI) #treinar a lista com Machine Learning

while True: # laço para a interação de perguntas e respostas do bot 
    pergunta = input("Você:")
    resposta = bot.get_rsposta(pergunta)

print("Bot:",resposta)


