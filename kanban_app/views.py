from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# import json
from .dummy_data import gadgets

# Create your views here.

def start_page_view(request):
    return HttpResponse("funktioniert")

def single_gadget_view(request, gadget_id):
    return JsonResponse({"result:": gadget_id})


# type slug und slugify