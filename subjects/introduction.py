import numpy as np
import cv2 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


"""
Carregar imagens em escala de cinza e colorida. 

Analisar os tipos de dados. Converter entre eles. (uint8, uint16, double, etc).

Realizar operações aritméticas entre duas matrizes de tipos de dados diferentes. Avalie o que acontece.

Apresentar ambas usando matolotlib e opencv (highgui). Qual a diferença entre as duas formas de visualização?
"""

#load grayscale image
grayscale_img = cv2.imread('../images/relampago.png',cv2.IMREAD_GRAYSCALE)

#load colorful image
colorful_img = cv2.imread('../images/relampago.png',cv2.IMREAD_COLOR)


# cv2.imshow('image',colorful_img)
# cv2.waitKey(0)

def display_image_by_type():
    types = [np.uint8,np.uint16,np.float32, np.double]
    for t in types:
        _img = colorful_img.astype(t)
        cv2.imshow(f'image {_img.dtype}', _img)
        cv2.waitKey(0)


def updateImage(value, image):
    img = image * value
    cv2.imshow(f'image {image.dtype}', img)
    

def multiply_by_scalar():
    types = [np.uint8,np.uint16,np.float32, np.double]
    for t in types:
        _img = colorful_img.astype(t)         
        window_name = f'image {_img.dtype}'
        cv2.namedWindow(window_name)
        cv2.createTrackbar('scalar', window_name, 1, 255, lambda value: updateImage(value, _img))
        cv2.waitKey(0)
        
def add_matrices():
    types = [np.uint8,np.uint16,np.float32, np.double]
    _img = colorful_img.astype(types[0])
    _img2 = grayscale_img.astype(types[3])

    #transforming the shape (600,600) -> (600,600,1)
    im2= np.repeat(np.expand_dims(_img2, -1), 3, axis=-1)
    # cv2.imshow(f'image {_img.dtype}', _img)
    # cv2.imshow(f'image {_img2.dtype}', _img2)
    # cv2.waitKey(0)
    cv2.imshow(f'image {_img.dtype} + {_img2.dtype}', _img + im2)
    cv2.waitKey(0)

#display_image_by_type()
multiply_by_scalar()
#add_matrices()

#Matplotlib 

mat_img = mpimg.imread('../images/relampago.png')
plt.imshow(mat_img*255)
plt.show()
