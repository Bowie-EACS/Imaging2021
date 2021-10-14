# -*- coding: utf-8 -*-
""" Created on Thu Sep  9 15:33:46 2021
@author: Decker Padgett
"""

#Decker Padgett, 8th period

import cv2
import numpy
import os.path


#This is for making sure the sliders don't go too low for the image
def trackPosition(slider_name, window_name, min_val):
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print("Back off")
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
#cv2.namedWindow('Red Parts of Image')
#cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')



image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]


maroon_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
red_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

yellow_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
blue_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
green_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
periwinkle_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
orange_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
pink_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)

maroon_paper[0:image_height,0:image_width, 0:image_channels] = [0,0,128]
red_paper[0:image_height,0:image_width, 0:image_channels] = [0,0,255]
yellow_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
blue_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,0]
green_paper[0:image_height,0:image_width, 0:image_channels] = [0,128,0]
periwinkle_paper[0:image_height,0:image_width, 0:image_channels] = [255,204,204]
orange_paper[0:image_height,0:image_width, 0:image_channels] = [255,165,0]
pink_paper[0:image_height,0:image_width, 0:image_channels] = [147,20,255]


cv2.createTrackbar('maroon/red', 'Sliders', 25, 255, lambda x:None)
cv2.createTrackbar('red/yellow', 'Sliders', 50, 255, lambda x:None)
cv2.createTrackbar('yellow/orange', 'Sliders', 75, 255, lambda x:None)
cv2.createTrackbar('orange/pink', 'Sliders', 100, 255, lambda x:None)
cv2.createTrackbar('pink/periwinkle', 'Sliders', 125, 255, lambda x:None)
cv2.createTrackbar('periwinkle/blue', 'Sliders', 150, 255, lambda x:None)
cv2.createTrackbar('blue/green', 'Sliders', 175, 255, lambda x:None)

cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)

keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
    grayscale_break = cv2.getTrackbarPos('maroon/red', 'Sliders')
    grayscale_break1 = cv2.getTrackbarPos('red/yellow', 'Sliders')
    grayscale_break2 = cv2.getTrackbarPos('yellow/orange', 'Sliders')
    grayscale_break3 = cv2.getTrackbarPos('orange/pink', 'Sliders')
    grayscale_break4 = cv2.getTrackbarPos('pink/periwinkle', 'Sliders')
    grayscale_break5 = cv2.getTrackbarPos('periwinkle/blue', 'Sliders')
    grayscale_break6 = cv2.getTrackbarPos('blue/green', 'Sliders')
    
    #This is the minimum position that the sliders will go before you are told to back off
    trackPosition('maroon/red', "Sliders", 1)
    trackPosition('red/yellow', "Sliders", 25)
    trackPosition('yellow/orange', "Sliders", 50)
    trackPosition('orange/pink', "Sliders", 75)
    trackPosition('pink/periwinkle', "Sliders", 100)
    trackPosition('periwinkle/blue', "Sliders", 125)
    trackPosition('blue/green', "Sliders", 150)
    
    #This is to reset the sliders when you move them from their original positions
    if keypressed == ord('r'):
         cv2.setTrackbarPos('maroon/red', "Sliders", 25)
         cv2.setTrackbarPos('red/yellow', 'Sliders', 50)
         cv2.setTrackbarPos('yellow/orange', 'Sliders', 75)
         cv2.setTrackbarPos('orange/pink', 'Sliders', 100)
         cv2.setTrackbarPos('pink/periwinkle', 'Sliders', 125)
         cv2.setTrackbarPos('periwinkle/blue', 'Sliders', 150)
         cv2.setTrackbarPos('blue/green', 'Sliders', 175)
    
    min_grayscale_for_maroon = [0,0,0]
    max_grayscale_for_maroon = [grayscale_break,grayscale_break,grayscale_break]
    min_grayscale_for_red = [grayscale_break+1,grayscale_break+1,grayscale_break+1]
    max_grayscale_for_red = [grayscale_break1,grayscale_break1,grayscale_break1]
    min_grayscale_for_yellow = [grayscale_break1+1,grayscale_break1+1,grayscale_break1+1]
    max_grayscale_for_yellow = [grayscale_break2,grayscale_break2,grayscale_break2]
    min_grayscale_for_orange = [grayscale_break2+1,grayscale_break2+1, 
                                grayscale_break2+1]
    max_grayscale_for_orange = [grayscale_break3,grayscale_break3,grayscale_break3]
    min_grayscale_for_pink = [grayscale_break3+1,grayscale_break3+1, 
                                grayscale_break3+1]
    max_grayscale_for_pink = [grayscale_break4,grayscale_break4,grayscale_break4]
    min_grayscale_for_periwinkle = [grayscale_break4+1,grayscale_break4+1, 
                                grayscale_break4+1]
    max_grayscale_for_periwinkle = [grayscale_break5,grayscale_break5,grayscale_break5]
    min_grayscale_for_blue = [grayscale_break5+1,grayscale_break5+1, 
                                grayscale_break5+1]
    max_grayscale_for_blue = [grayscale_break6,grayscale_break6,grayscale_break6]
    min_grayscale_for_green = [grayscale_break6+1,grayscale_break6+1, 
                                grayscale_break6+1]
    max_grayscale_for_green = [255,255,255]
    
    min_grayscale_for_maroon = numpy.array(min_grayscale_for_maroon, dtype = "uint8")
    max_grayscale_for_maroon = numpy.array(max_grayscale_for_maroon, dtype = "uint8")
    min_grayscale_for_red = numpy.array(min_grayscale_for_red, dtype = "uint8")
    max_grayscale_for_red = numpy.array(max_grayscale_for_red, dtype = "uint8")
    min_grayscale_for_yellow = numpy.array(min_grayscale_for_yellow,
                                           dtype = "uint8")
    max_grayscale_for_yellow = numpy.array(max_grayscale_for_yellow,
                                           dtype = "uint8")
    min_grayscale_for_orange = numpy.array(min_grayscale_for_orange, dtype = "uint8")
    max_grayscale_for_orange = numpy.array(max_grayscale_for_orange, dtype = "uint8")
    min_grayscale_for_pink = numpy.array(min_grayscale_for_pink, dtype = "uint8")
    max_grayscale_for_pink = numpy.array(max_grayscale_for_pink, dtype = "uint8") 
    min_grayscale_for_periwinkle = numpy.array(min_grayscale_for_periwinkle, dtype = "uint8")
    max_grayscale_for_periwinkle = numpy.array(max_grayscale_for_periwinkle, dtype = "uint8")
    min_grayscale_for_blue = numpy.array(min_grayscale_for_blue, dtype = "uint8")
    max_grayscale_for_blue = numpy.array(max_grayscale_for_blue, dtype = "uint8")
    min_grayscale_for_green = numpy.array(min_grayscale_for_green,
                                           dtype = "uint8")
    max_grayscale_for_green = numpy.array(max_grayscale_for_green,
                                           dtype = "uint8")
    
    block_all_but_the_maroon_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_maroon,
                                              max_grayscale_for_maroon)
    block_all_but_the_red_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_red,
                                              max_grayscale_for_red)
    block_all_but_the_yellow_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_yellow,
                                                 max_grayscale_for_yellow)
    block_all_but_the_orange_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_orange,
                                              max_grayscale_for_orange)
    block_all_but_the_pink_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_pink,
                                              max_grayscale_for_pink)
    block_all_but_the_periwinkle_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_periwinkle,
                                              max_grayscale_for_periwinkle)
    block_all_but_the_blue_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_blue,
                                              max_grayscale_for_blue)
    block_all_but_the_green_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_green,
                                                 max_grayscale_for_green)
    
    
    maroon_parts_of_image = cv2.bitwise_or(maroon_paper, maroon_paper,
                                        mask = block_all_but_the_maroon_parts)
    red_parts_of_image = cv2.bitwise_or(red_paper, red_paper,
                                        mask = block_all_but_the_red_parts)
    yellow_parts_of_image = cv2.bitwise_or(yellow_paper, yellow_paper,
                                        mask = block_all_but_the_yellow_parts)
    orange_parts_of_image = cv2.bitwise_or(orange_paper, orange_paper,
                                           mask = block_all_but_the_orange_parts)
    pink_parts_of_image = cv2.bitwise_or(pink_paper, pink_paper,
                                           mask = block_all_but_the_pink_parts)
    periwinkle_parts_of_image = cv2.bitwise_or(periwinkle_paper, periwinkle_paper,
                                           mask = block_all_but_the_periwinkle_parts)
    blue_parts_of_image = cv2.bitwise_or(blue_paper, blue_paper,
                                           mask = block_all_but_the_blue_parts)
    green_parts_of_image = cv2.bitwise_or(green_paper, green_paper,
                                           mask = block_all_but_the_green_parts)
    
    
    customized_image = cv2.bitwise_or(maroon_parts_of_image, red_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, yellow_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, orange_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, pink_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, periwinkle_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, blue_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, green_parts_of_image)
    

    cv2.imshow('Customized Image',customized_image)
  
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()
