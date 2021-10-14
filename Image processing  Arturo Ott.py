# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path
import random


print ("Save your original image in the same folder as this program.")
filename_valid = False

# Ask for name of file with the file extension
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")


# Create function that sets a minimum and maximum value to the trackbar
def newTrackbarPos(tbarName, tbarWin, minValue, maxValue):
    currentPos = cv2.getTrackbarPos(tbarName, tbarWin)
    if currentPos < minValue:
        cv2.setTrackbarPos(tbarName, tbarWin, minValue)
        print('Too low')
        return minValue
    elif currentPos > maxValue:
        cv2.setTrackbarPos(tbarName, tbarWin, maxValue)
        print('Too High')
        return maxValue
    else:
        return currentPos
    


# Read the image and set to grayscale
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

# cv2.namedWindow('Original Image')
# cv2.namedWindow('Grayscale Image')
# cv2.namedWindow('Red Parts of Image')
# cv2.namedWindow('Yellow Parts of Image')
# cv2.namedWindow('Customized Image')

# Create window named Image
cv2.namedWindow('Image')
# cv2.namedWindow('Slider')

# Set the image height and width
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]


# Create a paper for each color
red_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
yellow_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
blue_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
green_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
black_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
pink_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
white_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

# Set the height and width of each paper
# Set the BGR value for the color
red_paper[0:image_height,0:image_width, 0:image_channels] = [0,0,255]
yellow_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
blue_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,0]
green_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,0]
black_paper[0:image_height,0:image_width, 0:image_channels] = [0,0,0]
pink_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,255]
white_paper[0:image_height,0:image_width, 0:image_channels] = [255,255,255]

# Crate a trackbar for each color
cv2.createTrackbar('Grayscale', 'Image', 127, 254, lambda x:None)
cv2.createTrackbar('Bluescale', 'Image', 127, 254, lambda x:None)
cv2.createTrackbar('Greenscale', 'Image', 127, 254, lambda x:None)
cv2.createTrackbar('Blackscale', 'Image', 127, 254, lambda x:None)
cv2.createTrackbar('Pinkscale', 'Image', 127, 254, lambda x:None)
cv2.createTrackbar('Whitescale', 'Image', 127, 254, lambda x:None)

#cv2.imshow('Original Image', original_image)
#cv2.imshow('Grayscale Image',grayscale_image)



# While loop does not break unless 'esc' key or 's' key pressed
keypressed = 1

while (keypressed != 27 and keypressed != ord('s')):
    # Create variable for the trackbar position for each trackbar
    # Set minimum and maximum valuesfor trackbar position
    grayscale_break = newTrackbarPos('Grayscale', 'Image', 0, 45)
    bluescale_break = newTrackbarPos('Bluescale', 'Image', 45, 90)
    greenscale_break = newTrackbarPos('Greenscale', "Image", 90, 135)
    blackscale_break = newTrackbarPos('Blackscale', 'Image', 135, 180)
    pinkscale_break = newTrackbarPos('Pinkscale', 'Image', 180, 225)
    whitescale_break = newTrackbarPos('Whitescale', 'Image', 225, 255)
    
    # Set the minimum and maximum BGR value for each color
    min_grayscale_for_red = [0,0,0]
    max_grayscale_for_red = [grayscale_break,grayscale_break,grayscale_break]
    min_grayscale_for_yellow = [grayscale_break+1,grayscale_break+1, 
                                grayscale_break+1]
    max_grayscale_for_yellow = [bluescale_break,bluescale_break,bluescale_break]
    
    min_grayscale_for_blue = [bluescale_break+1, bluescale_break+1, bluescale_break+1]
    max_grayscale_for_blue = [greenscale_break, greenscale_break, greenscale_break]
    
    min_grayscale_for_green = [greenscale_break+1, greenscale_break+1, greenscale_break+1]
    max_grayscale_for_green = [blackscale_break, blackscale_break, blackscale_break]
    
    min_grayscale_for_black = [blackscale_break+1, blackscale_break+1, blackscale_break+1]
    max_grayscale_for_black = [pinkscale_break,pinkscale_break,pinkscale_break]
    
    min_grayscale_for_pink = [pinkscale_break+1, pinkscale_break+1, pinkscale_break+1]
    max_grayscale_for_pink = [whitescale_break,whitescale_break,whitescale_break]
    
    min_grayscale_for_white = [whitescale_break+1, whitescale_break+1, whitescale_break+1]
    max_grayscale_for_white = [255,255,255]
    
    
    # Formats data correctly
    min_grayscale_for_red = numpy.array(min_grayscale_for_red, dtype = "uint8")
    max_grayscale_for_red = numpy.array(max_grayscale_for_red, dtype = "uint8")
    
    min_grayscale_for_yellow = numpy.array(min_grayscale_for_yellow,
                                           dtype = "uint8")
    max_grayscale_for_yellow = numpy.array(max_grayscale_for_yellow,
                                           dtype = "uint8")
    
    min_grayscale_for_blue = numpy.array(min_grayscale_for_blue, dtype = "uint8")
    max_grayscale_for_blue = numpy.array(max_grayscale_for_blue, dtype = "uint8")
    
    min_grayscale_for_green = numpy.array(min_grayscale_for_green, dtype = "uint8")
    max_grayscale_for_green = numpy.array(max_grayscale_for_green, dtype = "uint8")
    
    min_grayscale_for_black = numpy.array(min_grayscale_for_black, dtype = "uint8")
    max_grayscale_for_black = numpy.array(max_grayscale_for_black, dtype = "uint8")
    
    min_grayscale_for_pink = numpy.array(min_grayscale_for_pink, dtype = "uint8")
    max_grayscale_for_pink = numpy.array(max_grayscale_for_pink, dtype = "uint8")
    
    min_grayscale_for_white = numpy.array(min_grayscale_for_white, dtype = "uint8")
    max_grayscale_for_white = numpy.array(max_grayscale_for_white, dtype = "uint8")
    
    
    # Creates a paper with only one color
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
    block_all_but_the_black_parts = cv2.inRange(grayscale_image,
                                                min_grayscale_for_black,
                                                max_grayscale_for_black)
    block_all_but_the_pink_parts = cv2.inRange(grayscale_image,
                                               min_grayscale_for_pink,
                                               max_grayscale_for_pink)
    block_all_but_the_white_parts = cv2.inRange(grayscale_image,
                                                min_grayscale_for_white,
                                                max_grayscale_for_white)
    
    red_parts_of_image = cv2.bitwise_or(red_paper, red_paper,
                                        mask = block_all_but_the_red_parts)
    yellow_parts_of_image = cv2.bitwise_or(yellow_paper, yellow_paper,
                                           mask = block_all_but_the_yellow_parts)
    blue_parts_of_image = cv2.bitwise_or(blue_paper, blue_paper, mask = block_all_but_the_blue_parts)
    green_parts_of_image = cv2.bitwise_or(green_paper, green_paper, mask = block_all_but_the_green_parts)
    black_parts_of_image = cv2.bitwise_or(black_paper, black_paper, mask = block_all_but_the_black_parts)
    pink_parts_of_image = cv2.bitwise_or(pink_paper, pink_paper, mask = block_all_but_the_pink_parts)
    white_parts_of_image = cv2.bitwise_or(white_paper, white_paper, mask = block_all_but_the_white_parts)
    
    
    # Combine all of the papers to form one image
    customized_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, blue_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, green_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, black_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, pink_parts_of_image)
    customized_image1 = cv2.bitwise_or(customized_image, white_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, customized_image1)



    # cv2.imshow('Red Parts of Image',red_parts_of_image)
    # cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
    

    # Combine the original image, customized image, and sliders in one window
    horizontal = numpy.concatenate((original_image, customized_image), axis=1)
    
    # Show the one image window
    cv2.imshow('Image', horizontal)
    
    #print(original_image)
    
    keypressed = cv2.waitKey(1)
    
    # If 'r' key pressed then reset all values to the middle
    # If '/' key pressed the set all trackbars to a random position within the range set
    if keypressed == ord('r'):
        cv2.setTrackbarPos('Grayscale', 'Image', 127)
        cv2.setTrackbarPos('Bluescale', 'Image', 127)
        cv2.setTrackbarPos('Greenscale', 'Image', 127)
        cv2.setTrackbarPos('Blackscale', 'Image', 127)
        cv2.setTrackbarPos('Pinkscale', 'Image', 127)
        cv2.setTrackbarPos('Whitescale', 'Image', 127)
    elif keypressed == ord('/'):
        cv2.setTrackbarPos('Grayscale', 'Image', random.randint(0, 45))
        cv2.setTrackbarPos('Bluescale', 'Image', random.randint(45, 90))
        cv2.setTrackbarPos('Greenscale', 'Image', random.randint(90, 135))
        cv2.setTrackbarPos('Blackscale', 'Image', random.randint(135, 180))
        cv2.setTrackbarPos('Pinkscale', 'Image', random.randint(180, 225))
        cv2.setTrackbarPos('Whitescale', 'Image', random.randint(225, 255))        
    
        
if keypressed == 27:
     cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    # cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()

