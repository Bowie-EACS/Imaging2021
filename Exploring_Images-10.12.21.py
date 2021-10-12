# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:00:21 2021

@author: s10141622


Sebastian Baker 
Period 5



"""

import cv2
import numpy
import os.path
import random

def newTrackbarPos(trackbar_name, trackbar_window, min_val):
    currentpos = cv2.getTrackbarPos(trackbar_name, trackbar_window)
    if currentpos < min_val:
        cv2.setTrackbarPos(trackbar_name, trackbar_window, min_val)
        return min_val
    else:
        return currentpos
    

print ("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False: #Loop to find correct filename
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")


#This grabs the image and changes it to gray
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)



#This Makes the windows
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
#cv2.namedWindow('Red Parts of Image')
#cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow('Customized Image')

cv2.namedWindow('Color_1')
cv2.namedWindow('Color_2')
cv2.namedWindow('Color_3')
cv2.namedWindow('Color_4')
cv2.namedWindow('Color_5')
cv2.namedWindow('Color_6')
cv2.namedWindow('Color_7')
cv2.namedWindow('Color_8')
cv2.namedWindow('Color_9')
cv2.namedWindow('Color_10')




#This sets the image size
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]



#This gives image parameters for the various windows equal to the 
#origional image


paper_1 = numpy.zeros((image_height,image_width,image_channels), 
                          numpy.uint8)
paper_2 = numpy.zeros((image_height,image_width,image_channels),
                          numpy.uint8)
paper_3 = numpy.zeros((image_height,image_width,image_channels),
                          numpy.uint8)
paper_4 = numpy.zeros((image_height,image_width,image_channels),
                          numpy.uint8)
paper_5 = numpy.zeros((image_height,image_width,image_channels),
                          numpy.uint8)
paper_6 = numpy.zeros((image_height,image_width,image_channels),
                          numpy.uint8)
paper_7 = numpy.zeros((image_height,image_width,image_channels),
                          numpy.uint8)
paper_8 = numpy.zeros((image_height,image_width,image_channels),
                          numpy.uint8)
paper_9 = numpy.zeros((image_height,image_width,image_channels),
                          numpy.uint8)
paper_10 = numpy.zeros((image_height,image_width,image_channels),
                          numpy.uint8)



#creates trackbars and sets their initial positions
cv2.createTrackbar('Grayscale-1', 'Color_1', 14, 254, lambda x:None)
cv2.createTrackbar('Grayscale-2', 'Color_2', 28, 254, lambda x:None) 
cv2.createTrackbar('Grayscale-3', 'Color_3', 56, 254, lambda x:None)
cv2.createTrackbar('Grayscale-4', 'Color_4', 84, 254, lambda x:None) 
cv2.createTrackbar('Grayscale-5', 'Color_5', 100, 254, lambda x:None)
cv2.createTrackbar('Grayscale-6', 'Color_6', 128, 254, lambda x:None) 
cv2.createTrackbar('Grayscale-7', 'Color_7', 154, 254, lambda x:None)
cv2.createTrackbar('Grayscale-8', 'Color_8', 176, 254, lambda x:None) 
cv2.createTrackbar('Grayscale-9', 'Color_9', 200, 254, lambda x:None)

#creates colors for the sliders
cv2.createTrackbar('Blue_1', 'Color_1', 0, 254, lambda x:None)
cv2.createTrackbar('Green_1', 'Color_1', 0, 254, lambda x:None)
cv2.createTrackbar('Red_1', 'Color_1', 0, 254, lambda x:None)

cv2.createTrackbar('Blue_2', 'Color_2', 10, 254, lambda x:None)
cv2.createTrackbar('Green_2', 'Color_2', 10, 254, lambda x:None)
cv2.createTrackbar('Red_2', 'Color_2', 10, 254, lambda x:None)

cv2.createTrackbar('Blue_3', 'Color_3', 17, 254, lambda x:None)
cv2.createTrackbar('Green_3', 'Color_3', 17, 254, lambda x:None)
cv2.createTrackbar('Red_3', 'Color_3', 17, 254, lambda x:None)

cv2.createTrackbar('Blue_4', 'Color_4', 25, 254, lambda x:None)
cv2.createTrackbar('Green_4', 'Color_4', 25, 254, lambda x:None)
cv2.createTrackbar('Red_4', 'Color_4', 25, 254, lambda x:None)

cv2.createTrackbar('Blue_5', 'Color_5', 50, 254, lambda x:None)
cv2.createTrackbar('Green_5', 'Color_5', 50, 254, lambda x:None)
cv2.createTrackbar('Red_5', 'Color_5', 50, 254, lambda x:None)

cv2.createTrackbar('Blue_6', 'Color_6', 75, 254, lambda x:None)
cv2.createTrackbar('Green_6', 'Color_6', 75, 254, lambda x:None)
cv2.createTrackbar('Red_6', 'Color_6', 75, 254, lambda x:None)

cv2.createTrackbar('Blue_7', 'Color_7', 100, 254, lambda x:None)
cv2.createTrackbar('Green_7', 'Color_7', 100, 254, lambda x:None)
cv2.createTrackbar('Red_7', 'Color_7', 100, 254, lambda x:None)

cv2.createTrackbar('Blue_8', 'Color_8', 150, 254, lambda x:None)
cv2.createTrackbar('Green_8', 'Color_8', 150, 254, lambda x:None)
cv2.createTrackbar('Red_8', 'Color_8', 150, 254, lambda x:None)

cv2.createTrackbar('Blue_9', 'Color_9', 200, 254, lambda x:None)
cv2.createTrackbar('Green_9', 'Color_9', 200, 254, lambda x:None)
cv2.createTrackbar('Red_9', 'Color_9', 200, 254, lambda x:None)

cv2.createTrackbar('Blue_10', 'Color_10', 250, 254, lambda x:None)
cv2.createTrackbar('Green_10', 'Color_10', 250, 254, lambda x:None)
cv2.createTrackbar('Red_10', 'Color_10', 250, 254, lambda x:None)

   



keypressed = 1
print("Press the esc or s key to finalize your value, press 1, 2, or 3 to show/refresh different windows")
print("Press 1 to get random colors! ")
while (keypressed != 27 and keypressed != ord('s')):     
    
    #This is the random function
    if keypressed == 49:
        Blue_1 = random.randrange(0, 255) 
        cv2.setTrackbarPos('Blue_1', 'Color_1', Blue_1)
        Green_1 = random.randrange(0, 255)
        cv2.setTrackbarPos('Green_1', 'Color_1', Green_1)
        Red_1 = random.randrange(0, 255)
        cv2.setTrackbarPos('Red_1', 'Color_1', Red_1)
        
        Blue_2 = random.randrange(0, 255)
        cv2.setTrackbarPos('Blue_2', 'Color_2', Blue_2)
        Green_2 = random.randrange(0, 255)
        cv2.setTrackbarPos('Green_2', 'Color_2', Green_2)
        Red_2 = random.randrange(0, 255)
        cv2.setTrackbarPos('Red_2', 'Color_2', Red_2)
        
        Blue_3 = random.randrange(0, 255)
        cv2.setTrackbarPos('Blue_3', 'Color_3', Blue_3)
        Green_3 = random.randrange(0, 255)
        cv2.setTrackbarPos('Green_3', 'Color_3', Green_3)
        Red_3 = random.randrange(0, 255)
        cv2.setTrackbarPos('Red_3', 'Color_3', Red_3)
        
        Blue_4 = random.randrange(0, 255)
        cv2.setTrackbarPos('Blue_4', 'Color_4', Blue_4)
        Green_4 = random.randrange(0, 255)
        cv2.setTrackbarPos('Green_4', 'Color_4', Green_4)
        Red_4 = random.randrange(0, 255)
        cv2.setTrackbarPos('Red_4', 'Color_4', Red_4)
        
        Blue_5 = random.randrange(0, 255)
        cv2.setTrackbarPos('Blue_5', 'Color_5', Blue_5)
        Green_5 = random.randrange(0, 255)
        cv2.setTrackbarPos('Green_5', 'Color_5', Green_5)
        Red_5 = random.randrange(0, 255)
        cv2.setTrackbarPos('Red_5', 'Color_5', Red_5)
        
        Blue_6 = random.randrange(0, 255)
        cv2.setTrackbarPos('Blue_6', 'Color_6', Blue_6)
        Green_6 = random.randrange(0, 255)
        cv2.setTrackbarPos('Green_6', 'Color_6', Green_6)
        Red_6 = random.randrange(0, 255)
        cv2.setTrackbarPos('Red_6', 'Color_6', Red_6)
        
        Blue_7 = random.randrange(0, 255)
        cv2.setTrackbarPos('Blue_7', 'Color_7', Blue_7)
        Green_7 = random.randrange(0, 255)
        cv2.setTrackbarPos('Green_7', 'Color_7', Green_7)
        Red_7 = random.randrange(0, 255)
        cv2.setTrackbarPos('Red_7', 'Color_7', Red_7)
        
        Blue_8 = random.randrange(0, 255)
        cv2.setTrackbarPos('Blue_8', 'Color_8', Blue_8)
        Green_8 = random.randrange(0, 255)
        cv2.setTrackbarPos('Green_8', 'Color_8', Green_8)
        Red_8 = random.randrange(0, 255)
        cv2.setTrackbarPos('Red_8', 'Color_8', Red_8)
        
        Blue_9 = random.randrange(0, 255)
        cv2.setTrackbarPos('Blue_9', 'Color_9', Blue_9)
        Green_9 = random.randrange(0, 255)
        cv2.setTrackbarPos('Green_9', 'Color_9', Green_9)
        Red_9 = random.randrange(0, 255)
        cv2.setTrackbarPos('Red_9', 'Color_9', Red_9)
        
        Blue_10 = random.randrange(0, 255)
        cv2.setTrackbarPos('Blue_10', 'Color_10', Blue_10)
        Green_10 = random.randrange(0, 255)
        cv2.setTrackbarPos('Green_10', 'Color_10', Green_10)
        Red_10 = random.randrange(0, 255)
        cv2.setTrackbarPos('Red_10', 'Color_10', Red_10)    
        
    else:
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
            
        Blue_9 = cv2.getTrackbarPos('Blue_9', 'Color_9')
        Green_9 = cv2.getTrackbarPos('Green_9', 'Color_9') 
        Red_9 = cv2.getTrackbarPos('Red_9', 'Color_9')
            
        Blue_10 = cv2.getTrackbarPos('Blue_10', 'Color_10') 
        Green_10 = cv2.getTrackbarPos('Green_10', 'Color_10') 
        Red_10 = cv2.getTrackbarPos('Red_10', 'Color_10')
            
    
    #this sets the colors to their own layer/paper
    paper_1[0:image_height,0:image_width, 0:image_channels] = [Blue_1, Green_1, Red_1]
    paper_2[0:image_height,0:image_width, 0:image_channels] = [Blue_2, Green_2, Red_2]
    paper_3[0:image_height,0:image_width, 0:image_channels] = [Blue_3, Green_3, Red_3]
    paper_4[0:image_height,0:image_width, 0:image_channels] = [Blue_4, Green_4, Red_4]
    paper_5[0:image_height,0:image_width, 0:image_channels] = [Blue_5, Green_5, Red_5]
    paper_6[0:image_height,0:image_width, 0:image_channels] = [Blue_6, Green_6, Red_6]
    paper_7[0:image_height,0:image_width, 0:image_channels] = [Blue_7, Green_7, Red_7]
    paper_8[0:image_height,0:image_width, 0:image_channels] = [Blue_8, Green_8, Red_8]
    paper_9[0:image_height,0:image_width, 0:image_channels] = [Blue_9, Green_9, Red_9]
    paper_10[0:image_height,0:image_width, 0:image_channels] = [Blue_10, Green_10, Red_10]
        
    
    
    #This links the sliders
    grayscale_break_1 = newTrackbarPos('Grayscale-1', 'Color_1', 0)
    grayscale_break_2 = newTrackbarPos('Grayscale-2', 'Color_2', grayscale_break_1+1)
    grayscale_break_3 = newTrackbarPos('Grayscale-3', 'Color_3', grayscale_break_2+1)
    grayscale_break_4 = newTrackbarPos('Grayscale-4', 'Color_4', grayscale_break_3+1)
    grayscale_break_5 = newTrackbarPos('Grayscale-5', 'Color_5', grayscale_break_4+1)
    grayscale_break_6 = newTrackbarPos('Grayscale-6', 'Color_6', grayscale_break_5+1)
    grayscale_break_7 = newTrackbarPos('Grayscale-7', 'Color_7', grayscale_break_6+1)
    grayscale_break_8 = newTrackbarPos('Grayscale-8', 'Color_8', grayscale_break_7+1)
    grayscale_break_9 = newTrackbarPos('Grayscale-9', 'Color_9', grayscale_break_8+1)
    
    
    
    #This sets the range of the first paper
    min_grayscale_for_paper_1 = [0,0,0]
    max_grayscale_for_paper_1 = [grayscale_break_1,grayscale_break_1,grayscale_break_1]
    
    #This sets it for paper 2, the +1 just means it is above paper 1 by 1
    min_grayscale_for_paper_2 = [grayscale_break_1+1,grayscale_break_1+1, grayscale_break_1+1]
    max_grayscale_for_paper_2 = [grayscale_break_2,grayscale_break_2, grayscale_break_2]
    
    min_grayscale_for_paper_3 = [grayscale_break_2+1,grayscale_break_2+1, grayscale_break_2+1]
    max_grayscale_for_paper_3 = [grayscale_break_3,grayscale_break_3, grayscale_break_3]
    
    min_grayscale_for_paper_4 = [grayscale_break_3+1,grayscale_break_3+1, grayscale_break_3+1]
    max_grayscale_for_paper_4 = [grayscale_break_4,grayscale_break_4, grayscale_break_4]
    
    min_grayscale_for_paper_5 = [grayscale_break_4+1,grayscale_break_4+1, grayscale_break_4+1]
    max_grayscale_for_paper_5 = [grayscale_break_5,grayscale_break_5, grayscale_break_5]    
    
    min_grayscale_for_paper_6 = [grayscale_break_5+1,grayscale_break_5+1, grayscale_break_5+1]
    max_grayscale_for_paper_6 = [grayscale_break_6,grayscale_break_6, grayscale_break_6]    
    
    min_grayscale_for_paper_7 = [grayscale_break_6+1,grayscale_break_6+1, grayscale_break_6+1]
    max_grayscale_for_paper_7 = [grayscale_break_7,grayscale_break_7, grayscale_break_7]

    min_grayscale_for_paper_8 = [grayscale_break_7+1,grayscale_break_7+1, grayscale_break_7+1]
    max_grayscale_for_paper_8 = [grayscale_break_8,grayscale_break_8, grayscale_break_8]

    min_grayscale_for_paper_9 = [grayscale_break_8+1,grayscale_break_8+1, grayscale_break_8+1]
    max_grayscale_for_paper_9 = [grayscale_break_9,grayscale_break_9, grayscale_break_9]

    min_grayscale_for_paper_10 = [grayscale_break_9+1,grayscale_break_9+1, grayscale_break_9+1]
    max_grayscale_for_paper_10 = [255,255,255]


    
    min_grayscale_for_paper_1 = numpy.array(min_grayscale_for_paper_1, dtype = "uint8")
    max_grayscale_for_paper_1 = numpy.array(max_grayscale_for_paper_1, dtype = "uint8")
   
    min_grayscale_for_paper_2 = numpy.array(min_grayscale_for_paper_2, dtype = "uint8")
    max_grayscale_for_paper_2 = numpy.array(max_grayscale_for_paper_2, dtype = "uint8")
    
    min_grayscale_for_paper_3 = numpy.array(min_grayscale_for_paper_3, dtype = "uint8")
    max_grayscale_for_paper_3 = numpy.array(max_grayscale_for_paper_3, dtype = "uint8")

    min_grayscale_for_paper_4 = numpy.array(min_grayscale_for_paper_4, dtype = "uint8")
    max_grayscale_for_paper_4 = numpy.array(max_grayscale_for_paper_4, dtype = "uint8")
    
    min_grayscale_for_paper_5 = numpy.array(min_grayscale_for_paper_5, dtype = "uint8")
    max_grayscale_for_paper_5 = numpy.array(max_grayscale_for_paper_5, dtype = "uint8")

    min_grayscale_for_paper_6 = numpy.array(min_grayscale_for_paper_6, dtype = "uint8")
    max_grayscale_for_paper_6 = numpy.array(max_grayscale_for_paper_6, dtype = "uint8")

    min_grayscale_for_paper_7 = numpy.array(min_grayscale_for_paper_7, dtype = "uint8")
    max_grayscale_for_paper_7 = numpy.array(max_grayscale_for_paper_7, dtype = "uint8")

    min_grayscale_for_paper_8 = numpy.array(min_grayscale_for_paper_8, dtype = "uint8")
    max_grayscale_for_paper_8 = numpy.array(max_grayscale_for_paper_8, dtype = "uint8")

    min_grayscale_for_paper_9 = numpy.array(min_grayscale_for_paper_9, dtype = "uint8")
    max_grayscale_for_paper_9 = numpy.array(max_grayscale_for_paper_9, dtype = "uint8")
    
    min_grayscale_for_paper_10 = numpy.array(min_grayscale_for_paper_10, dtype = "uint8")
    max_grayscale_for_paper_10 = numpy.array(max_grayscale_for_paper_10, dtype = "uint8")    
  
    
    #The in range cuts out all pixles in a range, just add more as you go
    block_all_but_the_paper_1_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_paper_1,
                                                  max_grayscale_for_paper_1)

    block_all_but_the_paper_2_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_paper_2,
                                                  max_grayscale_for_paper_2)
    
    block_all_but_the_paper_3_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_paper_3,
                                                  max_grayscale_for_paper_3)

    block_all_but_the_paper_4_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_paper_4,
                                                  max_grayscale_for_paper_4)
    
    block_all_but_the_paper_5_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_paper_5,
                                                  max_grayscale_for_paper_5)    
    
    block_all_but_the_paper_6_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_paper_6,
                                                  max_grayscale_for_paper_6)    
    
    block_all_but_the_paper_7_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_paper_7,
                                                  max_grayscale_for_paper_7)    
    
    block_all_but_the_paper_8_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_paper_8,
                                                  max_grayscale_for_paper_8)    
    
    block_all_but_the_paper_9_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_paper_9,
                                                  max_grayscale_for_paper_9)    
    
    block_all_but_the_paper_10_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_paper_10,
                                                  max_grayscale_for_paper_10)    
    
    
    
    #Combines the images together
    paper_1_parts_of_image = cv2.bitwise_or(paper_1, 
                                            paper_1,
                                            mask = block_all_but_the_paper_1_parts)
    
    paper_2_parts_of_image = cv2.bitwise_or(paper_2, 
                                            paper_2,
                                            mask = block_all_but_the_paper_2_parts)
    
    paper_3_parts_of_image = cv2.bitwise_or(paper_3, 
                                            paper_3,
                                            mask = block_all_but_the_paper_3_parts)
    
    paper_4_parts_of_image = cv2.bitwise_or(paper_4, 
                                            paper_4,
                                            mask = block_all_but_the_paper_4_parts)
    
    paper_5_parts_of_image = cv2.bitwise_or(paper_5, 
                                            paper_5,
                                            mask = block_all_but_the_paper_5_parts)    
    
    paper_6_parts_of_image = cv2.bitwise_or(paper_6, 
                                            paper_6,
                                            mask = block_all_but_the_paper_6_parts)    
    
    paper_7_parts_of_image = cv2.bitwise_or(paper_7, 
                                            paper_7,
                                            mask = block_all_but_the_paper_7_parts)    
    
    paper_8_parts_of_image = cv2.bitwise_or(paper_8, 
                                            paper_8,
                                            mask = block_all_but_the_paper_8_parts)    
    
    paper_9_parts_of_image = cv2.bitwise_or(paper_9, 
                                            paper_9,
                                            mask = block_all_but_the_paper_9_parts)    
    
    paper_10_parts_of_image = cv2.bitwise_or(paper_10, 
                                            paper_10,
                                            mask = block_all_but_the_paper_10_parts)    
    
    
    
    #This only adds 2 variables together
    customized_image_1 = cv2.bitwise_or(paper_1_parts_of_image, paper_2_parts_of_image)
    
    customized_image_2 = cv2.bitwise_or(customized_image_1, paper_3_parts_of_image)
    
    customized_image_3 = cv2.bitwise_or(customized_image_2, paper_4_parts_of_image)
    
    customized_image_4 = cv2.bitwise_or(customized_image_3, paper_5_parts_of_image)
    
    customized_image_5 = cv2.bitwise_or(customized_image_4, paper_6_parts_of_image)
    
    customized_image_6 = cv2.bitwise_or(customized_image_5, paper_7_parts_of_image)
    
    customized_image_7 = cv2.bitwise_or(customized_image_6, paper_8_parts_of_image)
    
    customized_image_8 = cv2.bitwise_or(customized_image_7, paper_9_parts_of_image)
    
    customized_image_9 = cv2.bitwise_or(customized_image_8, paper_10_parts_of_image)    
  
    
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Grayscale Image',grayscale_image)
    cv2.imshow('Customized Image',customized_image_9)
  
    '''   
    if keypressed == 49:
        cv2.imshow('Original Image', original_image)
        cv2.destroyWindow('Grayscale Image')
        cv2.destroyWindow('Customized Image')
    
    if keypressed == 50:
        cv2.imshow('Grayscale Image',grayscale_image)
        cv2.destroyWindow('Customized Image')
        cv2.destroyWindow('Original Image')

    if keypressed == 51:
        cv2.imshow('Customized Image',customized_image_9)
        cv2.destroyWindow('Grayscale Image')
        cv2.destroyWindow('Original Image')
    '''
    #cv2.imshow('Red Parts of Image',red_parts_of_image)
    #cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
    

    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image_9)
    cv2.destroyAllWindows()
