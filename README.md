# Fraud Detection in Digital Transactions

This repository contains a project designed to detect fraudulent digital transactions, particularly credit card fraud, using a deep learning model and an API built with Django. The solution is structured into two main components:

1. **Deep Learning Model**: A neural network for identifying fraudulent activity.
2. **Django API**: An API that serves the trained model for real-time predictions.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [API Usage](#api-usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

Fraud detection in digital transactions is a critical task for the financial industry. This project uses a neural network model trained on transactional data to classify transactions as fraudulent or legitimate. The Django API allows users to submit transactions and receive a fraud risk prediction in real time.

## Project Structure

```
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
├── requirements.txt      # Python dependencies
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
   pip install -r requirements.txt
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
       "feature_1": value1,
       "feature_2": value2,
       "...": "..."
     }
   }
   ```
4. The API will return a prediction in the form:
   ```json
   {
     "fraud_prediction": "Fraud" or "Legitimate"
   }
   ```

## Contributing

Contributions are welcome! If you'd like to improve this project or fix bugs, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
