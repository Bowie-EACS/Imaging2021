"""
Peter Yu  8th period
"""
# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path
import random
import json

#random color values
b = random.randrange(0, 255)
g = random.randrange(0, 255)
r = random.randrange(0, 255)
b1 = random.randrange(0, 255)
g1 = random.randrange(0, 255)
r1 = random.randrange(0, 255)
b2 = random.randrange(0, 255)
g2 = random.randrange(0, 255)
r2 = random.randrange(0, 255)
b3 = random.randrange(0, 255)
g3 = random.randrange(0, 255)
r3 = random.randrange(0, 255)
b4 = random.randrange(0, 255)
g4 = random.randrange(0, 255)
r4 = random.randrange(0, 255)
b5 = random.randrange(0, 255)
g5 = random.randrange(0, 255)
r5 = random.randrange(0, 255)
b6 = random.randrange(0, 255)
g6 = random.randrange(0, 255)
r6 = random.randrange(0, 255)
b7 = random.randrange(0, 255)
g7 = random.randrange(0, 255)
r7 = random.randrange(0, 255)
b8 = random.randrange(0, 255)
g8 = random.randrange(0, 255)
r8 = random.randrange(0, 255)
b9 = random.randrange(0, 255)
g9 = random.randrange(0, 255)
r9 = random.randrange(0, 255)

def trackPosition(slider_name, window_name, min_val):
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print("Hey, that's too low")
        cv2.setTrackbarPos(slider_name, window_name, min_val)
        return min_val
    # if current_pos > max_val:
    #     print("Hey, that's too high")
    #     cv2.setTrackbarPos(slider_name, window_name, max_val)
    #     return max_val
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
#the 0 kills the color values
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)
#make windows  
#the names are not matching with the colors they show
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Red Parts of Image')
cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow('Blue Parts of Image')
cv2.namedWindow('Green Parts of Image')
cv2.namedWindow('Purple Parts of Image')
cv2.namedWindow('White Parts of Image')
cv2.namedWindow('Orange Parts of Image')
cv2.namedWindow('Pink Parts of Image')
cv2.namedWindow('Mustard Parts of Image')
cv2.namedWindow('Hot Pink Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')
cv2.resizeWindow('Sliders', 400, 500)
#window resize 

#reads dimensions of the original image 
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]
#make the array the right size
paper_0 = numpy.zeros((image_height,image_width,image_channels), 
                           numpy.uint8)
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


#gives the pictures colors
#numbers in comments are previous presets
paper_0[0:image_height,0:image_width, 0:image_channels] = [b, g, r]
#0 0 255
paper_1[0:image_height,0:image_width, 0:image_channels] = [b3,g3,r3]
#0,255,255
paper_2[0:image_height,0:image_width, 0:image_channels] = [b4,g4,r4]
#255,0,0
paper_3[0:image_height,0:image_width, 0:image_channels] = [b5,g5,r5]
#0,255,0
paper_4[0:image_height,0:image_width, 0:image_channels] = [b6,g6,r6]
#255,0,255
paper_5[0:image_height,0:image_width, 0:image_channels] = [b7,g7,r7]
#255,255,255
paper_6[0:image_height,0:image_width, 0:image_channels] = [b8,g8,r8]
#0,200,255
paper_7[0:image_height,0:image_width, 0:image_channels] = [b9,g9,r9]
#200,125,255
paper_8[0:image_height,0:image_width, 0:image_channels] = [b1, g1, r1]
#100 200 200
paper_9[0:image_height,0:image_width, 0:image_channels] = [b2, g2, r2]
#200 100 255


preset = input("Would you like to use a color preset? (yes/no): ")
if preset == "yes":
    preset_name = input("Enter the preset name: ")
    with open (preset_name) as w:
        data = json.load(w)
        
#a random value that splits the image to choose colors

cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image', grayscale_image)
cv2.createTrackbar('Grayscale 0', 'Sliders', 0, 25, lambda x:None)
cv2.createTrackbar('Grayscale 1', 'Sliders', 26, 51, lambda x:None)
cv2.createTrackbar('Grayscale 2', 'Sliders', 52, 77, lambda x:None)
cv2.createTrackbar('Grayscale 3', 'Sliders', 78, 103, lambda x:None)
cv2.createTrackbar('Grayscale 4', 'Sliders', 104, 129, lambda x:None)
cv2.createTrackbar('Grayscale 5', 'Sliders', 130, 155, lambda x:None)
cv2.createTrackbar('Grayscale 6', 'Sliders', 156, 181, lambda x:None)
cv2.createTrackbar('Grayscale 7', 'Sliders', 182, 207, lambda x:None)
cv2.createTrackbar('Grayscale 8', 'Sliders', 208, 233, lambda x:None)
cv2.createTrackbar('Grayscale 9', 'Sliders', 234, 255, lambda x:None)


keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
    grayscale_break0 = trackPosition('Grayscale 0', 'Sliders', 0)
    grayscale_break1 = trackPosition('Grayscale 1', 'Sliders', 26)
    grayscale_break2 = trackPosition('Grayscale 2', 'Sliders', 52)
    grayscale_break3 = trackPosition('Grayscale 3', 'Sliders', 78)
    grayscale_break4 = trackPosition('Grayscale 4', 'Sliders', 104)
    grayscale_break5 = trackPosition('Grayscale 5', 'Sliders', 130)
    grayscale_break6 = trackPosition('Grayscale 6', 'Sliders', 156)
    grayscale_break7 = trackPosition('Grayscale 7', 'Sliders', 182)
    grayscale_break8 = trackPosition('Grayscale 8', 'Sliders', 208)
    grayscale_break9 = trackPosition('Grayscale 9', 'Sliders', 234)
 
    
    min_grayscale_for_red = [0,0,0]
    max_grayscale_for_red = [grayscale_break0+25,grayscale_break0+25,
                             grayscale_break0+25]
    min_grayscale_for_yellow = [grayscale_break1,grayscale_break1, 
                                grayscale_break1]
    max_grayscale_for_yellow = [grayscale_break1+25, grayscale_break1+25, 
                                grayscale_break1+25]
    min_grayscale_for_blue = [grayscale_break2, grayscale_break2, 
                              grayscale_break2]
    max_grayscale_for_blue = [grayscale_break2+25, grayscale_break2+25, 
                              grayscale_break2+25]
    min_grayscale_for_green = [grayscale_break3, grayscale_break3, 
                              grayscale_break3]
    max_grayscale_for_green = [grayscale_break3+25, grayscale_break3+25, 
                              grayscale_break3+25]
    min_grayscale_for_purple = [grayscale_break4, grayscale_break4, 
                              grayscale_break4]
    max_grayscale_for_purple =  [grayscale_break4+25, grayscale_break4+25, 
                              grayscale_break4+25]
    min_grayscale_for_white = [grayscale_break5, grayscale_break5, 
                              grayscale_break5]
    max_grayscale_for_white = [grayscale_break5+25, grayscale_break5+25, 
                              grayscale_break5+25]   
    min_grayscale_for_orange = [grayscale_break6, grayscale_break6, 
                              grayscale_break6]
    max_grayscale_for_orange = [grayscale_break6+25, grayscale_break6+25, 
                              grayscale_break6+25] 
    min_grayscale_for_pink = [grayscale_break7, grayscale_break7, 
                              grayscale_break7]
    max_grayscale_for_pink = [grayscale_break7+25, grayscale_break7+25,
                              grayscale_break7+25] 
    min_grayscale_for_germany = [grayscale_break8, grayscale_break8, 
                              grayscale_break8]
    max_grayscale_for_germany = [grayscale_break8+25, grayscale_break8+25,
                              grayscale_break8+25] 
    min_grayscale_for_hotpink = [grayscale_break9, grayscale_break9, 
                              grayscale_break9]
    max_grayscale_for_hotpink = [255,255,255] 
    
    
    min_grayscale_for_red = numpy.array(min_grayscale_for_red, dtype = "uint8")
    max_grayscale_for_red = numpy.array(max_grayscale_for_red, dtype = "uint8")
    min_grayscale_for_yellow = numpy.array(min_grayscale_for_yellow,
                                           dtype = "uint8")
    max_grayscale_for_yellow = numpy.array(max_grayscale_for_yellow,
                                           dtype = "uint8")
    min_grayscale_for_blue = numpy.array(min_grayscale_for_blue,
                                           dtype = "uint8")
    max_grayscale_for_blue = numpy.array(max_grayscale_for_blue,
                                           dtype = "uint8")
    min_grayscale_for_green = numpy.array(min_grayscale_for_green,
                                           dtype = "uint8")
    max_grayscale_for_green = numpy.array(max_grayscale_for_green,
                                           dtype = "uint8")
    min_grayscale_for_purple = numpy.array(min_grayscale_for_purple,
                                           dtype = "uint8")
    max_grayscale_for_purple = numpy.array(max_grayscale_for_purple,
                                           dtype = "uint8")
    min_grayscale_for_white = numpy.array(min_grayscale_for_white,
                                           dtype = "uint8")
    max_grayscale_for_white = numpy.array(max_grayscale_for_white,
                                           dtype = "uint8")
    min_grayscale_for_orange = numpy.array(min_grayscale_for_orange,
                                           dtype = "uint8")
    max_grayscale_for_orange = numpy.array(max_grayscale_for_orange,
                                           dtype = "uint8")
    min_grayscale_for_pink = numpy.array(min_grayscale_for_pink,
                                           dtype = "uint8")
    max_grayscale_for_pink = numpy.array(max_grayscale_for_pink,
                                           dtype = "uint8")
    min_grayscale_for_germany = numpy.array(min_grayscale_for_germany,
                                           dtype = "uint8")
    max_grayscale_for_germany = numpy.array(max_grayscale_for_germany,
                                           dtype = "uint8")
    min_grayscale_for_hotpink = numpy.array(min_grayscale_for_hotpink,
                                           dtype = "uint8")
    max_grayscale_for_hotpink = numpy.array(max_grayscale_for_hotpink,
                                           dtype = "uint8")
    #makes everything not in certain ranges blocked
    block_all_but_the_red_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_red,
                                              max_grayscale_for_red) 
    block_all_but_the_yellow_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_yellow,
                                                 max_grayscale_for_yellow)
    block_all_but_the_blue_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_blue,
                                                 max_grayscale_for_blue)
    block_all_but_the_green_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_green,
                                                 max_grayscale_for_green)
    block_all_but_the_purple_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_purple,
                                                 max_grayscale_for_purple)
    block_all_but_the_white_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_white,
                                                 max_grayscale_for_white)
    block_all_but_the_orange_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_orange,
                                                 max_grayscale_for_orange)
    block_all_but_the_pink_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_pink,
                                                 max_grayscale_for_pink)
    block_all_but_the_color_8_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_germany,
                                                 max_grayscale_for_germany)
    block_all_but_the_color_9_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_hotpink,
                                                 max_grayscale_for_hotpink)
    #cuts the blocked parts of the images
    red_parts_of_image = cv2.bitwise_or(paper_0, paper_0,
                                        mask = block_all_but_the_red_parts)
    yellow_parts_of_image = cv2.bitwise_or(paper_1, paper_1,
                                           mask = block_all_but_the_yellow_parts)
    blue_parts_of_image = cv2.bitwise_or(paper_2, paper_2,
                                           mask = block_all_but_the_blue_parts)
    green_parts_of_image = cv2.bitwise_or(paper_3, paper_3,
                                           mask = block_all_but_the_green_parts)
    purple_parts_of_image = cv2.bitwise_or(paper_4, paper_4,
                                           mask = block_all_but_the_purple_parts)
    white_parts_of_image = cv2.bitwise_or(paper_5, paper_5,
                                           mask = block_all_but_the_white_parts)
    orange_parts_of_image = cv2.bitwise_or(paper_6, paper_6,
                                           mask = block_all_but_the_orange_parts)
    pink_parts_of_image = cv2.bitwise_or(paper_7, paper_7,
                                           mask = block_all_but_the_pink_parts)
    part_8_of_image = cv2.bitwise_or(paper_8, paper_8,
                                           mask = block_all_but_the_color_8_parts)
    part_9_of_image = cv2.bitwise_or(paper_9, paper_9,
                                           mask = block_all_but_the_color_9_parts)
    
     
    customized_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, blue_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, green_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, purple_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, white_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, orange_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, pink_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, part_8_of_image)
    customized_image = cv2.bitwise_or(customized_image, part_9_of_image)    
    

    #final_image = cv2.bitwise_or(customized_image, customized_image_2)
    #put images in the windows
    cv2.imshow('Red Parts of Image',red_parts_of_image)
    cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
    cv2.imshow('Blue Parts of Image',blue_parts_of_image)
    cv2.imshow('Green Parts of Image',green_parts_of_image)
    cv2.imshow('Purple Parts of Image',purple_parts_of_image)
    cv2.imshow('White Parts of Image',white_parts_of_image)
    cv2.imshow('Orange Parts of Image',orange_parts_of_image)
    cv2.imshow('Pink Parts of Image',pink_parts_of_image)
    cv2.imshow('Mustard Parts of Image',pink_parts_of_image)
    cv2.imshow('Hot Pink Parts of Image',pink_parts_of_image)
    cv2.imshow('Customized Image',customized_image)
    #27 is esc key which destroys all window

    keypressed = cv2.waitKey(1)
    
    
if keypressed == 27:
    cv2.destroyAllWindows()
    
#option to save a color set 
elif keypressed == ord('c'):
    save = input("Do you want to save these colors? (yes/no): ")
    color_list = [b,g,r,b1,g1,r1,b2,g2,r2,b3,g3,r3,b4,g5,r5,b6,g6,r6,b7,g,r7,
                  b8,g8,r8,b9,g9,r9]    
    preset_name = input("Name this color list: ")
    with open(preset_name, 'w') as json_file:
        json.dump(color_list, json_file)
        

    #if s is pressed, ask user to name 
elif keypressed == ord('s'): 
    file_name = input("What do you want to name this image? include .[file type] at the end: ")
    str(file_name)
    cv2.imwrite('gray ' + file_name,grayscale_image)
    cv2.imwrite(file_name, customized_image)
    cv2.destroyAllWindows()