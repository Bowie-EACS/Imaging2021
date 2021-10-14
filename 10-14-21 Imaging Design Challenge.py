# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:06:10 2021

@author: Garrett Metting
"""


# Images_01_Starting_Code
# Engineer Your World
#Imports Stuff Required
import cv2
import numpy
import os.path
import random


def trackPosition(slider_name, window_name, min_val, max_val):
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print("Hey, that's too low")
        cv2.setTrackbarPos(slider_name, window_name, min_val)
        return min_val
    else: 
        return current_pos
    if current_pos > max_val:
        print("Hey, that's too high")
        cv2.setTrackbarPos(slider_name, window_name, max_val)
        return max_val
    else: 
        return current_pos

#This is to create aa random color value
def rando():
    val = random.randint(0, 255)
    return val


    

# Tells what the person is supposed to do while still in the program
print ("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    #If the Image is correct
    if os.path.isfile(filename) == True:
        filename_valid = True
    #In case the person does something wrong
    else:
        print ("Something was wrong with that filename. Please try again.")
''''Takes the file from the folder with the program and uses that image 
                                    for the windows'''
                                    
                                    
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)



"""Adds windows and colors"""
cv2.namedWindow('Original Image') #Original Image Displayed
cv2.namedWindow('Grayscale Image') #Grayscale Image
cv2.namedWindow('Customized Image') #Image inputed
cv2.namedWindow('Sliders') #This is for the sliders
cv2.resizeWindow('Sliders', 960, 540)


#Size of the original image
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]


#This creates the size of the windows for the images that are all seperate
paper_1 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

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

#This makes random color integers

paper_1[0:image_height,0:image_width, 0:image_channels] = [rando(),rando(),rando()]
paper_2[0:image_height,0:image_width, 0:image_channels] = [rando(),rando(),rando()]
paper_3[0:image_height, 0:image_width, 0:image_channels] = [rando(), rando(), rando()]
paper_4[0:image_height, 0:image_width, 0:image_channels] = [rando(), rando(), rando()]
paper_5[0:image_height, 0:image_width, 0:image_channels] = [rando(), rando(), rando()]
paper_6[0:image_height, 0:image_width, 0:image_channels] = [rando(), rando(), rando()]
paper_7[0:image_height, 0:image_width, 0:image_channels] = [rando(), rando(), rando()]
paper_8[0:image_height, 0:image_width, 0:image_channels] = [rando(), rando(), rando()]
paper_9[0:image_height, 0:image_width, 0:image_channels] = [rando(), rando(), rando()]
paper_10[0:image_height, 0:image_width, 0:image_channels] = [rando(), rando(), rando()]

#This creates a trackbar for the movable slider


cv2.createTrackbar('Grayscale Break For 1/2', 'Sliders', 0, 25, lambda x:None)
cv2.createTrackbar('Grayscale Break For 2/3', 'Sliders', 26, 50, lambda x:None)
cv2.createTrackbar('Grayscale Break For 3/4', 'Sliders', 51, 75, lambda x:None)
cv2.createTrackbar('Grayscale Break For 4/5', 'Sliders', 76, 100, lambda x:None)
cv2.createTrackbar('Grayscale Break For 5/6', 'Sliders', 101, 125, lambda x:None)
cv2.createTrackbar('Grayscale Break For 6/7', 'Sliders', 126, 150, lambda x:None)
cv2.createTrackbar('Grayscale Break For 7/8', 'Sliders', 151, 175, lambda x:None)
cv2.createTrackbar('Grayscale Break For 8/9', 'Sliders', 176, 200, lambda x:None)
cv2.createTrackbar('Grayscale Break For 9/10', 'Sliders', 201, 255, lambda x:None)



#This shows the grayscale and original image. Put here to shave off load time
cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)

#This Shows the minimun and maximum Grayscale for red and yellow for now
""" SLIDERS NEED TO BE HELD DOWN WHILE MOVING THE SLIDER"""
keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
    grayscale_break = trackPosition('Grayscale Break For 1/2', 'Sliders', 0, 25)
    grayscale_break_2 = trackPosition('Grayscale Break For 2/3', 'Sliders', 26, 50)
    grayscale_break_3 = trackPosition('Grayscale Break For 3/4', 'Sliders', 51, 75)
    grayscale_break_4 = trackPosition('Grayscale Break For 4/5', 'Sliders', 76, 100)
    grayscale_break_5 = trackPosition('Grayscale Break For 5/6', 'Sliders', 101, 125)
    grayscale_break_6 = trackPosition('Grayscale Break For 6/7', 'Sliders', 126, 150)
    grayscale_break_7 = trackPosition('Grayscale Break For 7/8', 'Sliders', 151, 175)
    grayscale_break_8 = trackPosition('Grayscale Break For 8/9', 'Sliders', 176, 200)
    grayscale_break_9 = trackPosition('Grayscale Break For 9/10', 'Sliders', 201, 255)
    

    
    min_grayscale_for_color_1 = [0,0,0]
    max_grayscale_for_color_1 = [grayscale_break,grayscale_break,grayscale_break]

    
    min_grayscale_for_color_2 = [grayscale_break + 1,grayscale_break + 1, 
                                grayscale_break + 1]
    max_grayscale_for_color_2 = [grayscale_break_2, grayscale_break_2, grayscale_break_2]
    
    
    min_grayscale_for_color_3 = [grayscale_break_2 + 1,grayscale_break_2 + 1, 
                                grayscale_break_2 + 1]
    max_grayscale_for_color_3 = [grayscale_break_3, grayscale_break_3, grayscale_break_3]
    
    
    min_grayscale_for_color_4 = [grayscale_break_3 + 1,grayscale_break_3 + 1, 
                                grayscale_break_3 + 1]
    max_grayscale_for_color_4 = [grayscale_break_4, grayscale_break_4, grayscale_break_4]
    
    
    min_grayscale_for_color_5 = [grayscale_break_4 + 1,grayscale_break_4 + 1, 
                                grayscale_break_4 + 1]
    max_grayscale_for_color_5 = [grayscale_break_5, grayscale_break_5, grayscale_break_5]
    
    
    min_grayscale_for_color_6 = [grayscale_break_5 + 1,grayscale_break_5 + 1, 
                                grayscale_break_5 + 1]
    max_grayscale_for_color_6 = [grayscale_break_6, grayscale_break_6, grayscale_break_6]
    
    
    min_grayscale_for_color_7 = [grayscale_break_6 + 1,grayscale_break_6 + 1, 
                                grayscale_break_6 + 1]
    max_grayscale_for_color_7 = [grayscale_break_7, grayscale_break_7, grayscale_break_7]
    
    
    min_grayscale_for_color_8 = [grayscale_break_7 + 1,grayscale_break_7 + 1, 
                                grayscale_break_7 + 1]
    max_grayscale_for_color_8 = [grayscale_break_8, grayscale_break_8, grayscale_break_8]
    
    
    min_grayscale_for_color_9 = [grayscale_break_8 + 1,grayscale_break_8 + 1, 
                                grayscale_break_8 + 1]
    max_grayscale_for_color_9 = [grayscale_break_9, grayscale_break_9, grayscale_break_9]
    
    
    min_grayscale_for_color_10 = [grayscale_break_9 + 1,grayscale_break_9 + 1, 
                                grayscale_break_9 + 1]
    max_grayscale_for_color_10 = [255, 255, 255]
    


    ''' This shows is the cut of point of the gryscale between red 
    and yellow for now'''
    min_grayscale_for_color_1 = numpy.array(min_grayscale_for_color_1, dtype = "uint8")
    max_grayscale_for_color_1 = numpy.array(max_grayscale_for_color_1, dtype = "uint8")
    
    
    min_grayscale_for_color_2 = numpy.array(min_grayscale_for_color_2, dtype = "uint8")
    max_grayscale_for_color_2 = numpy.array(max_grayscale_for_color_2, dtype = "uint8")
    
    
    min_grayscale_for_color_3 = numpy.array(min_grayscale_for_color_3,dtype = "uint8")
    max_grayscale_for_color_3 = numpy.array(max_grayscale_for_color_3,dtype = "uint8")
    
    
    min_grayscale_for_color_4 = numpy.array(min_grayscale_for_color_4,dtype = "uint8")
    max_grayscale_for_color_4 = numpy.array(max_grayscale_for_color_4,dtype = "uint8")
    
    
    min_grayscale_for_color_5 = numpy.array(min_grayscale_for_color_5,dtype = "uint8")
    max_grayscale_for_color_5 = numpy.array(max_grayscale_for_color_5,dtype = "uint8")
    
    
    min_grayscale_for_color_6 = numpy.array(min_grayscale_for_color_6,dtype = "uint8")
    max_grayscale_for_color_6 = numpy.array(max_grayscale_for_color_6,dtype = "uint8")
    
    
    min_grayscale_for_color_7 = numpy.array(min_grayscale_for_color_7,dtype = "uint8")
    max_grayscale_for_color_7 = numpy.array(max_grayscale_for_color_7,dtype = "uint8")
    
    
    min_grayscale_for_color_8 = numpy.array(min_grayscale_for_color_8,dtype = "uint8")
    max_grayscale_for_color_8 = numpy.array(max_grayscale_for_color_8,dtype = "uint8")
    
    
    min_grayscale_for_color_9 = numpy.array(min_grayscale_for_color_9,dtype = "uint8")
    max_grayscale_for_color_9 = numpy.array(max_grayscale_for_color_9,dtype = "uint8")
    
    
    min_grayscale_for_color_10 = numpy.array(min_grayscale_for_color_10,dtype = "uint8")
    max_grayscale_for_color_10 = numpy.array(max_grayscale_for_color_10,dtype = "uint8")
    
    #Min and max grayscales for the colors

    
    
    block_all_but_color_1 = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color_1,
                                              max_grayscale_for_color_1)
    
    
    block_all_but_color_2 = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color_2,
                                                 max_grayscale_for_color_2)
    
    
    block_all_but_color_3 = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_3,
                                              max_grayscale_for_color_3)
    
    
    block_all_but_color_4 = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_4,
                                              max_grayscale_for_color_4)
    
    
    block_all_but_color_5 = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_5,
                                              max_grayscale_for_color_5)
    
    
    block_all_but_color_6 = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_6,
                                              max_grayscale_for_color_6)
    
    
    block_all_but_color_7 = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_7,
                                              max_grayscale_for_color_7)
    
    
    block_all_but_color_8 = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_8,
                                              max_grayscale_for_color_8)
    
    
    block_all_but_color_9 = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_9,
                                              max_grayscale_for_color_9)
    
    
    block_all_but_color_10 = cv2.inRange(grayscale_image, 
                                         min_grayscale_for_color_10, 
                                         max_grayscale_for_color_10)
    #Blocks all the colors for windows
    
    
    color_1_parts_of_image = cv2.bitwise_or(paper_1, paper_1,
                                        mask = block_all_but_color_1)
   
    
    color_2_parts_of_image = cv2.bitwise_or(paper_2, paper_2,
                                           mask = block_all_but_color_2)
    
    
    color_3_parts_of_image = cv2.bitwise_or(paper_3, paper_3,
                                           mask = block_all_but_color_3)
    
    
    color_4_parts_of_image = cv2.bitwise_or(paper_4, paper_4,
                                           mask = block_all_but_color_4)
    
    
    color_5_parts_of_image = cv2.bitwise_or(paper_5, paper_5,
                                           mask = block_all_but_color_5)
    
    
    color_6_parts_of_image = cv2.bitwise_or(paper_6, paper_6,
                                           mask = block_all_but_color_6)
    
    
    color_7_parts_of_image = cv2.bitwise_or(paper_7, paper_7,
                                           mask = block_all_but_color_7)
    
    
    color_8_parts_of_image = cv2.bitwise_or(paper_8, paper_8,
                                           mask = block_all_but_color_8)
    
    
    color_9_parts_of_image = cv2.bitwise_or(paper_9, paper_9,
                                           mask = block_all_but_color_9)
    
    
    color_10_parts_of_image = cv2.bitwise_or(paper_10, paper_10,
                                           mask = block_all_but_color_10)
    
    
    
    #ascii table
    
    # This Is To Display The Images On The Window
    # If statements to display windows one at a time
    #This Part of the program is what displays the images
        
    customized_image = cv2.bitwise_or(color_2_parts_of_image, color_3_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_1_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_4_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_5_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_6_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_7_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_8_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_9_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_10_parts_of_image)

    
    if keypressed == 49:
        #create window
        #destroys windows when other window key is pressed
        cv2.imshow('Color 1',color_1_parts_of_image) # keypressed = Wait Key 
        if keypressed != 49:
            cv2.destroyWindow(cv2.imshow('Color 1',color_1_parts_of_image))
        
        
    elif keypressed == 50:
        cv2.imshow('Color 2',color_2_parts_of_image)
        if keypressed != 50:
            cv2.destroyWindow(cv2.imshow('Color 2',color_2_parts_of_image))
        
        
    elif keypressed == 51:
        cv2.imshow('Color 3', color_3_parts_of_image)
        if keypressed != 51:
            cv2.destroyWindow(cv2.imshow('Color 3', color_3_parts_of_image))
        
        
    elif keypressed == 52:
        cv2.imshow('Color 4', color_4_parts_of_image)
        if keypressed != 52:
            cv2.destroyWindow(cv2.imshow('Color 4', color_4_parts_of_image))
        
        
    elif keypressed == 53:
        cv2.imshow('Color 5', color_5_parts_of_image)
        if keypressed != 53:
            cv2.destroyWindow(cv2.imshow('Color 5', color_5_parts_of_image))
        
        
    elif keypressed == 54:
        cv2.imshow('Color 6', color_6_parts_of_image)
        if keypressed != 54: 
            cv2.destroyWindow(cv2.imshow('Color 6', color_6_parts_of_image))
        
        
    elif keypressed == 55:
        cv2.imshow('Color 7', color_7_parts_of_image)
        if keypressed != 55:
            cv2.destroyWindow(cv2.imshow('Color 7', color_7_parts_of_image))
        
        
    elif keypressed == 56:
        cv2.imshow('Color 8', color_8_parts_of_image)
        if keypressed != 56:
            cv2.destroyWindow(cv2.imshow('Color 8', color_8_parts_of_image))
        
        
    elif keypressed == 57:
        cv2.imshow('Color 9', color_9_parts_of_image)
        if keypressed != 57:
            cv2.destroyWindow(cv2.imshow('Color 9', color_9_parts_of_image))
        
        
    elif keypressed == 48:
        cv2.imshow('Color 10', color_10_parts_of_image)
        if keypressed != 48:
            cv2.destroyWindow(cv2.imshow('Color 10', color_10_parts_of_image))
            

        
  
    else:
        cv2.imshow('Customized Image',customized_image)
    keypressed = cv2.waitKey(1)





# Creates A List
listy = [color_1_parts_of_image, color_2_parts_of_image, color_3_parts_of_image, 
         color_4_parts_of_image, color_5_parts_of_image, color_6_parts_of_image, 
         color_7_parts_of_image, color_8_parts_of_image, color_9_parts_of_image, 
         color_10_parts_of_image]




  #This closes the program if the escape key is pressed      
   
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    save = input("What would you like to name the file? (Make Sure It is a .jpg file) ")
    print(save)
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()
#End everything









