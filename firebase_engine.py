import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/Users/laylamusallam/Downloads/CS3050/warmup-project-ea50f-firebase-adminsdk-fbsvc-29b43b0a28.json")
firebase_admin.initialize_app(cred)
