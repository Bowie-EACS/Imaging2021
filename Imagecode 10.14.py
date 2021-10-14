# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:37:57 2021

@author: Marc Galindo
"""

# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path

def newTrackbarPos(trackbar_name, trackbar_window, min_val):
    current_pos = cv2.getTrackbarPos(trackbar_name, trackbar_window)
    if current_pos < min_val:
        cv2.setTrackbarPos(trackbar_name, trackbar_window, min_val)
        print("That's too low")
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
cv2.namedWindow('Red Parts of Image')
cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow('Green Parts of Image')
cv2.namedWindow('Purple Parts of Image')
cv2.namedWindow('Blue Parts of Image')
cv2.namedWindow('Orange Parts of Image')
cv2.namedWindow('Final')
cv2.namedWindow('Sliders')

image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]


color1_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

color2_paper = numpy.zeros((image_height,image_width,image_channels), 
                      numpy.uint8)
color3_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color4_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color5_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color6_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

color1_paper[0:image_height,0:image_width, 0:image_channels] = [0,0,255]
color2_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
color3_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,0]
color4_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,255]
color5_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,0]
color6_paper[0:image_height,0:image_width, 0:image_channels] = [0,128,255]


cv2.createTrackbar('Red&Yellow', 'Sliders', 42, 254, lambda x:None)
cv2.createTrackbar('Yellow&Green', 'Sliders', 84, 254, lambda x:None)
cv2.createTrackbar('Green&Purple', 'Sliders', 126, 254, lambda x:None)
cv2.createTrackbar('Purple&Blue', 'Sliders', 168, 254, lambda x:None)
cv2.createTrackbar('Blue&Orange', 'Sliders', 210, 254, lambda x:None)




cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image', grayscale_image)

keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
    
    grayscale_break1 = newTrackbarPos('Red&Yellow', 'Sliders', 0)
    grayscale_break2 = newTrackbarPos('Yellow&Green', 'Sliders', grayscale_break1+1)
    grayscale_break3 = newTrackbarPos('Green&Purple', 'Sliders', grayscale_break2+1)
    grayscale_break4 = newTrackbarPos('Purple&Blue', 'Sliders', grayscale_break3+1)
    grayscale_break5 = newTrackbarPos('Blue&Orange', 'Sliders', grayscale_break4+1)



    #All code for red
    min_grayscale_for_color1 = [0,0,0]
    max_grayscale_for_color1 = [grayscale_break1,grayscale_break1,grayscale_break1]
    min_grayscale_for_color1 = numpy.array(min_grayscale_for_color1, dtype = "uint8")
    max_grayscale_for_color1 = numpy.array(max_grayscale_for_color1, dtype = "uint8")
    block_all_but_the_color1_parts = cv2.inRange(grayscale_image, 
                                            min_grayscale_for_color1, 
                                            max_grayscale_for_color1)
    color1_parts_of_image = cv2.bitwise_or(color1_paper, color1_paper,
                                        mask = block_all_but_the_color1_parts)
    
    #all code for yellow
    min_grayscale_for_color2 = [grayscale_break1+1,grayscale_break1+1, 
                                grayscale_break1+1]
    max_grayscale_for_color2 = [grayscale_break2,grayscale_break2,grayscale_break2]
    min_grayscale_for_color2 = numpy.array(min_grayscale_for_color2,
                                       dtype = "uint8")
    max_grayscale_for_color2 = numpy.array(max_grayscale_for_color2,
                                           dtype = "uint8")
    block_all_but_the_color2_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color2,
                                                 max_grayscale_for_color2)
    color2_parts_of_image = cv2.bitwise_or(color2_paper, color2_paper,
                                           mask = block_all_but_the_color2_parts)
    #All code for green
    min_grayscale_for_color3 = [grayscale_break3,grayscale_break3,grayscale_break3]
    max_grayscale_for_color3 = [grayscale_break3+1,grayscale_break3+1,grayscale_break3+1]
    min_grayscale_for_color3 = numpy.array(min_grayscale_for_color3, dtype = "uint8")
    max_grayscale_for_color3 = numpy.array(max_grayscale_for_color3, dtype = "uint8")
    block_all_but_the_color3_parts = cv2.inRange(grayscale_image, 
                                            min_grayscale_for_color3, 
                                            max_grayscale_for_color3)
    color3_parts_of_image = cv2.bitwise_or(color3_paper, color3_paper,
                                        mask = block_all_but_the_color3_parts)
    #All code for purple
    max_grayscale_for_color4 = [grayscale_break4,grayscale_break4,grayscale_break4]
    min_grayscale_for_color4 = [grayscale_break4+1,grayscale_break4+1,grayscale_break4+1]
    min_grayscale_for_color4 = numpy.array(min_grayscale_for_color4, dtype = "uint8")
    max_grayscale_for_color4 = numpy.array(max_grayscale_for_color4, dtype = "uint8")
    block_all_but_the_color4_parts = cv2.inRange(grayscale_image, 
                                            min_grayscale_for_color4, 
                                            max_grayscale_for_color4)
    color4_parts_of_image = cv2.bitwise_or(color4_paper, color4_paper,
                                        mask = block_all_but_the_color4_parts)
    #all code for blue
    min_grayscale_for_color5 = [grayscale_break5,grayscale_break5,grayscale_break5]
    max_grayscale_for_color5 = [grayscale_break5+1,grayscale_break5+1,grayscale_break5+1]
    min_grayscale_for_color5 = numpy.array(min_grayscale_for_color5, dtype = "uint8")
    max_grayscale_for_color5 = numpy.array(max_grayscale_for_color5, dtype = "uint8")
    block_all_but_the_color5_parts = cv2.inRange(grayscale_image, 
                                            min_grayscale_for_color5, 
                                            max_grayscale_for_color5)
    color5_parts_of_image = cv2.bitwise_or(color5_paper, color5_paper,
                                        mask = block_all_but_the_color5_parts)
    #all code for orange
    max_grayscale_for_color6 = [255,255,255]
    min_grayscale_for_color6 = [grayscale_break5+1,grayscale_break5+1,grayscale_break5+1]
    min_grayscale_for_color6 = numpy.array(min_grayscale_for_color6, dtype = "uint8")
    max_grayscale_for_color6 = numpy.array(max_grayscale_for_color6, dtype = "uint8")
    block_all_but_the_color6_parts = cv2.inRange(grayscale_image, 
                                            min_grayscale_for_color6, 
                                            max_grayscale_for_color6)
    color6_parts_of_image = cv2.bitwise_or(color6_paper, color6_paper,
                                        mask = block_all_but_the_color6_parts)
    
    
    customized_image1 = cv2.bitwise_or(color1_parts_of_image, color2_parts_of_image)
    customized_image2 = cv2.bitwise_or(color3_parts_of_image, color4_parts_of_image)
    customized_image3 = cv2.bitwise_or(color5_parts_of_image, color6_parts_of_image)
    customized_image4 = cv2.bitwise_or(customized_image1, customized_image2)
    final_image = cv2.bitwise_or(customized_image4, customized_image3)

    cv2.imshow('Red Parts of Image',color1_parts_of_image)
    cv2.imshow('Yellow Parts of Image',color2_parts_of_image)
    cv2.imshow('Green Parts of Image',color3_parts_of_image)
    cv2.imshow('Purple Parts of Image',color4_parts_of_image)
    cv2.imshow('Blue Parts of Image',color5_parts_of_image)
    cv2.imshow('Orange Parts of Image',color6_parts_of_image)
    cv2.imshow('Final', final_image)
    
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',final_image)
    cv2.destroyAllWindows()

