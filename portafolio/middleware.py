import datetime
from ipware import get_client_ip
from django.http import HttpResponse
from users.models import IpAddress
import requests

BLACK_LIST = [

]

class IPIsValid:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        print(type(ip))
        print(ip, is_routable)        
        if is_routable:
            IpAddress.objects.create(pub_date = datetime.date.today(), ip_address = ip)
        
        return self.get_response(request)

