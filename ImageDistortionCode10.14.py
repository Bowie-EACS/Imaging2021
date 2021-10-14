# Images_01_Starting_Code
# Engineer Your World
# Kyle Thompson s2125327 

import cv2
import numpy
import os.path

def newTrackbarPos(trackbar_name, trackbar_window, min_val):
    current_pos = cv2.getTrackbarPos(trackbar_name, trackbar_window)
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

original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

#Windows that will show when the program is run
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Red Parts of Image')
cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow('Green Parts of Image')
cv2.namedWindow('Blue Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders2')

image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

color_1 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color_2 = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color_3 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color_4 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8) 
color_5 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8) 
color_6 = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

#Trackbar to change the colors
cv2.createTrackbar('Grayscale1', 'Sliders2', 50, 255, lambda x:None) 
cv2.createTrackbar('Grayscale2', 'Sliders2', 100, 255, lambda x:None)
cv2.createTrackbar('Grayscale3', 'Sliders2', 150, 255, lambda x:None)
cv2.createTrackbar('Grayscale4', 'Sliders2', 150, 255, lambda x:None)

#Color of the image
color_1[0:image_height,0:image_width, 0:image_channels] = [0,0,255]
color_2[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
color_3[0:image_height,0:image_width, 0:image_channels] = [0,255,0]
color_4[0:image_height,0:image_width, 0:image_channels] = [255,0,0] 
color_5[0:image_height,0:image_width, 0:image_channels] = [225,246,36]
color_6[0:image_height,0:image_width, 0:image_channels] = [218,56,196]

cv2.imshow('Original Image', original_image) 
cv2.imshow('Grayscale Image',grayscale_image) 

keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
    
    #breaking up the grayscale picture into chunks
    grayscale_break1 = newTrackbarPos('Grayscale1', 'Sliders2', 10 ) 
    grayscale_break2 = newTrackbarPos('Grayscale2', 'Sliders2', 50 )
    grayscale_break3 = newTrackbarPos('Grayscale3', 'Sliders2', 90) 
    grayscale_break4 = newTrackbarPos('Grayscale4', 'Sliders2', 100)
    grayscale_break5 = newTrackbarPos('Grayscale5', 'Sliders2', 100)
    
    #Peramaters of the minimum and maximum for the color
    min_grayscale_for_color_1 = [0,0,0]
    max_grayscale_for_color_1 = [grayscale_break1,grayscale_break1,grayscale_break1]
    
    min_grayscale_for_color_2 = [grayscale_break1+1,grayscale_break1+1, 
                                grayscale_break1+1]
    max_grayscale_for_color_2 = [grayscale_break2,grayscale_break2,grayscale_break2] 
    
    min_grayscale_for_color_3 = [grayscale_break2+1,grayscale_break2+1,grayscale_break2+1] 
    max_grayscale_for_color_3 = [grayscale_break3,grayscale_break3,grayscale_break3]
    
    min_grayscale_for_color_4 = [grayscale_break3+1,grayscale_break3+1,grayscale_break3+1] 
    max_grayscale_for_color_4 = [grayscale_break4,grayscale_break4,grayscale_break4]
    
    min_grayscale_for_color_5 = [grayscale_break4+1,grayscale_break4+1,grayscale_break4+1]
    max_grayscale_for_color_5 = [grayscale_break5,grayscale_break5,grayscale_break5]
    
    min_grayscale_for_color_6 = [grayscale_break5+1,grayscale_break5+1,grayscale_break5+1]
    max_grayscale_for_color_6 = [255,255,255]
    
    #Reformatig previous list into data that can be processed easier
    min_grayscale_for_color_1 = numpy.array(min_grayscale_for_color_1, dtype = "uint8")
    max_grayscale_for_color_1 = numpy.array(max_grayscale_for_color_1, dtype = "uint8")
    
    min_grayscale_for_color_2 = numpy.array(min_grayscale_for_color_2,
                                           dtype = "uint8")
    max_grayscale_for_color_2 = numpy.array(max_grayscale_for_color_2,
                                           dtype = "uint8")
    
    min_grayscale_for_color_3 = numpy.array(min_grayscale_for_color_3, dtype = "uint8")
    max_grayscale_for_color_3 = numpy.array(max_grayscale_for_color_3, dtype = "uint8")
    
    min_grayscale_for_color_4 = numpy.array(min_grayscale_for_color_4, dtype = "uint8")
    max_grayscale_for_color_4 = numpy.array(max_grayscale_for_color_4, dtype = "uint8") 
    
    min_grayscale_for_color_5 = numpy.array(min_grayscale_for_color_5, dtype = "uint8")
    max_grayscale_for_color_5 = numpy.array(max_grayscale_for_color_5, dtype = "uint8")  
    
    min_grayscale_for_color_6 = numpy.array(min_grayscale_for_color_6, dtype = "uint8")
    max_grayscale_for_color_6 = numpy.array(max_grayscale_for_color_6, dtype = "uint8")
    
    #gets the range that was created and blocks everything but the color input
    block_all_but_the_color_1_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color_1,
                                              max_grayscale_for_color_1) 
    block_all_but_the_color_2_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color_2,
                                                 max_grayscale_for_color_2)
    block_all_but_the_color_3_parts = cv2.inRange(grayscale_image,
                                                min_grayscale_for_color_3,
                                                max_grayscale_for_color_3)
    block_all_but_the_color_4_parts = cv2.inRange(grayscale_image,
                                               min_grayscale_for_color_4,
                                               max_grayscale_for_color_4)
    block_all_but_the_color_5_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_color_5,
                                                  max_grayscale_for_color_5)
    block_all_but_the_color_6_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_color_6,
                                                  max_grayscale_for_color_6)
    
    color_1_parts_of_image = cv2.bitwise_or(color_1, color_1,
                                        mask = block_all_but_the_color_1_parts)
    color_2_parts_of_image = cv2.bitwise_or(color_2, color_2,
                                           mask = block_all_but_the_color_2_parts)
    color_3_parts_of_image = cv2.bitwise_or(color_3, color_3,
                                          mask = block_all_but_the_color_3_parts) 
    color_4_parts_of_image = cv2.bitwise_or(color_4, color_4,
                                         mask = block_all_but_the_color_4_parts)
    color_5_parts_of_image = cv2.bitwise_or(color_5, color_5,
                                            mask = block_all_but_the_color_5_parts)
    color_6_parts_of_image = cv2.bitwise_or(color_6, color_6,
                                            mask = block_all_but_the_color_6_parts)
    
    #adding the color options to the customized image 
    customized_image = cv2.bitwise_or(color_1_parts_of_image, color_2_parts_of_image)
    customized_image = cv2.bitwise_or(color_3_parts_of_image, customized_image)
    customized_image = cv2.bitwise_or(color_4_parts_of_image, customized_image)
    customized_image = cv2.bitwise_or(color_5_parts_of_image, customized_image)
    customized_image = cv2.bitwise_or(color_6_parts_of_image, customized_image)

    #Image in one specific color  
    cv2.imshow('Red Parts of Image',color_1_parts_of_image) 
    cv2.imshow('Yellow Parts of Image',color_2_parts_of_image) 
    cv2.imshow('Green Parts of Image',color_3_parts_of_image)
    cv2.imshow('Blue Parts of Image',color_4_parts_of_image) 
    cv2.imshow('Orange Parts of Image',color_5_parts_of_image)
    cv2.imshow('Magenta Parts of Image',color_6_parts_of_image) 
    cv2.imshow('Customized Image',customized_image) 

    keypressed = cv2.waitKey(1)  
    
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()
