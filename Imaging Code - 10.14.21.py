# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:38:07 2021

@author: S2124946 - Santiago Montesinos
"""
 
# Images_01_Starting_Code
# Engineer Your World

#to define a function:
    #def functionName(argument1, argument2):

import cv2
import numpy
import os.path

def newTrackbarPos(trackbar_name,trackbar_window, min_val):
    current_pos = cv2.getTrackbarPos(trackbar_name,trackbar_window)
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

#takes the file and stores it as original_image
original_image = cv2.imread(filename,1)
#cv2.imread's second argument determines if there is a color dimension
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

#Creates the display windows
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Red Parts of Image')
cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow("Green Parts of Image")
cv2.namedWindow("Blue Parts of Image")
cv2.namedWindow("Pink Parts of Image")
cv2.namedWindow("Teal Parts of Image")
cv2.namedWindow('Customized Image')
#slider windows
cv2.namedWindow("Sliders")
cv2.namedWindow('Color1')
cv2.namedWindow('Color2')
cv2.namedWindow('Color3')
cv2.namedWindow('Color4')
cv2.namedWindow('Color5')
cv2.namedWindow('Color6')


#Returns the values of each dimension of the images
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#numpy.zeros makes images that are the exact same as the original so it is consistent
color1 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color2 = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color3 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color4 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color5 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color6 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color7 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color8 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)


#Creates trackbars
cv2.createTrackbar('Red/Yellow', 'Sliders', 42, 254, lambda x:None)
cv2.createTrackbar('Yellow/Green', 'Sliders', 84, 254, lambda x:None)
cv2.createTrackbar('Green/Blue', 'Sliders', 126, 254, lambda x:None)
cv2.createTrackbar('Blue/Pink', 'Sliders', 168, 254, lambda x:None)
cv2.createTrackbar('Pink/Teal', 'Sliders', 212, 254, lambda x:None)

#individual color slider trackbars
cv2.createTrackbar('B1', 'Color1', 0, 255, lambda x:None)
cv2.createTrackbar('G1', 'Color1', 0, 255, lambda x:None)
cv2.createTrackbar('R1', 'Color1', 255, 255, lambda x:None)
cv2.createTrackbar('B2', 'Color2', 0, 255, lambda x:None)
cv2.createTrackbar('G2', 'Color2', 255, 255, lambda x:None)
cv2.createTrackbar('R2', 'Color2', 255, 255, lambda x:None)
cv2.createTrackbar('B3', 'Color3', 0, 255, lambda x:None)
cv2.createTrackbar('G3', 'Color3', 255, 255, lambda x:None)
cv2.createTrackbar('R3', 'Color3', 0, 255, lambda x:None)
cv2.createTrackbar('B4', 'Color4', 255, 255, lambda x:None)
cv2.createTrackbar('G4', 'Color4', 0, 255, lambda x:None)
cv2.createTrackbar('R4', 'Color4', 0, 255, lambda x:None)
cv2.createTrackbar('B5', 'Color5', 255, 255, lambda x:None)
cv2.createTrackbar('G5', 'Color5', 0, 255, lambda x:None)
cv2.createTrackbar('R5', 'Color5', 255, 255, lambda x:None)
cv2.createTrackbar('B6', 'Color6', 255, 255, lambda x:None)
cv2.createTrackbar('G6', 'Color6', 255, 255, lambda x:None)
cv2.createTrackbar('R6', 'Color6', 255, 255, lambda x:None)



#opens up the original images
cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)



#sets the point at which the "light" and "dark" are separated
keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
    #adjust the values of specific colors with the individual sliders
    blue1 = cv2.getTrackbarPos('B1', 'Color1')
    green1 = cv2.getTrackbarPos('G1', 'Color1')
    red1 = cv2.getTrackbarPos('R1', 'Color1')
    
    blue2 = cv2.getTrackbarPos('B2', 'Color2')
    green2 = cv2.getTrackbarPos('G2', 'Color2')
    red2 = cv2.getTrackbarPos('R2', 'Color2')

    blue3 = cv2.getTrackbarPos('B3', 'Color3')
    green3 = cv2.getTrackbarPos('G3', 'Color3')
    red3 = cv2.getTrackbarPos('R3', 'Color3')
    
    blue4 = cv2.getTrackbarPos('B4', 'Color4')
    green4 = cv2.getTrackbarPos('G4', 'Color4')
    red4 = cv2.getTrackbarPos('R4', 'Color4')

    blue5 = cv2.getTrackbarPos('B5', 'Color5')
    green5 = cv2.getTrackbarPos('G5', 'Color5')
    red5 = cv2.getTrackbarPos('R5', 'Color5')
    
    blue6 = cv2.getTrackbarPos('B6', 'Color6')
    green6 = cv2.getTrackbarPos('G6', 'Color6')
    red6 = cv2.getTrackbarPos('R6', 'Color6')

    #using the color values found from the trackbars, the individual colors are changed
    color1[0:image_height,0:image_width, 0:image_channels] = [blue1,green1,red1]
    color2[0:image_height,0:image_width, 0:image_channels] = [blue2,green2,red2]
    color3[0:image_height,0:image_width, 0:image_channels] = [blue3,green3,red3]
    color4[0:image_height,0:image_width, 0:image_channels] = [blue4,green4,red4]
    color5[0:image_height,0:image_width, 0:image_channels] = [blue5,green5,red5]
    color6[0:image_height,0:image_width, 0:image_channels] = [blue6,green6,red6]
    
    #breaks for the combined color values
    grayscale_break1 = newTrackbarPos('Red/Yellow', 'Sliders', 0)
    grayscale_break2 = newTrackbarPos('Yellow/Green', 'Sliders', grayscale_break1+1)
    grayscale_break3 = newTrackbarPos('Green/Blue', 'Sliders', grayscale_break2+1)
    grayscale_break4 = newTrackbarPos('Blue/Pink', 'Sliders', grayscale_break3+1)
    grayscale_break5 = newTrackbarPos('Pink/Teal', 'Sliders', grayscale_break4+1)
    
    #All pieces related to color1 - red
    min_grayscale_for_color1 = [0,0,0]
    max_grayscale_for_color1 = [grayscale_break1,grayscale_break1,grayscale_break1]
    min_grayscale_for_color1 = numpy.array(min_grayscale_for_color1, dtype = "uint8")
    max_grayscale_for_color1 = numpy.array(max_grayscale_for_color1, dtype = "uint8")
    block_all_but_color1 = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color1,
                                              max_grayscale_for_color1)
    color1_parts = cv2.bitwise_or(color1, color1,
                                        mask = block_all_but_color1)
    
    #All pieces of color2 - yellow
    min_grayscale_for_color2 = [grayscale_break1+1,grayscale_break1+1, 
                                grayscale_break1+1]
    max_grayscale_for_color2 = [grayscale_break2,grayscale_break2,grayscale_break2]
    min_grayscale_for_color2 = numpy.array(min_grayscale_for_color2,
                                           dtype = "uint8")
    max_grayscale_for_color2 = numpy.array(max_grayscale_for_color2,
                                           dtype = "uint8")
    block_all_but_color2 = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color2,
                                                 max_grayscale_for_color2)
    block_all_but_color2 = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color2,
                                                 max_grayscale_for_color2)
    color2_parts = cv2.bitwise_or(color2, color2,
                                           mask = block_all_but_color2)

    #All pieces of color3 - green
    min_grayscale_for_color3 = [grayscale_break2+1,grayscale_break2+1,grayscale_break2+1]
    max_grayscale_for_color3 = [grayscale_break3,grayscale_break3,grayscale_break3]
    min_grayscale_for_color3 = numpy.array(min_grayscale_for_color3, dtype = "uint8")
    max_grayscale_for_color3 = numpy.array(max_grayscale_for_color3, dtype = "uint8")
    block_all_but_color3 = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color3,
                                                 max_grayscale_for_color3)
    color3_parts = cv2.bitwise_or(color3, color3,
                                           mask = block_all_but_color3)
    
    #All pieces of color4 - blue    
    min_grayscale_for_color4 = [grayscale_break3+1, grayscale_break3+1, grayscale_break3+1]
    max_grayscale_for_color4 = [grayscale_break4,grayscale_break4,grayscale_break4]  
    min_grayscale_for_color4= numpy.array(min_grayscale_for_color4, dtype = "uint8")
    max_grayscale_for_color4 = numpy.array(max_grayscale_for_color4, dtype = "uint8")
    block_all_but_color4 = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color4,
                                                 max_grayscale_for_color4)
    color4_parts = cv2.bitwise_or(color4, color4,
                                           mask = block_all_but_color4)
     #All pieces for color5 - pink
    min_grayscale_for_color5 = [grayscale_break4+1,grayscale_break4+1,grayscale_break4+1]
    max_grayscale_for_color5 = [grayscale_break5,grayscale_break5,grayscale_break5]
    min_grayscale_for_color5 = numpy.array(min_grayscale_for_color5, dtype = "uint8")
    max_grayscale_for_color5 = numpy.array(max_grayscale_for_color5, dtype = "uint8")
    block_all_but_color5 = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color5,
                                              max_grayscale_for_color5)
    color5_parts = cv2.bitwise_or(color5, color5,
                                        mask = block_all_but_color5)

    #All parts to color6 - teal
    min_grayscale_for_color6 = [grayscale_break5+1,grayscale_break5+1,grayscale_break5+1]
    max_grayscale_for_color6 = [255,255,255]
    min_grayscale_for_color6 = numpy.array(min_grayscale_for_color6, dtype = "uint8")
    max_grayscale_for_color6 = numpy.array(max_grayscale_for_color6, dtype = "uint8")
    block_all_but_color6 = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color6,
                                              max_grayscale_for_color6)
    color6_parts = cv2.bitwise_or(color6, color6,
                                        mask = block_all_but_color6)
   
   
    #combines the cut out parts of red and yellow into one
    red_and_yellow = cv2.bitwise_or(color1_parts, color2_parts)
    red_yellow_and_green = cv2.bitwise_or(red_and_yellow, color3_parts)
    red_yellow_green_and_blue = cv2.bitwise_or(red_yellow_and_green, color4_parts)
    red_yellow_green_blue_and_pink = cv2.bitwise_or(red_yellow_green_and_blue, color5_parts)
    final_image = cv2.bitwise_or(red_yellow_green_blue_and_pink, color6_parts)
    

    cv2.imshow('Customized Image',final_image)
    cv2.imshow('Grayscale Image', grayscale_image)
    cv2.imshow('Red Parts of Image',color1_parts)
    cv2.imshow('Yellow Parts of Image',color2_parts)
    cv2.imshow('Green Parts of Image',color3_parts)
    cv2.imshow('Blue Parts of Image', color4_parts)
    cv2.imshow('Pink Parts of Image', color5_parts)
    cv2.imshow('Teal Parts of Image', color6_parts)
    #cv2.imshow('Red and Yellow',red_and_yellow)
    #cv2.imshow('Red Yellow and Green',red_yellow_and_green)
    #cv2.imshow('Red Yellow Green and Blue', red_yellow_green_and_blue)
    #cv2.imshow('RGBYP', red_yellow_green_blue_and_pink)

    
    keypressed = cv2.waitKey(1)

#if the esc key is pressed all windows close
if keypressed == 27:
    cv2.destroyAllWindows()

#save function. asks which colors to save and under what name
elif keypressed == ord('s'):
    file_name = input("What would you like to name your file? The color and extension"\
                      "are already taken care of: ")
    
        
    #creates a table with each option to save    
    print("Here are your options for colors. Please enter the number value provided")
    print('{0:2}  {1}'.format("Color to Save:", "Enter Number:"))
    print ('{0:2}              {1}'.format("Grayscale","0" ))
    print ('{0:2}                 {1}'.format("Custom","1" ))
    print ('{0:2}                    {1}'.format("Red","2" ))
    print('{0:2}                 {1}'.format("Yellow", "3"))
    print('{0:2}                  {1}'.format("Green", "4"))
    print('{0:2}                   {1}'.format("Blue", "5"))
    print('{0:2}                   {1}'.format("Pink", "6"))
    print('{0:2}                   {1}'.format("Teal", "7"))
    print('{0:2}         {1}'.format("Red and Yellow", "8"))
    print('{0:2}       {1}'.format("Red Yellow Green", "9"))
    print('{0:2}             {1}'.format("RGB+Yellow", "10"))
    print('{0:2}        {1}'.format("RGB+Yellow+Pink", "11"))
    color_save = input("Which color would you like to save? ")
    
    if color_save == "0":
        cv2.imwrite(file_name+'_GS.jpg',grayscale_image)
    elif color_save == "1":
        cv2.imwrite(file_name+'_Custom.jpg',final_image)
#Red
    elif color_save == "2":
        cv2.imwrite(file_name+'_Red.jpg',color1_parts)
#Yellow
    elif color_save == "3":
        cv2.imwrite(file_name+'_Yellow.jpg',color2_parts)
#Green
    elif color_save == "4":
        cv2.imwrite(file_name+'_Green.jpg',color3_parts)
#Blue
    elif color_save == "5":
        cv2.imwrite(file_name+'_Blue.jpg',color4_parts)
#Pink
    elif color_save == "6":
        cv2.imwrite(file_name+'_Pink.jpg',color5_parts)
#Teal
    elif color_save == "7":
        cv2.imwrite(file_name+'_Teal.jpg',color6_parts)
#Red and Yellow
    elif color_save == "8":
        cv2.imwrite(file_name+'_RY.jpg',red_and_yellow)
#Red, Yellow and Green
    elif color_save == "9":
        cv2.imwrite(file_name+'_RYG.jpg',red_yellow_and_green)
#Red, Yellow, Green and Blue
    elif color_save == "10":
        cv2.imwrite(file_name+'_RGBY.jpg', red_yellow_green_and_blue)
#Red, Yellow, Green, Blue, and Pink        
    elif color_save == "11":
        cv2.imwrite(file_name+'_RGBYP.jpg', red_yellow_green_blue_and_pink)
