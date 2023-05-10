from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# import json
from recebezap.models import Chamada
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

@csrf_exempt


def recebezap(request):
    if request.method == 'POST':
        caller = request.GET.get('caller', None,)
        fone_origem = caller[1:]        
        fone_receptor = request.GET.get('receiver', None,)        
        if fone_origem:
            print("Valor do fone_origem:", fone_origem)
            print ("Valor do fone_receptor:", fone_receptor)
            Chamada.objects.create(numero=fone_origem , receptor=fone_receptor)
        return HttpResponse('ok')


    else:
        return JsonResponse({'status': 'error', 'message': 'Metodo invalido.'})


def lista_chamadas(request):
    chamadas = Chamada.objects.all()
    return render(request, 'lista_chamadas.html', {'chamadas': chamadas})

def novas_chamadas(request):
    last_id = int(request.GET.get('last_id', 0))
    chamadas = Chamada.objects.filter(id__gt=last_id)
    chamadas_list = list(chamadas.values('id', 'numero' , 'receptor'))
    Chamada.objects.all().delete()
    return JsonResponse(chamadas_list, safe=False)


# def recebezap(request):
#     if request.method == 'POST':
#         # data = request.POST
#         datajson = json.loads(request.body.decode('UTF-8'))
#         print(datajson)
        # if datajson:
            # datajson = json.loads(datajson)
            # fone_receptor = datajson['entry'][0]['changes'][0]['value']['metadata']['display_phone_number'] # Telefone de Destino -> que recebe os eventos.

            # # fone_origen = datajson['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id'] # Telefone de Origem -> que executa os eventos.
            # fone_origen = datajson['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id'] # Telefone de Origem -> que executa os eventos.
            
            # celular = fone_origen[2:]
            # print ((celular))
            # print((fone_receptor))
            # # if fone_receptor == celular: 
            # Chamada.objects.create(numero=celular , receptor=fone_receptor)

        # return HttpResponse('ok')


    # elif request.method == 'GET' and request.GET.get('hub.challenge'):
    #     print('-----challenge:', request.GET['hub.challenge'])
    #     return HttpResponse(request.GET['hub.challenge'])


# @login_required
