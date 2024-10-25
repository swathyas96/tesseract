# This code imports necessary libraries for the application:
# - streamlit (st): Used for creating web applications
# - PIL (Python Imaging Library): For image processing
# - pytesseract: An optical character recognition (OCR) tool
# - pdf2image: For converting PDF files to images
# - numpy (np): For numerical operations on arrays

import streamlit as st
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
import numpy as np


def pdf_2_image(pdf_file):
    images = convert_from_bytes(pdf_file)
    return images

st.title('Optical Character Recognition')

upload_file = st.file_uploader('choose pdf or image', type = ['jpeg', 'jpg','png','pdf'])
condition = st.button('convert')
if condition:
    if upload_file is not None:
        
        if upload_file.type == 'application/pdf':
            images = pdf_2_image(upload_file.getbuffer())
            for image in images:
                col1, col2 = st.columns(2)
                image = np.array(image)
                with col1:
                    st.image(image)
                with col2:    
                    text = pytesseract.image_to_string(image, lang="eng")
                    st.text(text)

        else:
            col1, col2 = st.columns(2)
            with col1:
                st.image(upload_file.read())
            with col2:
                image = Image.open(upload_file)
                text = pytesseract.image_to_string(image, lang="mal")
                st.text(text)
    else:
        st.warning("No file given")   
            
        
else:
    st.warning('Please upload a file')