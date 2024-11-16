import streamlit as st
from keras.models import load_model
from keras_contrib.layers.normalization.instancenormalization import InstanceNormalization
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import io

# Load the model
g_model = load_model('Models/g_model1.h5', custom_objects={'InstanceNormalization': InstanceNormalization})

def generate_image(sketch_array):
    # Preprocess the sketch image
    norm_sketch_array = (sketch_array - 127.5) / 127.5

    # Generate the image using the model
    generated_img_array = g_model.predict(np.expand_dims(norm_sketch_array, 0))[0]
    
    # Postprocessing: Convert the generated image to the correct scale and data type
    generated_img_array = (generated_img_array * 127.5 + 127.5).astype(np.uint8)
    
    return generated_img_array


st.title('Sketch to Image Generation')

uploaded_file = st.file_uploader("Upload a sketch image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Convert the uploaded file to an array for processing
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    sketch_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)

    # Display the uploaded sketch
    st.image(sketch_image, caption='Uploaded Sketch', use_column_width=True)

    if st.button('Generate Image'):
        # Resize the uploaded image to the expected input size
        resized_sketch = cv2.resize(sketch_image, (256, 256))
        
        # Process the sketch and generate an image
        generated_image = generate_image(resized_sketch)

        fig, ax = plt.subplots()
        ax.imshow(sketch_image)
        ax.set_title('Original Sketch')
        ax.axis('off')
        st.pyplot(fig)
        fig, ax = plt.subplots()
        ax.imshow(generated_image)
        ax.set_title('Generated Sketch')
        ax.axis('off')
        st.pyplot(fig)

