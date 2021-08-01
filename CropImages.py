# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 16:20:02 2021

@author: rapha
"""

#%% Imports
import cv2
import numpy as np
import PIL
from PIL import Image
import os
from tqdm import tqdm

#%% Callback function
def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping

    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y

    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False  # cropping is finished

        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2:  # when two points were found show the cropped image and save it
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", roi)
            cv2.imwrite(os.path.join(general_path,output_dir,name), roi)



#%% Settings
general_path=os.path.join(os.path.abspath(os.getcwd()),"dataset")
input_dir="other"
output_dir="cropped_other"

#%% Get files to crop and files already cropped
input_list=os.listdir(os.path.join(general_path,input_dir))
output_exists=os.listdir(os.path.join(general_path,output_dir))
file_list=[i for i in input_list if i not in output_exists] #files that have not already been cropped

#%% Iterate over files to crop
for name in tqdm(file_list):
    
    cv2.namedWindow("image") #create the display window
    cv2.setMouseCallback("image", mouse_crop) #call the callback function when acting with the mouse
    
    cropping = False
    
    x_start, y_start, x_end, y_end = 0, 0, 0, 0
    
    basewidth = 1000
    
    # Open the image
    img = Image.open(os.path.join(general_path,input_dir,name))
    
    #resize the image so that its width is display with basewidth
    wpercent = (basewidth/float(img.size[0])) 
    hsize = int((float(img.size[1])*float(wpercent)))
    img=img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    
    #convert to BGR (opencv standard) colormap
    image=cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    oriImage = image.copy()
    
    
    #crop the image, with the mouse 
    while True:
        i = image.copy()
    
        if not cropping:
            cv2.imshow("image", image)
    
        elif cropping:
            cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
            cv2.imshow("image", i)
    
        if cv2.waitKey(1)&0xFF == ord('q'):
            break
    cv2.destroyAllWindows()