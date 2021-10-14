# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:37:27 2021

@author: S10041442
"""

# Images_01_Starting_Code
# Engineer Your World

print("Santi Lmfao")

import cv2
import numpy
import os.path

def newTrackbarPos(trackbar_name, trackbar_window, min_val):
    current_pos = cv2.getTrackbarPos(trackbar_name, trackbar_window)
    if current_pos < min_val:
        cv2.setTrackbarPos(trackbar_name, trackbar_window, min_val)
        print("thats too low, smh try again.")
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

#creates files for original image, and grayscale
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)


#creates windows for different images
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
#cv2.namedWindow('Red Parts of Image')
#cv2.namedWindow('Yellow Parts of Image')
#cv2.namedWindow('Green Parts of Image')
#cv2.namedWindow('Blue Parts of Image')
#cv2.namedWindow('Lavender Parts of Image')
#cv2.namedWindow('Aqua Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')
cv2.namedWindow('Color1')
cv2.namedWindow('Color2')
cv2.namedWindow('Color3')
cv2.namedWindow('Color4')
cv2.namedWindow('Color5')
cv2.namedWindow('Color6')



image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

red_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
yellow_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
green_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
blue_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
lavender_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
aqua_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)


cv2.createTrackbar('Red/Yellow', 'Sliders', 63, 255, lambda x:None)
cv2.createTrackbar('Yellow/Green', 'Sliders', 64, 255, lambda x:None)
cv2.createTrackbar('Green/Blue', 'Sliders', 65, 255, lambda x:None)
cv2.createTrackbar('Blue/Lavender', 'Sliders', 65, 255, lambda x:None)
cv2.createTrackbar('Lavender/Aqua', 'Sliders', 65, 255, lambda x:None)

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
cv2.createTrackbar('B5', 'Color5', 245, 255, lambda x:None)
cv2.createTrackbar('G5', 'Color5', 61, 255, lambda x:None)
cv2.createTrackbar('R5', 'Color5', 208, 255, lambda x:None)
cv2.createTrackbar('B6', 'Color6', 245, 255, lambda x:None)
cv2.createTrackbar('G6', 'Color6', 245, 255, lambda x:None)
cv2.createTrackbar('R6', 'Color6', 61, 255, lambda x:None)

keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
            

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

    
    red_paper[0:image_height,0:image_width, 0:image_channels] = [blue1,green1,red1]
    yellow_paper[0:image_height,0:image_width, 0:image_channels] = [blue2,green2,red2]
    green_paper[0:image_height,0:image_width, 0:image_channels] = [blue3,green3,red3]
    blue_paper[0:image_height,0:image_width, 0:image_channels] = [blue4,green4,red4]
    lavender_paper[0:image_height,0:image_width, 0:image_channels] = [blue5,green5,red5]
    aqua_paper[0:image_height,0:image_width, 0:image_channels] = [blue6,green6,red6]
    
    grayscale_break1 = newTrackbarPos('Red/Yellow', 'Sliders', 0)
    grayscale_break2 = newTrackbarPos('Yellow/Green', 'Sliders', grayscale_break1+1)
    grayscale_break3 = newTrackbarPos('Green/Blue', 'Sliders', grayscale_break2+1)
    grayscale_break4 = newTrackbarPos('Blue/Lavender', 'Sliders', grayscale_break3+1)
    grayscale_break5 = newTrackbarPos('Lavender/Aqua', 'Sliders', grayscale_break4+1)
    
    min_grayscale_for_red = [0,0,0]
    max_grayscale_for_red = [grayscale_break1,grayscale_break1,grayscale_break1]
    min_grayscale_for_yellow = [grayscale_break1+1,grayscale_break1+1, 
                                grayscale_break1+1]
    max_grayscale_for_yellow = [grayscale_break2,grayscale_break2,grayscale_break2]
    min_grayscale_for_green = [grayscale_break2+1,grayscale_break2+1, 
                                grayscale_break2+1]
    max_grayscale_for_green = [grayscale_break3,grayscale_break3,grayscale_break3]
    min_grayscale_for_blue = [grayscale_break3+1,grayscale_break3+1, 
                                grayscale_break3+1]
    max_grayscale_for_blue = [grayscale_break4,grayscale_break4, grayscale_break4]
    min_grayscale_for_lavender = [grayscale_break4+1,grayscale_break4+1, 
                                grayscale_break4+1]
    max_grayscale_for_lavender = [grayscale_break5,grayscale_break5,grayscale_break5]
    min_grayscale_for_aqua = [grayscale_break5+1,grayscale_break5+1, 
                                grayscale_break5+1]
    max_grayscale_for_aqua = [255,255,255]
    
    
    
    min_grayscale_for_red = numpy.array(min_grayscale_for_red, dtype = "uint8")
    max_grayscale_for_red = numpy.array(max_grayscale_for_red, dtype = "uint8")
    min_grayscale_for_yellow = numpy.array(min_grayscale_for_yellow,
                                           dtype = "uint8")
    max_grayscale_for_yellow = numpy.array(max_grayscale_for_yellow,
                                           dtype = "uint8")
    min_grayscale_for_green = numpy.array(min_grayscale_for_green, dtype = "uint8")
    max_grayscale_for_green = numpy.array(max_grayscale_for_green, dtype = "uint8")
    min_grayscale_for_blue = numpy.array(min_grayscale_for_blue,
                                           dtype = "uint8")
    max_grayscale_for_blue = numpy.array(max_grayscale_for_blue,
                                           dtype = "uint8")
    min_grayscale_for_lavender = numpy.array(min_grayscale_for_lavender, dtype = "uint8")
    max_grayscale_for_lavender = numpy.array(max_grayscale_for_lavender, dtype = "uint8")
    min_grayscale_for_aqua = numpy.array(min_grayscale_for_aqua,
                                           dtype = "uint8")
    max_grayscale_for_aqua = numpy.array(max_grayscale_for_aqua,
                                           dtype = "uint8")
    
    
    
    
    block_all_but_the_red_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_red,
                                              max_grayscale_for_red)
    block_all_but_the_yellow_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_yellow,
                                                 max_grayscale_for_yellow)
    block_all_but_the_green_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_green,
                                              max_grayscale_for_green)
    block_all_but_the_blue_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_blue,
                                                 max_grayscale_for_blue)
    block_all_but_the_lavender_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_lavender,
                                              max_grayscale_for_lavender)
    block_all_but_the_aqua_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_aqua,
                                                 max_grayscale_for_aqua)
    
    
    
    
    red_parts_of_image = cv2.bitwise_or(red_paper, red_paper,
                                        mask = block_all_but_the_red_parts)
    yellow_parts_of_image = cv2.bitwise_or(yellow_paper, yellow_paper,
                                           mask = block_all_but_the_yellow_parts)
    green_parts_of_image = cv2.bitwise_or(green_paper, green_paper,
                                        mask = block_all_but_the_green_parts)
    blue_parts_of_image = cv2.bitwise_or(blue_paper, blue_paper,
                                           mask = block_all_but_the_blue_parts)
    lavender_parts_of_image = cv2.bitwise_or(lavender_paper, lavender_paper,
                                        mask = block_all_but_the_lavender_parts)
    aqua_parts_of_image = cv2.bitwise_or(aqua_paper, aqua_paper,
                                           mask = block_all_but_the_aqua_parts)
    
    
    
    
    customized_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, green_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, blue_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, lavender_parts_of_image)
    final_image = cv2.bitwise_or(customized_image, aqua_parts_of_image)
    
    
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Grayscale Image',grayscale_image)
    #cv2.imshow('Red Parts of Image',red_parts_of_image)
    #cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
    #cv2.imshow('Green Parts of Image',green_parts_of_image)
    #cv2.imshow('Blue Parts of Image',blue_parts_of_image)
    #cv2.imshow('lavender Parts of Image',lavender_parts_of_image)
    #cv2.imshow('aqua Parts of Image',aqua_parts_of_image)
    cv2.imshow('Customized Image',final_image)
    
    keypressed = cv2.waitKey(1)
    
#exit funtion
if keypressed == 27:
    cv2.destroyAllWindows()
    
#save function
elif keypressed == ord('s'): 
    file_name = input("What would you like to name your new image? file and extension not required.")
    
    
    #table of options
    print("Here are file save options to choose from. Enter the desired image. ")
    print('{0:2}          {1}'.format("Grayscale","0"))
    print('{0:2}          {1}'.format("Color 1","1"))
    print('{0:2}          {1}'.format("Color 2","2"))
    print('{0:2}          {1}'.format("Color 3","3"))
    print('{0:2}          {1}'.format("Color 4","4"))
    print('{0:2}          {1}'.format("Color 5","5"))
    print('{0:2}          {1}'.format("Color 6","6"))
    print('{0:2}          {1}'.format("Custom Image","7"))
    
    color_save = input("which image would you like to save? ")
    
    
    #save options
    if color_save == "0":
        cv2.imwrite(file_name+'_GS.jpg',grayscale_image)
    elif color_save == "1":
        cv2.imwrite(file_name+'_C1.jpg',red_parts_of_image)
    elif color_save == "2":
        cv2.imwrite(file_name+'_C2.jpg',yellow_parts_of_image)
    elif color_save == "3":
        cv2.imwrite(file_name+'_C3.jpg',green_parts_of_image)
    elif color_save == "4":
        cv2.imwrite(file_name+'_C4.jpg',blue_parts_of_image)
    elif color_save == "5":
        cv2.imwrite(file_name+'_C5.jpg',lavender_parts_of_image)
    elif color_save == "6":
        cv2.imwrite(file_name+'_C6.jpg',aqua_parts_of_image)
    elif color_save == "7":
        cv2.imwrite(file_name+'_CustomImage.jpg',final_image)
    
    
    cv2.destroyAllWindows()
