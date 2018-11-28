from django.shortcuts import render

from app.forms import ChatbotForm

import aiml
import os, sys # Para entrada e saída de dados e fechar o programa
from app.models import Dialog, Message

from django.views.decorators.csrf import csrf_exempt
import re
from django.contrib.auth.models import User


@csrf_exempt
def my_view(request):

    try:
        kernel = aiml.Kernel()

        kernel.learn("chatbot-aiml/start.xml")
        kernel.respond('load aiml')
    except Exception as e:
        print("Ocorreu um erro ao tentar fazer o aprendizado! ", e)

    if request.user.is_anonymous:
        user = User.objects.get_or_create(username='eu')[0]
    else:
        user = request.user

    dialogo = Dialog.objects.get_or_create(owner=user)[0]
    form = ChatbotForm()
    mensagens = Message.objects.filter(dialog=dialogo)
    # import ipdb; ipdb.set_trace();
    if request.method == 'POST':
        question = request.POST.get('message', '')
        mensagem1 = Message.objects.create(dialog=dialogo, sender=user, text=question)
        question = question.replace('ã', 'a').replace('ç', 'c').strip()
        response = kernel.respond(question, user.id)
        mensagem2 = Message.objects.create(dialog=dialogo, text=response)


    return render(request, 'base.html', {'form': form, 'objects_list': mensagens})
