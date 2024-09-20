# Web App
# User can start the computer webcam &
# They can capture an image with the camera - just two lines of code required to get to this point
# Convert the photo into grayscale (black and white)

import streamlit as st
from PIL import Image

with st.expander("Start My Camera"):
    #Start the camera
    #Capture an image and store it in a var
    my_camera_image = st.camera_input("My_Camera")
    #my_camera_image is a specific stramlit object that I can do some manipulation on
    #for example I can convert it to grayscale

    #Print out the captured image
    print(my_camera_image)

#For the conversion of my_camera_image stramlite object, I need another library called pillow
#It was already installed as a dependemcy from streamlit (it was installed when st was installed)
#import PIl
#but since I only need an image object from PIL, I only use "from PIL import Image.

#Image is a class/type in PIL, and I am gonna create PIL Image instances from that type
#Image type has a .open method(which takes an arg), which creates the Image instances

if my_camera_image:
    #Creat a pillow instance
    img = Image.open(my_camera_image)
    #Image recognizes my_camera_image, which is a streamlit image type
    #streamlit image type is used as an arg for the PIL Image type
    #Image.open(my_camera_image) is the pillow Image instance that have created

    #Convert the pillow image to grayscale
    #The pillow Image type has a convert method
    gray_img = img.convert("L")
    #"L" is an algo that converts to grayscale, provide it as an arg.

    #Render/display the grayscale image on the webpage
    st.image(gray_img)

# Note on Error
# AttributeError: 'NoneType' object has no attribute 'read'
# This is b/c the program already went ahead to create the
# pillow instance when I hadnt granted camera permission yet
# hence my_camera_image is a 'NoneType'
# so this None type is passed into img = Image.open(None) to create the instance
# hence the error in lin 27

# tHIS CAN BE FIXED with a conditional
# if my_camera_image is an actual object (not a None object), then do something
# if the image has not yet been captured then that block will not be executed
# the Image instance wont be created, it wont be converted, and not rendered yet

# What if I want to have more control over the cam?
# I do not want it to start as soon as I open the webpage
# Use expander component
# Hide the camera widget under an expander component/widget