#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:14:15 2021

@author: gabrielbodoh
"""

# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path
import random

def newTrackbarPos(trackbar_name, trackbar_window, min_val):
    current_pos = cv2.getTrackbarPos(trackbar_name, trackbar_window)
    if current_pos<min_val:
        cv2.setTrackbarPos(trackbar_name, trackbar_window, min_val)
        print("That's too low")
        return min_val
    else:
        return current_pos

print ("Save your original image in the same folder as this program.")#importing libraries
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")

original_image = cv2.imread(filename,1)#changing image to gray scale
grayscale_image_simple = cv2.imread(filename, 0)#0 tells to grayscale
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

print("press 1 to randomize colors")

#cv2.namedWindow('Original Image')
#cv2.namedWindow('Grayscale Image')
#cv2.namedWindow('Red Parts of Image')
#cv2.namedWindow('Yellow Parts of Image')
#cv2.namedWindow('Blue image')
cv2.namedWindow('Customized Image')#windows
cv2.namedWindow('Sliders')
cv2.namedWindow('Color 1 Slider')
cv2.namedWindow('Color 2 Slider')
cv2.namedWindow('Color 3 Slider')
cv2.namedWindow('Color 4 Slider')
cv2.namedWindow('Color 5 Slider')
cv2.namedWindow('Color 6 Slider')


image_height = original_image.shape[0]#shape of the image
image_width = original_image.shape[1]
image_channels = original_image.shape[2]#color channels

color1_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color2_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color3_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color4_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color5_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color6_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)


    
cv2.createTrackbar('Grayscale', 'Sliders', 42, 83, lambda x:None)#grayscale trackbars
cv2.createTrackbar('Grayscale 2', 'Sliders', 84, 125, lambda x:None)
cv2.createTrackbar('Grayscale 3', 'Sliders', 126, 167, lambda x:None)
cv2.createTrackbar('Grayscale 4', 'Sliders', 168, 209, lambda x:None)
cv2.createTrackbar('Grayscale 5', 'Sliders', 210, 255, lambda x:None)

#cv2.imshow('Original Image', original_image)
#cv2.imshow('Grayscale Image',grayscale_image)

cv2.createTrackbar('red1','Color 1 Slider' ,254, 254, lambda x:None)#color 1 slider
cv2.createTrackbar('green1', 'Color 1 Slider', 0, 254, lambda x:None)
cv2.createTrackbar('blue1', 'Color 1 Slider', 0, 254, lambda x:None)

cv2.createTrackbar('blue2', 'Color 2 Slider', 0, 254, lambda x:None)#color 2 slider
cv2.createTrackbar('green2', 'Color 2 Slider', 254, 254, lambda x:None)
cv2.createTrackbar('red2', 'Color 2 Slider', 254, 254, lambda x:None)

cv2.createTrackbar('blue3', 'Color 3 Slider',254, 254, lambda x:None)#color 3 slider
cv2.createTrackbar('green3', 'Color 3 Slider', 0, 254, lambda x:None)
cv2.createTrackbar('red3', 'Color 3 Slider', 0, 254, lambda x:None)

cv2.createTrackbar('blue4',  'Color 4 Slider', 0, 254, lambda x:None)#color 4 slider
cv2.createTrackbar('green4', 'Color 4 Slider', 254, 254, lambda x:None)
cv2.createTrackbar('red4', 'Color 4 Slider', 0, 254, lambda x:None)

cv2.createTrackbar('blue5', 'Color 5 Slider', 128, 254, lambda x:None)#color 5 slider
cv2.createTrackbar('green5', 'Color 5 Slider', 0, 254, lambda x:None)
cv2.createTrackbar('red5', 'Color 5 Slider', 128, 254, lambda x:None)

cv2.createTrackbar('blue6', 'Color 6 Slider', 180, 254, lambda x:None)#color 6 slider
cv2.createTrackbar('green6', 'Color 6 Slider', 105, 254, lambda x:None)
cv2.createTrackbar('red6', 'Color 6 Slider', 254, 254, lambda x:None)



keypressed=1
while (keypressed !=27 and keypressed !=ord('s')):
    
    if keypressed==49:#if the key "1" is pressed
        b1=random.randrange(0,255)
        cv2.setTrackbarPos('blue1', 'Color 1 Slider', b1)#setting color 1 slider to random range
        g1=random.randrange(0,255)
        cv2.setTrackbarPos('green1', 'Color 1 Slider', g1)
        r1=random.randrange(0,255)
        cv2.setTrackbarPos('red1', 'Color 1 Slider', r1)
        
        b2=random.randrange(0,255)
        cv2.setTrackbarPos('blue2', 'Color 2 Slider', b2)#color 2 slider to random range
        g2=random.randrange(0,255)
        cv2.setTrackbarPos('green2', 'Color 2 Slider', g2)
        r2=random.randrange(0,255)
        cv2.setTrackbarPos('red2', 'Color 2 Slider', r2)
        
        b3=random.randrange(0,255)
        cv2.setTrackbarPos('blue3', 'Color 3 Slider', b3)#color 3 slider random range
        g3=random.randrange(0,255)
        cv2.setTrackbarPos('green3', 'Color 3 Slider', g3)
        r3=random.randrange(0,255)
        cv2.setTrackbarPos('red3', 'Color 3 Slider', r3)
        
        b4=random.randrange(0,255)
        cv2.setTrackbarPos('blue4', 'Color 4 Slider', b4)#color 4 slider random range
        g4=random.randrange(0,255)
        cv2.setTrackbarPos('green4', 'Color 4 Slider', g4)
        r4=random.randrange(0,255)
        cv2.setTrackbarPos('red4', 'Color 4 Slider', r4)
        
        b5=random.randrange(0,255)
        cv2.setTrackbarPos('blue5', 'Color 5 Slider', b5)#color 5 random range
        g5=random.randrange(0,255)
        cv2.setTrackbarPos('green5', 'Color 5 Slider', g5)
        r5=random.randrange(0,255)
        cv2.setTrackbarPos('red5', 'Color 5 Slider', r5)
        
        b6=random.randrange(0,255)
        cv2.setTrackbarPos('blue6', 'Color 6 Slider', b6)#color 6 random range
        g6=random.randrange(0,255)
        cv2.setTrackbarPos('green6', 'Color 6 Slider', g6)
        r6=random.randrange(0,255)
        cv2.setTrackbarPos('red6', 'Color 6 Slider', r6)

    else:
        b1= cv2.getTrackbarPos('blue1', 'Color 1 Slider')#setting trackbar pos to random #
        g1= cv2.getTrackbarPos('green1', 'Color 1 Slider')
        r1=cv2.getTrackbarPos('red1', 'Color 1 Slider')
        
        b2= cv2.getTrackbarPos('blue2', 'Color 2 Slider')#setting trackbar pos to random #
        g2= cv2.getTrackbarPos('green2', 'Color 2 Slider')
        r2=cv2.getTrackbarPos('red2', 'Color 2 Slider')
        
        b3= cv2.getTrackbarPos('blue3', 'Color 3 Slider')#setting trackbar pos to random #
        g3= cv2.getTrackbarPos('green3', 'Color 3 Slider')
        r3=cv2.getTrackbarPos('red3', 'Color 3 Slider')
        
        b4= cv2.getTrackbarPos('blue4', 'Color 4 Slider')#setting trackbar pos to random #
        g4= cv2.getTrackbarPos('green4', 'Color 4 Slider')
        r4=cv2.getTrackbarPos('red4', 'Color 4 Slider')
        
        b5= cv2.getTrackbarPos('blue5', 'Color 5 Slider')#setting trackbar pos to random #
        g5= cv2.getTrackbarPos('green5', 'Color 5 Slider')
        r5=cv2.getTrackbarPos('red5', 'Color 5 Slider')
        
        b6= cv2.getTrackbarPos('blue6', 'Color 6 Slider')#setting trackbar pos to random #
        g6= cv2.getTrackbarPos('green6', 'Color 6 Slider')
        r6=cv2.getTrackbarPos('red6', 'Color 6 Slider')
    
        
    
    
    
    
    
    grayscale_break = cv2.getTrackbarPos('Grayscale', 'Sliders')#defines the "light" vs "dark" 
    grayscale_break_2=cv2.getTrackbarPos('Grayscale 2', 'Sliders')
    grayscale_break_3=cv2.getTrackbarPos('Grayscale 3', 'Sliders')
    grayscale_break_4=cv2.getTrackbarPos('Grayscale 4', 'Sliders')
    grayscale_break_5=cv2.getTrackbarPos('Grayscale 5', 'Sliders')
    
   
    
    color1_paper[0:image_height,0:image_width, 0:image_channels] = [b1,g1,r1]#turning red
    color2_paper[0:image_height,0:image_width, 0:image_channels] = [b2,g2,r2]#turning yellow
    color3_paper[0:image_height,0:image_width, 0:image_channels] = [b3,g3,r3]#blue
    color4_paper[0:image_height, 0: image_width, 0:image_channels]= [b4,g4,r4]#green
    color5_paper[0:image_height, 0: image_width, 0:image_channels]= [b5,g5,r5] #purple
    color6_paper[0:image_height, 0: image_width, 0:image_channels]= [b6,g6,r6] #hotpink
                                     
    
    min_grayscale_for_color1 = [0,0,0]#any color value between 0-100 will be red
    max_grayscale_for_color1 = [grayscale_break,grayscale_break,grayscale_break]
    min_grayscale_for_color2 = [grayscale_break+1,grayscale_break+1, 
                                grayscale_break+1]#any color between 101 and 255 will be yellow
    max_grayscale_for_color2 = [grayscale_break_2, grayscale_break_2, grayscale_break_2]
    min_grayscale_for_color3=[grayscale_break_2+1,grayscale_break_2+1,grayscale_break_2+1]
    max_grayscale_for_color3=[grayscale_break_3, grayscale_break_3, grayscale_break_3]
    
    min_grayscale_for_color4 = [grayscale_break_3+1, grayscale_break_3+1, grayscale_break_3+1]
    max_grayscale_for_color4 = [grayscale_break_4, grayscale_break_4, grayscale_break_4]
    
    min_grayscale_for_color5 = [grayscale_break_4+1, grayscale_break_4+1, grayscale_break_4+1]
    max_grayscale_for_color5 = [grayscale_break_5, grayscale_break_5, grayscale_break_5]
    
    min_grayscale_for_color6 = [grayscale_break_5+1, grayscale_break_5+1, grayscale_break_5+1]
    max_grayscale_for_color6 = [255,255,255]
    
   
    min_grayscale_for_color1 = numpy.array(min_grayscale_for_color1, dtype = "uint8")
    max_grayscale_for_color1 = numpy.array(max_grayscale_for_color1, dtype = "uint8")
    min_grayscale_for_color2 = numpy.array(min_grayscale_for_color2,
                                           dtype = "uint8")
    max_grayscale_for_color2 = numpy.array(max_grayscale_for_color2,
                                           dtype = "uint8")
    min_grayscale_for_color3 = numpy.array(min_grayscale_for_color3, dtype = "uint8")
    max_grayscale_for_color3 = numpy.array(max_grayscale_for_color3, dtype = "uint8")
    min_grayscale_for_color4 = numpy.array(min_grayscale_for_color4, dtype = "uint8")
    max_grayscale_for_color4 = numpy.array(max_grayscale_for_color4, dtype = "uint8")
    min_grayscale_for_color5 = numpy.array(min_grayscale_for_color5, dtype = "uint8")
    max_grayscale_for_color5 = numpy.array(max_grayscale_for_color5, dtype = "uint8")
    min_grayscale_for_color6 = numpy.array(min_grayscale_for_color6, dtype = "uint8")
    max_grayscale_for_color6 = numpy.array(max_grayscale_for_color6, dtype = "uint8")
    
    #print(min_grayscale_for_color2, max_grayscale_for_color2)
    
    
    block_all_but_the_color1_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color1,
                                              max_grayscale_for_color1)#delete all pixels not in the interval
    block_all_but_the_color2_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color2,
                                                 max_grayscale_for_color2)
    block_all_but_the_color3_parts= cv2.inRange(grayscale_image, 
                                              min_grayscale_for_color3,
                                              max_grayscale_for_color3)
    block_all_but_the_color4_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color4,
                                              max_grayscale_for_color4)
    block_all_but_the_color5_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color5,
                                              max_grayscale_for_color5)
    block_all_but_the_color6_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color6,
                                              max_grayscale_for_color6)
    
    
    color1_parts_of_image = cv2.bitwise_or(color1_paper, color1_paper,
                                        mask = block_all_but_the_color1_parts)
    color2_parts_of_image = cv2.bitwise_or(color2_paper, color2_paper,
                                           mask = block_all_but_the_color2_parts)
    color3_parts_of_image = cv2.bitwise_or(color3_paper, color3_paper,
                                         mask=block_all_but_the_color3_parts)
    color4_parts_of_image = cv2.bitwise_or(color4_paper, color4_paper,
                                        mask = block_all_but_the_color4_parts)
    color5_parts_of_image = cv2.bitwise_or(color5_paper, color5_paper,
                                        mask = block_all_but_the_color5_parts)
    color6_parts_of_image = cv2.bitwise_or(color6_paper, color6_paper,
                                        mask = block_all_but_the_color6_parts)
    
    customized_image = cv2.bitwise_or(color1_parts_of_image, color2_parts_of_image)
    customized_image=cv2.bitwise_or(customized_image, color3_parts_of_image)
    customized_image=cv2.bitwise_or(customized_image, color4_parts_of_image)
    customized_image=cv2.bitwise_or(customized_image, color5_parts_of_image)
    customized_image=cv2.bitwise_or(customized_image, color6_parts_of_image)
    
    #cv2.imshow('Original Image', original_image) #windows
    #cv2.imshow('Grayscale Image',grayscale_image)
    #cv2.imshow('Red Parts of Image',color1_parts_of_image)
    #cv2.imshow('Yellow Parts of Image',color2_parts_of_image)
    #cv2.imshow('Blue image', color3_parts_of_image)
    #cv2.imshow('Green image', color4_parts_of_image)
    #cv2.imshow('Purple image', color5_parts_of_image)
    #cv2.imshow('Pink image', color6_parts_of_image)
    cv2.imshow('Customized Image',customized_image)
    
  
  

    keypressed = cv2.waitKey(1)
    
    
    
if keypressed == 27:#close all windows when press escape
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()
