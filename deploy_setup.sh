#!/bin/bash

# Install Pillow from binary wheel
pip install --only-binary=:all: pillow==9.5.0

# Install the rest of the requirements
pip install -r streamlit_requirements.txt

# Start the Streamlit app
streamlit run app.py 