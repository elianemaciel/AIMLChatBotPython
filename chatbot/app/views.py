from django.shortcuts import render

from app.forms import ChatbotForm

import aiml
import os, sys # Para entrada e saída de dados e fechar o programa
from app.models import Dialog, Message

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):

    try:
        kernel = aiml.Kernel()

        if os.path.isfile("chatbot-aiml/bot_brain.brn"):
            kernel.bootstrap(brainFile = "bot_brain.brn")
        else:
            kernel.bootstrap(learnFiles="chatbot-aiml/start.xml", commands="load aiml b")
            kernel.saveBrain("chatbot-aiml/bot_brain.brn")
    except Exception as e:
        print("Ocorreu um erro ao tentar fazer o aprendizado! ", e)

    kernel.loadBrain("chatbot-aiml/bot_brain.brn")

    dialogo = Dialog.objects.get_or_create(owner=request.user)[0]
    form = ChatbotForm()
    mensagens = Message.objects.filter(dialog=dialogo)
    import ipdb; ipdb.set_trace();
    if request.method == 'POST':
        # dialogo = Dialog.objects.filter(owner=request.user).order_by('-id')[0]
        # form = ChatbotForm(request.POST)
        # check whether it's valid:
        question = request.POST.get('message', '')
        mensagem1 = Message.objects.create(dialog=dialogo, sender=request.user, text=question)
        response = kernel.respond(question, request.user.id)
        mensagem2 = Message.objects.create(dialog=dialogo, text=response)
            
        
    return render(request, 'base.html', {'form': form, 'objects_list': mensagens})
        

