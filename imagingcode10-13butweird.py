# -*- coding: utf-8 -*-
"""
i am so lost
"""

# Images_01_Starting_Code
# Engineer Your World


#HEY YO THIS IS PIERCE I DID NOT FORGET TO DO THIS 
import cv2
import numpy
import os.path

def newTrackbarPos(slider_name, window_name, min_val, max_val):
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print("hey that's too low")
        cv2.setTrackbarPos(slider_name, window_name, min_val)
        return min_val
    elif current_pos > max_val:
        print("hey that's too high")
        cv2.setTrackbarPos(slider_name, window_name, max_val)
        return max_val
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
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
#cv2.namedWindow('Red Parts of Image')
#cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Slider')

image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

color1_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color2_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color3_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color4_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color5_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color6_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color7_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)

color1_paper[0:image_height,0:image_width, 0:image_channels] = [255,153,204]
color2_paper[0:image_height,0:image_width, 0:image_channels] = [51,102,255]
color3_paper[0:image_height,0:image_width, 0:image_channels] = [255,204,0]
color4_paper[0:image_height,0:image_width, 0:image_channels] = [226,29,139]
color5_paper[0:image_height,0:image_width, 0:image_channels] = [204,255,255]
color6_paper[0:image_height,0:image_width, 0:image_channels] = [255,255,153]
color7_paper[0:image_height,0:image_width, 0:image_channels] = [153,153,255]
cv2.createTrackbar('grayscaletrack', 'Slider', 36, 254, lambda x:None)
cv2.createTrackbar('grayscaletrack2', 'Slider', 73, 254, lambda x:None)
cv2.createTrackbar('grayscaletrack3', 'Slider', 110, 254, lambda x:None)
cv2.createTrackbar('grayscaletrack4', 'Slider', 142, 254, lambda x:None)
cv2.createTrackbar('grayscaletrack5', 'Slider', 178, 254, lambda x:None)
cv2.createTrackbar('grayscaletrack6', 'Slider', 218, 254, lambda x:None)

cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)
#'move gray and original images here'

#color1 is red color2 is yellow color3 is green color4 is pink-purply
#the comment above can shut up because it is wrong

keypressed = 1
while(keypressed != 27 and keypressed != ord('s')): #add min and max
    grayscale_break = newTrackbarPos('grayscaletrack', 'Slider', 0, 36) #color 1 and 2
    grayscale_break2 = newTrackbarPos('grayscaletrack2', 'Slider', 37, 73) #mixed color above and 3
    grayscale_break3 = newTrackbarPos('grayscaletrack3', 'Slider', 74, 110) #mixed color above and 4
    grayscale_break4 = newTrackbarPos('grayscaletrack4', 'Slider', 111, 142) #mixed color above and 5
    grayscale_break5 = newTrackbarPos('grayscaletrack5', 'Slider', 143, 178) #mixed color above and 6
    grayscale_break6 = newTrackbarPos('grayscaletrack6', 'Slider', 179, 218) #mixed color above and 7
    
    #below is the ugly code that goes into the sliders
    min_grayscale_for_color1 = [0,0,0]
    max_grayscale_for_color1 = [grayscale_break,grayscale_break,grayscale_break]
    min_grayscale_for_color2 = [grayscale_break+1,grayscale_break+1, 
                                grayscale_break+1]
    
    max_grayscale_for_color2 = [grayscale_break2,grayscale_break2,grayscale_break2]
    min_grayscale_for_color3 = [grayscale_break2+1,grayscale_break2+1, 
                                grayscale_break2+1]
    
    max_grayscale_for_color3 = [grayscale_break3,grayscale_break3,grayscale_break3]
    min_grayscale_for_color4 = [grayscale_break3+1,grayscale_break3+1, 
                                grayscale_break3+1]
    
    max_grayscale_for_color4 = [grayscale_break4,grayscale_break4,grayscale_break4]
    min_grayscale_for_color5 = [grayscale_break4+1, grayscale_break4+1, grayscale_break4+1]
    
    max_grayscale_for_color5 = [grayscale_break5,grayscale_break5,grayscale_break5]
    min_grayscale_for_color6 = [grayscale_break5+1,grayscale_break5+1, 
                                grayscale_break5+1]
    
    max_grayscale_for_color6 = [grayscale_break6,grayscale_break6,grayscale_break6]
    min_grayscale_for_color7 = [grayscale_break6+1,grayscale_break6+1, 
                                grayscale_break6+1]
    
    max_grayscale_for_color7 = [255,255,255]
    
    min_grayscale_for_color1 = numpy.array(min_grayscale_for_color1, dtype = "uint8")
    max_grayscale_for_color1 = numpy.array(max_grayscale_for_color1, dtype = "uint8")
    min_grayscale_for_color2 = numpy.array(min_grayscale_for_color2,
                                           dtype = "uint8")
    max_grayscale_for_color2 = numpy.array(max_grayscale_for_color2,
                                           dtype = "uint8")
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
    
    customized_image = cv2.bitwise_or(color1_parts_of_image, color2_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color3_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color4_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color5_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color6_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color7_parts_of_image)

    
    
    #cv2.imshow('Red Parts of Image',red_parts_of_image)
    #cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
    cv2.imshow('Customized Image',customized_image)
    
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
     filename_valid = False
     while filename_valid == False:
        new_filename = input('Enter the new name of your custom image; be sure to include the file type as well-')
     else:
        print('That file name is not valid')
        #cv2.imwrite('photo_GS_1.jpg',grayscale_image)
        cv2.imwrite(new_filename+'.jpg',customized_image)
        cv2.destroyAllWindows()

