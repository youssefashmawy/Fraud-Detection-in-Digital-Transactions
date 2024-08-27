from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
import json
from .database.database import connect_db
import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('../Notebooks/PCA_dataset/neural_network_model_pca_80.keras')

@csrf_exempt
def checkTransaction(request):
    if request.method == 'POST':
        try:
            # Parse the JSON request body
            data = json.loads(request.body)
            
            # Get a reference to the Firebase database
            ref = connect_db().child('transactions')
            
            # Add the data to Firebase Realtime Database
            # `push()` will create a unique ID for each new transaction
            new_ref = ref.push(data)
            
            # Return a success response with the new record's ID
            return JsonResponse({'id': new_ref.key, 'status': 'success'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)


def isFraud(request):
    if request.method == 'GET':
        # transaction_id = request.GET.get('transaction_id')
        #
        # if not transaction_id:
        #     return JsonResponse({'error': 'Transaction ID not provided'}, status=400)
        #
        try:
        #     ref = connect_db()
        #     transaction_ref = ref.reference(f'transactions/{transaction_id}')
        #     transaction = transaction_ref.get()
        #
        #     if transaction.exists:
        #         return JsonResponse({'id': {transaction_id}, 'exists': 'yes'}, status=200)
        #     else:
        #         return JsonResponse({'id': {transaction_id}, 'exists': 'no'}, status=200)
            return JsonResponse({'id': '123', 'exists': 'no'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)

