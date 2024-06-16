from django.shortcuts import render
import cv2
import numpy as np
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest
from .models import ImageModel
from .utils import stripColors


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt # type: ignore
def processImage(request):
    if request.method == 'POST':
        id = 0

        try:
            id = request.POST.get('id')
            if 'image' in request.FILES:                                # Access uploaded file(s)
                image_file = request.FILES['image']
        except:
            raise ValueError("request body not loaded")

        if id:

            img = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
            data = stripColors(img)

            return HttpResponse(JsonResponse(data))
        