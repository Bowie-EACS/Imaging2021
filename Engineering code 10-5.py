# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:39:14 2021

@author: S2117393
"""

# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path

# This is where we define and introduce newTrackbar position and make it to where the user can't move the slider past its minimum.
def newTrackbarPos(trackbar_name, trackbar_window, min_val, end_point):
    current_pos = cv2.getTrackbarPos(trackbar_name, trackbar_window)
    if current_pos < min_val:
        cv2.setTrackbarPos(trackbar_name, trackbar_window, min_val)
        print("That's too low")
        return min_val
    elif current_pos > end_point:
        print("that's too high")
        return current_pos
    else:
        return current_pos
    
# This is where you insert a file name and the program sees if it's functional

print ("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")

# this is where the program takes your filename and introduces BGR colors
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

# this is where we open new windows that we want or need

cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
#cv2.namedWindow('Red Parts of Image')
#cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow('Customized Image')
#cv2.namedWindow('Sliders')
cv2.namedWindow('Sliders_2')

image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#This is where numpy.zero sets arrays of zeros

color_1 = numpy.zeros((image_height,image_width,image_channels), 
                         numpy.uint8)
color_2 = numpy.zeros((image_height,image_width,image_channels),
                         numpy.uint8)
color_3 = numpy.zeros((image_height,image_width,image_channels),
                         numpy.uint8)
color_4 = numpy.zeros((image_height,image_width,image_channels),
                         numpy.uint8)
color_5 = numpy.zeros((image_height,image_width,image_channels),
                         numpy.uint8)
color_6 = numpy.zeros((image_height,image_width,image_channels),
                         numpy.uint8)



# this sets the image to the exact same sizes

color_1[0:image_height,0:image_width, 0:image_channels] = [0,0,255]
color_2[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
color_3[0:image_height,0:image_width, 0:image_channels] = [255,0,0]
color_4[0:image_height,0:image_width, 0:image_channels] = [50,100,200]
color_5[0:image_height,0:image_width, 0:image_channels] = [128,0,128]
color_6[0:image_height,0:image_width, 0:image_channels] = [0,128,0]

# the create track bar is making it to where the sliders have a minimum and a maximum
# the lambda is making it to where it doesn't continue 

cv2.createTrackbar('grayscale_1', 'Sliders_2', 0, 255,  lambda x:None)
cv2.createTrackbar('grayscale_2', 'Sliders_2', 52, 255, lambda x:None)
cv2.createTrackbar('grayscale_3', 'Sliders_2', 103, 255, lambda x:None)
cv2.createTrackbar('grayscale_4', 'Sliders_2', 154, 255, lambda x:None)
cv2.createTrackbar('grayscale_5', 'Sliders_2', 205, 255, lambda x:None)

# imshow is where it shows the images that are in different windows

cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)

# the grayscale breaks are making it to where the images are separated

keypressed = 1
print("press the esc or s key to finalize your value")
while (keypressed != 27 and keypressed != ord('s')):
    grayscale_break_1 = newTrackbarPos('grayscale_1', 'Sliders_2', 0, 51) # where we separate the image. any color values between 0-100 are going to be red instead of gray. any color between 101 and 255 are going to be yellow
    grayscale_break_2 = newTrackbarPos('grayscale_2', 'Sliders_2', 52, 102) 
    grayscale_break_3 = newTrackbarPos('grayscale_3', 'Sliders_2', 103, 153) 
    grayscale_break_4 = newTrackbarPos('grayscale_4', 'Sliders_2', 154, 204)
    grayscale_break_5 = newTrackbarPos('grayscale_5', 'Sliders_2', 205, 255)
    
    # this is where we set the make it to where the minimum for the next color is 1 greater that the color before
    
    min_grayscale_for_color_1 = [0,0,0]
    max_grayscale_for_color_1 = [grayscale_break_1,grayscale_break_1,grayscale_break_1]
    min_grayscale_for_color_2 = [grayscale_break_1+1,grayscale_break_1+1,grayscale_break_1+1]
    max_grayscale_for_color_2 = [grayscale_break_2,grayscale_break_2,grayscale_break_2]
    
    min_grayscale_for_color_3 = [grayscale_break_2+1,grayscale_break_2+1,grayscale_break_2+1]
    max_grayscale_for_color_3 = [grayscale_break_3,grayscale_break_3,grayscale_break_3]
    min_grayscale_for_color_4 = [grayscale_break_3+1,grayscale_break_3+1,grayscale_break_3+1] 
    max_grayscale_for_color_4 = [grayscale_break_4,grayscale_break_4,grayscale_break_4]
    
    min_grayscale_for_color_5 = [grayscale_break_4+1,grayscale_break_4+1,grayscale_break_4+1]
    max_grayscale_for_color_5 = [grayscale_break_5,grayscale_break_5,grayscale_break_5]
    min_grayscale_for_color_6 = [grayscale_break_5+1,grayscale_break_5+1,grayscale_break_5+1] 
    max_grayscale_for_color_6 = [255,255,255]
    
    min_grayscale_for_color_1 = numpy.array(min_grayscale_for_color_1, dtype = "uint8")
    max_grayscale_for_color_1 = numpy.array(max_grayscale_for_color_1, dtype = "uint8")
    min_grayscale_for_color_2 = numpy.array(min_grayscale_for_color_2,dtype = "uint8")
    max_grayscale_for_color_2 = numpy.array(max_grayscale_for_color_2,dtype = "uint8")
    
    
    min_grayscale_for_color_3 = numpy.array(min_grayscale_for_color_3, dtype = "uint8")
    max_grayscale_for_color_3 = numpy.array(max_grayscale_for_color_3, dtype = "uint8")
    min_grayscale_for_color_4 = numpy.array(min_grayscale_for_color_4,dtype = "uint8")
    max_grayscale_for_color_4 = numpy.array(max_grayscale_for_color_4,dtype = "uint8")
    
    
    min_grayscale_for_color_5 = numpy.array(min_grayscale_for_color_5,dtype = "uint8")
    max_grayscale_for_color_5 = numpy.array(max_grayscale_for_color_5,dtype = "uint8")
    min_grayscale_for_color_6 = numpy.array(min_grayscale_for_color_6,dtype = "uint8")
    max_grayscale_for_color_6 = numpy.array(max_grayscale_for_color_6,dtype = "uint8")
    
    block_all_but_the_color_1_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color_1,
                                              max_grayscale_for_color_1)
    block_all_but_the_color_2_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color_2,
                                                 max_grayscale_for_color_2)
    
    block_all_but_the_color_3_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color_3,
                                              max_grayscale_for_color_3)
    block_all_but_the_color_4_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color_4,
                                                 max_grayscale_for_color_4)
    
    block_all_but_the_color_5_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color_5,
                                              max_grayscale_for_color_5)
    block_all_but_the_color_6_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color_6,
                                                 max_grayscale_for_color_6)
    
    #This is where the program takes each color and blocks everything but the color parts of the image.
    color_1_parts_of_image = cv2.bitwise_or(color_1, color_1,
                                        mask = block_all_but_the_color_1_parts)
    color_2_parts_of_image = cv2.bitwise_or(color_2, color_2,
                                           mask = block_all_but_the_color_2_parts)
    
    color_3_parts_of_image = cv2.bitwise_or(color_3, color_3,
                                        mask = block_all_but_the_color_3_parts)
    color_4_parts_of_image = cv2.bitwise_or(color_4, color_4,
                                           mask = block_all_but_the_color_4_parts)
    
    color_5_parts_of_image = cv2.bitwise_or(color_5, color_5,
                                        mask = block_all_but_the_color_5_parts)
    color_6_parts_of_image = cv2.bitwise_or(color_6, color_6,
                                           mask = block_all_but_the_color_6_parts)
    
    # all the color parts are being added together so that under customized image final we can show all the colors on a window
    
    customized_image_1 = cv2.bitwise_or(color_1_parts_of_image, color_2_parts_of_image)
    
    customized_image_2 = cv2.bitwise_or(color_3_parts_of_image, color_4_parts_of_image)
    
    customized_image_3 = cv2.bitwise_or(customized_image_1, customized_image_2)
    
    customized_image_4 = cv2.bitwise_or(color_5_parts_of_image, color_6_parts_of_image)
    
    customized_image_final = cv2.bitwise_or(customized_image_3, customized_image_4)
    
    #cv2.imshow('Red Parts of Image',color_1_parts_of_image)
    #cv2.imshow('Yellow Parts of Image',color_2_parts_of_image)
    cv2.imshow('Customized Image',customized_image_final)
    
    # This is where we close all the windows
    
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): #change this so a custim image name can be created
    #cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image_final)
    cv2.destroyAllWindows()
