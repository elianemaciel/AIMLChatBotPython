from django.shortcuts import render

from app.forms import ChatbotForm

import aiml
import os, sys # Para entrada e saída de dados e fechar o programa
from app.models import Dialog, Message

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):

    # Create the kernel and learn AIML files
    # import ipdb; ipdb.set_trace()
    try:
        kernel = aiml.Kernel()
        kernel.learn("chatbot-aiml/start.xml")
        kernel.respond("load aiml b")
    except:
        print("ERROR")
    # import ipdb; ipdb.set_trace()
    if request.method == 'POST':
        dialogo = Dialog.objects.filter(owner=request.user).order_by('-id')[0]
        form = ChatbotForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            question = form.cleaned_data['message']
            mensagem1 = Message.objects.create(dialog=dialogo, sender=request.user, text=question)
            response = kernel.respond(question)
            mensagem2 = Message.objects.create(dialog=dialogo, text=response)
            form = ChatbotForm()
            mensagens = Message.objects.filter(dialog=dialogo)
            return render(request, 'base.html', {'form': form, 'message': response, 'objects_list': mensagens})
    else:
        form = ChatbotForm()

        dialogo = Dialog.objects.get_or_create(owner=request.user)

        return render(request, 'base.html', {'form': form})
