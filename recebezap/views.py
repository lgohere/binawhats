from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def recebezap(request):
    if request.method == 'POST':
        data = request.POST
        datajson = request.POST.get('datajson', None)
        if datajson:
            datajson = json.loads(datajson)
            fone_origen = datajson['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
            print (fone_origen[2:])
        return (HttpResponse('ok'))

    elif request.method == 'GET' and request.GET.get('hub.challenge'):
        print('-----challenge:', request.GET['hub.challenge'])
        return HttpResponse(request.GET['hub.challenge'])

    else:
        return JsonResponse({'status': 'error', 'message': 'Metodo invalido.'})


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