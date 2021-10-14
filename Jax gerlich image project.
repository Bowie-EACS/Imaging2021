import json
import cv2
import numpy
import os.path

##TODO:
## make a reset color button


#makes sure the slider doesn't go too low nor high
def boundedGetPos(slider, window, minimum, maximum):
    position = cv2.getTrackbarPos(slider, window)
    if position <= minimum:
        cv2.setTrackbarPos(slider, window, minimum)
        return minimum
    elif position >= maximum:
        cv2.setTrackbarPos(slider, window, maximum)
        return maximum 
    else:
        return position
    
def colorSliders(window, color1, color2, color3):
    cv2.createTrackbar('Red', window, color3, 255, lambda x:None)
    cv2.createTrackbar('Green', window, color2, 255, lambda x:None)
    cv2.createTrackbar('Blue', window, color1, 255, lambda x:None)

print ("\n Save your original image in the same folder as this program. Press s to save the edited version, escape to close the program without saving, and r to reset the colors to default")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")

#Turns image greyscale
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

#creates a bunch of named windows
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')

array_of_color_windows = ['Color 1', 'Color 2',
                          'Color 3', 'Color 4',
                          'Color 5', 'Color 6',
                          'Color 7', 'Color 8',
                          'Color 9']

cv2.resizeWindow('Sliders', 960, 540)

cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)



#records the dimensions of the paper
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#makes array the right size
paper_a = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
paper_b = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
paper_c = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
paper_d = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
paper_e = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
paper_f = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
paper_g = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
paper_h = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
paper_i = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)

#defining variable to be used in the color changing section

try:
    with open('saved_colors.json') as f:
        data = json.load(f)
        a1, a2, a3 = data[0], data[1], data[2]
        b1, b2, b3 = data[3], data[4], data[5]
        c1, c2, c3 = data[6], data[7], data[8]
        d1, d2, d3 = data[9], data[10], data[11]
        e1, e2, e3 = data[12], data[13], data[14]
        f1, f2, f3 = data[15], data[16], data[17]
        g1, g2, g3 = data[18], data[19], data[20]
        h1, h2, h3 = data[21], data[22], data[23]
        i1, i2, i3 = data[24], data[25], data[26]
            
except:
    a1, a2, a3 = 0, 0, 255
    b1, b2, b3 = 0, 130, 255
    c1, c2, c3 = 0, 255, 255
    d1, d2, d3 = 0, 255, 0
    e1, e2, e3 = 255, 170, 55
    f1, f2, f3 = 255, 0, 0
    g1, g2, g3 = 140, 0, 0
    h1, h2, h3 = 90, 0, 20
    i1, i2, i3 = 0, 0, 0
    
list_o_variables = [0, 0, 255, 
                0, 130, 255,
                0, 255, 255,
                0, 255, 0,
                255, 170, 55,
                255, 0, 0,
                140, 0, 0,
                90, 0, 20,
                0, 0, 0]
    
    
    
saved_colors = [a1, a2, a3, 
                b1, b2, b3,
                c1, c2, c3,
                d1, d2, d3,
                e1, e2, e3,
                f1, f2, f3,
                g1, g2, g3,
                h1, h2, h3,
                i1, i2, i3]


opened1 = False
opened2 = False
opened3 = False
opened4 = False
opened5 = False
opened6 = False
opened7 = False
opened8 = False
opened9 = False

with open("saved_colors.json", 'w') as json_file:
    json.dump(saved_colors, json_file)



#colors each paper
paper_a[0:image_height,0:image_width, 0:image_channels] = [a1, a2, a3]
paper_b[0:image_height,0:image_width, 0:image_channels] = [b1, b2, b3]
paper_c[0:image_height,0:image_width, 0:image_channels] = [c1, c2, c3]
paper_d[0:image_height,0:image_width, 0:image_channels] = [d1, d2, d3]
paper_e[0:image_height,0:image_width, 0:image_channels] = [e1, e2, e3]
paper_f[0:image_height,0:image_width, 0:image_channels] = [f1, f2, f3]
paper_g[0:image_height,0:image_width, 0:image_channels] = [g1, g2, g3]
paper_h[0:image_height,0:image_width, 0:image_channels] = [h1, h2, h3]
paper_i[0:image_height,0:image_width, 0:image_channels] = [i1, i2, i3]


grayscale_break1 = 30
grayscale_break2 = 60
grayscale_break3 = 90
grayscale_break4 = 120
grayscale_break5 = 150
grayscale_break6 = 180
grayscale_break7 = 210
grayscale_break8 = 240


#Defines what values of gray turn into what colors
cv2.createTrackbar('Grayscale break 1', 'Sliders', grayscale_break1, 255, lambda x:None)
cv2.createTrackbar('Grayscale break 2', 'Sliders', grayscale_break2, 255, lambda x:None)
cv2.createTrackbar('Grayscale break 3', 'Sliders', grayscale_break3, 255, lambda x:None)
cv2.createTrackbar('Grayscale break 4', 'Sliders', grayscale_break4, 255, lambda x:None)
cv2.createTrackbar('Grayscale break 5', 'Sliders', grayscale_break5, 255, lambda x:None)
cv2.createTrackbar('Grayscale break 6', 'Sliders', grayscale_break6, 255, lambda x:None)
cv2.createTrackbar('Grayscale break 7', 'Sliders', grayscale_break7, 255, lambda x:None)
cv2.createTrackbar('Grayscale break 8', 'Sliders', grayscale_break8, 255, lambda x:None)


keypressed = 1
while (keypressed != 27 and keypressed != ord('s') and keypressed != ord('r')):
    

    
    grayscale_break1 = boundedGetPos('Grayscale break 1', 'Sliders', 0, grayscale_break2)
    grayscale_break2 = boundedGetPos('Grayscale break 2', 'Sliders', grayscale_break1, grayscale_break3)
    grayscale_break3 = boundedGetPos('Grayscale break 3', 'Sliders', grayscale_break2, grayscale_break4)
    grayscale_break4 = boundedGetPos('Grayscale break 4', 'Sliders', grayscale_break3, grayscale_break5)
    grayscale_break5 = boundedGetPos('Grayscale break 5', 'Sliders', grayscale_break4, grayscale_break6)
    grayscale_break6 = boundedGetPos('Grayscale break 6', 'Sliders', grayscale_break5, grayscale_break7)
    grayscale_break7 = boundedGetPos('Grayscale break 7', 'Sliders', grayscale_break6, grayscale_break8)
    grayscale_break8 = boundedGetPos('Grayscale break 8', 'Sliders', grayscale_break7, 255)
    
    
    #sets the gray values to their respective colors
    min_grayscale_for_a = [0,0,0]
    max_grayscale_for_a = [grayscale_break1,grayscale_break1,grayscale_break1]
    min_grayscale_for_b = [grayscale_break1+1,grayscale_break1+1,grayscale_break1+1]
    max_grayscale_for_b = [grayscale_break2,grayscale_break2,grayscale_break2]
    min_grayscale_for_c = [grayscale_break2+1,grayscale_break2+1,grayscale_break2+1]
    max_grayscale_for_c = [grayscale_break3,grayscale_break3,grayscale_break3]
    min_grayscale_for_d = [grayscale_break3+1,grayscale_break3+1,grayscale_break3+1]
    max_grayscale_for_d = [grayscale_break4,grayscale_break4,grayscale_break4]
    min_grayscale_for_e = [grayscale_break4+1,grayscale_break4+1,grayscale_break4+1]
    max_grayscale_for_e = [grayscale_break5,grayscale_break5,grayscale_break5]
    min_grayscale_for_f = [grayscale_break5+1,grayscale_break5+1,grayscale_break5+1]
    max_grayscale_for_f = [grayscale_break6,grayscale_break6,grayscale_break6]
    min_grayscale_for_g = [grayscale_break6+1,grayscale_break6+1,grayscale_break6+1]
    max_grayscale_for_g = [grayscale_break7,grayscale_break7,grayscale_break7]
    min_grayscale_for_h = [grayscale_break7+1,grayscale_break7+1,grayscale_break7+1]
    max_grayscale_for_h = [grayscale_break8,grayscale_break8,grayscale_break8]
    min_grayscale_for_i = [grayscale_break8+1,grayscale_break8+1,grayscale_break8+1]
    max_grayscale_for_i = 255
    
    #reformats variables that were just made
    min_grayscale_for_a = numpy.array(min_grayscale_for_a, dtype = "uint8")
    max_grayscale_for_a = numpy.array(max_grayscale_for_a, dtype = "uint8")
    min_grayscale_for_b = numpy.array(min_grayscale_for_b, dtype = "uint8")
    max_grayscale_for_b = numpy.array(max_grayscale_for_b, dtype = "uint8")
    min_grayscale_for_c = numpy.array(min_grayscale_for_c, dtype = "uint8")
    max_grayscale_for_c = numpy.array(max_grayscale_for_c, dtype = "uint8")
    min_grayscale_for_d = numpy.array(min_grayscale_for_d, dtype = "uint8")
    max_grayscale_for_d = numpy.array(max_grayscale_for_d, dtype = "uint8")
    min_grayscale_for_e = numpy.array(min_grayscale_for_e, dtype = "uint8")
    max_grayscale_for_e = numpy.array(max_grayscale_for_e, dtype = "uint8")
    min_grayscale_for_f = numpy.array(min_grayscale_for_f, dtype = "uint8")
    max_grayscale_for_f = numpy.array(max_grayscale_for_f, dtype = "uint8")
    min_grayscale_for_g = numpy.array(min_grayscale_for_g, dtype = "uint8")
    max_grayscale_for_g = numpy.array(max_grayscale_for_g, dtype = "uint8")
    min_grayscale_for_h = numpy.array(min_grayscale_for_h, dtype = "uint8")
    max_grayscale_for_h = numpy.array(max_grayscale_for_h, dtype = "uint8")
    min_grayscale_for_i = numpy.array(min_grayscale_for_i, dtype = "uint8")
    max_grayscale_for_i = numpy.array(max_grayscale_for_i, dtype = "uint8")
    
    #cuts out pieces of paper thats not the right color to turn gray
    block_all_but_a = cv2.inRange(grayscale_image, min_grayscale_for_a, max_grayscale_for_a)
    block_all_but_b = cv2.inRange(grayscale_image, min_grayscale_for_b, max_grayscale_for_b)
    block_all_but_c =  cv2.inRange(grayscale_image, min_grayscale_for_c, max_grayscale_for_c)
    block_all_but_d = cv2.inRange(grayscale_image, min_grayscale_for_d, max_grayscale_for_d)
    block_all_but_e = cv2.inRange(grayscale_image, min_grayscale_for_e, max_grayscale_for_e)
    block_all_but_f =  cv2.inRange(grayscale_image, min_grayscale_for_f, max_grayscale_for_f)
    block_all_but_g = cv2.inRange(grayscale_image, min_grayscale_for_g, max_grayscale_for_g)
    block_all_but_h = cv2.inRange(grayscale_image, min_grayscale_for_h, max_grayscale_for_h)
    block_all_but_i =  cv2.inRange(grayscale_image, min_grayscale_for_i, max_grayscale_for_i)
    
    #comnbines the different cut up papers
    a_parts_of_image = cv2.bitwise_or(paper_a, paper_a, mask = block_all_but_a)
    b_parts_of_image = cv2.bitwise_or(paper_b, paper_b, mask = block_all_but_b)
    c_parts_of_image = cv2.bitwise_or(paper_c, paper_c, mask = block_all_but_c)
    d_parts_of_image = cv2.bitwise_or(paper_d, paper_d, mask = block_all_but_d)
    e_parts_of_image = cv2.bitwise_or(paper_e, paper_e, mask = block_all_but_e)
    f_parts_of_image = cv2.bitwise_or(paper_f, paper_f, mask = block_all_but_f)
    g_parts_of_image = cv2.bitwise_or(paper_g, paper_g, mask = block_all_but_g)
    h_parts_of_image = cv2.bitwise_or(paper_h, paper_h, mask = block_all_but_h)
    i_parts_of_image = cv2.bitwise_or(paper_i, paper_i, mask = block_all_but_i)
    
    customized_image = cv2.bitwise_or(a_parts_of_image, b_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, c_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, d_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, e_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, f_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, g_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, h_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, i_parts_of_image)
    
    
    #displays the images in the windows
    if (keypressed == 49):
        if  opened1 == False:
            cv2.namedWindow('Color 1')
            colorSliders('Color 1', a1, a2, a3)
        opened1 = True
            
            
    elif (keypressed == 50):
        if  opened2 == False:
            cv2.namedWindow('Color 2')
            colorSliders('Color 2', b1, b2, b3)
        opened2 = True
        
            
    elif (keypressed == 51):
        if  opened3 == False:
            cv2.namedWindow('Color 3')
            colorSliders('Color 3', c1, c2, c3)
        opened3 = True
            
    elif (keypressed == 52):
        if  opened4 == False:
            cv2.namedWindow('Color 4')
            colorSliders('Color 4', d1, d2, d3)
        opened4 = True
            
    elif (keypressed == 53):
        if  opened5 == False:
            cv2.namedWindow('Color 5')
            colorSliders('Color 5', e1, e2, e3)
        opened5 = True
            
    elif (keypressed == 54):
        if  opened6 == False:
            cv2.namedWindow('Color 6')
            colorSliders('Color 6', f1, f2, f3)
        opened6 = True

    elif (keypressed == 55):
        if  opened7 == False:
            cv2.namedWindow('Color 7')
            colorSliders('Color 7', g1, g2, g3)
        opened7 = True
            
    elif (keypressed == 56):
        if  opened8 == False:
            cv2.namedWindow('Color 8')
            colorSliders('Color 8', h1, h2, h3)
        opened8 = True
            
    elif (keypressed == 57): 
        if  opened9 == False:
            cv2.namedWindow('Color 9')
            colorSliders('Color 9', i1, i2, i3)
        opened9 = True
        
    if opened1 == True:
        paper_a[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Blue', 'Color 1'), cv2.getTrackbarPos('Green', 'Color 1'), cv2.getTrackbarPos('Red', 'Color 1')]
        cv2.imshow('Color 1', a_parts_of_image)
        
    if opened2 == True:
        paper_b[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Blue', 'Color 2'), cv2.getTrackbarPos('Green', 'Color 2'), cv2.getTrackbarPos('Red', 'Color 2')]
        cv2.imshow('Color 2', b_parts_of_image)
        
    if opened3 == True:
        paper_c[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Blue', 'Color 3'), cv2.getTrackbarPos('Green', 'Color 3'), cv2.getTrackbarPos('Red', 'Color 3')]
        cv2.imshow('Color 3', c_parts_of_image) 
        
    if opened4 == True:
        paper_d[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Blue', 'Color 4'), cv2.getTrackbarPos('Green', 'Color 4'), cv2.getTrackbarPos('Red', 'Color 4')]
        cv2.imshow('Color 4', d_parts_of_image) 
        
    if opened5 == True:
        paper_e[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Blue', 'Color 5'), cv2.getTrackbarPos('Green', 'Color 5'), cv2.getTrackbarPos('Red', 'Color 5')]
        cv2.imshow('Color 5', e_parts_of_image) 
        
    if opened6 == True:
        paper_f[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Blue', 'Color 6'), cv2.getTrackbarPos('Green', 'Color 6'), cv2.getTrackbarPos('Red', 'Color 6')]
        cv2.imshow('Color 6', f_parts_of_image) 
        
    if opened7 == True:
        paper_g[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Blue', 'Color 7'), cv2.getTrackbarPos('Green', 'Color 7'), cv2.getTrackbarPos('Red', 'Color 7')]
        cv2.imshow('Color 7', g_parts_of_image) 
        
    if opened8 == True:
        paper_h[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Blue', 'Color 8'), cv2.getTrackbarPos('Green', 'Color 8'), cv2.getTrackbarPos('Red', 'Color 8')]
        cv2.imshow('Color 8', h_parts_of_image) 
        
    if opened9 == True:
        paper_i[0:image_height,0:image_width, 0:image_channels] = [cv2.getTrackbarPos('Blue', 'Color 9'), cv2.getTrackbarPos('Green', 'Color 9'), cv2.getTrackbarPos('Red', 'Color 9')]
        cv2.imshow('Color 9', i_parts_of_image) 

    if (keypressed == 48):
        for i in range(9):
            saved_colors[3*i] = cv2.getTrackbarPos('Blue', 'Color ' + str(i + 1))
            saved_colors[3*i+1] = cv2.getTrackbarPos('Green', 'Color ' + str(i + 1))
            saved_colors[3*i+2] = cv2.getTrackbarPos('Red', 'Color ' + str(i + 1))
            
        for i in range(9):
            if saved_colors[3*i] == -1:
                saved_colors[3*i] = list_o_variables[3*i]
            if saved_colors[3*i+1] == -1:
                saved_colors[3*i+1] = list_o_variables[3*i+1] 
            if saved_colors[3*i+2] == -1:
                saved_colors[3*i+2] = list_o_variables[3*i+2]  
        opened1 = False
        opened2 = False
        opened3 = False
        opened4 = False
        opened5 = False
        opened6 = False
        opened7 = False
        opened8 = False
        opened9 = False
        for i in range(9):
            cv2.destroyWindow('Color ' + str(i + 1))
       
    cv2.imshow('Customized Image',customized_image)

    keypressed = cv2.waitKey(1)
#Saves images [esc key == 27]
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('r'):
     with open("saved_colors.json", 'w') as json_file:
         json.dump(list_o_variables, json_file)
     cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    colors_valid = False
    while colors_valid == False:
        save_colors = input("y or n: Would you like to save these colors for later?: ")
        
        if save_colors == 'y' or save_colors == 'yes':
            with open("saved_colors.json", 'w') as json_file:
                json.dump(saved_colors, json_file)
                
            print("Colors successfully saved")
            colors_valid = True
            
        elif save_colors == 'n' or save_colors == 'no':
            print("no")
            colors_valid = True
            
        else: 
            print("That is not an input I understand :(")
    
    image_name = input("What would you like to save the image name as?: ")
    cv2.imwrite(image_name + ".jpg", customized_image)
    cv2.destroyAllWindows()
