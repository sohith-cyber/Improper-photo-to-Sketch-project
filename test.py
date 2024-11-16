import streamlit as st
import numpy as np
import cv2
from keras.models import load_model
from keras_contrib.layers.normalization.instancenormalization import InstanceNormalization
from PIL import Image
import matplotlib.pyplot as plt

# Define the custom layer
def custom_activation(x):
    return x

# Load the model
g_model = load_model('./g_model1.h5', custom_objects={'InstanceNormalization': InstanceNormalization})
def generate_image(sketch_img):
    # Convert image to NumPy array
    img = np.array(sketch_img)

    # Perform image translation
    img = cv2.resize(img, (256, 256))  
    norm_img = (img.copy() - 127.5) / 127.5

    g_img = g_model.predict(np.expand_dims(norm_img, 0))[0]
    g_img = g_img * 127.5 + 127.5

    g_img = cv2.resize(g_img, (250, 200))  
    g_img = g_img.astype('uint8')
    
    # Convert the NumPy array to a PIL Image
    g_img = Image.fromarray(g_img)
    
    return g_img

# Streamlit interface
st.title("Face Sketch Using GAN")
st.write("Upload a sketch image for translation.")

# File uploader
uploaded_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    # Generate the translated image
    g_img = generate_image(uploaded_file)
    
    # Display the translated image
    st.image(g_img, caption='Translated Image', use_column_width=True)

    # Plot the translated image using matplotlib
    plt.imshow(g_img)
    plt.axis('off')
    plt.show()
