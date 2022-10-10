# Images_01_Starting_Code
# Engineer Your World
#
# Things to do :)
#   [x] add 6 colors
#   [x] add sliders to the colors
#   [x] add sliders to the grey scale
#   [] comment new code
#   [x] minimise window and take out the rest 
#   [x] add new file name
#   [x] remove color association
#   [] add 10 more colors  
#   [] save colors
#   [x] resize windows

import cv2
import numpy
import os.path
#---------------------------------
#This code asks the user for what image they want to use. The user types in the image name along with .jpg and then the
    #program uses it. If the user types it in wrong the code sends an error message asking if you typed it in wrong. 

print ("Save your original image in the same folder as this program.") 
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")               
    if os.path.isfile(filename) == True:
        filename_valid = True                                                          
    else:
        print ("Something was wrong with that filename. Please try again.")  

#This next portion works with the image the user types in, reads the image, and turns it into a grayscale image. Then the code replaces
    #the grayscale image with BGR pixels so the image will have color

original_image = cv2.imread(filename,1)               
grayscale_image_simple = cv2.imread(filename, 0) 
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)


#-----------------------
#This portion creates and names windows 
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Color Sliders') 


#-------------------------
#resizing the grayscale slide bar window
cv2.resizeWindow('Color Sliders' , 1000, 1000) 
cv2.resizeWindow('Customized Image' , 200, 200)
#-------------------------
#This part of the code sets the initial value on the side bars in a such a way so that the final
    #custom image starts in a rainbow configuration. The user can change these color values on the slide bars that pop up. 
#red c1         
a=0 
b=0
c=255
#orange c2
d=3
e=152
f=252
#yellow c3
g=0
h=255
i=255
#green c4
j=0
k=255
l=0
#blue c5
m=255
n=0
o=0
#purple c6 
p=245
q=66
r=185
#pink c7 
s= 227
t= 66
u= 245


#-------------------------
#These lines of code create trackbars for the grayscale as well as each color. The user is able to manipulate these sliders
    #due to later lines of code.

#grayscale 
cv2.createTrackbar("trackbar1","Customized Image", 255, 255, lambda x: None)
#red c1
cv2.createTrackbar("B1", "Color Sliders", a, 255, lambda x: None)                     #creates trackbars for the 6 colors ("c" stands for color)
cv2.createTrackbar("G1", "Color Sliders", b, 255, lambda x: None)
cv2.createTrackbar("R1", "Color Sliders", c, 255, lambda x: None)
#orange c2
cv2.createTrackbar("B2", "Color Sliders", d, 255, lambda x: None)                    
cv2.createTrackbar("G2", "Color Sliders", e, 255, lambda x: None)
cv2.createTrackbar("R2", "Color Sliders", f, 255, lambda x: None)
#yellow c3
cv2.createTrackbar("B3", "Color Sliders", g, 255, lambda x: None)                    
cv2.createTrackbar("G3", "Color Sliders", h, 255, lambda x: None)
cv2.createTrackbar("R3", "Color Sliders", i, 255, lambda x: None)
#green c4
cv2.createTrackbar("B4", "Color Sliders", j, 255, lambda x: None)                    
cv2.createTrackbar("G4", "Color Sliders", k, 255, lambda x: None)
cv2.createTrackbar("R4", "Color Sliders", l, 255, lambda x: None)
#blue c5
cv2.createTrackbar("B5", "Color Sliders", m, 255, lambda x: None)                    
cv2.createTrackbar("G5", "Color Sliders", n, 255, lambda x: None)
cv2.createTrackbar("R5", "Color Sliders", o, 255, lambda x: None)
#purple c6
cv2.createTrackbar("B6", "Color Sliders", p, 255, lambda x: None)                    
cv2.createTrackbar("G6", "Color Sliders", q, 255, lambda x: None)
cv2.createTrackbar("R6", "Color Sliders", r, 255, lambda x: None)
#pink c7
cv2.createTrackbar("B7", "Color Sliders", s, 255, lambda x: None)                    
cv2.createTrackbar("G7", "Color Sliders", t, 255, lambda x: None)
cv2.createTrackbar("R7", "Color Sliders", u, 255, lambda x: None)


#---------------------
#helps reformat the image
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]


#----------------------------
#this next portion starts a loop so that the user can see the colors and grayscale update in real time
keypressed = 0
while keypressed != 27 and keypressed != ord('s') :
    
    #This aggigns names to the color so that it can be called upon later 
    c1_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    c2_paper = numpy.zeros((image_height,image_width,image_channels),
                               numpy.uint8)
    c3_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    c4_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    c5_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    c6_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    c7_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    
    #this code achually finds the track bars so you can change each individual color value 
    cv2.getTrackbarPos("B1", "Color Sliders")  
    cv2.getTrackbarPos("G1", "Color Sliders")
    cv2.getTrackbarPos("R1", "Color Sliders")
    
    cv2.getTrackbarPos("B2", "Color Sliders")
    cv2.getTrackbarPos("G2", "Color Sliders")
    cv2.getTrackbarPos("R2", "Color Sliders")
    
    cv2.getTrackbarPos("B3", "Color Sliders")
    cv2.getTrackbarPos("G3", "Color Sliders")
    cv2.getTrackbarPos("R3", "Color Sliders")
    
    cv2.getTrackbarPos("B4", "Color Sliders")
    cv2.getTrackbarPos("G4", "Color Sliders")
    cv2.getTrackbarPos("R4", "Color Sliders")
    
    cv2.getTrackbarPos("B5", "Color Sliders")
    cv2.getTrackbarPos("G5", "Color Sliders")
    cv2.getTrackbarPos("R5", "Color Sliders")
    
    cv2.getTrackbarPos("B6", "Color Sliders")
    cv2.getTrackbarPos("G6", "Color Sliders")
    cv2.getTrackbarPos("R6", "Color Sliders")
    
    cv2.getTrackbarPos("B7", "Color Sliders")
    cv2.getTrackbarPos("G7", "Color Sliders")
    cv2.getTrackbarPos("R7", "Color Sliders")
    
    #assigns the color papers to 3 BGR (Blue, Green, Red) values 
    c1_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos("B1", "Color Sliders"), cv2.getTrackbarPos("G1", "Color Sliders"), cv2.getTrackbarPos("R1", "Color Sliders")]  
    c2_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos("B2", "Color Sliders"), cv2.getTrackbarPos("G2", "Color Sliders"), cv2.getTrackbarPos("R2", "Color Sliders")]
    c3_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos("B3", "Color Sliders"), cv2.getTrackbarPos("G3", "Color Sliders"), cv2.getTrackbarPos("R3", "Color Sliders")]
    c4_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos("B4", "Color Sliders"), cv2.getTrackbarPos("G4", "Color Sliders"), cv2.getTrackbarPos("R4", "Color Sliders")]
    c5_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos("B5", "Color Sliders"), cv2.getTrackbarPos("G5", "Color Sliders"), cv2.getTrackbarPos("R5", "Color Sliders")]
    c6_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos("B6", "Color Sliders"), cv2.getTrackbarPos("G6", "Color Sliders"), cv2.getTrackbarPos("R6", "Color Sliders")]
    c7_paper[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos("B7", "Color Sliders"), cv2.getTrackbarPos("G7", "Color Sliders"), cv2.getTrackbarPos("R7", "Color Sliders")] 
    
    #this breaks up the gray values and assigns them a name so it can be assigned a specific color later
    grayscale_break = cv2.getTrackbarPos("trackbar1", "Customized Image") /7
    grayscale_break1 = grayscale_break*2
    grayscale_break2 = grayscale_break*3
    grayscale_break3 = grayscale_break*4
    grayscale_break4 = grayscale_break*5
    grayscale_break5 = grayscale_break*6
    grayscale_break6 = grayscale_break*7
    
    #This gives each color a maximum and minimum gray value so that the colors do not overlap later. 
    min_grayscale_for_c1 = [0,0,0]
    max_grayscale_for_c1 = [grayscale_break,grayscale_break,grayscale_break] 
    min_grayscale_for_c2 = [grayscale_break+1,grayscale_break+1, 
                                grayscale_break+1]
    max_grayscale_for_c2 = [grayscale_break1,grayscale_break1,grayscale_break1] 
    min_grayscale_for_c3 = [grayscale_break1+1,grayscale_break1+1,grayscale_break1+1]
    max_grayscale_for_c3 = [grayscale_break2,grayscale_break2,grayscale_break2]
    min_grayscale_for_c4 = [grayscale_break2+1, grayscale_break2+1, grayscale_break2+1]
    max_grayscale_for_c4 = [grayscale_break3, grayscale_break3,grayscale_break3]
    min_grayscale_for_c5 = [grayscale_break3+1, grayscale_break3+1, grayscale_break3+1]
    max_grayscale_for_c5 = [grayscale_break4, grayscale_break4,grayscale_break4]
    min_grayscale_for_c6 = [grayscale_break4+1, grayscale_break4+1, grayscale_break4+1]
    max_grayscale_for_c6 = [grayscale_break5, grayscale_break5, grayscale_break5]
    min_grayscale_for_c7 = [grayscale_break5+1, grayscale_break5+1,grayscale_break5+1]
    max_grayscale_for_c7 = [255, 255, 255]  #last value is 255 so that the last color goes all the way to the max scale value

    #this reformats the code above so it works properly (changes it from [x x x] to [x,x,x]
    min_grayscale_for_c1 = numpy.array(min_grayscale_for_c1, dtype = "uint8")
    max_grayscale_for_c1 = numpy.array(max_grayscale_for_c1, dtype = "uint8")
    min_grayscale_for_c2 = numpy.array(min_grayscale_for_c2,
                                           dtype = "uint8")
    max_grayscale_for_c2 = numpy.array(max_grayscale_for_c2,
                                           dtype = "uint8")
    min_grayscale_for_c3 = numpy.array(min_grayscale_for_c3, dtype = "uint8")
    max_grayscale_for_c3 = numpy.array(max_grayscale_for_c3, dtype = "uint8")
    min_grayscale_for_c4 = numpy.array(min_grayscale_for_c4, dtype = "uint8")
    max_grayscale_for_c4 = numpy.array(max_grayscale_for_c4, dtype = "uint8")
    min_grayscale_for_c5 = numpy.array(min_grayscale_for_c5, dtype = "uint8")
    max_grayscale_for_c5 = numpy.array(max_grayscale_for_c5, dtype = "uint8")
    min_grayscale_for_c6 = numpy.array(min_grayscale_for_c6, dtype = "uint8")
    max_grayscale_for_c6 = numpy.array(max_grayscale_for_c6, dtype = "uint8")
    min_grayscale_for_c7 = numpy.array(min_grayscale_for_c7, dtype = "uint8")
    max_grayscale_for_c7 = numpy.array(max_grayscale_for_c7, dtype = "uint8")
    
    #this adds the color to the max and min grayscale values 
    block_all_but_the_c1_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_c1,
                                              max_grayscale_for_c1)
    block_all_but_the_c2_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_c2,
                                                 max_grayscale_for_c2)
    block_all_but_the_c3_parts = cv2.inRange(grayscale_image,
                                                min_grayscale_for_c3,
                                                max_grayscale_for_c3)
    block_all_but_the_c4_parts = cv2.inRange(grayscale_image,
                                                min_grayscale_for_c4,
                                                max_grayscale_for_c4)
    block_all_but_the_c5_parts = cv2.inRange(grayscale_image,
                                                min_grayscale_for_c5,
                                                max_grayscale_for_c5)
    block_all_but_the_c6_parts = cv2.inRange(grayscale_image,
                                                min_grayscale_for_c6,
                                                max_grayscale_for_c6)
    block_all_but_the_c7_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_c7,
                                                 max_grayscale_for_c7)

    #Makes the image look like only one of the colors with all other space being black. 
    c1_parts_of_image = cv2.bitwise_or(c1_paper, c1_paper,
                                        mask = block_all_but_the_c1_parts)
    c2_parts_of_image = cv2.bitwise_or(c2_paper, c2_paper,
                                           mask = block_all_but_the_c2_parts)
    c3_parts_of_image = cv2.bitwise_or(c3_paper, c3_paper,
                                          mask = block_all_but_the_c3_parts)
    c4_parts_of_image = cv2.bitwise_or(c4_paper, c4_paper,
                                          mask = block_all_but_the_c4_parts)
    c5_parts_of_image = cv2.bitwise_or(c5_paper, c5_paper,
                                          mask = block_all_but_the_c5_parts)
    c6_parts_of_image = cv2.bitwise_or(c6_paper, c6_paper,
                                          mask = block_all_but_the_c6_parts)
    c7_parts_of_image = cv2.bitwise_or(c7_paper, c7_paper,
                                           mask = block_all_but_the_c7_parts)


    #Puts the colores images with the black space together to make one colorful image. 
    customized_image = cv2.bitwise_or(c1_parts_of_image, c2_parts_of_image)
    final_custom_image1 = cv2.bitwise_or(customized_image, c3_parts_of_image)
    final_custom_image2 = cv2.bitwise_or(final_custom_image1, c4_parts_of_image)
    final_custom_image3 = cv2.bitwise_or(final_custom_image2, c5_parts_of_image)
    final_custom_image4 = cv2.bitwise_or(final_custom_image3, c6_parts_of_image)
    final_custom_image = cv2.bitwise_or(final_custom_image4, c7_parts_of_image) 

    
    #Shows the desired images 
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Grayscale Image',grayscale_image)
    cv2.imshow('Customized Image',final_custom_image)
    
    #------------------------
    #saves or DESTROYS the final colored image as well as the grayscale image. 
    keypressed = cv2.waitKey(30)  
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'):
    greyimg = input ("What do you want your gray scale image to be named? ") #asks to save the grey scale picture 
    colorimg = input ("What do you want your color image to be named? ") #asks to save the final color image 
    cv2.imwrite(greyimg + '.jpg' ,grayscale_image)
    cv2.imwrite(colorimg + '.jpg' ,final_custom_image)
    cv2.destroyAllWindows()
