# -*- coding: utf-8 -*-
import aiml
import os, sys # Para entrada e saída de dados e fechar o program


try:
    kernel = aiml.Kernel()

    kernel.learn("start.xml")
    kernel.respond('load aiml')
except Exception as e:
    print("Ocorreu um erro ao tentar fazer o aprendizado! ", e)

# kernel.loadBrain("chatbot-aiml/bot_brain.brn")

while True:
    question = input("Enter your message >> ")
    response = kernel.respond(question, 25)

    print(response)
