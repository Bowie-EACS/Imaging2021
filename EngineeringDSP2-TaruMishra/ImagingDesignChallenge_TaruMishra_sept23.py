# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:33:21 2021

@author: s2125120
"""

# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path

#def trackPosition(slider_name, window_name, min_val):
    #camelCase naming convention being implemented in the function above
 #   current_pos = cv2.getTrackbarPos(slider_name, window_name)
  #  if current_pos < min_val:
   #     print("That value is too low")
    #    cv2.setTrackbarPos(slider_name, window_name, min_val)
     #   return min_val
    #else: 
     #   return current_pos
      
    #if current_pos > max_val:
        #print("That value is too big")
        #cv2.setTrackbarPos(slider_name, window_name, max_val)
        #return max_val
    
   
        
    
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

original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Color1 Parts of Image')
cv2.namedWindow('Color2 Parts of Image')  #windows are being titled
cv2.namedWindow('Sliders2')
cv2.namedWindow('Color3 Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Color4 Parts of Image')
cv2.namedWindow('Color5 Parts of Image')
cv2.namedWindow('Color6 Parts of Image')

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
color3_paper[0:image_height,0:image_width, 0:image_channels] = [255, 0,0]
color4_paper[0:image_height,0:image_width, 0:image_channels] = [255, 0, 150]
color5_paper[0:image_height,0:image_width, 0:image_channels] = [100, 0, 150]
color6_paper[0:image_height,0:image_width, 0:image_channels] = [120, 0, 250]

#grayscale_break = 100
cv2.createTrackbar('Grayscale','Sliders2',100,150, lambda x:None) 
cv2.createTrackbar('Grayscale 2','Sliders2',151, 175, lambda x:None)
cv2.createTrackbar('Grayscale 3','Sliders2',176, 190, lambda x:None)
cv2.createTrackbar('Grayscale 4','Sliders2',191, 200, lambda x:None)
cv2.createTrackbar('Grayscale 5','Sliders2',201, 220, lambda x:None)
cv2.createTrackbar('Grayscale 6','Sliders2',221, 250, lambda x:None)

keypressed = 1

while(keypressed != 27 and keypressed != ord('s')):
    grayscale_break = cv2.getTrackbarPos('Grayscale','Sliders2')
    grayscale_break2 = trackPosition('Grayscale 2','Sliders2',140)
    grayscale_break3 = trackPosition('Grayscale 3','Sliders2',200)
    grayscale_break4 = trackPosition('Grayscale 4', 'Sliders2', 125)
    grayscale_break5 =trackPosition('Grayscale 5', 'Sliders2', 110)
                            
    #grayscale_break2 = 151
    
    min_grayscale_for_color1 = [0,0,0]
    max_grayscale_for_color1 = [grayscale_break,grayscale_break,grayscale_break]
    
    min_grayscale_for_color2 = [grayscale_break+1, grayscale_break+1, grayscale_break+1]
    max_grayscale_for_color2 = [grayscale_break2,grayscale_break2,grayscale_break2]
    #TestingGreyScale for other colors
    
    min_grayscale_for_color3 = [grayscale_break2+1, grayscale_break2+1, grayscale_break2+1]
    max_grayscale_for_color3 = [100,100,100]
    
    #print(min_grayscale_for_color3, max_grayscale_for_blue)

    
    min_grayscale_for_color4 = [grayscale_break3+1, grayscale_break3+1, grayscale_break3+1]
    max_grayscale_for_color4 = [150,150,150]
    
    min_grayscale_for_color5= [grayscale_break4+1, grayscale_break4+1, grayscale_break4+1]
    max_grayscale_for_color5 = [200,200,200]
    
    min_grayscale_for_color6 = [grayscale_break5+1, grayscale_break5+1, grayscale_break5+1]
    max_grayscale_for_color6 = [255,255,255]
    
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
    
    block_all_but_the_color1_parts = cv2.inRange(grayscale_image,
                                          min_grayscale_for_color1,
                                          max_grayscale_for_color1)
    block_all_but_the_color2_parts = cv2.inRange(grayscale_image,
                                             min_grayscale_for_color2,
                                             max_grayscale_for_color2)
    block_all_but_the_color3_parts = cv2.inRange(grayscale_image,
                                          min_grayscale_for_color3,
                                          max_grayscale_for_color3)
    block_all_but_the_color4_parts = cv2.inRange(grayscale_image, min_grayscale_for_color4, max_grayscale_for_color4)

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

    customized_image = cv2.bitwise_or(color1_parts_of_image, color2_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color3_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color4_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color5_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color6_parts_of_image)

    cv2.imshow('Original Image', original_image) #Puts an image inside that window
    cv2.imshow('Grayscale Image',grayscale_image)
   # cv2.imshow('Color1 Parts of Image',color1_parts_of_image)
    #cv2.imshow('Color2 Parts of Image',color2_parts_of_image)
    #cv2.imshow('Color3 Parts of Image', block_all_but_the_color3_parts)
    #cv2.imshow('Color4 Parts of Image', block_all_but_the_color4_parts)
    
    cv2.imshow('Customized Image',customized_image)    
    keypressed = cv2.waitKey(2) #Waiting for keyboard to be pressed 
    
if keypressed == 27:   # 27 is the escape key
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()
    
trackPosition = cv2.getTrackbarPos('Grayscale', 'Sliders2')


#red = color 1
#yellow = color 2
#blue = color 3
#green = color 4