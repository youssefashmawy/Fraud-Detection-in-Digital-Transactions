import firebase_admin
from firebase_admin import credentials, db

def connect_db():
    # Load credentials and initialize the Firebase app
    cred = credentials.Certificate("../database/credentials.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://frauddetection-147b7-default-rtdb.europe-west1.firebasedatabase.app/'
    })

    # Return the reference to the root of the database or a specific node
    ref = db.reference('/')
    return ref