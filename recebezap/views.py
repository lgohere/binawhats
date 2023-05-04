from django.shortcuts import render , redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from recebezap.models import Chamada
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@csrf_exempt
def recebezap(request):
    if request.method == 'POST':
        # data = request.POST
        datajson = json.loads(request.body.decode('UTF-8'))
        if datajson:
            # datajson = json.loads(datajson)
            fone_origen = datajson['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
            celular = fone_origen[2:]
            print ((celular))
        #     # Cria uma nova instância do modelo Chamada
            Chamada.objects.create(numero=celular)

        return HttpResponse('ok')


    elif request.method == 'GET' and request.GET.get('hub.challenge'):
        print('-----challenge:', request.GET['hub.challenge'])
        return HttpResponse(request.GET['hub.challenge'])

    else:
        return JsonResponse({'status': 'error', 'message': 'Metodo invalido.'})


# @login_required
def lista_chamadas(request):
    chamadas = Chamada.objects.all()
    return render(request, 'lista_chamadas.html', {'chamadas': chamadas})

def novas_chamadas(request):
    last_id = int(request.GET.get('last_id', 0))
    chamadas = Chamada.objects.filter(id__gt=last_id)
    chamadas_list = list(chamadas.values('id', 'numero')) # Aqui, altere 'celular' para 'numero'
    return JsonResponse(chamadas_list, safe=False)




# Autenticação do Usuário:


def login_view(request):
    if request.method == 'POST':
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')

        user = authenticate(request, telefone=telefone, password=senha)

        if user is not None:
            login(request, user)
            return redirect('lista_chamadas')
        else:
            error_message = 'Telefone ou senha incorretos.'
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})








            # nova_ligacao.save()

        # return render(request, 'recebezap/index.html', {})


            # print ('Telefone do contato: {}' .format(celular))
            # ahgasUrl= 'https://portal.gasdelivery.com.br/secure/client/?primary_phone='+ celular
            # webbrowser.open(ahgasUrl)
        # return HttpResponse('Dado salvo com sucesso!')    




# @app.route('/recebezap', methods=['GET','POST']
# def recebe_zap():
#     print('-----recebi:', request)
#     # request.args
#     if request.method == 'GET' and request.args.get('hub.challenge'):
#         #print('-----challenge:', request.args['hub.challenge'])
#         return request.args['hub.challenge']

#     if request.method == 'POST':
#         data = request.form
#         datajson = request.get_json()
#         fone_origen = datajson['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
#         print (fone_origen[2:0])
#         return 'ok'

# def novas_Chamada(request):
#     ultima = Chamada.objects.last()
#     celular = ultima.celular if ultima else ''
#     return render(request, 'index.html', {'celular': celular})
