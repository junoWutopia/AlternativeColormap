import cv2
import os
import numpy as np

def dftypes(pic,ctype):
    im_gray = cv2.imread(pic, cv2.IMREAD_GRAYSCALE)

    if (ctype in range(22)):
        im_color = cv2.applyColorMap(im_gray, ctype)
    elif ctype==-1: 
        im_color = im_gray
    
    im_dir = os.path.dirname(os.path.realpath(__file__))  + "\colormap"+str(ctype)+".png"
    cv2.imwrite(im_dir, im_color)

#table=np.array([i for i in range(256)],dtype='uint8')
def custom(pic,table):
    im_gray = cv2.imread(pic, cv2.IMREAD_GRAYSCALE)

    im_color = cv2.LUT(im_gray,table)

    im_dir = os.path.dirname(os.path.realpath(__file__))  + "\colormapct.png"
    cv2.imwrite(im_dir, im_color)

if __name__ == '__main__':
	dftypes(pic,ctype=11)