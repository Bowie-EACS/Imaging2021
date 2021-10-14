# Ekamjit Luban, period ocho

import cv2
import numpy
import os.path


def trackPosition(slider_name, window_name, min_val, max_val):
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print("Thats Too low!")
        cv2.setTrackbarPos(slider_name, window_name, min_val)
        return min_val
    if current_pos > max_val:
        print("Thats too high!")
        cv2.setTrackbarPos(slider_name, window_name, max_val)
        return max_val
    else:
        return current_pos


#Chooses File to work with
print ("Save your original image in the same folder as this program.")
#Additional print statement to provide the user the option to later save their images
print ("If you would like to save your customized or gray scale images, please press 's'")
filename_valid = False
while filename_valid == False:
    filename = input("PLZ Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")

#creates windows
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Blue Parts of Image')
cv2.namedWindow('Red Parts of Image')
cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow('Green Parts of Image')
cv2.namedWindow('Purple Parts of Image')
cv2.namedWindow('Orange Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')
cv2.namedWindow('Color Bars')


#resave file
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)



#Fits the size of the widnow
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#colors are created here
green_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
blue_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
red_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
yellow_paper = numpy.zeros((image_height,image_width,image_channels),numpy.uint8)
purple_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
orange_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)


cv2.createTrackbar('Color_uno_B', 'Color Bars', 0, 255, lambda x:None) # color one
cv2.createTrackbar('Color_uno_G', 'Color Bars', 0, 255, lambda x:None)
cv2.createTrackbar('Color_uno_R', 'Color Bars', 255, 255, lambda x:None)

cv2.createTrackbar('Color_dos_B', 'Color Bars', 0, 255, lambda x:None) #color 2
cv2.createTrackbar('Color_dos_G', 'Color Bars', 255, 255, lambda x:None)
cv2.createTrackbar('Color_dos_R', 'Color Bars', 255, 255, lambda x:None)

cv2.createTrackbar('Color_tres_B', 'Color Bars', 0, 255, lambda x:None) # color 3
cv2.createTrackbar('Color_tres_G', 'Color Bars', 255, 255, lambda x:None)
cv2.createTrackbar('Color_tres_R', 'Color Bars', 0,    255, lambda x:None)

cv2.createTrackbar('Color_cuatro_B', 'Color Bars', 255, 255, lambda x:None) # color 4
cv2.createTrackbar('Color_cuatro_G', 'Color Bars', 0, 255, lambda x:None)
cv2.createTrackbar('Color_cuatro_R', 'Color Bars', 0, 255, lambda x:None)

cv2.createTrackbar('Color_cinco_B', 'Color Bars', 255, 255, lambda x:None) # color 5
cv2.createTrackbar('Color_cinco_G', 'Color Bars', 0, 255, lambda x:None)
cv2.createTrackbar('Color_cinco_R', 'Color Bars', 255, 255, lambda x:None)

cv2.createTrackbar('Color_seis_B', 'Color Bars', 0, 255, lambda x:None) # color 6
cv2.createTrackbar('Color_seis_G', 'Color Bars', 165, 255, lambda x:None)
cv2.createTrackbar('Color_seis_R', 'Color Bars', 255, 255, lambda x:None)




cv2.createTrackbar('Greyscale', 'Sliders', 42, 255, lambda x:None)
cv2.createTrackbar('Greyscale_2', 'Sliders', 84, 255, lambda x:None)
cv2.createTrackbar('Greyscale_3', 'Sliders', 126, 255, lambda x:None)
cv2.createTrackbar('Greyscale_4', 'Sliders', 168, 255, lambda x:None)
cv2.createTrackbar('Greyscale_5', 'Sliders', 210, 255, lambda x:None)
cv2.createTrackbar('Greyscale_6', 'Sliders', 255, 255, lambda x:None)

cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)




keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
    grayscale_break = trackPosition('Greyscale', 'Sliders', 0, 42)
    grayscale_break_2 = trackPosition('Greyscale_2', 'Sliders', 43, 84)
    grayscale_break_3 = trackPosition('Greyscale_3', 'Sliders', 85, 126)
    grayscale_break_4 = trackPosition('Greyscale_4', 'Sliders',127, 168)
    grayscale_break_5 = trackPosition('Greyscale_5', 'Sliders', 169, 210)
    grayscale_break_6 = trackPosition('Greyscale_6', 'Sliders', 211, 255)
    #colors are defined here


    red_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color_uno_B', 'Color Bars'),cv2.getTrackbarPos('Color_uno_G', 'Color Bars'),cv2.getTrackbarPos('Color_uno_R', 'Color Bars')]
    yellow_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color_dos_B', 'Color Bars'),cv2.getTrackbarPos('Color_dos_G', 'Color Bars'),cv2.getTrackbarPos('Color_dos_R', 'Color Bars')]
    green_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color_tres_B', 'Color Bars'),cv2.getTrackbarPos('Color_tres_G', 'Color Bars'),cv2.getTrackbarPos('Color_tres_R', 'Color Bars')]
    blue_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color_cuatro_B', 'Color Bars'),cv2.getTrackbarPos('Color_cuatro_G', 'Color Bars'),cv2.getTrackbarPos('Color_cuatro_R', 'Color Bars')]
    purple_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color_cinco_B', 'Color Bars'),cv2.getTrackbarPos('Color_cinco_G', 'Color Bars'),cv2.getTrackbarPos('Color_cinco_R', 'Color Bars')]
    orange_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Color_seis_B', 'Color Bars'),cv2.getTrackbarPos('Color_seis_G', 'Color Bars'),cv2.getTrackbarPos('Color_seis_R', 'Color Bars')]




   
    min_grayscale_for_red = [0,0,0]
    max_grayscale_for_red = [grayscale_break,grayscale_break,grayscale_break]
   
    min_grayscale_for_yellow = [grayscale_break+1,grayscale_break+1,grayscale_break+1]
    max_grayscale_for_yellow = [grayscale_break_2,grayscale_break_2,grayscale_break_2]
   
    min_grayscale_for_blue = [grayscale_break_2+1,grayscale_break_2+1,grayscale_break_2+1]
    max_grayscale_for_blue = [grayscale_break_3,grayscale_break_3,grayscale_break_3]
   
    min_grayscale_for_green = [grayscale_break_3+1,grayscale_break_3+1,grayscale_break_3+1]
    max_grayscale_for_green = [grayscale_break_4,grayscale_break_4,grayscale_break_4]
   
    min_grayscale_for_purple = [grayscale_break_4+1,grayscale_break_4+1,grayscale_break_4+1]
    max_grayscale_for_purple = [grayscale_break_5,grayscale_break_5,grayscale_break_5]
   
    min_grayscale_for_orange = [grayscale_break_5+1,grayscale_break_5+1,grayscale_break_5+1]
    max_grayscale_for_orange = [grayscale_break_6,grayscale_break_6,grayscale_break_6]
   
   
   
    min_grayscale_for_red = numpy.array(min_grayscale_for_red, dtype = "uint8")
    max_grayscale_for_red = numpy.array(max_grayscale_for_red, dtype = "uint8")
   
    min_grayscale_for_yellow = numpy.array(min_grayscale_for_yellow,dtype = "uint8")
    max_grayscale_for_yellow = numpy.array(max_grayscale_for_yellow,dtype = "uint8")
   
    min_grayscale_for_blue = numpy.array(min_grayscale_for_blue, dtype = "uint8")
    max_grayscale_for_blue = numpy.array(max_grayscale_for_blue, dtype = "uint8")
   
    min_grayscale_for_green = numpy.array(min_grayscale_for_green, dtype = "uint8")
    max_grayscale_for_green = numpy.array(max_grayscale_for_green, dtype = "uint8")
   
    min_grayscale_for_purple = numpy.array(min_grayscale_for_purple, dtype = "uint8")
    max_grayscale_for_purple = numpy.array(max_grayscale_for_purple, dtype = "uint8")
   
    min_grayscale_for_orange = numpy.array(min_grayscale_for_orange, dtype = "uint8")
    max_grayscale_for_orange = numpy.array(max_grayscale_for_orange, dtype = "uint8")
   
    #chooses color
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
    block_all_but_the_orange_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_orange,
                                                 max_grayscale_for_orange)
    block_all_but_the_purple_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_purple,
                                                 max_grayscale_for_purple)

   
    red_parts_of_image = cv2.bitwise_or(red_paper, red_paper,
                                        mask = block_all_but_the_red_parts)
    yellow_parts_of_image = cv2.bitwise_or(yellow_paper, yellow_paper,
                                        mask = block_all_but_the_yellow_parts)
    blue_parts_of_image = cv2.bitwise_or(blue_paper, blue_paper,
                                        mask = block_all_but_the_blue_parts)
    green_parts_of_image = cv2.bitwise_or(green_paper, green_paper,
                                        mask = block_all_but_the_green_parts)
    orange_parts_of_image = cv2.bitwise_or(orange_paper, orange_paper,
                                        mask = block_all_but_the_orange_parts)
    purple_parts_of_image = cv2.bitwise_or(purple_paper, purple_paper,
                                        mask = block_all_but_the_purple_parts)
 
   
    customized_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, blue_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, green_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, purple_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, orange_parts_of_image)
   
    #used to display an image in a window, (name which is a string, variable)
    cv2.imshow('Red Parts of Image',red_parts_of_image)
    cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
    cv2.imshow('Blue Parts of Image',blue_parts_of_image)
    cv2.imshow('Green Parts of Image',green_parts_of_image)
    cv2.imshow('Purple Parts of Image',purple_parts_of_image)
    cv2.imshow('Orange Parts of Image',orange_parts_of_image)
    cv2.imshow('Customized Image',customized_image)
   
   
    keypressed = cv2.waitKey(1)
if keypressed == 27: # ESC to close all opened imaging windows
    cv2.destroyAllWindows()
elif keypressed == ord('s'): # user can press 's' to save their iamge, ln(220) retrieves customimage name, ln(222) retrieves grayscaleimage name
    name_of_file = input("What would you like to name this image? include the file type ex: .jpg, .jpeg, .png: ")
    str(name_of_file)
    gimage_name = input("What would you like to name the grayscale image? include the file type ex: .jpg, .jpeg, .png: ")
    cv2.imwrite(gimage_name,grayscale_image) #saves grayscaleimage file as the user given name
    cv2.imwrite(name_of_file ,customized_image) # saves customimage file as the user given name
    cv2.destroyAllWindows()
