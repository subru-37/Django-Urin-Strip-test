from django.db import models

import cv2 
import numpy as np 
from matplotlib import pyplot as plt 

# Create your models here.

# For future application for storing data
class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50, default='undefined') 
    def __str__(self):
        return self.name
    