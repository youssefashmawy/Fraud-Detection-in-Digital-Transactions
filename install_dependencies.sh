#!/bin/bash

# Update package lists
sudo apt-get update

# Install Python package manager (pip) if not already installed
sudo apt-get install -y python3-pip

# Install necessary libraries
pip3 install numpy pandas tensorflow scikit-learn joblib ipython kaggle django djangorestframework

# Kaggle API setup
mkdir -p ~/.kaggle

# Assuming you have your kaggle.json in the current directory (add your own path if needed)
mv kaggle.json ~/.kaggle/

# Ensure the kaggle.json has the correct permissions
chmod 600 ~/.kaggle/kaggle.json

# Download the credit card fraud dataset from Kaggle
kaggle datasets download -d mlg-ulb/creditcardfraud

# Unzip the dataset
unzip -o creditcardfraud.zip

# Clean up by removing the zip file
rm -rf creditcardfraud.zip

# Check TensorFlow and Keras versions
python3 -c "import tensorflow as tf; import keras; print(f'TensorFlow version: {tf.__version__}'); print(f'Keras version: {keras.__version__}')"
