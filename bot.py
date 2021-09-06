from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from time import sleep

bot = ChatBot('Test')


conversaInicial1 = [
    "Olá",
    "Olá, como posso te ajudar?",
    "ola",
    "Olá, como posso te ajudar?",
    "bom dia",
    "Olá, como posso te ajudar?",
    "boa tarde",
    "Olá, como posso te ajudar?",
    "voce pode me ajudar?",
    "Olá, como posso te ajudar?",
    "oi, tudo bem?",
    "Olá, como posso te ajudar?",
    "oi!"
]


conversacovid1 = [
    "estou com covid",
    "Ao sentir dor de cabeça, tosse, e falta de ar, procure um médico imediatamente",
]

coversaSintomas = [
    "sintomas",
    "quais os sintomas do covid",
    "Os sintomas mais comuns são: febre, tosse seca, fadiga e tosse com catarro",
    "sintomas covid",
    "Os sintomas mais comuns são: febre, tosse seca, fadiga e tosse com catarro",
    "sintomas coronavirus",
    "Os sintomas mais comuns são: febre, tosse seca, fadiga e tosse com catarro",
    "sintomas coronavírus",
    "Os sintomas mais comuns são: febre, tosse seca, fadiga e tosse com catarro",
    "sintomas do covid-19",
    "Os sintomas mais comuns são: febre, tosse seca, fadiga e tosse com catarro",
    "como saber se to com covid",
    "Os sintomas mais comuns são: febre, tosse seca, fadiga e tosse com catarro",

]

conversavacina = [
      "posso me vacinar?",
      "Verifique sua possibilidade de vacinação no site: https://www.vacinaja.sp.gov.br/",
      "vacina",
      "Verifique sua possibilidade de vacinação no site: https://www.vacinaja.sp.gov.br/",
      "quero vacinar",
      "Verifique sua possibilidade de vacinação no site: https://www.vacinaja.sp.gov.br/",
      "quando irei me vacinar?",
      "Verifique sua possibilidade de vacinação no site: https://www.vacinaja.sp.gov.br/",
      "quando vou vacina",
      "Verifique sua possibilidade de vacinação no site: https://www.vacinaja.sp.gov.br/",
      "quando vo tomar vacina",
      "Verifique sua possibilidade de vacinação no site: https://www.vacinaja.sp.gov.br/",
      "quando eu vou tomar vacina?",
      "Verifique sua possibilidade de vacinação no site: https://www.vacinaja.sp.gov.br/",
      "quando eu irei tomar vacina? ",
      "Verifique sua possibilidade de vacinação no site: https://www.vacinaja.sp.gov.br/",
      "Devo me vacinar?",
      "Sim, vacine-se, para que possamos vencer essa pandemia!",
]



trainer = ListTrainer(bot)


trainer.train(conversaInicial1)
trainer.train(conversacovid1)
trainer.train(coversaSintomas)
trainer.train(conversavacina)

print('Bem vindo(a) ao healhtBot👩‍🏫')
print('...')
sleep(2)
print('Estou aqui para responder dúvidas sobre o coronavírus, como por exemplo: dicas de prevenção e informações sobre a vacinação!')
print('...')
sleep(2)
print('A COVID-19 é uma doença infecciosa causada pelo novo coronavírus (SARS-CoV-2) e tem como principais sintomas febre, cansaço e tosse seca.')


while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    if float(response.confidence)>=0.001:
        print('HealthBot👩‍🏫: ', response)
    else:
        print('HealthBot👩‍🏫: Desculpe, não entendi, por favor refaça a pergunta.')