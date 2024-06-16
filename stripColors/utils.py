import cv2
import numpy as np


def stripColors(img):
    num_squares = 10

    height, width, _ = img.shape                                                 # Calculate the width of each square
    img = cv2.resize(img, (int(width/1.8),int( height/1.8)))                     # resize the image for better viewing 
    image = img[int(height*0.01):int(height*0.36),int(width*0.3):int(width*0.4)] # Crop the image for better accuracy while diving 
    square_height = image.shape[0] // num_squares                                # image into 10 sections along with height
    
    data = []
    for i in range(num_squares):
        y1 = int(i * square_height)                                              # Define the coordinates of the squares in each iteration
        y2 = int((i + 1) * square_height)
        x1 = 0
        x2 = width

        b,g,r = cv2.split(image[y1:y2, x1:x2])
        data.append([np.round(np.mean(r)), np.round(np.mean(g)), np.round(np.mean(b))])
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    my_dict = {
        'URO': data[0],
        'BIL': data[1],
        'KET': data[2],
        'BLD': data[3],
        'PRO': data[4],
        'NIT': data[5],
        'LEU': data[6],
        'GLU': data[7],
        'SG': data[8],
        'PH': data[9]
    }
    
    return my_dict
