#Turns the whole code into a function so that I can use the entire script in the main code
def functionTwo():

    import cv2
    import numpy
    import os.path
    import random
    

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
    
    #A function that detects where the postion in the trackbar is
    def trackPosition(slider_name, window_name, min_val):
        current_pos = cv2.getTrackbarPos(slider_name, window_name)
        if current_pos < min_val:
            print('Too Low!')
            cv2.setTrackbarPos(slider_name, window_name, min_val)
            return min_val
        else:
            return current_pos
        
    # a function that creates a random color value between 0 and 255
    def rando_color():
        a = random.randint(0,255)
        return a
    
    
    original_image = cv2.imread(filename,1)
    grayscale_image_simple = cv2.imread(filename, 0)
    grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)
    

    cv2.namedWindow('Slider')
    
    image_height = original_image.shape[0] 
    image_width = original_image.shape[1]
    image_channels = original_image.shape[2]  
    
    color_one = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    color_two = numpy.zeros((image_height,image_width,image_channels),
                               numpy.uint8)
    color_three = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    color_four = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    color_five = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    color_six = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    color_seven = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    color_eight = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
    
    
    #Each RGB value is a random number between 0 and 255 to get a random color for the custom image
    color_one[0:image_height,0:image_width, 0:image_channels] = [rando_color(),rando_color(),rando_color()]
    color_two[0:image_height,0:image_width, 0:image_channels] = [rando_color(),rando_color(),rando_color()]
    color_three[0:image_height,0:image_width, 0:image_channels] = [rando_color(),rando_color(),rando_color()]
    color_four[0:image_height,0:image_width, 0:image_channels] = [rando_color(),rando_color(),rando_color()]
    color_five[0:image_height,0:image_width, 0:image_channels] = [rando_color(),rando_color(),rando_color()]
    color_six[0:image_height,0:image_width, 0:image_channels] = [rando_color(),rando_color(),rando_color()]
    color_seven[0:image_height,0:image_width, 0:image_channels] = [rando_color(),rando_color(),rando_color()]
    color_eight[0:image_height,0:image_width, 0:image_channels] = [rando_color(),rando_color(),rando_color()]
    
    
    #Creates a trackbar to change the hue for each color value
    cv2.createTrackbar('Grayscale', 'Slider', 100, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_2', 'Slider', 125, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_3', 'Slider', 135, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_4', 'Slider', 140, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_5', 'Slider', 170, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_6', 'Slider', 180, 255, lambda x:None)
    cv2.createTrackbar('Grayscale_7', 'Slider', 187, 255, lambda x:None)
    
    
    keypressed = 1
    while (keypressed != 27 and keypressed != ord('s')):
        grayscale_break = trackPosition('Grayscale', 'Slider', 0)
        grayscale_break_2 = trackPosition('Grayscale_2', 'Slider', 0)
        grayscale_break_3 = trackPosition('Grayscale_3', 'Slider', 0)
        grayscale_break_4 = trackPosition('Grayscale_4', 'Slider', 0)
        grayscale_break_5 = trackPosition('Grayscale_5', 'Slider', 0)
        grayscale_break_6 = trackPosition('Grayscale_6', 'Slider', 0)
        grayscale_break_7 = trackPosition('Grayscale_7', 'Slider', 0)
    
        
        min_grayscale_for_one = [0,0,0]
        max_grayscale_for_one = [grayscale_break,grayscale_break,grayscale_break]
        min_grayscale_for_two = [grayscale_break+1,grayscale_break+1,grayscale_break+1]
        max_grayscale_for_two = [grayscale_break_2,grayscale_break_2, 
                                    grayscale_break_2]
        min_grayscale_for_three = [grayscale_break_2+1,grayscale_break_2+1,grayscale_break_2+1]
        max_grayscale_for_three = [grayscale_break_3,grayscale_break_3, 
                                    grayscale_break_3]
        min_grayscale_for_four = [grayscale_break_3+1,grayscale_break_3+1,grayscale_break_3+1]
        max_grayscale_for_four = [grayscale_break_4,grayscale_break_4, 
                                    grayscale_break_4]
        min_grayscale_for_five = [grayscale_break_4+1,grayscale_break_4+1, 
                                    grayscale_break_4+1]
        max_grayscale_for_five = [grayscale_break_5,grayscale_break_5, 
                                    grayscale_break_5]
        min_grayscale_for_six = [grayscale_break_5+1,grayscale_break_5+1, 
                                    grayscale_break_5+1]
        max_grayscale_for_six = [grayscale_break_6,grayscale_break_6, 
                                    grayscale_break_6]
        min_grayscale_for_seven = [grayscale_break_6+1,grayscale_break_6+1, 
                                    grayscale_break_6+1]
        max_grayscale_for_seven = [grayscale_break_7,grayscale_break_7, 
                                    grayscale_break_7]
        min_grayscale_for_eight = [grayscale_break_7+1,grayscale_break_7+1, 
                                    grayscale_break_7+1]
        max_grayscale_for_eight = [255,255,255]
        
        min_grayscale_for_one = numpy.array(min_grayscale_for_one, dtype = "uint8")
        max_grayscale_for_one = numpy.array(max_grayscale_for_one, dtype = "uint8")
        min_grayscale_for_two = numpy.array(min_grayscale_for_two, dtype = "uint8")
        max_grayscale_for_two = numpy.array(max_grayscale_for_two, dtype = "uint8")
        min_grayscale_for_three = numpy.array(min_grayscale_for_three, dtype = "uint8")
        max_grayscale_for_three = numpy.array(max_grayscale_for_three, dtype = "uint8")
        min_grayscale_for_four = numpy.array(min_grayscale_for_four, dtype = "uint8")
        max_grayscale_for_four = numpy.array(max_grayscale_for_four, dtype = "uint8")
        min_grayscale_for_five = numpy.array(min_grayscale_for_five,
                                               dtype = "uint8")
        max_grayscale_for_five = numpy.array(max_grayscale_for_five,
                                               dtype = "uint8")
        min_grayscale_for_six = numpy.array(min_grayscale_for_six,
                                               dtype = "uint8")
        max_grayscale_for_six = numpy.array(max_grayscale_for_six,
                                               dtype = "uint8")
        min_grayscale_for_seven  = numpy.array(min_grayscale_for_seven,
                                               dtype = "uint8")
        max_grayscale_for_seven = numpy.array(max_grayscale_for_seven,
                                               dtype = "uint8")
        min_grayscale_for_eight  = numpy.array(min_grayscale_for_eight,
                                               dtype = "uint8")
        max_grayscale_for_eight = numpy.array(max_grayscale_for_eight,
                                               dtype = "uint8")
        
        
        block_all_but_the_one_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_one,
                                                  max_grayscale_for_one)
        block_all_but_the_two_parts = cv2.inRange(grayscale_image,
                                                     min_grayscale_for_two,
                                                     max_grayscale_for_two)
        block_all_but_the_three_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_three,
                                                  max_grayscale_for_three)
        block_all_but_the_four_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_four,
                                                  max_grayscale_for_four)
        block_all_but_the_five_parts = cv2.inRange(grayscale_image,
                                                     min_grayscale_for_five,
                                                     max_grayscale_for_five)
        block_all_but_the_six_parts = cv2.inRange(grayscale_image,
                                                     min_grayscale_for_six,
                                                     max_grayscale_for_six)
        block_all_but_the_seven_parts = cv2.inRange(grayscale_image,
                                                     min_grayscale_for_seven, 
                                                     max_grayscale_for_seven)
        block_all_but_the_eight_parts = cv2.inRange(grayscale_image,
                                                     min_grayscale_for_eight,
                                                     max_grayscale_for_eight)
        
        one_parts_of_image = cv2.bitwise_or(color_one, color_one,
                                            mask = block_all_but_the_one_parts)
        two_parts_of_image = cv2.bitwise_or(color_two, color_two,
                                            mask = block_all_but_the_two_parts)
        three_parts_of_image = cv2.bitwise_or(color_three, color_three,
                                            mask = block_all_but_the_three_parts)
        four_parts_of_image = cv2.bitwise_or(color_four, color_four,
                                            mask = block_all_but_the_four_parts)
        five_parts_of_image = cv2.bitwise_or(color_five, color_five,
                                               mask = block_all_but_the_five_parts)
        six_parts_of_image = cv2.bitwise_or(color_six, color_six,
                                               mask = block_all_but_the_six_parts)
        seven_parts_of_image = cv2.bitwise_or(color_seven, color_seven,
                                               mask = block_all_but_the_seven_parts)
        eight_parts_of_image = cv2.bitwise_or(color_eight, color_eight,
                                               mask = block_all_but_the_eight_parts)
        
        customized_image = cv2.bitwise_or(one_parts_of_image, three_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, two_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, four_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, five_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, six_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, seven_parts_of_image)
        customized_image = cv2.bitwise_or(customized_image, eight_parts_of_image)
    
    
        #displays four windows into one a horizontal window stack
        numpy_horizontal = numpy.hstack((one_parts_of_image , two_parts_of_image, three_parts_of_image, four_parts_of_image))
        numpy_horizontal_2 = numpy.hstack((five_parts_of_image , six_parts_of_image, seven_parts_of_image, eight_parts_of_image))
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
        
        
        

