from django.shortcuts import render
import cv2
import numpy as np
# Create your views here.
from django.http import HttpResponse
from django.http import Http404
# from django.http import Http

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest
from .models import ImageModel
from .myfunctions import stripsColors
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt # type: ignore
def processImage(request):
    if request.method == 'POST':
        id = 0
        # print(id)
        try:
            id = request.POST.get('id')
            
            # Access uploaded file(s)
            if 'image' in request.FILES:
                image_file = request.FILES['image']
        except:
            raise ValueError("request body not loaded")
        # print(id)
        if id:
            # request_data = json.loads(request.body)
            # # id = request_data.get('id')  # Extract ID from request body
            # image_file = file_data.image
            # id = request_data.id
            img = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
            # processed_image = ImageModel(image=image_file, name=id)
            # processed_image.save()
            data = stripsColors(img)
            return HttpResponse(JsonResponse(data))
        
        # converting image into grayscale image 
        