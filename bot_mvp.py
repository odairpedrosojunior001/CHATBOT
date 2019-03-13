#-*- coding: utf-8 -*-


from chatterbot import ChatBot #importação biblioteca bot
from chatterbot.trainers import ListTrainer #importação biblioteca de aprendizado bot ( machine learning)



bot = ChatBot('Célula Implantação')
trainer = ListTrainer(bot)


#criação dos diálogos
trainer.train([
    'Ola',
    'Ola,em que posso ajudar?',
    'Hoje teremos contagem de CDE?',
    'Não, segue os proximos dias de contagem em Março: 15 ; 18 ; 20 ; 22 ; 25 e 27  ',
    'Obrigado',
    'Agradecemos seu contato.'
    
])



while True:  # laço para a interação de perguntas e respostas do usuário e do bot
    quest = input("Você: ")
    response = bot.get_response(quest)
    print("Bot: ", response)
else:
    print ("Bot: Resposta não encontrada")





