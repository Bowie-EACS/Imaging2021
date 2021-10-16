#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:00:19 2021

@author: Abigail Proffitt | 8th period
"""

import cv2
import numpy
import os.path


def trackPosition(slider_name, window_name, min_val):
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print("hop off")
        cv2.setTrackbarPos(slider_name, window_name, min_val)
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

original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')

image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#KEY: 
     # b = "base color" --> view file name to figure out what the base color is
     # 1-10 = color's brightness --> the higher the value the darker the color gets
     

b1_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
b2_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
b3_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
b4_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
b5_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
b6_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
b7_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
b8_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
b9_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
b10_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)



#Lines 70-79 are where you can input new vallues to change the colors
#The numbers are listed in [B, G, R] order 
#INSTRUCTIONS FOR CHANGING OUT COLORS
    # look up BGR color codes (check if the value you find is given in BGR format and not RGB)
    # enter in new BGR values
b1_paper[0:image_height,0:image_width, 0:image_channels] = [255,204,246]
b2_paper[0:image_height,0:image_width, 0:image_channels] = [255,153,238]
b3_paper[0:image_height,0:image_width, 0:image_channels] = [255,102,229]
b4_paper[0:image_height,0:image_width, 0:image_channels] = [255,51,221]
b5_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,212]
b6_paper[0:image_height,0:image_width, 0:image_channels] = [204,0,170]
b7_paper[0:image_height,0:image_width, 0:image_channels] = [153,0,127]
b8_paper[0:image_height,0:image_width, 0:image_channels] = [102,0,85]
b9_paper[0:image_height,0:image_width, 0:image_channels] = [51,0,42]
b10_paper[0:image_height,0:image_width, 0:image_channels] = [26,0,21]



#Here you can see where the trackbars are set to whenever you first run the program
#You can also rename the slider bars to whatever you prefer 
#For example if you wanted the track bar that shows up as 'b1/b2' to show up as 'color 1'
#Just rewrite 'b1/b2' as 'color 1'
cv2.createTrackbar('b1/b2', 'Sliders', 100, 255, lambda x:None)
cv2.createTrackbar('b2/b3', 'Sliders', 105, 255, lambda x:None)
cv2.createTrackbar('b3/b4', 'Sliders', 110, 255, lambda x:None)
cv2.createTrackbar('b4/b5', 'Sliders', 115, 255, lambda x:None)
cv2.createTrackbar('b5/b6', 'Sliders', 120, 255, lambda x:None)
cv2.createTrackbar('b6/b7', 'Sliders', 125, 255, lambda x:None)
cv2.createTrackbar('b7/b8', 'Sliders', 130, 255, lambda x:None)
cv2.createTrackbar('b8/b9', 'Sliders', 135, 255, lambda x:None)
cv2.createTrackbar('b9/b10', 'Sliders', 140, 255, lambda x:None)



cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)
    
keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):

    grayscale_break = cv2.getTrackbarPos('b1/b2', 'Sliders')
    grayscale_break_2 = cv2.getTrackbarPos('b2/b3', 'Sliders')
    grayscale_break_3 = cv2.getTrackbarPos('b3/b4', 'Sliders')
    grayscale_break_4 = cv2.getTrackbarPos('b4/b5', 'Sliders')
    grayscale_break_5 = cv2.getTrackbarPos('b5/b6', 'Sliders')
    grayscale_break_6 = cv2.getTrackbarPos('b6/b7', 'Sliders')
    grayscale_break_7 = cv2.getTrackbarPos('b7/b8', 'Sliders')
    grayscale_break_8 = cv2.getTrackbarPos('b8/b9', 'Sliders')
    grayscale_break_9 = cv2.getTrackbarPos('b9/b10', 'Sliders')



    min_grayscale_for_b1 = [0,0,0]
    max_grayscale_for_b1 = [grayscale_break,grayscale_break,grayscale_break]
    min_grayscale_for_b2 = [grayscale_break+1, grayscale_break+1, grayscale_break+1]
    max_grayscale_for_b2 = [grayscale_break_2,grayscale_break_2,grayscale_break_2]
    min_grayscale_for_b3 = [grayscale_break_2+1, grayscale_break_2+1, grayscale_break_2+1]
    max_grayscale_for_b3 = [grayscale_break_3,grayscale_break_3,grayscale_break_3]
    min_grayscale_for_b4 = [grayscale_break_3+1, grayscale_break_3+1, grayscale_break_3+1]
    max_grayscale_for_b4 = [grayscale_break_4,grayscale_break_4,grayscale_break_4]
    min_grayscale_for_b5 = [grayscale_break_4+1, grayscale_break_4+1, grayscale_break_4+1]
    max_grayscale_for_b5 = [grayscale_break_5,grayscale_break_5,grayscale_break_5]
    min_grayscale_for_b6 = [grayscale_break_5+1, grayscale_break_5+1, grayscale_break_5+1]
    max_grayscale_for_b6 = [grayscale_break_6,grayscale_break_6,grayscale_break_6]
    min_grayscale_for_b7 = [grayscale_break_6+1, grayscale_break_6+1, grayscale_break_6+1]
    max_grayscale_for_b7 = [grayscale_break_7,grayscale_break_7,grayscale_break_7]
    min_grayscale_for_b8 = [grayscale_break_7+1, grayscale_break_7+1, grayscale_break_7+1]
    max_grayscale_for_b8 = [grayscale_break_8,grayscale_break_8,grayscale_break_8]
    min_grayscale_for_b9 = [grayscale_break_8+1, grayscale_break_8+1, grayscale_break_8+1]
    max_grayscale_for_b9 = [grayscale_break_9,grayscale_break_9,grayscale_break_9]
    min_grayscale_for_b10 = [grayscale_break_9+1,grayscale_break_9+1,grayscale_break_9+1]
    max_grayscale_for_b10 = [255,255,255]
    
    
    
    min_grayscale_for_b1 = numpy.array(min_grayscale_for_b1, dtype = "uint8")
    max_grayscale_for_b1 = numpy.array(max_grayscale_for_b1, dtype = "uint8")
    min_grayscale_for_b2 = numpy.array(min_grayscale_for_b2, dtype = "uint8")
    max_grayscale_for_b2 = numpy.array(max_grayscale_for_b2, dtype = "uint8")
    min_grayscale_for_b3 = numpy.array(min_grayscale_for_b3, dtype = "uint8")
    max_grayscale_for_b3 = numpy.array(max_grayscale_for_b3, dtype = "uint8")
    min_grayscale_for_b4 = numpy.array(min_grayscale_for_b4, dtype = "uint8")
    max_grayscale_for_b4 = numpy.array(max_grayscale_for_b4, dtype = "uint8")
    min_grayscale_for_b5 = numpy.array(min_grayscale_for_b5, dtype = "uint8")
    max_grayscale_for_b5 = numpy.array(max_grayscale_for_b5, dtype = "uint8")
    min_grayscale_for_b6 = numpy.array(min_grayscale_for_b6, dtype = "uint8")
    max_grayscale_for_b6 = numpy.array(max_grayscale_for_b6, dtype = "uint8")
    min_grayscale_for_b7 = numpy.array(min_grayscale_for_b7, dtype = "uint8")
    max_grayscale_for_b7 = numpy.array(max_grayscale_for_b7, dtype = "uint8")
    min_grayscale_for_b8 = numpy.array(min_grayscale_for_b8, dtype = "uint8")
    max_grayscale_for_b8 = numpy.array(max_grayscale_for_b8, dtype = "uint8")
    min_grayscale_for_b9 = numpy.array(min_grayscale_for_b9, dtype = "uint8")
    max_grayscale_for_b9 = numpy.array(max_grayscale_for_b9, dtype = "uint8")
    min_grayscale_for_b10 = numpy.array(min_grayscale_for_b10, dtype = "uint8")
    max_grayscale_for_b10 = numpy.array(max_grayscale_for_b10, dtype = "uint8")
    
    
    
    block_all_but_the_b1_parts = cv2.inRange(grayscale_image, min_grayscale_for_b1, max_grayscale_for_b1)
    block_all_but_the_b2_parts = cv2.inRange(grayscale_image, min_grayscale_for_b2, max_grayscale_for_b2)
    block_all_but_the_b3_parts = cv2.inRange(grayscale_image, min_grayscale_for_b3, max_grayscale_for_b3)
    block_all_but_the_b4_parts = cv2.inRange(grayscale_image, min_grayscale_for_b4, max_grayscale_for_b4)
    block_all_but_the_b5_parts = cv2.inRange(grayscale_image, min_grayscale_for_b5, max_grayscale_for_b5)
    block_all_but_the_b6_parts = cv2.inRange(grayscale_image, min_grayscale_for_b6, max_grayscale_for_b6)
    block_all_but_the_b7_parts = cv2.inRange(grayscale_image, min_grayscale_for_b7, max_grayscale_for_b7)
    block_all_but_the_b8_parts = cv2.inRange(grayscale_image, min_grayscale_for_b8, max_grayscale_for_b8)
    block_all_but_the_b9_parts = cv2.inRange(grayscale_image, min_grayscale_for_b9, max_grayscale_for_b9)
    block_all_but_the_b10_parts = cv2.inRange(grayscale_image, min_grayscale_for_b10, max_grayscale_for_b10)
    
    
    
    b1_parts_of_image = cv2.bitwise_or(b1_paper, b1_paper, mask = block_all_but_the_b1_parts)
    b2_parts_of_image = cv2.bitwise_or(b2_paper, b2_paper, mask = block_all_but_the_b2_parts)
    b3_parts_of_image = cv2.bitwise_or(b3_paper, b3_paper, mask = block_all_but_the_b3_parts)
    b4_parts_of_image = cv2.bitwise_or(b4_paper, b4_paper, mask = block_all_but_the_b4_parts)
    b5_parts_of_image = cv2.bitwise_or(b5_paper, b5_paper, mask = block_all_but_the_b5_parts)
    b6_parts_of_image = cv2.bitwise_or(b6_paper, b6_paper, mask = block_all_but_the_b6_parts)
    b7_parts_of_image = cv2.bitwise_or(b7_paper, b7_paper, mask = block_all_but_the_b7_parts)
    b8_parts_of_image = cv2.bitwise_or(b8_paper, b8_paper, mask = block_all_but_the_b8_parts)
    b9_parts_of_image = cv2.bitwise_or(b9_paper, b9_paper, mask = block_all_but_the_b9_parts)
    b10_parts_of_image = cv2.bitwise_or(b10_paper, b10_paper, mask = block_all_but_the_b10_parts)
    
    
    
    customized_image = cv2.bitwise_or(b1_parts_of_image, b2_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, b2_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, b3_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, b4_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, b5_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, b6_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, b7_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, b8_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, b9_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, b10_parts_of_image)
    
    
    
    cv2.imshow('Customized Image',customized_image)
    
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()
