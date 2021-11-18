# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:09:19 2021

@author: klkel
"""

import cv2
import numpy as np
gray_img=np.zeros([1024,1024],dtype=np.uint8)
gray_img[512][512]=255 #unit impulse

w=np.array([[1, 1, 1],[1, 1, 1],[1, 1, 1]]) #kernel
pad=1 #padding types

img=gray_img.copy()

height_kernel,width_kernel=w.shape


img_type='gray'
padding=np.zeros([img.shape[0]+2*height_kernel,img.shape[1]+2*width_kernel],dtype=np.uint8)
height,width=img.shape


#add img on black space (zero-padding for img)
for i in range(len(img)):
    for j in range(len(img[i])):
        padding[i+height_kernel][j+width_kernel]=img[i][j] #get img to be centered
           
tot_sum=0
for k in range(len(w)):
    for l in range(len(w[k])):
        tot_sum=tot_sum+w[k][l]
# print(tot_sum)
if tot_sum==0:
    tot_sum=1

sides=np.floor(height_kernel/2)
up_dn=np.floor(width_kernel/2)
k_up=0  #kernel up
K_down=0 #kernel down
if height_kernel%2==0:
    #height even
    k_up=up_dn
    k_down=-up_dn+1
else:
    k_up=up_dn
    k_down=-up_dn
    
if width_kernel%2==0:
    #width even
    k_lf=-up_dn+1
    k_rt=up_dn
else:
    k_lf=-up_dn
    k_rt=up_dn
    
    
# print(k_down,k_up, k_lf,k_rt)
output_img=padding.copy()

if img_type=='gray':
    for i in range(len(img)):
        for j in range(len(img[i])):
            val=0
            w_val_x=0
            for k in range(int(k_down),int(k_up)+1):
                
                w_val_y=0
                for l in range(int(k_lf),int(k_rt)+1):
                    if i+k>=len(padding) or j+l>=len(padding[i]) or i+k<0 or j+l<0:
                        continue
                    else:
                        val+=int(padding[i+k][j+l])*int(w[w_val_x][w_val_y])
                    w_val_y+=1
                w_val_x+=1
            hold=round(val/tot_sum)
            if hold>255:
                hold=255
            output_img[i][j]=hold
            val=0

kernel=w/tot_sum
dst=cv2.filter2D(padding,-1,kernel)    

final_o=img.copy()
shortened=img.copy()
#crop version
for i in range(0,len(img)):
    for j in range(0,len(img[i])):
        if img_type=='gray':
            final_o[i][j]=output_img[i+height_kernel][j+width_kernel]
            shortened[i][j]=dst[i+height_kernel][j+width_kernel]
        else:
            for m in range(0,len(img[i][j])):
                final_o[i][j][m]=output_img[i+height_kernel][j+width_kernel][m]
                shortened[i][j][m]=dst[i+height_kernel][j+width_kernel][m]
            

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)

# cv2.namedWindow('padding',cv2.WINDOW_NORMAL)
# cv2.imshow('padding',padding)
# cv2.namedWindow('goal',cv2.WINDOW_NORMAL)
# cv2.imshow('goal',shortened)
cv2.namedWindow('output',cv2.WINDOW_NORMAL)
cv2.imshow('output',final_o)

cv2.waitKey(0)
filename='GreyImage.png'
cv2.imwrite(filename,img)
filename='GreyImageConvoluted.png'
cv2.imwrite(filename,final_o)
cv2.destroyAllWindows()

