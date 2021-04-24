import cv2
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import shape

def region_of_interest(img,vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255          #(255,) * channel_count
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv2.bitwise_and(img,mask)
    return masked_image

def draw_lines(img,lines):
    img = np.copy(img)
    line_img = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_img,(x1,y1),(x2,y2),(0,255,0),thickness=10)
    
    img = cv2.addWeighted(img,0.8,line_img,1,0.0)
    return img

img = cv2.imread("OpenCV/test_image.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(img.shape)
h = img.shape[0]
w = img.shape[1]

gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
canny_img = cv2.Canny(gray_img, 100,200)

region_of_interest_vertices = [(0,h),(w/2,h/2),(w,h)]

crop_img = region_of_interest(canny_img,np.array([region_of_interest_vertices],np.int32))
lines = cv2.HoughLinesP(crop_img,rho=6,theta=np.pi/60,threshold=160,lines=np.array([]),minLineLength=40,maxLineGap=25)

img_with_lines = draw_lines(img,lines)
plt.imshow(img_with_lines)
plt.show()
