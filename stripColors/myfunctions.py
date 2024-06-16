import cv2
import numpy as np

# def stripsColors(img):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Apply a blur to reduce noise
#     blurred = cv2.GaussianBlur(gray, (3, 3), 0)

#     # Threshold the image to create a binary image
#     ret, threshold = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#     # using a findContours() function 
#     contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

#     i = 0
#     print(len(contours))
#     # dictionary for storing names of shapes 
#     data = {
#     'URO': [],
#     'BIL': [],
#     'KET': [],
#     'BLD': [],
#     'PRO': [],
#     'NIT': [],
#     'LEU': [],
#     'GLU': [],
#     'SG': [],
#     'PH': []
#     }

# # Detect contours

#     # Draw the contours on the image
#     cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

#     # Detect lines using Hough Line Transform
#     # cv2.imshow('Masked Region', img)
#     # cv2.waitKey(0)
#     # return data
#     for contour in contours: 
#         if i == 0: 
#             i = 1
#             continue
#         else:
            
#             cv2.imshow('Masked Region', img)
#             cv2.waitKey(0)
#     return data

def stripsColors(img):
    num_squares = 10

    # Calculate the width of each square
    height, width, _ = img.shape
    img = cv2.resize(img, (int(width/1.8),int( height/1.8)))
    image = img[:int(height*0.375),int(width*0.2):int(width*0.5)]
    square_height = image.shape[0] // num_squares
    data = []
    cv2.imshow('mat',img[int(height*0.01):int(height*0.37),int(width*0.3):int(width*0.4)])
    cv2.waitKey(0)
    for i in range(num_squares):
        # Define the coordinates of the current square
        y1 = int(i * square_height)
        y2 = int((i + 1) * square_height)
        x1 = 0
        x2 = width
        # print(width, square_height)
        print(image[y1:y2, x1:x2].shape)
        print(type(image[y1:y2, x1:x2]))
        b,g,r = cv2.split(image[y1:y2, x1:x2])
        b_mean = np.mean(b)
        g_mean = np.mean(g)
        r_mean = np.mean(r)
        data.append([r_mean, g_mean, b_mean])
    my_dict = {
        'URO': list(data[0]),
    'BIL': list(data[1]),
    'KET': list(data[2]),
    'BLD': list(data[3]),
    'PRO': list(data[4]),
    'NIT': list(data[5]),
    'LEU': list(data[6]),
    'GLU': list(data[7]),
    'SG': list(data[8]),
    'PH': list(data[9])
    }
    # my_dict = {
    # 'URO': [],
    # 'BIL': [],
    # 'KET': [],
    # 'BLD': [],
    # 'PRO': [],
    # 'NIT': [],
    # 'LEU': [],
    # 'GLU': [],
    # 'SG': [],
    # 'PH': []
    # }
    return my_dict
