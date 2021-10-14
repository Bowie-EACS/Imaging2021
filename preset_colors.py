#Tyler Harrison period 8

def preset_colors():

    import cv2
    import numpy
    import os.path
    
    
    def trackPosition(slider_name, window_name, min_val):
        current_pos = cv2.getTrackbarPos(slider_name, window_name)
        if current_pos < min_val:
            print("Hey. That's too low")
            cv2.setTrackbarPos(slider_name, window_name, min_val)
            return min_val
        else:
            return current_pos
    
    #asks user for the name of what the picture is saved as
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
    
    #Sets the name for the windows
    cv2.namedWindow('Original Image')
    cv2.namedWindow('Grayscale Image')
    cv2.namedWindow('Red Parts of Image')
    cv2.namedWindow('Yellow Parts of Image')
    cv2.namedWindow('Green Parts of Image')
    cv2.namedWindow('Blue Parts of Image')
    cv2.namedWindow('Neon Purple Parts of Image')
    cv2.namedWindow('Orange Parts of Image')
    cv2.namedWindow('Cyan Parts of Image')
    cv2.namedWindow('Pink Parts of Image')
    cv2.namedWindow('Customized Image')
    cv2.namedWindow('Sliders_5')
    
    image_height = original_image.shape[0]
    image_width = original_image.shape[1]
    image_channels = original_image.shape[2]
    
    red_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    yellow_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    blue_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    green_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    orange_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    neon_purple_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    cyan_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    pink_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    
    #sets the BGR values for the colors
    red_paper[0:image_height,0:image_width, 0:image_channels] = [0,0,255]
    yellow_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
    blue_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,0]
    green_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,0]
    orange_paper[0:image_height,0:image_width, 0:image_channels] = [0,165,255]
    neon_purple_paper[0:image_height,0:image_width, 0:image_channels] = [255,38,176]
    cyan_paper[0:image_height,0:image_width, 0:image_channels] = [255, 255, 0]
    pink_paper[0:image_height,0:image_width, 0:image_channels] = [203, 192, 255]
    
    #creates the trackbars for the colors
    cv2.createTrackbar('Grayscale', 'Sliders_5', 100, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_2', 'Sliders_5', 150, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_3', 'Sliders_5', 160, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_4', 'Sliders_5', 170, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_5', 'Sliders_5', 180, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_6', 'Sliders_5', 190, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_7', 'Sliders_5', 200, 255, lambda x:None)
    
    #displays the original image and grayscale image outside of the loop
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Grayscale Image',grayscale_image)
    
    #Loops code so slider can work
    keypressed = 1
    while (keypressed != 27 and keypressed != ord('s')):
        #sets tranbar position and gives it a minimum value
        grayscale_break = trackPosition('Grayscale', 'Sliders_5', 50)
        grayscale_break_2 = trackPosition('Grayscale_2', 'Sliders_5', 55)
        grayscale_break_3 = trackPosition('Grayscale_3', 'Sliders_5', 65)
        grayscale_break_4 = trackPosition('Grayscale_4', 'Sliders_5', 70)
        grayscale_break_5 = trackPosition('Grayscale_5', 'Sliders_5', 75)
        grayscale_break_6 = trackPosition('Grayscale_6', 'Sliders_5', 80)
        grayscale_break_7 = trackPosition('Grayscale_7', 'Sliders_5', 85)
        
        #sets the minimum and max values for the BGR of the colors
        min_grayscale_for_red = [0,0,0]
        max_grayscale_for_red = [grayscale_break,grayscale_break,grayscale_break]
        min_grayscale_for_blue = [grayscale_break+1, grayscale_break+1, grayscale_break+1]
        max_grayscale_for_blue = [grayscale_break_2,grayscale_break_2,grayscale_break_2]
        min_grayscale_for_green = [grayscale_break_2+1, grayscale_break_2+1, grayscale_break_2+1]
        max_grayscale_for_green = [grayscale_break_3 ,grayscale_break_3,grayscale_break_3]
        min_grayscale_for_orange = [grayscale_break_3+1, grayscale_break_3+1, grayscale_break_3+1]
        max_grayscale_for_orange = [grayscale_break_4 ,grayscale_break_4,grayscale_break_4]
        min_grayscale_for_neon_purple = [grayscale_break_4+1, grayscale_break_4+1, grayscale_break_4+1]
        max_grayscale_for_neon_purple = [grayscale_break_5, grayscale_break_5, grayscale_break_5]
        min_grayscale_for_cyan = [grayscale_break_5+1, grayscale_break_5+1, grayscale_break_5+1]
        max_grayscale_for_cyan = [grayscale_break_6, grayscale_break_6, grayscale_break_6]
        min_grayscale_for_pink = [grayscale_break_6+1, grayscale_break_6+1, grayscale_break_6+1]
        max_grayscale_for_pink = [grayscale_break_7, grayscale_break_7, grayscale_break_7]
        min_grayscale_for_yellow = [grayscale_break_7+1, grayscale_break_7+1, grayscale_break_7+1]
        max_grayscale_for_yellow = [255,255,255]
        
        min_grayscale_for_red = numpy.array(min_grayscale_for_red, dtype = "uint8")
        max_grayscale_for_red = numpy.array(max_grayscale_for_red, dtype = "uint8")
        min_grayscale_for_yellow = numpy.array(min_grayscale_for_yellow,dtype = "uint8")
        max_grayscale_for_yellow = numpy.array(max_grayscale_for_yellow,dtype = "uint8")
        min_grayscale_for_blue = numpy.array(min_grayscale_for_blue, dtype = "uint8")
        max_grayscale_for_blue = numpy.array(max_grayscale_for_blue, dtype = "uint8")
        min_grayscale_for_green = numpy.array(min_grayscale_for_green, dtype = "uint8")
        max_grayscale_for_green = numpy.array(max_grayscale_for_green, dtype = "uint8")
        min_grayscale_for_orange = numpy.array(min_grayscale_for_orange, dtype = "uint8")
        max_grayscale_for_orange = numpy.array(max_grayscale_for_orange, dtype = "uint8")
        min_grayscale_for_neon_purple = numpy.array(min_grayscale_for_neon_purple, dtype = "uint8")
        max_grayscale_for_neon_purple = numpy.array(max_grayscale_for_neon_purple, dtype = "uint8")
        min_grayscale_for_cyan = numpy.array(min_grayscale_for_cyan, dtype = "uint8")
        max_grayscale_for_cyan = numpy.array(max_grayscale_for_cyan, dtype = "uint8")
        min_grayscale_for_pink = numpy.array(min_grayscale_for_pink, dtype = "uint8")
        max_grayscale_for_pink = numpy.array(max_grayscale_for_pink, dtype = "uint8")
        
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
        block_all_but_the_neon_purple_parts = cv2.inRange(grayscale_image,
                                                     min_grayscale_for_neon_purple,
                                                     max_grayscale_for_neon_purple)
        block_all_but_the_cyan_parts = cv2.inRange(grayscale_image,
                                                     min_grayscale_for_cyan,
                                                     max_grayscale_for_cyan)
        block_all_but_the_pink_parts = cv2.inRange(grayscale_image,
                                                     min_grayscale_for_pink,
                                                     max_grayscale_for_pink)
        
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
        neon_purple_parts_of_image = cv2.bitwise_or(neon_purple_paper, neon_purple_paper,
                                            mask = block_all_but_the_neon_purple_parts)
        cyan_parts_of_image = cv2.bitwise_or(cyan_paper, cyan_paper,
                                            mask = block_all_but_the_cyan_parts)
        pink_parts_of_image = cv2.bitwise_or(pink_paper, pink_paper,
                                            mask = block_all_but_the_pink_parts)
        
        #combines all the colors that were chosen into one customized image
        customized_image = cv2.bitwise_or(blue_parts_of_image, green_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, red_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, yellow_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, neon_purple_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, cyan_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, orange_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, pink_parts_of_image)
    
        #displays the colors of the image in the windows
        cv2.imshow('Red Parts of Image',red_parts_of_image)
        cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
        cv2.imshow('Blue Parts of Image', blue_parts_of_image)
        cv2.imshow('Green Parts of Image', green_parts_of_image)
        cv2.imshow('Customized Image',customized_image)
        cv2.imshow('Orange Parts of Image', orange_parts_of_image)
        cv2.imshow('Neon Purple Parts of Image', neon_purple_parts_of_image)
        cv2.imshow('Cyan Parts of Image', cyan_parts_of_image)
        cv2.imshow('Pink Parts of Image', pink_parts_of_image)
        
        keypressed = cv2.waitKey(1)
    
    #stops running the program
    if keypressed == 27:
        cv2.destroyAllWindows()
    elif keypressed == ord('s'): 
        cv2.imwrite('photo_GS_1.jpg',grayscale_image)
        cv2.imwrite('photo_RY_1.jpg',customized_image)
        cv2.destroyAllWindows()
 
