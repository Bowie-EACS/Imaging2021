# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:38:05 2021

@author: s2124944
"""

# Images_01_Starting_Code
# Engineer Your World

#Imports library
import cv2
import numpy
import os.path
import random

#defines newtrackbarpos max and minimum limits, and displays message and returns to max/min val when exceeding limit.
def newTrackbarPos(trackbar_name, trackbar_window, min_val, max_val):
    current_pos = cv2.getTrackbarPos(trackbar_name, trackbar_window)
    if current_pos < min_val:
            cv2.setTrackbarPos(trackbar_name, trackbar_window, min_val)
            print ("That's too low")
            return min_val
        
    if current_pos > max_val:
            cv2.setTrackbarPos(trackbar_name, trackbar_window, max_val)
            print ("That's too high")
            return max_val
    else:
        return current_pos
        
        
#Enter file name of image into prompt, if invalid display error message    
print ("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")
        
#Takes image, removes color demension [123], and makes it grey [123,123,123]
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)


#Create windows for original, grayscale, customized image, and sliders.
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
#cv2.namedWindow('Green Parts of Image')
#cv2.namedWindow('Blue Parts of Image')
#cv2.namedWindow('Red Parts of Image')
#cv2.namedWindow('Yellow Parts of Image')
#cv2.namedWindow('Purple Parts of Image')
#cv2.namedWindow('Orange Parts of Image')
#cv2.namedWindow('Cyan Parts of Image')
#cv2.namedWindow('Magenta Parts of Image')
#cv2.namedWindow('Red/Yellow Image')
#cv2.namedWindow('Blue/Green Image')
#cv2.namedWindow('Orange/Green Image')
#cv2.namedWindow('Cyan/Magenta Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')
cv2.namedWindow('Color_1')
cv2.namedWindow('Color_2')
cv2.namedWindow('Color_3')
cv2.namedWindow('Color_4')
cv2.namedWindow('Color_5')
cv2.namedWindow('Color_6')
cv2.namedWindow('Color_7')
cv2.namedWindow('Color_8')


image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

Color_1_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
Color_2_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
Color_3_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
Color_4_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
Color_5_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
Color_6_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
Color_7_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
Color_8_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

#Red base value
Blue_1 = 0
Green_1 = 0
Red_1 = 255
#Blue base value
Blue_2 = 255
Green_2 = 0
Red_2 = 0
#Green base value
Blue_3 = 0
Green_3 = 255
Red_3 = 0
#Yellow base value
Blue_4 = 255
Green_4 = 255
Red_4 = 0
#Orange base value
Blue_5 = 0
Green_5 = 128
Red_5 = 255
#Purple base value
Blue_6 = 128
Green_6 = 0
Red_6 = 128
#Cyan base value
Blue_7 = 255
Green_7 = 255
Red_7 = 0
#Magenta base value
Blue_8 = 255
Green_8 = 0
Red_8 = 255



#Creates a blue, green and red trackbar for each color. 
cv2.createTrackbar('Blue_1', 'Color_1', 10, 254, lambda x:None)
cv2.createTrackbar('Green_1', 'Color_1', 10, 254, lambda x:None)
cv2.createTrackbar('Red_1', 'Color_1', 10, 254, lambda x:None)

cv2.createTrackbar('Blue_2', 'Color_2', 40, 254, lambda x:None)
cv2.createTrackbar('Green_2', 'Color_2', 40, 254, lambda x:None)
cv2.createTrackbar('Red_2', 'Color_2', 40, 254, lambda x:None)

cv2.createTrackbar('Blue_3', 'Color_3', 70, 254, lambda x:None)
cv2.createTrackbar('Green_3', 'Color_3', 70, 254, lambda x:None)
cv2.createTrackbar('Red_3', 'Color_3', 70, 254, lambda x:None)

cv2.createTrackbar('Blue_4', 'Color_4', 100, 254, lambda x:None)
cv2.createTrackbar('Green_4', 'Color_4', 100, 254, lambda x:None)
cv2.createTrackbar('Red_4', 'Color_4', 100, 254, lambda x:None)

cv2.createTrackbar('Blue_5', 'Color_5', 140, 254, lambda x:None)
cv2.createTrackbar('Green_5', 'Color_5', 140, 254, lambda x:None)
cv2.createTrackbar('Red_5', 'Color_5', 140, 254, lambda x:None)

cv2.createTrackbar('Blue_6', 'Color_6', 170, 254, lambda x:None)
cv2.createTrackbar('Green_6', 'Color_6', 170, 254, lambda x:None)
cv2.createTrackbar('Red_6', 'Color_6', 170, 254, lambda x:None)

cv2.createTrackbar('Blue_7', 'Color_7', 200, 254, lambda x:None)
cv2.createTrackbar('Green_7', 'Color_7', 200, 254, lambda x:None)
cv2.createTrackbar('Red_7', 'Color_7', 200, 254, lambda x:None)

cv2.createTrackbar('Blue_8', 'Color_8', 230, 254, lambda x:None)
cv2.createTrackbar('Green_8', 'Color_8', 230, 254, lambda x:None)
cv2.createTrackbar('Red_8', 'Color_8', 230, 254, lambda x:None)



#Create grayscale break limits
grayscale_break = cv2.createTrackbar('Red', 'Sliders', 10, 254, lambda x:None)
grayscale_break2 = cv2.createTrackbar('Yellow', 'Sliders', 40, 254, lambda x:None)
grayscale_break3 = cv2.createTrackbar('Green', 'Sliders', 70, 254, lambda x:None)
grayscale_break4 = cv2.createTrackbar('Blue', 'Sliders' , 100, 254, lambda x:None)
grayscale_break5 = cv2.createTrackbar('Orange', 'Sliders', 140, 254, lambda x:None)
grayscale_break6 = cv2.createTrackbar('Purple', 'Sliders', 170, 254, lambda x:None)
grayscale_break7 = cv2.createTrackbar('Cyan', 'Sliders', 200, 254, lambda x:None)




#While esc key not pressed
keypressed = 1
while (keypressed != 27 and keypressed != ord('s')): 
 
    
#If 1 key is pressed, run loop
    if keypressed == 49:
        
        #Takes base rgb values and randomizes them from 0-255 range. Sets trackbar to new value.
        Blue_1 = random.randrange(0,255)
        cv2.setTrackbarPos('Blue_1', 'Color_1', Blue_1)
        Green_1 = random.randrange(0,255)
        cv2.setTrackbarPos('Green_1', 'Color_1', Green_1)
        Red_1 = random.randrange(0,255)
        cv2.setTrackbarPos('Red_1', 'Color_1', Red_1)

        Blue_2 = random.randrange(0,255)
        cv2.setTrackbarPos('Blue_2', 'Color_2', Blue_2)
        Green_2 = random.randrange(0,255)
        cv2.setTrackbarPos('Green_2', 'Color_2', Green_2)
        Red_2 = random.randrange(0,255)
        cv2.setTrackbarPos('Red_2', 'Color_2', Red_2)
        
        Blue_3 = random.randrange(0,255)
        cv2.setTrackbarPos('Blue_3', 'Color_3', Blue_3)
        Green_3 = random.randrange(0,255)
        cv2.setTrackbarPos('Green_3', 'Color_3', Green_3)
        Red_3 = random.randrange(0,255)
        cv2.setTrackbarPos('Red_3', 'Color_3', Red_3)
        
        Blue_4 = random.randrange(0,255)
        cv2.setTrackbarPos('Blue_4', 'Color_4', Blue_4)
        Green_4 = random.randrange(0,255)
        cv2.setTrackbarPos('Green_4', 'Color_4', Green_4)
        Red_4 = random.randrange(0,255)
        cv2.setTrackbarPos('Red_4', 'Color_4', Red_4)
        
        Blue_5 = random.randrange(0,255)
        cv2.setTrackbarPos('Blue_5', 'Color_5', Blue_5)
        Green_5 = random.randrange(0,255)
        cv2.setTrackbarPos('Green_5', 'Color_5', Green_5)
        Red_5 = random.randrange(0,255)
        cv2.setTrackbarPos('Red_5', 'Color_5', Red_5)
        
        Blue_6 = random.randrange(0,255)
        cv2.setTrackbarPos('Blue_6', 'Color_6', Blue_6)
        Green_6 = random.randrange(0,255)
        cv2.setTrackbarPos('Green_6', 'Color_6', Green_6)
        Red_6 = random.randrange(0,255)
        cv2.setTrackbarPos('Red_6', 'Color_6', Red_6)
        
        Blue_7 = random.randrange(0,255)
        cv2.setTrackbarPos('Blue_7', 'Color_7', Blue_7)
        Green_7 = random.randrange(0,255)
        cv2.setTrackbarPos('Green_7', 'Color_7', Green_7)
        Red_7 = random.randrange(0,255)
        cv2.setTrackbarPos('Red_7', 'Color_7', Red_7)
        
        Blue_8 = random.randrange(0,255)
        cv2.setTrackbarPos('Blue_8', 'Color_8', Blue_8)
        Green_8 = random.randrange(0,255)
        cv2.setTrackbarPos('Green_8', 'Color_8', Green_8)
        Red_8 = random.randrange(0,255)
        cv2.setTrackbarPos('Red_8', 'Color_8', Red_8)
           
    else:     
        #Sets them equal to current value if 1 key not pressed again
        Blue_1 = cv2.getTrackbarPos('Blue_1', 'Color_1')
        Green_1 = cv2.getTrackbarPos('Green_1', 'Color_1')
        Red_1 = cv2.getTrackbarPos('Red_1', 'Color_1')
             
        Blue_2 = cv2.getTrackbarPos('Blue_2', 'Color_2')
        Green_2 = cv2.getTrackbarPos('Green_2', 'Color_2')
        Red_2 = cv2.getTrackbarPos('Red_2', 'Color_2')
             
        Blue_3 = cv2.getTrackbarPos('Blue_3', 'Color_3')
        Green_3 = cv2.getTrackbarPos('Green_3', 'Color_3')
        Red_3 = cv2.getTrackbarPos('Red_3', 'Color_3')
         
        Blue_4 = cv2.getTrackbarPos('Blue_4', 'Color_4')
        Green_4 = cv2.getTrackbarPos('Green_4', 'Color_4')
        Red_4 = cv2.getTrackbarPos('Red_4', 'Color_4')
             
        Blue_5 = cv2.getTrackbarPos('Blue_5', 'Color_5')
        Green_5 = cv2.getTrackbarPos('Green_5', 'Color_5')
        Red_5 = cv2.getTrackbarPos('Red_5', 'Color_5')
                 
        Blue_6 = cv2.getTrackbarPos('Blue_6', 'Color_6')
        Green_6 = cv2.getTrackbarPos('Green_6', 'Color_6')
        Red_6 = cv2.getTrackbarPos('Red_6', 'Color_6')
             
        Blue_7 = cv2.getTrackbarPos('Blue_7', 'Color_7')
        Green_7 = cv2.getTrackbarPos('Green_7', 'Color_7')
        Red_7 = cv2.getTrackbarPos('Red_7', 'Color_7')
                 
        Blue_8 = cv2.getTrackbarPos('Blue_8', 'Color_8')
        Green_8 = cv2.getTrackbarPos('Green_8', 'Color_8')
        Red_8 = cv2.getTrackbarPos('Red_8', 'Color_8')
    
    #Gives new randomized color to the papers
    Color_1_paper[0:image_height,0:image_width, 0:image_channels] = [Blue_1,Green_1,Red_1]
    Color_2_paper[0:image_height,0:image_width, 0:image_channels] = [Blue_2,Green_2,Red_2]
    Color_3_paper[0:image_height,0:image_width, 0:image_channels] = [Blue_3,Green_3,Red_3]
    Color_4_paper[0:image_height,0:image_width, 0:image_channels] = [Blue_4,Green_4,Red_4]
    Color_5_paper[0:image_height,0:image_width, 0:image_channels] = [Blue_5,Green_5,Red_5]
    Color_6_paper[0:image_height,0:image_width, 0:image_channels] = [Blue_6,Green_6,Red_6]
    Color_7_paper[0:image_height,0:image_width, 0:image_channels] = [Blue_7,Green_7,Red_7]
    Color_8_paper[0:image_height,0:image_width, 0:image_channels] = [Blue_8,Green_8,Red_8]



    #Sets limit on trackbar for each grayscale break
    grayscale_break = newTrackbarPos('Red', 'Sliders', 1, 31)
    grayscale_break2 = newTrackbarPos('Yellow', 'Sliders', 32, 63)
    grayscale_break3 = newTrackbarPos('Green', 'Sliders', 64, 95)
    grayscale_break4 = newTrackbarPos('Blue', 'Sliders' , 96, 127)
    grayscale_break5 = newTrackbarPos('Orange', 'Sliders', 128, 159)
    grayscale_break6 = newTrackbarPos('Purple', 'Sliders', 160, 191)
    grayscale_break7 = newTrackbarPos('Cyan', 'Sliders', 192, 224)
    
   
    #Creates min and max grayscale value for each color, making sure not to overlap
    min_grayscale_for_red = [0,0,0]
    max_grayscale_for_red = [grayscale_break,grayscale_break,grayscale_break]
    min_grayscale_for_yellow = [grayscale_break+1,grayscale_break+1, grayscale_break+1]
    max_grayscale_for_yellow = [grayscale_break2, grayscale_break2, grayscale_break2]
    
    min_grayscale_for_green = [grayscale_break2+1, grayscale_break2+1, grayscale_break2+1]
    max_grayscale_for_green = [grayscale_break3, grayscale_break3, grayscale_break3]
    min_grayscale_for_blue = [grayscale_break3+1, grayscale_break3+1, grayscale_break3+1]
    max_grayscale_for_blue = [grayscale_break4, grayscale_break4, grayscale_break4]
    
    min_grayscale_for_orange = [grayscale_break4+1, grayscale_break4+1, grayscale_break4+1]
    max_grayscale_for_orange = [grayscale_break5, grayscale_break5, grayscale_break5]
    min_grayscale_for_purple = [grayscale_break5+1, grayscale_break5+1, grayscale_break5+1]
    max_grayscale_for_purple = [grayscale_break6, grayscale_break6, grayscale_break6]
    
    min_grayscale_for_cyan = [grayscale_break6+1, grayscale_break6+1, grayscale_break6+1]
    max_grayscale_for_cyan = [grayscale_break7 , grayscale_break7, grayscale_break7]
    min_grayscale_for_magenta = [grayscale_break7+1, grayscale_break7+1, grayscale_break7+1]
    max_grayscale_for_magenta = [255, 255, 255]
    
    
    
    min_grayscale_for_red = numpy.array(min_grayscale_for_red, dtype = "uint8")
    max_grayscale_for_red = numpy.array(max_grayscale_for_red, dtype = "uint8")
    min_grayscale_for_yellow = numpy.array(min_grayscale_for_yellow, dtype = "uint8")
    max_grayscale_for_yellow = numpy.array(max_grayscale_for_yellow, dtype = "uint8")
    
    min_grayscale_for_green = numpy.array(min_grayscale_for_green, dtype = "uint8")
    max_grayscale_for_green = numpy.array(max_grayscale_for_green, dtype = "uint8")
    min_grayscale_for_blue = numpy.array(min_grayscale_for_blue, dtype = "uint8")
    max_grayscale_for_blue = numpy.array(max_grayscale_for_blue, dtype = "uint8")
    
    min_grayscale_for_orange = numpy.array(min_grayscale_for_green, dtype = "uint8")
    max_grayscale_for_orange= numpy.array(max_grayscale_for_green, dtype = "uint8")
    min_grayscale_for_purple = numpy.array(min_grayscale_for_blue, dtype = "uint8")
    max_grayscale_for_purple = numpy.array(max_grayscale_for_blue, dtype = "uint8")
    
    min_grayscale_for_cyan = numpy.array(min_grayscale_for_cyan, dtype = "uint8")
    max_grayscale_for_cyan = numpy.array(max_grayscale_for_cyan, dtype = "uint8")
    min_grayscale_for_magenta = numpy.array(min_grayscale_for_magenta, dtype = "uint8")
    max_grayscale_for_magenta = numpy.array(max_grayscale_for_magenta, dtype = "uint8")
    
    
    
    
    #cuts out pixels that are not in the range of grayscale values previously defined
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
    
    block_all_but_the_orange_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_orange,
                                              max_grayscale_for_orange)
    block_all_but_the_purple_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_purple,
                                              max_grayscale_for_purple)
    
    block_all_but_the_cyan_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_cyan,
                                              max_grayscale_for_cyan)
    block_all_but_the_magenta_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_magenta,
                                              max_grayscale_for_magenta)
    
    
    
    #Cuts out parts of each color, and blocks out the other parts of the image.
    red_parts_of_image = cv2.bitwise_or(Color_1_paper, Color_1_paper, mask = block_all_but_the_red_parts)
    yellow_parts_of_image = cv2.bitwise_or(Color_2_paper, Color_2_paper, mask = block_all_but_the_yellow_parts)
    green_parts_of_image = cv2.bitwise_or(Color_3_paper, Color_3_paper, mask = block_all_but_the_green_parts)
    blue_parts_of_image = cv2.bitwise_or(Color_4_paper, Color_4_paper, mask = block_all_but_the_blue_parts)
    orange_parts_of_image = cv2.bitwise_or(Color_5_paper, Color_5_paper, mask = block_all_but_the_orange_parts)
    purple_parts_of_image = cv2.bitwise_or(Color_6_paper, Color_6_paper, mask = block_all_but_the_purple_parts)
    cyan_parts_of_image = cv2.bitwise_or(Color_7_paper, Color_7_paper, mask = block_all_but_the_cyan_parts)
    magenta_parts_of_image = cv2.bitwise_or(Color_8_paper, Color_8_paper, mask = block_all_but_the_magenta_parts)    
    
    #creates customized images by combining previous color parts 
    red_yellow_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)
    blue_green_image = cv2.bitwise_or(green_parts_of_image, blue_parts_of_image)
    orange_purple_image = cv2.bitwise_or(orange_parts_of_image, purple_parts_of_image)
    cyan_magenta_image = cv2.bitwise_or(cyan_parts_of_image, magenta_parts_of_image)
    customized1_image = cv2.bitwise_or(red_yellow_image,blue_green_image)
    customized2_image = cv2.bitwise_or(cyan_magenta_image, orange_purple_image)
    customized_image = cv2.bitwise_or(customized1_image, customized2_image)
    
    #Shows image windows named original, grayscale, and customized.
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Grayscale Image',grayscale_image)
   #cv2.imshow('Red Parts of Image',red_parts_of_image)
    #cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
    #cv2.imshow('Red/Yellow Image',red_yellow_image)
    #cv2.imshow('Green Parts of Image',green_parts_of_image)
    #cv2.imshow('Blue Parts of Image', blue_parts_of_image)
    #cv2.imshow('Blue/Green Image',blue_green_image)
    #cv2.imshow('Orange Parts of Image',orange_parts_of_image)
    #cv2.imshow('Purple Parts of Image',purple_parts_of_image)
    #cv2.imshow('Orange/Purple Image',orange_purple_image)
    #cv2.imshow('Cyan Parts of Image', cyan_parts_of_image)
    #cv2.imshow('Magenta Parts of Image', magenta_parts_of_image)
    #cv2.imshow('Cyan/Magenta Image', cyan_magenta_image)
    cv2.imshow('Customized Image', customized_image)
 
#If esc key pressed: destroy all windows. If 's' key pressed: save image as 'Customized Image'
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('Customized Image', customized_image)
    cv2.destroyAllWindows()
