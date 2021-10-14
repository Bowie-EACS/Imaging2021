# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:37:23 2021

@author: S2124526
"""
# Kristian De La Garza
# Period 5
#import libraries
import cv2
import numpy
import os.path


def newTrackbarPos(trackbar_name, trackbar_window, min_value):
    current_pos = cv2.getTrackbarPos(trackbar_name, trackbar_window)
    if current_pos < min_value:
        cv2.setTrackbarPos(trackbar_name, trackbar_window, min_value)
        print("This is not a valid value")
        return min_value
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
#conversion from original to black and white
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)
#^ turns image into threee dimensional array 
# making of windows
#cv2.namedWindow('Original Image')
#cv2.namedWindow('Grayscale Image')
#cv2.namedWindow('Red Parts of Image')
#cv2.namedWindow('Yellow Parts of Image')
#cv2.namedWindow('Customized Image')
#cv2.namedWindow('Color Sliders')
cv2.namedWindow('Image')
#new color


image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]
# making images with same dimensions as originals
color_1 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color_2 = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color_3 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color_4 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color_5 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color_6 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color_7 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)


color_1[0:image_height,0:image_width, 0:image_channels] = [0,0,255]
color_2[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
color_3[0:image_height,0:image_width,0:image_channels] = [255, 0, 0]
color_4[0:image_height,0:image_width,0:image_channels] = [0,255,0]
color_5[0:image_height,0:image_width,0:image_channels] = [255,165,0]
color_6[0:image_height,0:image_width, 0:image_channels] = [150,77,0]
color_7[0:image_height,0:image_width, 0:image_channels] = [0,0,0]


cv2.createTrackbar('Red', 'Image', 254, 254, lambda x:None)
cv2.createTrackbar('Blue', 'Image', 254, 254, lambda x:None)
cv2.createTrackbar('Green', 'Image',254, 254, lambda x:None)
cv2.createTrackbar('Orange', 'Image', 254, 254, lambda x:None)
cv2.createTrackbar('Brown', 'Image', 254, 254, lambda x:None)
cv2.createTrackbar('Black', 'Image', 254, 254, lambda x:None)

#cv2.imshow('Original Image', original_image)
#cv2.imshow('Grayscale Image',grayscale_image)
keypressed = 1
while (keypressed != 27 and keypressed != ord('s')): 
    grayscale_break = newTrackbarPos('Red', 'Image', 0) #divide light from dark, over 100 = light
    #blue track bar
    grayscale_3 = newTrackbarPos('Blue', 'Image', 0)
    grayscale_4 = newTrackbarPos('Green', 'Image', 0)
    grayscale_5 = newTrackbarPos('Orange', 'Image', 0)
    grayscale_6 = newTrackbarPos('Brown', 'Image', 0)
    grayscale_7 = newTrackbarPos('Black', 'Image', 0)

    # any color value between 0 and 100 are converted to red
    min_grayscale_for_1 = [0,0,0]
    max_grayscale_for_1 = [grayscale_break,grayscale_break,grayscale_break]

    # any color value between 0 and 100 are converted to yellow
    min_grayscale_for_2 = [grayscale_break+1,grayscale_break+1, 
                                grayscale_break+1]
    max_grayscale_for_2 = [grayscale_3,grayscale_3,grayscale_3]
    #blue
    min_grayscale_for_3 = [grayscale_3+1,grayscale_3+1,grayscale_3+1]
    max_grayscale_for_3 = [grayscale_4, grayscale_4, grayscale_4]
    
 
    max_grayscale_for_4 = [grayscale_4+1, grayscale_4+1, grayscale_4+1]
    min_grayscale_for_4 = [grayscale_5,grayscale_5,grayscale_5]
    
    min_grayscale_for_5 = [grayscale_5+1,grayscale_5+1,grayscale_5+1]
    max_grayscale_for_5 = [grayscale_6, grayscale_6, grayscale_6]
    
    min_grayscale_for_6 = [grayscale_6+1,grayscale_6+1,grayscale_6+1]
    max_grayscale_for_6 = [grayscale_7,grayscale_7,grayscale_7]
    
    min_grayscale_for_7 = [grayscale_7+1,grayscale_7+1,grayscale_7+1]
    max_grayscale_for_7 = [255,255,255]
    #makes sure data is formatted correctly
    min_grayscale_for_1 = numpy.array(min_grayscale_for_1, dtype = "uint8")
    max_grayscale_for_1 = numpy.array(max_grayscale_for_1, dtype = "uint8")
    min_grayscale_for_2 = numpy.array(min_grayscale_for_2,
                                           dtype = "uint8")
    max_grayscale_for_2 = numpy.array(max_grayscale_for_2,
                                           dtype = "uint8")
    #blue
    min_grayscale_for_3 = numpy.array(min_grayscale_for_3, dtype = "uint8")
    max_grayscale_for_3 = numpy.array(max_grayscale_for_3, dtype = "uint8")
    
    min_grayscale_for_4 = numpy.array(min_grayscale_for_4, dtype = "uint8")
    max_grayscale_for_4 = numpy.array(max_grayscale_for_4, dtype = "uint8")
    
    min_grayscale_for_5 = numpy.array(min_grayscale_for_5, dtype = "uint8")
    max_grayscale_for_5 = numpy.array(max_grayscale_for_5, dtype = "uint8")
    
    min_grayscale_for_6 = numpy.array(min_grayscale_for_6, dtype = "uint8")
    max_grayscale_for_6 = numpy.array(max_grayscale_for_6, dtype = "uint8")
    
    min_grayscale_for_7 = numpy.array(min_grayscale_for_7, dtype = "uint8")
    max_grayscale_for_7 = numpy.array(max_grayscale_for_7, dtype = "uint8")

    
    # inrange cuts out pixels not within range of values
    block_all_but_the_red_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_1,
                                              max_grayscale_for_1)
    block_all_but_the_yellow_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_2,
                                                 max_grayscale_for_2)
    #blue
    block_all__but_blue_parts = cv2.inRange(grayscale_image, min_grayscale_for_3, max_grayscale_for_3)
   
    block_all_but_green_parts = cv2.inRange(grayscale_image, min_grayscale_for_4, max_grayscale_for_4)
    
    block_all__but_orange_parts = cv2.inRange(grayscale_image, min_grayscale_for_5, max_grayscale_for_5)
    
    block_all__but_brown_parts = cv2.inRange(grayscale_image, min_grayscale_for_6, max_grayscale_for_6)
    
    block_all__but_black_parts = cv2.inRange(grayscale_image, min_grayscale_for_7, max_grayscale_for_7)

    #cuts out from red paper the parts of the image that should be red
    red_parts_of_image = cv2.bitwise_or(color_1, color_1,
                                        mask = block_all_but_the_red_parts)
    yellow_parts_of_image = cv2.bitwise_or(color_2, color_2,
                                           mask = block_all_but_the_yellow_parts)
    #blue
    blue_parts_of_image = cv2.bitwise_or(color_3, color_3,
                                         mask = block_all__but_blue_parts)
    green_parts_of_image = cv2.bitwise_or(color_4, color_4,
                                          mask = block_all_but_green_parts)
    
    orange_parts_of_image = cv2.bitwise_or(color_5, color_5,
                                           mask = block_all__but_orange_parts)
    brown_parts_of_image = cv2.bitwise_or(color_6, color_6,
                                           mask = block_all__but_brown_parts)
    black_parts_of_image = cv2.bitwise_or(color_7, color_7,
                                           mask = block_all__but_black_parts)
    #combines red and yellow parts to create customized
    customized_image1 = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image,)
    customized_image2 = cv2.bitwise_or(blue_parts_of_image, green_parts_of_image)
    customized_image3 = cv2.bitwise_or(customized_image1, customized_image2)
    customized_image4 = cv2.bitwise_or(orange_parts_of_image, brown_parts_of_image)
    customized_image5 = cv2.bitwise_or(customized_image4, customized_image3)
    customized_image = cv2.bitwise_or(customized_image5, black_parts_of_image)
    
    # filling windows with images

    #cv2.imshow('Red Parts of Image',red_parts_of_image)
    #cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
    #cv2.imshow('Customized Image',customized_image)
    #cv2.imshow('Blue Image', blue_parts_of_image)
            
    image = numpy.concatenate((original_image, customized_image), axis = 1)
    
    cv2.imshow('Image', image)
    

    keypressed = cv2.waitKey(1) #refreshes every 1 second
    if keypressed == ord('r'):
# ^resets colors to 254
        newTrackbarPos('Red', 'Image', 255)
        newTrackbarPos('Blue', 'Image', 255)
        newTrackbarPos('Green', 'Image', 255)
        newTrackbarPos('Orange', 'Image', 255)
        newTrackbarPos('Brown', 'Image', 255)
        newTrackbarPos('Black', 'Image', 255) 
if keypressed == 27:
    cv2.destroyAllWindows()
 

elif keypressed == ord('s'): 
    
    cv2.imwrite('photo_C_1.jpg',customized_image)
    cv2.imwrite('photo_RY_1.jpg',image)

    cv2.imwrite('photo_RS_tiger.jpg', red_parts_of_image)
    windows = False
# optional destruction of windows after saving
    while windows == False:
        answer = input("Would you like to close the open windows? Y/N")
        if answer == " Y" or "Y":
            cv2.destroyAllWindows()
            windows = True
        elif answer == " N" or "N":  
             print ("No Problem")
             windows = True
