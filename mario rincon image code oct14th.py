# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:08:57 2021
#Mario Rincon - mars-r1n
@author: S10000140
"""
# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path
import random


   

# made slider function by limiting the mins and maxes of each slider
#also makes random color function so that when the customized image comes up it will be preset with a random set of colors
def trackPosition(slider_name, window_name, min_val, max_val):
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print("Hey that's too low my boy")
        cv2.setTrackbarPos(slider_name, window_name, min_val)
        return min_val
    if current_pos > max_val:
        print("Hey that's too high my boy")
        cv2.setTrackbarPos(slider_name, window_name, max_val)
        return max_val
    else:
        return current_pos
def randoColor():
    rand = random.randrange(0, 255)
    return rand
    

#function to let user input the exact name of the file of their pic
print("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "
                     "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print("Something was wrong with that filename. Please try again.")
# resaves file"
original_image = cv2.imread(filename, 1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)
# creates the windows"
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Color 1 Parts of Image')
cv2.namedWindow('Color 2 Parts of Image')
cv2.namedWindow('Color 3 Parts of Image')
cv2.namedWindow('Color 4 Parts of Image')
cv2.namedWindow('Color 5 Parts of Image')
cv2.namedWindow('Color 6 Parts of Image')
cv2.namedWindow('Color 7 Parts of Image')
cv2.namedWindow('Color 8 Parts of Image')
cv2.namedWindow('Color 9 Parts of Image')
cv2.namedWindow('Color 10 Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')
# creates the size of the windows"
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]
# creates the colors that are shown on the pictures"
color_1_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
color_2_paper = numpy.zeros((image_height, image_width, image_channels),
                           numpy.uint8)
color_3_paper = numpy.zeros((image_height, image_width, image_channels),
                         numpy.uint8)
color_4_paper = numpy.zeros((image_height, image_width, image_channels),
                         numpy.uint8)
color_5_paper = numpy.zeros((image_height, image_width, image_channels),
                         numpy.uint8)
color_6_paper = numpy.zeros((image_height, image_width, image_channels),
                         numpy.uint8)
color_7_paper = numpy.zeros((image_height, image_width, image_channels),
                         numpy.uint8)
color_8_paper = numpy.zeros((image_height, image_width, image_channels),
                         numpy.uint8)
color_9_paper = numpy.zeros((image_height, image_width, image_channels),
                         numpy.uint8)
color_10_paper = numpy.zeros((image_height, image_width, image_channels),
                         numpy.uint8)
#creates the different trackbars for the BGR for each color
cv2.createTrackbar('Color 1B', 'Color 1 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 1G', 'Color 1 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 1R', 'Color 1 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 2B', 'Color 2 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 2G', 'Color 2 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 2R', 'Color 2 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 3B', 'Color 3 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 3G', 'Color 3 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 3R', 'Color 3 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 4B', 'Color 4 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 4G', 'Color 4 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 4R', 'Color 4 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 5B', 'Color 5 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 5G', 'Color 5 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 5R', 'Color 5 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 6B', 'Color 6 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 6G', 'Color 6 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 6R', 'Color 6 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 7B', 'Color 7 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 7G', 'Color 7 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 7R', 'Color 7 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 8B', 'Color 8 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 8G', 'Color 8 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 8R', 'Color 8 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 9B', 'Color 9 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 9G', 'Color 9 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 9R', 'Color 9 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 10B', 'Color 10 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 10G', 'Color 10 Parts of Image', randoColor(), 255, lambda x: None)
cv2.createTrackbar('Color 10R', 'Color 10 Parts of Image', randoColor(), 255, lambda x: None)
#creates names and max, min for trackbars
cv2.createTrackbar('Grayscale', 'Sliders', 25, 255, lambda x: None)
cv2.createTrackbar('Grayscale_2', 'Sliders', 50, 255, lambda x: None)
cv2.createTrackbar('Grayscale_3', 'Sliders', 75, 255, lambda x: None)
cv2.createTrackbar('Grayscale_4', 'Sliders', 100, 255, lambda x: None)
cv2.createTrackbar('Grayscale_5', 'Sliders', 125, 255, lambda x: None)
cv2.createTrackbar('Grayscale_6', 'Sliders', 150, 255, lambda x: None)
cv2.createTrackbar('Grayscale_7', 'Sliders', 175, 255, lambda x: None)
cv2.createTrackbar('Grayscale_8', 'Sliders', 200, 255, lambda x: None)
cv2.createTrackbar('Grayscale_9', 'Sliders', 225, 255, lambda x: None)


# mins and maxes define what the colors are on the window
keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
    color_1_paper[0:image_height, 0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color 1B', 'Color 1 Parts of Image'),cv2.getTrackbarPos('Color 1G', 'Color 1 Parts of Image'),cv2.getTrackbarPos('Color 1R', 'Color 1 Parts of Image')]
    color_2_paper[0:image_height, 0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color 2B', 'Color 2 Parts of Image'),cv2.getTrackbarPos('Color 2G', 'Color 2 Parts of Image'),cv2.getTrackbarPos('Color 2R', 'Color 2 Parts of Image')]
    color_3_paper[0:image_height, 0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color 3B', 'Color 3 Parts of Image'),cv2.getTrackbarPos('Color 3G', 'Color 3 Parts of Image'),cv2.getTrackbarPos('Color 3R', 'Color 3 Parts of Image')]
    color_4_paper[0:image_height, 0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color 4B', 'Color 4 Parts of Image'),cv2.getTrackbarPos('Color 4G', 'Color 4 Parts of Image'),cv2.getTrackbarPos('Color 4R', 'Color 4 Parts of Image')]
    color_5_paper[0:image_height, 0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color 5B', 'Color 5 Parts of Image'),cv2.getTrackbarPos('Color 5G', 'Color 5 Parts of Image'),cv2.getTrackbarPos('Color 5R', 'Color 5 Parts of Image')]
    color_6_paper[0:image_height, 0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color 6B', 'Color 6 Parts of Image'),cv2.getTrackbarPos('Color 6G', 'Color 6 Parts of Image'),cv2.getTrackbarPos('Color 6R', 'Color 6 Parts of Image')]
    color_7_paper[0:image_height, 0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color 7B', 'Color 7 Parts of Image'),cv2.getTrackbarPos('Color 7G', 'Color 7 Parts of Image'),cv2.getTrackbarPos('Color 7R', 'Color 7 Parts of Image')]
    color_8_paper[0:image_height, 0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color 8B', 'Color 8 Parts of Image'),cv2.getTrackbarPos('Color 8G', 'Color 8 Parts of Image'),cv2.getTrackbarPos('Color 8R', 'Color 8 Parts of Image')]
    color_9_paper[0:image_height, 0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color 9B', 'Color 9 Parts of Image'),cv2.getTrackbarPos('Color 9G', 'Color 9 Parts of Image'),cv2.getTrackbarPos('Color 9R', 'Color 9 Parts of Image')]
    color_10_paper[0:image_height, 0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color 10B', 'Color 10 Parts of Image'),cv2.getTrackbarPos('Color 10G', 'Color 10 Parts of Image'),cv2.getTrackbarPos('Color 10R', 'Color 10 Parts of Image')]
    
    grayscale_break = trackPosition('Grayscale', 'Sliders', 50, 247)
    grayscale_break_2 = trackPosition('Grayscale_2', 'Sliders', grayscale_break+1, 248)
    grayscale_break_3 = trackPosition('Grayscale_3', 'Sliders', grayscale_break_2+1, 249)
    grayscale_break_4 = trackPosition('Grayscale_4', 'Sliders', grayscale_break_3+1, 250)
    grayscale_break_5 = trackPosition('Grayscale_5', 'Sliders', grayscale_break_4+1, 251)
    grayscale_break_6 = trackPosition('Grayscale_6', 'Sliders', grayscale_break_5+1, 252)
    grayscale_break_7 = trackPosition('Grayscale_7', 'Sliders', grayscale_break_6+1, 253)
    grayscale_break_8 = trackPosition('Grayscale_8', 'Sliders', grayscale_break_7+1, 254)
    grayscale_break_9 = trackPosition('Grayscale_9', 'Sliders', grayscale_break_8+1, 255)

    
#sets the mins and maxes for each grayscale so they don't overlap colors
    min_grayscale_for_color_1 = [0, 0, 0]
    max_grayscale_for_color_1 = [grayscale_break, grayscale_break, grayscale_break]
    
    min_grayscale_for_color_2 = [grayscale_break+1, grayscale_break+1,
                                grayscale_break+1]
    max_grayscale_for_color_2 = [grayscale_break_2, grayscale_break_2,
                                grayscale_break_2]
    min_grayscale_for_color_3 = [grayscale_break_2 +
                              1, grayscale_break_2+1, grayscale_break_2+1]
    max_grayscale_for_color_3 = [grayscale_break_3,
                              grayscale_break_3, grayscale_break_3]
    min_grayscale_for_color_4 = [grayscale_break_3+1, grayscale_break_3+1,
                                grayscale_break_3+1]
    max_grayscale_for_color_4 = [grayscale_break_4, grayscale_break_4,
                                grayscale_break_4]
    min_grayscale_for_color_5 = [grayscale_break_4+1, grayscale_break_4+1,
                                grayscale_break_4+1]
    max_grayscale_for_color_5 = [grayscale_break_5, grayscale_break_5,
                                grayscale_break_5]
    min_grayscale_for_color_6 = [grayscale_break_5+1, grayscale_break_5+1,
                                grayscale_break_5+1]
    max_grayscale_for_color_6 = [grayscale_break_6, grayscale_break_6,
                                grayscale_break_6]
    min_grayscale_for_color_7 = [grayscale_break_6+1, grayscale_break_6+1,
                                grayscale_break_6+1]
    max_grayscale_for_color_7 = [grayscale_break_7, grayscale_break_7,
                                grayscale_break_7]
    min_grayscale_for_color_8 = [grayscale_break_7+1, grayscale_break_7+1,
                                grayscale_break_7+1]
    max_grayscale_for_color_8 = [grayscale_break_8, grayscale_break_8,
                                grayscale_break_8]
    min_grayscale_for_color_9 = [grayscale_break_8+1, grayscale_break_8+1,
                                grayscale_break_8+1]
    max_grayscale_for_color_9 = [grayscale_break_9, grayscale_break_9,
                                grayscale_break_9]
    min_grayscale_for_color_10 = [grayscale_break_9+1, grayscale_break_9+1,
                                grayscale_break_9+1]
    max_grayscale_for_color_10 = [255, 255, 255]

    min_grayscale_for_color_1 = numpy.array(min_grayscale_for_color_1, dtype="uint8")
    max_grayscale_for_color_1 = numpy.array(max_grayscale_for_color_1, dtype="uint8")
    min_grayscale_for_color_2 = numpy.array(min_grayscale_for_color_2,
                                           dtype="uint8")
    max_grayscale_for_color_2 = numpy.array(max_grayscale_for_color_2,
                                           dtype="uint8")
    min_grayscale_for_color_3 = numpy.array(min_grayscale_for_color_3, dtype="uint8")
    max_grayscale_for_color_3 = numpy.array(max_grayscale_for_color_3, dtype="uint8")
    min_grayscale_for_color_4 = numpy.array(min_grayscale_for_color_4, dtype="uint8")
    max_grayscale_for_color_4 = numpy.array(max_grayscale_for_color_4, dtype="uint8")
    min_grayscale_for_color_5 = numpy.array(min_grayscale_for_color_5, dtype="uint8")
    max_grayscale_for_color_5 = numpy.array(max_grayscale_for_color_5, dtype="uint8")
    min_grayscale_for_color_6 = numpy.array(min_grayscale_for_color_6, dtype="uint8")
    max_grayscale_for_color_6 = numpy.array(max_grayscale_for_color_6, dtype="uint8")
    min_grayscale_for_color_7 = numpy.array(min_grayscale_for_color_7, dtype="uint8")
    max_grayscale_for_color_7 = numpy.array(max_grayscale_for_color_7, dtype="uint8")
    min_grayscale_for_color_8 = numpy.array(min_grayscale_for_color_8, dtype="uint8")
    max_grayscale_for_color_8 = numpy.array(max_grayscale_for_color_8, dtype="uint8")
    min_grayscale_for_color_9 = numpy.array(min_grayscale_for_color_9, dtype="uint8")
    max_grayscale_for_color_9 = numpy.array(max_grayscale_for_color_9, dtype="uint8")
    min_grayscale_for_color_10 = numpy.array(min_grayscale_for_color_10, dtype="uint8")
    max_grayscale_for_color_10 = numpy.array(max_grayscale_for_color_10, dtype="uint8")
    # selects which color is displayed"
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
    block_all_but_the_color_7_parts = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_7,
                                               max_grayscale_for_color_7)
    block_all_but_the_color_8_parts = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_8,
                                               max_grayscale_for_color_8)
    block_all_but_the_color_9_parts = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_9,
                                               max_grayscale_for_color_9)
    block_all_but_the_color_10_parts = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_10,
                                               max_grayscale_for_color_10)
    color_1_parts_of_image = cv2.bitwise_or(color_1_paper, color_1_paper,
                                        mask=block_all_but_the_color_1_parts)
    color_2_parts_of_image = cv2.bitwise_or(color_2_paper, color_2_paper,
                                           mask=block_all_but_the_color_2_parts)
    color_3_parts_of_image = cv2.bitwise_or(color_3_paper, color_3_paper,
                                         mask=block_all_but_the_color_3_parts)
    color_4_parts_of_image = cv2.bitwise_or(color_4_paper, color_4_paper,
                                         mask=block_all_but_the_color_4_parts)
    color_5_parts_of_image = cv2.bitwise_or(color_5_paper, color_5_paper,
                                         mask=block_all_but_the_color_5_parts)
    color_6_parts_of_image = cv2.bitwise_or(color_6_paper, color_6_paper,
                                         mask=block_all_but_the_color_6_parts)
    color_7_parts_of_image = cv2.bitwise_or(color_7_paper, color_7_paper,
                                         mask=block_all_but_the_color_7_parts)
    color_8_parts_of_image = cv2.bitwise_or(color_8_paper, color_8_paper,
                                         mask=block_all_but_the_color_8_parts)
    color_9_parts_of_image = cv2.bitwise_or(color_9_paper, color_9_paper,
                                         mask=block_all_but_the_color_9_parts)
    color_10_parts_of_image = cv2.bitwise_or(color_10_paper, color_10_paper,
                                         mask=block_all_but_the_color_10_parts)
  
#puts all of the different colors with their grayscales onto the coustomized image
    customized_image = cv2.bitwise_or(color_1_parts_of_image, color_2_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_3_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_4_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_5_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_6_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_7_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_8_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_9_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_10_parts_of_image)
#displays all of the windows to the user
    cv2.imshow('Color 1 Parts of Image', color_1_parts_of_image)
    cv2.imshow('Color 2 Parts of Image', color_2_parts_of_image)
    cv2.imshow('Color 3 Parts of Image', color_3_parts_of_image)
    cv2.imshow('Color 4 Parts of Image', color_4_parts_of_image)
    cv2.imshow('Color 5 Parts of Image', color_5_parts_of_image)
    cv2.imshow('Color 6 Parts of Image', color_6_parts_of_image)
    cv2.imshow('Color 7 Parts of Image', color_7_parts_of_image)
    cv2.imshow('Color 8 Parts of Image', color_8_parts_of_image)
    cv2.imshow('Color 9 Parts of Image', color_9_parts_of_image)
    cv2.imshow('Color 10 Parts of Image', color_10_parts_of_image)
    cv2.imshow('Customized Image', customized_image)
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Grayscale Image', grayscale_image)

    # this just says if I press escape then it destroys the program
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
    #this makes it so that when you save your customized image you can name what you want the file name to be
elif keypressed == ord('s'):   
    save= input("What would you like to name the file?(Make sure to end your name with .jpg!!!!!!!!!!): ")
    print(save)
    #cv2.imwrite('save', grayscale_image)
    cv2.imwrite(save, customized_image)
    cv2.destroyAllWindows()
