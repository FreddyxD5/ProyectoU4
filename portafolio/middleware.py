from ipware import get_client_ip
from django.http import HttpResponse
import requests

BLACK_LIST = [

]

class IPIsValid:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        print(ip, is_routable)

        # if ip in BLACK_LIST:
        #     return HttpResponse('Bad Request', status = 400)
        # else:
        #     return self.get_response(request)
        # Aceptar solo peticiones para direcciones de ip de PERU
        response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=5fb9b750658b4428b009c147df975e7c&ip_address=" + ip)        
        data = response.json()
        print(data)
        response = self.get_response(request)
        if data['country'] is not None and data['country']=='Peru':
            return response        
        print("Esto es solo para Peru")
        return response

