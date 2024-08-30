from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
import json
from .database.database import connect_db
import tensorflow as tf
import joblib
import numpy as np

# Load the model
model = tf.keras.models.load_model('../Notebooks/PCA_dataset/neural_network_model_pca_80.keras')

# Load the scaler
scaler = joblib.load('../Notebooks/PCA_dataset/scaler.pkl')

# List of feature names expected in the request
feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']


@csrf_exempt
def checkTransaction(request):
    if request.method == 'POST':
        try:
            # Parse the JSON request body
            data = json.loads(request.body)

            # Extract and scale the features
            features = [data.get(name, 0) for name in feature_names]
            features = np.array(features).reshape(1, -1)
            scaled_features = scaler.transform(features)
            
            # Predict and determine if fraudulent
            prediction = model.predict(scaled_features)
            is_fraudulent = bool(prediction[0][0] > 0.5)

            # Prepare data to store in Firebase
            data_to_store = {
                'features': features.tolist(),
                'prediction': is_fraudulent
            }

            # Get the Firebase reference and save data
            ref = connect_db()
            new_ref = ref.child('transactions').push(data_to_store)
            
            # Return a success response with the new record's ID
            return JsonResponse({'id': new_ref.key, 'status': 'success'}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def isFraud(request):
    if request.method == 'GET':
        try:
            # Extract the transaction ID from the request
            transaction_id = request.GET.get('id')
            if not transaction_id:
                return JsonResponse({'error': 'Transaction ID not provided'}, status=400)
            
            # Get the Firebase reference
            ref = connect_db()
            
            # Retrieve the specific transaction by its ID
            transaction_ref = ref.child('transactions').child(transaction_id)
            transaction_data = transaction_ref.get()
            
            if transaction_data is None:
                return JsonResponse({'error': 'Transaction not found'}, status=404)
            
            # Extract the fraud prediction value
            is_fraudulent = transaction_data.get('prediction')
            
            # Return the fraud status in the response
            return JsonResponse({'id': transaction_id, 'is_fraudulent': is_fraudulent}, status=200)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid method'}, status=405)
