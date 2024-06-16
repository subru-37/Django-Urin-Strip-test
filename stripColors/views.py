from django.shortcuts import render
import cv2
import numpy as np
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest, Http404
from .models import ImageModel
from .utils import stripColors


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt # type: ignore
def processImage(request):
    if request.method == 'POST':
        id = 0
        image_file = []
        try:
            id = request.POST.get('uuid')
            # print(id)
        except:
            raise Http404("Id not loaded")
        # print(request.FILES)
        try: 
            image_file = request.FILES['image']                     # Access uploaded file(s)
            # print(request.FILES)
        except: 
            raise Http404("image not loaded")
        if id and len(image_file)!=0:

            img = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
            data = stripColors(img)
            print(data)
            return HttpResponse(JsonResponse(data))
        else: 
            raise Http404("id doesn't exist") 
        