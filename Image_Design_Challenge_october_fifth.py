#Turns the whole code into a function so that I can use the entire script in the main code
def functionOne():
    
    import cv2
    import numpy
    import os.path 

#A function that detects where the postion in the trackbar is
    def trackPosition(slider_name, window_name, min_val):
        current_pos = cv2.getTrackbarPos(slider_name, window_name)
        if current_pos < min_val:
            print(slider_name, 'is Too Low!')
            cv2.setTrackbarPos(slider_name, window_name, min_val)
            return min_val
        else:
            return current_pos
        
#Asks the user what their photo name is
    print ("Save your original image in the same folder as this program.")
    filename_valid = False
    while filename_valid == False:
        filename = input("Enter the name of your file, including the extension, and then press 'enter': ")
        if os.path.isfile(filename) == True:
            filename_valid = True
        else:
            print ("Something was wrong with that filename. Please try again.")
    
    
    original_image = cv2.imread(filename,1)
    grayscale_image_simple = cv2.imread(filename, 0)
    grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)
    

    cv2.namedWindow('Slider')
    
    image_height = original_image.shape[0] 
    image_width = original_image.shape[1]
    image_channels = original_image.shape[2]  
    
    red_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    yellow_paper = numpy.zeros((image_height,image_width,image_channels),
                               numpy.uint8)
    blue_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    lime_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    purple_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    green_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    pink_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    
    
    #Sets the values for each color the image will use
    #Written in B,G,R
    red_paper[0:image_height,0:image_width, 0:image_channels] = [0,0,255]
    yellow_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
    blue_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,0]
    lime_paper[0:image_height,0:image_width, 0:image_channels] = [33,229,200]
    purple_paper[0:image_height,0:image_width, 0:image_channels] = [255,51,153]
    green_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,0]
    pink_paper[0:image_height,0:image_width, 0:image_channels] = [147,20,255]
    
    
    
    
    #Creates a trackbar to change the hue for each color value
    cv2.createTrackbar('Red/Blue', 'Slider', 80 , 255, lambda x:None)
    cv2.createTrackbar('Blue/Lime', 'Slider', 90 , 255, lambda x:None)
    cv2.createTrackbar('Lime/Purple', 'Slider', 100 , 255, lambda x:None)
    cv2.createTrackbar('Purple/Green', 'Slider', 110 , 255, lambda x:None)
    cv2.createTrackbar('Green/Pink', 'Slider', 120 , 255, lambda x:None)
    cv2.createTrackbar('Pink/Yellow', 'Slider', 130 , 255, lambda x:None)
    
    
    
    keypressed = 1
    while (keypressed != 27 and keypressed != ord('s')):
        grayscale_break = trackPosition('Red/Blue', 'Sliders', 70)
        grayscale_break_2 = trackPosition('Blue/Lime', 'Slider', 80)
        grayscale_break_3 = trackPosition('Lime/Purple', 'Slider', 90)
        grayscale_break_4 = trackPosition('Purple/Green', 'Slider', 100)
        grayscale_break_5 = trackPosition('Green/Pink', 'Slider', 110)
        grayscale_break_6 = trackPosition('Pink/Yellow', 'Slider', 120)
    
    
        
        min_grayscale_for_red = [0,0,0]
        max_grayscale_for_red = [grayscale_break,grayscale_break,grayscale_break]
        min_grayscale_for_blue = [grayscale_break+1,grayscale_break+1,grayscale_break+1]
        max_grayscale_for_blue = [grayscale_break_2,grayscale_break_2, 
                                    grayscale_break_2]
        min_grayscale_for_lime = [grayscale_break_2+1,grayscale_break_2+1,grayscale_break_2+1]
        max_grayscale_for_lime = [grayscale_break_3,grayscale_break_3, 
                                    grayscale_break_3]
        min_grayscale_for_purple = [grayscale_break_3+1,grayscale_break_3+1,grayscale_break_3+1]
        max_grayscale_for_purple = [grayscale_break_4,grayscale_break_4, 
                                    grayscale_break_4]
        min_grayscale_for_green = [grayscale_break_4+1,grayscale_break_4+1,grayscale_break_4+1]
        max_grayscale_for_green = [grayscale_break_5,grayscale_break_5, 
                                    grayscale_break_5]
        min_grayscale_for_pink = [grayscale_break_5+1,grayscale_break_5+1,grayscale_break_5+1]
        max_grayscale_for_pink = [grayscale_break_6,grayscale_break_6, 
                                    grayscale_break_6]
        min_grayscale_for_yellow = [grayscale_break_6+1,grayscale_break_6+1, 
                                    grayscale_break_6+1]
        max_grayscale_for_yellow = [255,255,255]
        
        min_grayscale_for_red = numpy.array(min_grayscale_for_red, dtype = "uint8")
        max_grayscale_for_red = numpy.array(max_grayscale_for_red, dtype = "uint8")
        min_grayscale_for_blue = numpy.array(min_grayscale_for_blue, dtype = "uint8")
        max_grayscale_for_blue = numpy.array(max_grayscale_for_blue, dtype = "uint8")
        min_grayscale_for_lime = numpy.array(min_grayscale_for_lime, dtype = "uint8")
        max_grayscale_for_lime = numpy.array(max_grayscale_for_lime, dtype = "uint8")
        min_grayscale_for_purple = numpy.array(min_grayscale_for_purple, dtype = "uint8")
        max_grayscale_for_purple = numpy.array(max_grayscale_for_purple, dtype = "uint8")
        min_grayscale_for_green = numpy.array(min_grayscale_for_green, dtype = "uint8")
        max_grayscale_for_green = numpy.array(max_grayscale_for_green, dtype = "uint8")
        min_grayscale_for_pink = numpy.array(min_grayscale_for_pink, dtype = "uint8")
        max_grayscale_for_pink = numpy.array(max_grayscale_for_pink, dtype = "uint8")
        min_grayscale_for_yellow = numpy.array(min_grayscale_for_yellow,
                                               dtype = "uint8")
        max_grayscale_for_yellow = numpy.array(max_grayscale_for_yellow,
                                               dtype = "uint8")
        
        
        block_all_but_the_red_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_red,
                                                  max_grayscale_for_red)
        block_all_but_the_blue_parts = cv2.inRange(grayscale_image,
                                                     min_grayscale_for_blue,
                                                     max_grayscale_for_blue)
        block_all_but_the_lime_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_lime,
                                                  max_grayscale_for_lime)
        block_all_but_the_purple_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_purple,
                                                  max_grayscale_for_purple)
        block_all_but_the_green_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_green,
                                                  max_grayscale_for_green)
        block_all_but_the_pink_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_pink,
                                                  max_grayscale_for_pink)
        block_all_but_the_yellow_parts = cv2.inRange(grayscale_image,
                                                     min_grayscale_for_yellow,
                                                     max_grayscale_for_yellow)
        
        red_parts_of_image = cv2.bitwise_or(red_paper, red_paper,
                                            mask = block_all_but_the_red_parts)
        blue_parts_of_image = cv2.bitwise_or(blue_paper, blue_paper,
                                            mask = block_all_but_the_blue_parts)
        lime_parts_of_image = cv2.bitwise_or(lime_paper, lime_paper,
                                            mask = block_all_but_the_lime_parts)
        purple_parts_of_image = cv2.bitwise_or(purple_paper, purple_paper,
                                            mask = block_all_but_the_purple_parts)
        green_parts_of_image = cv2.bitwise_or(green_paper, green_paper,
                                            mask = block_all_but_the_green_parts)
        pink_parts_of_image = cv2.bitwise_or(pink_paper, pink_paper,
                                            mask = block_all_but_the_pink_parts)
        yellow_parts_of_image = cv2.bitwise_or(yellow_paper, yellow_paper,
                                               mask = block_all_but_the_yellow_parts)
        
        customized_image = cv2.bitwise_or(red_parts_of_image, blue_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, yellow_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, lime_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, purple_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, green_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, pink_parts_of_image)
    
    
        #displays four windows into one a horizontal window stack
        numpy_horizontal = numpy.hstack((red_parts_of_image, green_parts_of_image , blue_parts_of_image, lime_parts_of_image ))
        numpy_horizontal_2 = numpy.hstack((green_parts_of_image , yellow_parts_of_image , purple_parts_of_image, pink_parts_of_image ))
        numpy_horizontal_3 = numpy.hstack((original_image , grayscale_image , customized_image ))
    
    
    
        cv2.imshow('Colored Parts', numpy_horizontal)
        cv2.imshow('Colored Parts 2', numpy_horizontal_2)
        cv2.imshow('Orignal, Grayscale, and Custom', numpy_horizontal_3)
                
        keypressed = cv2.waitKey(1)
        
    #If esc is pressed, it destorys all the windows, and if "s" is pressed, it saved the custom image
    if keypressed == 27:
        cv2.destroyAllWindows()
    elif keypressed == ord('s'): 
        cv2.imwrite('photo_GS_1.jpg',grayscale_image)
        cv2.imwrite('photo_RY_1.jpg',customized_image)
        cv2.destroyAllWindows()


