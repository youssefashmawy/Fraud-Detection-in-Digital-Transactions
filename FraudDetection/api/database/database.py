import firebase_admin
from firebase_admin import credentials, db
import os
from django.conf import settings


def connect_db():
    if not firebase_admin._apps:
        # Load credentials and initialize the Firebase app
        file_path = os.path.join(settings.BASE_DIR, 'api', 'database', 'credentials.json')
        cred = credentials.Certificate(file_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://frauddetection-147b7-default-rtdb.europe-west1.firebasedatabase.app/'
        })
    # Return the reference to the root of the database or a specific node
    ref = db.reference('/')
    return ref