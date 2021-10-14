# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:33:21 2021

@author: s2125120
"""

# Images_01_Starting_Code
# Engineer Your World

#Taru Mishra

#Importing the proper functions in our code from the library that allow us present colors, display image, add sliders
import cv2
import numpy
import os.path
#Allow us to add a random color for our image
import random

#Creating separate variables that will be used as indexes in our random color
var1 = random.randrange(0, 255)
var2 = random.randrange(0, 255)
var3 = random.randrange(0, 255)
#Array selected that will be called in our color_list to use as the ranges for the random color
random_color = [var1, var2, var3]

#Library of colors (1-7 including the random color)
color_list = [[0,0,255],[0,255,255],[255,0,0],[100,100,100],[0,10,0],[0,255,0], [100, 80, 220]]
#color 1 = purple
#color 2 = yellow
#color 3 = blue
#color 4 = grey
#color 5 = green
#color 6 = black
#color7 = random color

#Trackbar position in our data for our data
trackPosition = cv2.getTrackbarPos('Grayscale', 'Sliders2')

#Function created to set a minimum value for the colors in our sliders
def trackPosition(slider_name, window_name, min_val):
#camelCase naming convention being implemented in the function above
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print("That value is too low")
        cv2.setTrackbarPos(slider_name, window_name, min_val)
        return min_val

    else: 
        return current_pos       
    
#Saving the image and informing the user how to save this image
print ("Save your original image in the same folder as this program.")
#Naming the file, images will be locaated in the same place as the script
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")

#Image colors and file name setting
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

#Creating windows for the different images and original images
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
#cv2.namedWindow('Color1 Parts of Image')
#cv2.namedWindow('Color2 Parts of Image')  #windows are being titled
cv2.namedWindow('Sliders2')
#cv2.namedWindow('Color3 Parts of Image')
#cv2.namedWindow('Customized Image')
#cv2.namedWindow('Color4 Parts of Image')
#cv2.namedWindow('Color5 Parts of Image')
#cv2.namedWindow('Color6 Parts of Image')

#Initial index values for the image colors
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]


#Setting the heights and the widths for the colors in the image
color1_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

color2_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color3_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

color4_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

color5_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

color6_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

color7_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

color8_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

#Setting the heights and widths for the different image values
color1_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[0]]
color2_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[1]]
color3_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[2]]
color4_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[3]]
color5_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[4]]
color6_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[5]]
color7_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[6]]
color8_paper[0:image_height,0:image_width, 0:image_channels] = random_color



#Sliders for the differernt colors and ranges for the sliders with the minimum and maximum values

#grayscale_break = 100
cv2.createTrackbar('Grayscale','Sliders2',30,255, lambda x:None) 
cv2.createTrackbar('Grayscale 2','Sliders2',70, 255, lambda x:None)
cv2.createTrackbar('Grayscale 3','Sliders2',110, 255, lambda x:None)
cv2.createTrackbar('Grayscale 4','Sliders2',150, 255, lambda x:None)
cv2.createTrackbar('Grayscale 5','Sliders2',190, 255, lambda x:None)
cv2.createTrackbar('Grayscale 6','Sliders2',230, 255, lambda x:None)
cv2.createTrackbar('Random','Sliders2',245, 255, lambda x:None)


keypressed = 1

while(keypressed != 27 and keypressed != ord('s')):
    #Creating the sliders for the different colors which will be adjustable by the user
    #grayscale_break = cv2.getTrackbarPos('Grayscale','Sliders2',10)
    grayscale_break = trackPosition('Grayscale','Sliders2',10)
    grayscale_break2 = trackPosition('Grayscale 2','Sliders2', 40)
    grayscale_break3 = trackPosition('Grayscale 3','Sliders2',80)
    grayscale_break4 = trackPosition('Grayscale 4', 'Sliders2', 120)
    grayscale_break5 =trackPosition('Grayscale 5', 'Sliders2', 160)
    grayscale_break6 =trackPosition('Grayscale 6', 'Sliders2', 200) 
    grayscale_break7 = trackPosition('Random', 'Sliders2', 240)
                         
    #grayscale_break2 = 151
    
    #Adding the minimum and maximum index values for the colors
    min_grayscale_for_color1 = [0,0,0]
    max_grayscale_for_color1 = [grayscale_break,grayscale_break,grayscale_break]
    
    min_grayscale_for_color2 = [grayscale_break+1, grayscale_break+1, grayscale_break+1]
    max_grayscale_for_color2 = [grayscale_break2,grayscale_break2,grayscale_break2]
    #TestingGreyScale for other colors
    
    min_grayscale_for_color3 = [grayscale_break2+1, grayscale_break2+1, grayscale_break2+1]
    max_grayscale_for_color3 = [grayscale_break3, grayscale_break3, grayscale_break3]
    
    #print(min_grayscale_for_color3, max_grayscale_for_blue)
  
    #Adds the ranges for the different colors
    min_grayscale_for_color4 = [grayscale_break3+1, grayscale_break3+1, grayscale_break3+1]
    max_grayscale_for_color4 = [grayscale_break4, grayscale_break4, grayscale_break4]
    
    min_grayscale_for_color5= [grayscale_break4+1, grayscale_break4+1, grayscale_break4+1]
    max_grayscale_for_color5 = [grayscale_break5, grayscale_break5, grayscale_break5]
    
    min_grayscale_for_color6 = [grayscale_break5+1, grayscale_break5+1, grayscale_break5+1]
    max_grayscale_for_color6 = [grayscale_break6, grayscale_break6, grayscale_break6]
    
    min_grayscale_for_color7 = [grayscale_break6+1, grayscale_break6+1, grayscale_break6+1]
    max_grayscale_for_color7 = [grayscale_break7, grayscale_break7, grayscale_break7]
    
    min_grayscale_for_color8 = [grayscale_break7+1, grayscale_break7+1, grayscale_break7+1]
    max_grayscale_for_color8 = [255,255,255]
   
    #Calling the minimum and maximum levels for the different colors in our code
    min_grayscale_for_color1 = numpy.array(min_grayscale_for_color1, dtype = "uint8")
    max_grayscale_for_color1 = numpy.array(max_grayscale_for_color1, dtype = "uint8")
    
    min_grayscale_for_color2 = numpy.array(min_grayscale_for_color2, dtype = "uint8")
    max_grayscale_for_color2 = numpy.array(max_grayscale_for_color2, dtype = "uint8")
    
    min_grayscale_for_color3 = numpy.array(min_grayscale_for_color3, dtype = "uint8")
    max_grayscale_for_color3 = numpy.array(max_grayscale_for_color3, dtype = "uint8")
    
    min_grayscale_for_color4 = numpy.array(min_grayscale_for_color4, dtype = "uint8")
    max_grayscale_for_color4 = numpy.array(max_grayscale_for_color4, dtype = "uint8")
   
    min_grayscale_for_color5 = numpy.array(min_grayscale_for_color5, dtype = "uint8")
    max_grayscale_for_color5 = numpy.array(max_grayscale_for_color5, dtype = "uint8")
    
    min_grayscale_for_color6 = numpy.array(min_grayscale_for_color6, dtype = "uint8")
    max_grayscale_for_color6 = numpy.array(max_grayscale_for_color6, dtype = "uint8")
    
    min_grayscale_for_color7 = numpy.array(min_grayscale_for_color7, dtype = "uint8")
    max_grayscale_for_color7 = numpy.array(max_grayscale_for_color7, dtype = "uint8")
    
    min_grayscale_for_color8 = numpy.array(min_grayscale_for_color8, dtype = "uint8")
    max_grayscale_for_color8 = numpy.array(max_grayscale_for_color8, dtype = "uint8")
    
    #print(min_grayscale_for_color8)
    #print(max_grayscale_for_color8)
 
    #Blocks different parts of the image corresponding to their color
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
    
    block_all_but_the_color7_parts = cv2.inRange(grayscale_image,
                                          min_grayscale_for_color7,
                                          max_grayscale_for_color7)
    #Parts of random color
    block_all_but_the_color8_parts = cv2.inRange(grayscale_image,
                                          min_grayscale_for_color8,
                                          max_grayscale_for_color8)
#Takes the different parts of the image and displays them in the image
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
    color7_parts_of_image = cv2.bitwise_or(color7_paper, color7_paper,
                                    mask = block_all_but_the_color7_parts)
    #Parts of random color
    color8_parts_of_image = cv2.bitwise_or(color8_paper, color8_paper,
                                    mask = block_all_but_the_color8_parts)

    customized_image = cv2.bitwise_or(color1_parts_of_image, color2_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color3_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color4_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color5_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color6_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color7_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color8_parts_of_image)

    cv2.imshow('Original Image', original_image) #Puts an image inside that window
    cv2.imshow('Grayscale Image',color8_parts_of_image)
    #cv2.imshow('Color1 Parts of Image',color1_parts_of_image)
    #cv2.imshow('Color2 Parts of Image',color2_parts_of_image)
    #cv2.imshow('Color3 Parts of Image', block_all_but_the_color3_parts)
    #cv2.imshow('Color4 Parts of Image', block_all_but_the_color4_parts)
    
    cv2.imshow('Customized Image',customized_image)    
    keypressed = cv2.waitKey(1) #Waiting for keyboard to be pressed 
 
    #Allows the user to save the image
if keypressed == 27:   # 27 is the escape key
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    #new_file = input ("Please enter a name for your file")
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()
    
#Takes the position of the trackbar
trackPosition = cv2.getTrackbarPos('Grayscale', 'Sliders2')


#red = color 1
#yellow = color 2
#blue = color 3
#green = color 4