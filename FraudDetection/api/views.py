from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from database.database import connect_db

# Create your views here.
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