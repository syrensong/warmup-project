import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('/Users/laylamusallam/Downloads/CS3050/warmup-project-ea50f-firebase-adminsdk-fbsvc-29b43b0a28.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

cities = db.child("Cities").get()
print(cities.val())