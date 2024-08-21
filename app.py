from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore

# Create flask app
app = Flask(__name__)

# Initialize firebase
cred = credentials.Certificate("firebase-credentials.json")

@app.route('/')
def fraud():
    return 'Fraud Transaction!'