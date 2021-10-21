# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:05:51 2021

@author: S10025687

 """

# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path
import json

listy = [10,20,30,40,50]

with open ('listylist.json', 'w') as json_file:
    json.dump(listy, json_file)
    
with open('listylist.json') as f:
  data = json.load(f)

print (data[3])

print ("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ") #First thing the code askes when opend
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.") #Incorrect file name will result in the rentering of the correct file name

def trackposition(slider_name, window_name, min_val, max_val):
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print ("Too low")
        cv2.setTrackbarPos(slider_name, window_name, max_val)
        return min_val
    if current_pos > max_val:
        print("Too high")
        return max_val
    else:
        return current_pos

original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR) #Program loads geryscale photo as well as red, yellow, and cutom images

cv2.namedWindow('Original Image') #Program names the 5 diffrent images
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Red Parts of Image')
cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow('Blue Parts of Image')
cv2.namedWindow('Purple Parts of Image')
cv2.namedWindow('Green Parts of Image')
cv2.namedWindow('Cyan Parts of Image')
cv2.namedWindow('Pink Parts of Image')
#cv2.namedWindow('Orange Parts of Image')
#cv2.namedWindow('Lime Parts of Image')
#cv2.namedWindow('LB Parts of Image')  #LB = light blue
#cv2.namedWindow('Lavender Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')
cv2.resizeWindow('Sliders', 960, 540)


image_height = original_image.shape[0] #Program gather dimmentions for the images to be displayed correctly
image_width = original_image.shape[1]
image_channels = original_image.shape[2] 

red_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
yellow_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
blue_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
purple_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
green_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
cyan_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
pink_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
orange_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
lime_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
lb_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
lavender_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)


red_paper[0:image_height,0:image_width, 0:image_channels] = [0,0,255] #Program presets BRG values for the red, yellow, and custom image for the user
yellow_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
blue_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,0]
purple_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,255]
green_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,0]
cyan_paper[0:image_height,0:image_width, 0:image_channels] = [255,255,0]
pink_paper[0:image_height,0:image_width, 0:image_channels] = [203,192,255]
orange_paper[0:image_height,0:image_width, 0:image_channels] = [0,128,255]
lime_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,128]
lb_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
lavender_paper[0:image_height,0:image_width, 0:image_channels] = [255,51,153]


cv2.createTrackbar('Grayscale', 'Sliders', 25, 255, lambda x:None) #program generates slider for grayscale and colored images
cv2.createTrackbar('Grayscale2', 'Sliders', 35, 255, lambda x:None) #add min ands max
cv2.createTrackbar('Grayscale3', 'Sliders', 65, 255, lambda x:None)
cv2.createTrackbar('Grayscale4', 'Sliders', 95, 255, lambda x:None)
cv2.createTrackbar('Grayscale5', 'Sliders', 125, 255, lambda x:None)
cv2.createTrackbar('Grayscale6', 'Sliders',155 , 255, lambda x: None)
cv2.createTrackbar('Grayscale7', 'Sliders',195 , 255, lambda x: None)
cv2.createTrackbar('Grayscale8', 'Sliders',215 , 255, lambda x: None)
cv2.createTrackbar('Grayscale9', 'Sliders',225 , 255, lambda x: None)
cv2.createTrackbar('Grayscale10', 'Sliders',246 , 255, lambda x: None)


keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):

    grayscale_break = trackposition('Grayscale', 'Sliders',0, 34)#Program gets track bar to display to the user
    grayscale_break2 = trackposition('Grayscale2', 'Sliders',35, 64)
    grayscale_break3 = trackposition('Grayscale3', 'Sliders',65, 94)
    grayscale_break4 = trackposition('Grayscale4', 'Sliders',95, 124)
    grayscale_break5 = trackposition('Grayscale5', 'Sliders',125, 154)
    grayscale_break6 = trackposition('Grayscale6', 'Sliders',155, 194)
    grayscale_break7 = trackposition('Grayscale7', 'Sliders',195, 214)
    grayscale_break8 = trackposition('Grayscale8', 'Sliders',215, 224)
    grayscale_break9 = trackposition('Grayscale9', 'Sliders',225, 245)
    grayscale_break10 = trackposition('Grayscale10','Sliders',246, 255)

    
    min_grayscale_for_red = [0,0,0]
    max_grayscale_for_red = [grayscale_break,grayscale_break,grayscale_break]
    min_grayscale_for_yellow = [grayscale_break+1,grayscale_break+1, grayscale_break+1]
    max_grayscale_for_yellow = [grayscale_break2,grayscale_break2,grayscale_break2]
    min_grayscale_for_blue = [grayscale_break2+1,grayscale_break2+1,grayscale_break2+1]
    max_grayscale_for_blue = [grayscale_break3,grayscale_break3,grayscale_break3]
    min_grayscale_for_purple = [grayscale_break3+1,grayscale_break3+1,grayscale_break3+1]
    max_grayscale_for_purple = [grayscale_break4,grayscale_break4,grayscale_break4]
    min_grayscale_for_green = [grayscale_break4+1,grayscale_break4+1,grayscale_break4+1]
    max_grayscale_for_green = [grayscale_break5,grayscale_break5,grayscale_break5]
    min_grayscale_for_cyan = [grayscale_break5+1,grayscale_break5+1,grayscale_break5+1]
    max_grayscale_for_cyan = [grayscale_break6,grayscale_break6,grayscale_break6]
    min_grayscale_for_pink = [grayscale_break6+1,grayscale_break6+1,grayscale_break6+1]
    max_grayscale_for_pink = [grayscale_break7,grayscale_break7,grayscale_break7]
    min_grayscale_for_orange = [grayscale_break7+1,grayscale_break7+1,grayscale_break7+1]
    max_grayscale_for_orange = [grayscale_break8,grayscale_break8,grayscale_break8]
    min_grayscale_for_lime = [grayscale_break8+1,grayscale_break8+1,grayscale_break8+1]
    max_grayscale_for_lime = [grayscale_break9,grayscale_break9,grayscale_break9]
    min_grayscale_for_lb = [grayscale_break9+1,grayscale_break9+1,grayscale_break9+1]
    max_grayscale_for_lb = [grayscale_break10,grayscale_break10,grayscale_break10]
    min_grayscale_for_lavender = [grayscale_break10+1,grayscale_break10+1,grayscale_break10+1]
    max_grayscale_for_lavender = [255,255,255]
    
       
    
    min_grayscale_for_red = numpy.array(min_grayscale_for_red, dtype = "uint8")
    max_grayscale_for_red = numpy.array(max_grayscale_for_red, dtype = "uint8")
    min_grayscale_for_yellow = numpy.array(min_grayscale_for_yellow, dtype = "uint8")
    max_grayscale_for_yellow = numpy.array(max_grayscale_for_yellow, dtype = "uint8")
    min_grayscale_for_blue = numpy.array(min_grayscale_for_blue, dtype = "uint8")
    max_grayscale_for_blue = numpy.array(max_grayscale_for_blue, dtype = "uint8")
    min_grayscale_for_purple = numpy.array(min_grayscale_for_purple, dtype = "uint8")
    max_grayscale_for_purple = numpy.array(max_grayscale_for_purple, dtype = "uint8")
    min_grayscale_for_green = numpy.array(min_grayscale_for_green, dtype = "uint8")
    max_grayscale_for_green = numpy.array(max_grayscale_for_green, dtype = "uint8")
    min_grayscale_for_cyan = numpy.array(min_grayscale_for_cyan, dtype = "uint8")
    max_grayscale_for_cyan = numpy.array(max_grayscale_for_cyan, dtype = "uint8")
    min_grayscale_for_pink = numpy.array(min_grayscale_for_pink, dtype = "uint8")
    max_grayscale_for_pink = numpy.array(max_grayscale_for_pink, dtype = "uint8")
    min_grayscale_for_orange = numpy.array(min_grayscale_for_orange, dtype = "uint8")
    max_grayscale_for_orange = numpy.array(max_grayscale_for_orange, dtype = "uint8")
    min_grayscale_for_lime = numpy.array(min_grayscale_for_lime, dtype = "uint8")
    max_grayscale_for_lime = numpy.array(max_grayscale_for_lime, dtype = "uint8")
    min_grayscale_for_lb = numpy.array(min_grayscale_for_lb, dtype = "uint8")
    max_grayscale_for_lb = numpy.array(max_grayscale_for_lb, dtype = "uint8")
    min_grayscale_for_lavender = numpy.array(min_grayscale_for_lavender, dtype = "uint8")
    max_grayscale_for_lavender = numpy.array(max_grayscale_for_lavender, dtype = "uint8")
    
    
    print(min_grayscale_for_red)
    print(max_grayscale_for_red)
    print(min_grayscale_for_yellow)
    print(max_grayscale_for_yellow)
    print(min_grayscale_for_blue)
    print(max_grayscale_for_blue)
    print(min_grayscale_for_purple)
    print(max_grayscale_for_purple)
    print(min_grayscale_for_green)
    print(max_grayscale_for_green)
    print(min_grayscale_for_cyan)
    print(max_grayscale_for_cyan)
    print(min_grayscale_for_pink)
    print(max_grayscale_for_pink)
    print(min_grayscale_for_orange)
    print(max_grayscale_for_orange)
    print(min_grayscale_for_lime)
    print(max_grayscale_for_lime)
    print(min_grayscale_for_lb)
    print(max_grayscale_for_lb)
    print(min_grayscale_for_lavender)
    print(max_grayscale_for_lavender)

    
    block_all_but_the_red_parts = cv2.inRange(grayscale_image, min_grayscale_for_red, max_grayscale_for_red)
    block_all_but_the_yellow_parts = cv2.inRange(grayscale_image, min_grayscale_for_yellow, max_grayscale_for_yellow)
    block_all_but_the_blue_parts = cv2.inRange(grayscale_image, min_grayscale_for_blue, max_grayscale_for_blue)
    block_all_but_the_purple_parts = cv2.inRange(grayscale_image, min_grayscale_for_purple, max_grayscale_for_purple)
    block_all_but_the_green_parts = cv2.inRange(grayscale_image, min_grayscale_for_green, max_grayscale_for_green)
    block_all_but_the_cyan_parts = cv2.inRange(grayscale_image, min_grayscale_for_cyan, max_grayscale_for_cyan)
    block_all_but_the_pink_parts = cv2.inRange(grayscale_image, min_grayscale_for_pink, max_grayscale_for_pink)
    block_all_but_the_orange_parts = cv2.inRange(grayscale_image, min_grayscale_for_orange, max_grayscale_for_orange)
    block_all_but_the_lime_parts = cv2.inRange(grayscale_image, min_grayscale_for_lime, max_grayscale_for_lime)
    block_all_but_the_lb_parts = cv2.inRange(grayscale_image, min_grayscale_for_lb, max_grayscale_for_lb)
    block_all_but_the_lavender_parts = cv2.inRange(grayscale_image, min_grayscale_for_lavender, max_grayscale_for_lavender)

    
    red_parts_of_image = cv2.bitwise_or(red_paper, red_paper, mask = block_all_but_the_red_parts)
    yellow_parts_of_image = cv2.bitwise_or(yellow_paper, yellow_paper, mask = block_all_but_the_yellow_parts)
    blue_parts_of_image = cv2.bitwise_or(blue_paper, blue_paper, mask = block_all_but_the_blue_parts)
    purple_parts_of_image = cv2.bitwise_or(purple_paper, purple_paper, mask = block_all_but_the_purple_parts)
    green_parts_of_image = cv2.bitwise_or(green_paper, green_paper, mask = block_all_but_the_green_parts)
    cyan_parts_of_image = cv2.bitwise_or(cyan_paper, cyan_paper, mask = block_all_but_the_cyan_parts)
    pink_parts_of_image = cv2.bitwise_or(pink_paper, pink_paper, mask = block_all_but_the_pink_parts)
    orange_parts_of_image = cv2.bitwise_or(orange_paper, orange_paper, mask = block_all_but_the_orange_parts)
    lime_parts_of_image = cv2.bitwise_or(lime_paper, lime_paper, mask = block_all_but_the_lime_parts)
    lb_parts_of_image = cv2.bitwise_or(lb_paper, lb_paper, mask = block_all_but_the_lb_parts)
    lavender_parts_of_image = cv2.bitwise_or(lavender_paper, lavender_paper, mask = block_all_but_the_lavender_parts)

    
    customized_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, blue_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, purple_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, green_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, cyan_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, pink_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, orange_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, lime_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, lb_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, lavender_parts_of_image)

     
   # Original_Images = cv2.bitwise_or(original_image,grayscale_image) 
    
    cv2.imshow('Original Image',original_image) #Program displays the 5 images to the user
    cv2.imshow('Grayscale Image',grayscale_image)
    cv2.imshow('Red Parts of Image',red_parts_of_image)
    cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
    cv2.imshow('Blue Parts of Image',blue_parts_of_image)
    cv2.imshow('Purple Parts of Image',purple_parts_of_image)
    cv2.imshow('Green Parts of Image',green_parts_of_image)
    cv2.imshow('Cyan Parts of Image',cyan_parts_of_image)
    cv2.imshow('Pink Parts of Image',pink_parts_of_image)
    cv2.imshow('Orange Parts of Image',orange_parts_of_image)
    cv2.imshow('Lime Parts of Image',lime_parts_of_image)
    cv2.imshow('LB Parts of Image',lb_parts_of_image)
    cv2.imshow('Lavender Parts of Image',lavender_parts_of_image)

    cv2.imshow('Customized Image',customized_image)
    

    
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
   
    print ("Please enter new file name")
    newfilename = input ("New file name:")
    
    #cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite_(newfilename ,customized_image)
    cv2.destroyAllWindows()
    
# if keypressed == 
