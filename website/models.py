import pyrebase
import firebase_admin
import json
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate('fbadminconfig.json')
firebase = firebase_admin.initialize_app(cred, json.load(open('website/fbconfig.json')))
pyrebase_pb = pyrebase.initialize_app(json.load(open('website/fbconfig.json')))
db = firestore.client()
bucket = storage.bucket()