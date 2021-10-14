"""
By B. Almaguer  -  09.9.2021
"""

# Images_01_Starting_Code
# Engineer Your World
#BGR

import cv2
import numpy
import os.path
import json 

#defines a function to create a maximum and minimum value for the grayscales
def trackPosition(slider_name, window_name, min_val, max_val):
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print("Hey. That's too low.")
        cv2.setTrackbarPos(slider_name, window_name, min_val)
        return min_val
    elif current_pos > max_val:
            print("Hey. That's too high.")
            cv2.setTrackbarPos(slider_name, window_name, max_val)
            return max_val
    else:
        return current_pos

#asks the user to give an image
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
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

#creates the windows that will be used
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Color1 Parts of Image')
cv2.namedWindow('Color2 Parts of Image')
cv2.namedWindow('Color3 Parts of Image')
cv2.namedWindow('Color4 Parts of Image')
cv2.namedWindow('Color5 Parts of Image')
cv2.namedWindow('Color6 Parts of Image')
cv2.namedWindow('Color7 Parts of Image')
cv2.namedWindow('Color8 Parts of Image')
cv2.namedWindow('Color9 Parts of Image')
cv2.namedWindow('Color10 Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')

image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#creates colored papers and matches their size to that of the image
color1_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color2_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color3_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color4_paper = numpy.zeros((image_height,image_width,image_channels),numpy.uint8)
color5_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color6_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color7_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color8_paper = numpy.zeros((image_height,image_width,image_channels),numpy.uint8)
color9_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color10_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

#creates trackbars for the colors
cv2.createTrackbar('Blue1', 'Color1 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Green1', 'Color1 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Red1', 'Color1 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Blue2', 'Color2 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Green2', 'Color2 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Red2', 'Color2 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Blue3', 'Color3 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Green3', 'Color3 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Red3', 'Color3 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Blue4', 'Color4 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Green4', 'Color4 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Red4', 'Color4 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Blue5', 'Color5 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Green5', 'Color5 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Red5', 'Color5 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Blue6', 'Color6 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Green6', 'Color6 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Red6', 'Color6 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Blue7', 'Color7 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Green7', 'Color7 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Red7', 'Color7 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Blue8', 'Color8 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Green8', 'Color8 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Red8', 'Color8 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Blue9', 'Color9 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Green9', 'Color9 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Red9', 'Color9 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Blue10', 'Color10 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Green10', 'Color10 Parts of Image', 100, 255, lambda x:None)
cv2.createTrackbar('Red10', 'Color10 Parts of Image', 100, 255, lambda x:None)

#ask color data question here
preset = input("Would you like to use a color preset? (yes/no): ")
if preset == "yes":
    name_of_preset = input("Enter the preset name: ")
    with open (name_of_preset) as f:
        data = json.load(f)

#creates variables for the color values
    blue1 = cv2.setTrackbarPos('Blue1', 'Color1 Parts of Image', data[0])
    green1 = cv2.setTrackbarPos('Green1', 'Color1 Parts of Image', data[1])
    red1 = cv2.setTrackbarPos('Red1', 'Color1 Parts of Image', data[2])
    blue2 = cv2.setTrackbarPos('Blue2', 'Color2 Parts of Image', data[3])
    green2 = cv2.setTrackbarPos('Green2', 'Color2 Parts of Image', data[4])
    red2 = cv2.setTrackbarPos('Red2', 'Color2 Parts of Image', data[5])
    blue3 = cv2.setTrackbarPos('Blue3', 'Color3 Parts of Image', data[6])
    green3 = cv2.setTrackbarPos('Green3', 'Color3 Parts of Image', data[7])
    red3 = cv2.setTrackbarPos('Red3', 'Color3 Parts of Image', data[8])
    blue4 = cv2.setTrackbarPos('Blue4', 'Color4 Parts of Image', data[9])
    green4 = cv2.setTrackbarPos('Green4', 'Color4 Parts of Image', data[10])
    red4 = cv2.setTrackbarPos('Red4', 'Color4 Parts of Image', data[11])
    blue5 = cv2.setTrackbarPos('Blue5', 'Color5 Parts of Image', data[12])
    green5 = cv2.setTrackbarPos('Green5', 'Color5 Parts of Image', data[13])
    red5 = cv2.setTrackbarPos('Red5', 'Color5 Parts of Image', data[14])
    blue6 = cv2.setTrackbarPos('Blue6', 'Color6 Parts of Image', data[15])
    green6 = cv2.setTrackbarPos('Green6', 'Color6 Parts of Image', data[16])
    red6 = cv2.setTrackbarPos('Red6', 'Color6 Parts of Image', data[17])
    blue7 = cv2.setTrackbarPos('Blue7', 'Color7 Parts of Image', data[18])
    green7 = cv2.setTrackbarPos('Green7', 'Color7 Parts of Image', data[19])
    red7 = cv2.setTrackbarPos('Red7', 'Color7 Parts of Image', data[20])
    blue8 = cv2.setTrackbarPos('Blue8', 'Color8 Parts of Image', data[21])
    green8 = cv2.setTrackbarPos('Green8', 'Color8 Parts of Image', data[22])
    red8 = cv2.setTrackbarPos('Red8', 'Color8 Parts of Image', data[23])
    blue9 = cv2.setTrackbarPos('Blue9', 'Color9 Parts of Image', data[24])
    green9 = cv2.setTrackbarPos('Green9', 'Color9 Parts of Image', data[25])
    red9 = cv2.setTrackbarPos('Red9', 'Color9 Parts of Image', data[26])
    blue10 = cv2.setTrackbarPos('Blue10', 'Color10 Parts of Image', data[27])
    green10 = cv2.setTrackbarPos('Green10', 'Color10 Parts of Image', data[28])
    red10 = cv2.setTrackbarPos('Red10', 'Color10 Parts of Image', data[29])

#creates trackbars for the grayscales
cv2.createTrackbar('Grayscale 1', 'Sliders', 100, 255, lambda x:None)
cv2.createTrackbar('Grayscale 2', 'Sliders', 100, 255, lambda x:None)
cv2.createTrackbar('Grayscale 3', 'Sliders', 100, 255, lambda x:None)
cv2.createTrackbar('Grayscale 4', 'Sliders', 100, 255, lambda x:None)
cv2.createTrackbar('Grayscale 5', 'Sliders', 100, 255, lambda x:None)
cv2.createTrackbar('Grayscale 6', 'Sliders', 100, 255, lambda x:None)
cv2.createTrackbar('Grayscale 7', 'Sliders', 100, 255, lambda x:None)
cv2.createTrackbar('Grayscale 8', 'Sliders', 100, 255, lambda x:None)
cv2.createTrackbar('Grayscale 9', 'Sliders', 100, 255, lambda x:None)
 
#creates a loop to use the trackbar value of the grayscale and allows the image to update when the grayscale changes
cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)
keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):   
#Creates three trackbars for each color (one for each RBG variable)
    blue1 = cv2.getTrackbarPos('Blue1', 'Color1 Parts of Image')
    green1 = cv2.getTrackbarPos('Green1', 'Color1 Parts of Image')
    red1 = cv2.getTrackbarPos('Red1', 'Color1 Parts of Image')
    blue2 = cv2.getTrackbarPos('Blue2', 'Color2 Parts of Image')
    green2 = cv2.getTrackbarPos('Green2', 'Color2 Parts of Image')
    red2 = cv2.getTrackbarPos('Red2', 'Color2 Parts of Image')
    blue3 = cv2.getTrackbarPos('Blue3', 'Color3 Parts of Image')
    green3 = cv2.getTrackbarPos('Green3', 'Color3 Parts of Image')
    red3 = cv2.getTrackbarPos('Red3', 'Color3 Parts of Image')
    blue4 = cv2.getTrackbarPos('Blue4', 'Color4 Parts of Image')
    green4 = cv2.getTrackbarPos('Green4', 'Color4 Parts of Image')
    red4 = cv2.getTrackbarPos('Red4', 'Color4 Parts of Image')
    blue5 = cv2.getTrackbarPos('Blue5', 'Color5 Parts of Image')
    green5 = cv2.getTrackbarPos('Green5', 'Color5 Parts of Image')
    red5 = cv2.getTrackbarPos('Red5', 'Color5 Parts of Image')
    blue6 = cv2.getTrackbarPos('Blue6', 'Color6 Parts of Image')
    green6 = cv2.getTrackbarPos('Green6', 'Color6 Parts of Image')
    red6 = cv2.getTrackbarPos('Red6', 'Color6 Parts of Image')
    blue7 = cv2.getTrackbarPos('Blue7', 'Color7 Parts of Image')
    green7 = cv2.getTrackbarPos('Green7', 'Color7 Parts of Image')
    red7 = cv2.getTrackbarPos('Red7', 'Color7 Parts of Image')
    blue8 = cv2.getTrackbarPos('Blue8', 'Color8 Parts of Image')
    green8 = cv2.getTrackbarPos('Green8', 'Color8 Parts of Image')
    red8 = cv2.getTrackbarPos('Red8', 'Color8 Parts of Image')
    blue9 = cv2.getTrackbarPos('Blue9', 'Color9 Parts of Image')
    green9 = cv2.getTrackbarPos('Green9', 'Color9 Parts of Image')
    red9 = cv2.getTrackbarPos('Red9', 'Color9 Parts of Image')
    blue10 = cv2.getTrackbarPos('Blue10', 'Color10 Parts of Image')
    green10 = cv2.getTrackbarPos('Green10', 'Color10 Parts of Image')
    red10 = cv2.getTrackbarPos('Red10', 'Color10 Parts of Image')
    
#establishes the colors that will be used
    color1_paper[0:image_height,0:image_width, 0:image_channels] = [blue1,green1,red1]
    color2_paper[0:image_height,0:image_width, 0:image_channels] = [blue2,green2,red2]
    color3_paper[0:image_height,0:image_width, 0:image_channels] = [blue3,green3,red3]
    color4_paper[0:image_height,0:image_width, 0:image_channels] = [blue4,green4,red4]
    color5_paper[0:image_height,0:image_width, 0:image_channels] = [blue5,green5,red5]
    color6_paper[0:image_height,0:image_width, 0:image_channels] = [blue6,green6,red6] 
    color7_paper[0:image_height,0:image_width, 0:image_channels] = [blue7,green7,red7] 
    color8_paper[0:image_height,0:image_width, 0:image_channels] = [blue8,green8,red8] 
    color9_paper[0:image_height,0:image_width, 0:image_channels] = [blue9,green9,red9] 
    color10_paper[0:image_height,0:image_width, 0:image_channels] = [blue10,green10,red10] 
    
#establishes which section of the image each color will have    
    grayscale_break_1 = trackPosition('Grayscale 1', 'Sliders', 0, 90)
    grayscale_break_2 = trackPosition('Grayscale 2', 'Sliders', grayscale_break_1 + 1, grayscale_break_1 + 20)
    grayscale_break_3 = trackPosition('Grayscale 3', 'Sliders', grayscale_break_2 + 1, grayscale_break_2 + 20)
    grayscale_break_4 = trackPosition('Grayscale 4', 'Sliders', grayscale_break_3 + 1, grayscale_break_3 + 20)
    grayscale_break_5 = trackPosition('Grayscale 5', 'Sliders', grayscale_break_4 + 1, grayscale_break_4 + 20)
    grayscale_break_6 = trackPosition('Grayscale 6', 'Sliders', grayscale_break_5 + 1, grayscale_break_5 + 20)
    grayscale_break_7 = trackPosition('Grayscale 7', 'Sliders', grayscale_break_6 + 1, grayscale_break_6 + 20)
    grayscale_break_8 = trackPosition('Grayscale 8', 'Sliders', grayscale_break_7 + 1, grayscale_break_7 + 20)
    grayscale_break_9 = trackPosition('Grayscale 9', 'Sliders', grayscale_break_8 + 1, 255)

#creates the sections of the image that will be filled by each color    
    min_grayscale_for_color1 = [0,0,0]
    max_grayscale_for_color1 = [grayscale_break_1,grayscale_break_1,grayscale_break_1]
    min_grayscale_for_color2 = [grayscale_break_1 + 1, grayscale_break_1 + 1, grayscale_break_1 + 1]
    max_grayscale_for_color2 = [grayscale_break_2,grayscale_break_2,grayscale_break_2]
    min_grayscale_for_color3 = [grayscale_break_2 + 1, grayscale_break_2 + 1, grayscale_break_2 + 1]
    max_grayscale_for_color3 = [grayscale_break_3,grayscale_break_3,grayscale_break_3]
    min_grayscale_for_color4 = [grayscale_break_3 + 1, grayscale_break_3 + 1, grayscale_break_3 + 1]
    max_grayscale_for_color4 = [grayscale_break_4, grayscale_break_4, grayscale_break_4]
    min_grayscale_for_color5 = [grayscale_break_4 + 1, grayscale_break_4 + 1, grayscale_break_4 + 1] ####
    max_grayscale_for_color5 = [grayscale_break_5, grayscale_break_5, grayscale_break_5] ####
    min_grayscale_for_color6 = [grayscale_break_5 + 1, grayscale_break_5 + 1, grayscale_break_5 + 1] ####
    max_grayscale_for_color6 = [grayscale_break_6, grayscale_break_6, grayscale_break_6] ####
    min_grayscale_for_color7 = [grayscale_break_6 + 1, grayscale_break_6 + 1, grayscale_break_6 + 1] ####
    max_grayscale_for_color7 = [grayscale_break_7, grayscale_break_7, grayscale_break_7] ####
    min_grayscale_for_color8 = [grayscale_break_7 + 1, grayscale_break_7 + 1, grayscale_break_7 + 1] ####
    max_grayscale_for_color8 = [grayscale_break_8, grayscale_break_8, grayscale_break_8] ####
    min_grayscale_for_color9 = [grayscale_break_8 + 1, grayscale_break_8 + 1, grayscale_break_8 + 1] ####
    max_grayscale_for_color9 = [grayscale_break_9, grayscale_break_9, grayscale_break_9] ####
    min_grayscale_for_color10 = [grayscale_break_9 + 1, grayscale_break_9 + 1, grayscale_break_9 + 1] ####
    max_grayscale_for_color10 = [255,255,255] ####

#I do not know what this does    
    min_grayscale_for_color2 = numpy.array(min_grayscale_for_color2, dtype = "uint8")
    max_grayscale_for_color2 = numpy.array(max_grayscale_for_color2, dtype = "uint8")
    min_grayscale_for_color1 = numpy.array(min_grayscale_for_color1, dtype = "uint8")
    max_grayscale_for_color1 = numpy.array(max_grayscale_for_color1, dtype = "uint8")
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
    min_grayscale_for_color9 = numpy.array(min_grayscale_for_color9, dtype = "uint8") 
    max_grayscale_for_color9 = numpy.array(max_grayscale_for_color9, dtype = "uint8") 
    min_grayscale_for_color10 = numpy.array(min_grayscale_for_color10, dtype = "uint8") 
    max_grayscale_for_color10 = numpy.array(max_grayscale_for_color10, dtype = "uint8") 

#creates a mask with only the specific color filling its set location    
    block_all_but_the_color2_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color2,
                                              max_grayscale_for_color2)
    block_all_but_the_color1_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color1,
                                              max_grayscale_for_color1)
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
    block_all_but_the_color8_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color8,
                                              max_grayscale_for_color8)
    block_all_but_the_color9_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color9,
                                              max_grayscale_for_color9)
    block_all_but_the_color10_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color10,
                                              max_grayscale_for_color10)

#creates an image with only the specific color filling its set location        
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
    color8_parts_of_image = cv2.bitwise_or(color8_paper, color8_paper,
                                           mask = block_all_but_the_color8_parts)
    color9_parts_of_image = cv2.bitwise_or(color9_paper, color9_paper,
                                        mask = block_all_but_the_color9_parts)
    color10_parts_of_image = cv2.bitwise_or(color10_paper, color10_paper,
                                        mask = block_all_but_the_color10_parts)

#creates a final image with all of the colors combined    
    customized_image_1 = cv2.bitwise_or(color2_parts_of_image, color1_parts_of_image)
    customized_image_2 = cv2.bitwise_or(color3_parts_of_image, color4_parts_of_image)
    customized_image_3 = cv2.bitwise_or(color5_parts_of_image, color6_parts_of_image)
    customized_image_4 = cv2.bitwise_or(color7_parts_of_image, color8_parts_of_image)
    customized_image_5 = cv2.bitwise_or(color9_parts_of_image, color10_parts_of_image)
    customized_image_12 = cv2.bitwise_or(customized_image_1, customized_image_2)
    customized_image_34 = cv2.bitwise_or(customized_image_3, customized_image_4)
    customized_image_125 = cv2.bitwise_or(customized_image_12, customized_image_5)
    customized_image_final = cv2.bitwise_or(customized_image_125, customized_image_34)

#displays the windows created previously    
    cv2.imshow('Color1 Parts of Image',color1_parts_of_image)
    cv2.imshow('Color2 Parts of Image',color2_parts_of_image)
    cv2.imshow('Color3 Parts of Image',color3_parts_of_image)    
    cv2.imshow('Color4 Parts of Image',color4_parts_of_image)
    cv2.imshow('Color5 Parts of Image',color5_parts_of_image)
    cv2.imshow('Color6 Parts of Image',color6_parts_of_image)
    cv2.imshow('Color7 Parts of Image',color7_parts_of_image)    
    cv2.imshow('Color8 Parts of Image',color8_parts_of_image)
    cv2.imshow('Color9 Parts of Image',color9_parts_of_image)
    cv2.imshow('Color10 Parts of Image',color10_parts_of_image)
    cv2.imshow('Customized Image',customized_image_final)
        
#allows the windows to close when the user presses the "esc" key    
    keypressed = cv2.waitKey(1)
    
#saves the color selections if the user wants to
save = input("Would you like to save this color selection? (yes/no): ")
if save  == "yes":
    color_list = [blue1, green1, red1, blue2, green2, red2, blue3, green3, red3, blue4,
              green4, red4, blue5, green5, red5, blue6, green6, red6, blue7, green7,
              red7, blue8, green8, red8, blue9, green9, red9, blue10, green10, red10]    
    preset_name = input("Name your list: ")
    with open(preset_name, 'w') as json_file:
        json.dump(color_list, json_file)

if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    new_file_name = input("Name your new file: ")
    cv2.imwrite(new_file_name + '_grayscale.jpg',grayscale_image)
    cv2.imwrite(new_file_name + '.jpg',customized_image_final)
    cv2.destroyAllWindows()
