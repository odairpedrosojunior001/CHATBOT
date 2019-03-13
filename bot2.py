#-*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot('Célula Implantação')

trainer = ListTrainer(bot)

trainer.train([
    'Ola',
    'Ola,em que posso ajudar?',
    'Como posso faturar um pedido de celular no mobile?',
    'Primeiro realize a separação no mobile, coletando o IMEI, logo em seguida, finalize.',
    'Quanto tempo demora para faturar?',
    'Cerca de 10 a 30 segundos.'
])

while True:  # laço para a interação de perguntas e respostas do bot
    quest = input("Você: ")
    response = bot.get_response(quest)
    print("Bot: ", response)





