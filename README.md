# Fraud Detection in Digital Transactions

This repository contains a project designed to detect fraudulent digital transactions, particularly credit card fraud, using a deep learning model and an API built with Django. The solution is structured into two main components:

1. **Deep Learning Model**: A neural network for identifying fraudulent activity.
2. **Django API**: An API that serves the trained model for real-time predictions.

## Table of Contents

- [Fraud Detection in Digital Transactions](#fraud-detection-in-digital-transactions)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Model Training](#model-training)
    - [API Usage](#api-usage)
  - [Contributing](#contributing)

## Overview

Fraud detection in digital transactions is a critical task for the financial industry. This project uses a neural network model trained on transactional data to classify transactions as fraudulent or legitimate. The Django API allows users to submit transactions and receive a fraud risk prediction in real time.

## Project Structure

```txt
Fraud-Detection-in-Digital-Transactions/
│
├── model/                # Contains the deep learning model and training code
│   ├── credit card fraud detection pca final.ipynb          # Model architecture and training script
│   └── neural_network_model_pca_final.keras     # Model
│   
├── api/                  # Django project for the API
│   ├── fraud_detection/  # Main Django app
│   ├── manage.py         # Django management script
│   ├── views.py          # API views for model inference
│   └── urls.py           # API routing
│
├── install_dependencies.bat  # Python dependencies
├── README.md             # Project documentation
```

## Installation

To run the project locally, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/youssefashmawy/Fraud-Detection-in-Digital-Transactions.git
   cd Fraud-Detection-in-Digital-Transactions
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   install_dependencies.bat
   ```

4. Navigate to the `api` directory to set up the Django application:

   ```bash
   cd api
   python manage.py migrate
   ```

## Usage

### Model Training

The deep learning model is implemented using Python and can be trained using the provided dataset or your own data. To train the model:

1. Run the model training script:

   ```bash
   python model/model.py
   ```

2. The trained model will be saved in the `model/` directory.

### API Usage

The Django API serves the trained model to predict whether a transaction is fraudulent. 

1. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

2. The API can be accessed at `http://127.0.0.1:8000/predict/`.
3. To test the API, send a `POST` request with the following JSON format:

   ```json
   {
     "transaction_data": {
         "Time":56624.0,
         "V1":-7.9014213498,
         "V2":2.7204724869,
         "V3":-7.8859356724,
         "V4":6.3483335515,
         "V5":-5.4801190355,
         "V6":-0.3330592396,
         "V7":-8.6823764455,
         "V8":1.1644310779,
         "V9":-4.5424473856,
         "V10":-7.7484800495,
         "V11":5.2665858727,
         "V12":-8.6796788033,
         "V13":-1.1663656782,
         "V14":-8.1079746609,
         "V15":0.701364761,
         "V16":-6.2883057578,
         "V17":-13.7531307979,
         "V18":-4.3292392742,
         "V19":1.5042502109,
         "V20":-0.6147193445,
         "V21":0.0777390507,
         "V22":1.0924365948,
         "V23":0.3201327274,
         "V24":-0.4346425529,
         "V25":-0.3806870723,
         "V26":0.213630359,
         "V27":0.4236203294,
         "V28":-0.1051685335,
         "Amount":153.46
     }
   }
   ```

4. The API will return a prediction in the form:

   ```json
   {
     "fraud_prediction": "0: Legitimate" or "1: Fraud"
   }
   ```

## Contributing

Contributions are welcome! If you'd like to improve this project or fix bugs, feel free to open an issue or submit a pull request.
