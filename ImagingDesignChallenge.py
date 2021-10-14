#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:33:25 2021

@author: lindsay
"""
#Made by Lindsay Dahl

import cv2
import numpy
import os.path

def trackPosition(slider_name, window_name, min_val):
    current_pos = cv2.getTrackerPos(slider_name, window_name)
    if current_pos < min_val:
        print('Hey, that is too low!')
        return min_val
    else:
        return current_pos

print ("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")

#Takes colored image and makes a 2d and 3d grayscale version
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

#Creates display windows
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')

image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#Makes the images the correct size
color1_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color2_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color3_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color4_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color5_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color6_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
#Assigns specific colors
#Values are in order of B,G,R (blue, green, red) and can be changed to create different colors
color1_paper[0:image_height,0:image_width, 0:image_channels] = [0,0,255]
color2_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
color3_paper[0:image_height,0:image_width, 0:image_channels] = [0,128,0]
color4_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,0]
color5_paper[0:image_height,0:image_width, 0:image_channels] = [180,105,255]
color6_paper[0:image_height,0:image_width, 0:image_channels] = [0,165,255]

#Creates trackbars for the colors
#Sets which colors are "light" and "dark"
cv2.createTrackbar('Grayscale', 'Sliders', 30, 150, lambda x: None)
cv2.createTrackbar('Grayscale2', 'Sliders', 60, 175, lambda x: None)
cv2.createTrackbar('Grayscale2', 'Sliders', 90, 190, lambda x: None)
cv2.createTrackbar('Grayscale2', 'Sliders', 120, 205, lambda x: None)
cv2.createTrackbar('Grayscale2', 'Sliders', 165, 235, lambda x: None)

#Changes the image with input from the sliders
keypressed = 1
while keypressed != 27 and keypressed != ord('s'):
    grayscale_break = cv2.getTrackbarPos ('Grayscale', 'Sliders')
    grayscale_break2 = cv2.getTrackbarPos ('Grayscale2', 'Sliders')
    grayscale_break3 = cv2.getTrackbarPos ('Grayscale3', 'Sliders')
    grayscale_break4 = cv2.getTrackbarPos ('Grayscale4', 'Sliders')
    grayscale_break5 = cv2.getTrackbarPos ('Grayscale5', 'Sliders')
    
    min_grayscale_for_color1 = [0,0,0]
    max_grayscale_for_color1 = [grayscale_break,grayscale_break,grayscale_break]
    
    min_grayscale_for_color2 = [grayscale_break+1,grayscale_break+1,grayscale_break+1]
    max_grayscale_for_color2 = [grayscale_break2,grayscale_break2,grayscale_break2]
   
    min_grayscale_for_color3 = [grayscale_break2+1,grayscale_break2+1,grayscale_break2+1]
    max_grayscale_for_color3 = [grayscale_break3,grayscale_break3,grayscale_break3]
    
    min_grayscale_for_color4 = [grayscale_break3+1,grayscale_break3+1,grayscale_break3+1]
    max_grayscale_for_color4 = [grayscale_break4,grayscale_break4,grayscale_break4]
    
    min_grayscale_for_color5 = [grayscale_break4+1,grayscale_break4+1,grayscale_break4+1]
    max_grayscale_for_color5 = [grayscale_break5,grayscale_break5,grayscale_break5]
    
    min_grayscale_for_color6 = [grayscale_break5+1,grayscale_break5+1, 
                                grayscale_break5+1]
    max_grayscale_for_color6 = [255,255,255]
    
  
    min_grayscale_for_color1 = numpy.array(min_grayscale_for_color1, dtype = "uint8")
    max_grayscale_for_color1 = numpy.array(max_grayscale_for_color1, dtype = "uint8")
    
    min_grayscale_for_color2 = numpy.array(min_grayscale_for_color2, dtype = "uint8")
    max_grayscale_for_color2 = numpy.array(max_grayscale_for_color2, dtype = "uint8")
    
    min_grayscale_for_color3 = numpy.array(min_grayscale_for_color3, dtype = "uint8")
    max_grayscale_for_color3 = numpy.array(max_grayscale_for_color3, dtype = "uint8")
    
    min_grayscale_for_color4 = numpy.array(min_grayscale_for_color3, dtype = "uint8")
    max_grayscale_for_color4 = numpy.array(max_grayscale_for_color3, dtype = "uint8")
    
    min_grayscale_for_color5 = numpy.array(min_grayscale_for_color3, dtype = "uint8")
    max_grayscale_for_color5 = numpy.array(max_grayscale_for_color3, dtype = "uint8")
    
    min_grayscale_for_color6 = numpy.array(min_grayscale_for_color3, dtype = "uint8")
    max_grayscale_for_color6 = numpy.array(max_grayscale_for_color3, dtype = "uint8")
    
    #How colors appear on image
    block_all_but_the_color1_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color1,
                                              max_grayscale_for_color1)
    block_all_but_the_color2_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color2,
                                                 max_grayscale_for_color2)
    block_all_but_the_color3_parts = cv2.inRange(grayscale_image,
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
                                           mask = block_all_but_the_color3_parts)
    color4_parts_of_image = cv2.bitwise_or(color4_paper, color4_paper,
                                           mask = block_all_but_the_color4_parts)
    color5_parts_of_image = cv2.bitwise_or(color5_paper, color5_paper,
                                           mask = block_all_but_the_color5_parts)
    color6_parts_of_image = cv2.bitwise_or(color6_paper, color6_paper,
                                           mask = block_all_but_the_color6_parts)
    
    #Creates custom image
    customized_image = cv2.bitwise_or(color1_parts_of_image, color2_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color3_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color4_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color5_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color6_parts_of_image)
    
    #Displays windows
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Grayscale Image',grayscale_image)
    #cv2.imshow('Color1 Parts of Image',color1_parts_of_image)
    #cv2.imshow('Color2 Parts of Image',color2_parts_of_image)
    #cv2.imshow('Color3 Parts of Image',color3_parts_of_image)
    #cv2.imshow('Color4 Parts of Image',color4_parts_of_image)
    #cv2.imshow('Color5 Parts of Image',color5_parts_of_image)
    #cv2.imshow('Color6 Parts of Image',color6_parts_of_image)
    cv2.imshow('Customized Image',customized_image)
    
    
    #escapekey
    #press escape to exit program
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
    #press s to name and save image
elif keypressed == ord('s'): 
    new_file = input('Type the name of your file. Include .jpg at the end.')
   # cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()
