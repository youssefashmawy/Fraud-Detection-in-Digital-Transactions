@echo off

:: Install necessary libraries using pip
pip install numpy pandas tensorflow scikit-learn joblib ipython kaggle django djangorestframework

:: Kaggle API setup
mkdir %HOMEPATH%\.kaggle

:: Move kaggle.json to the .kaggle directory (Ensure kaggle.json is in the current directory)
move kaggle.json %HOMEPATH%\.kaggle\

:: Set the correct permissions for kaggle.json
icacls %HOMEPATH%\.kaggle\kaggle.json /inheritance:r /grant:r "%username%:F"

:: Download the credit card fraud dataset from Kaggle
kaggle datasets download -d mlg-ulb/creditcardfraud

:: Unzip the dataset
tar -xf creditcardfraud.zip

:: Clean up the zip file
del creditcardfraud.zip

:: Check TensorFlow and Keras versions
python -c "import tensorflow as tf; import keras; print(f'TensorFlow version: {tf.__version__}'); print(f'Keras version: {keras.__version__}')"
