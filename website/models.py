import pyrebase
import firebase_admin
import json
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate('fbadminconfig.json')
firebase = firebase_admin.initialize_app(cred, json.load(open('website/fbconfig.json')))
pyrebase_pb = pyrebase.initialize_app(json.load(open('website/fbconfig.json')))
db = firestore.client()
bucket = storage.bucket()


def areaDatabase():
    areas = ["Delhi","Mumbai","Calcutta"]

    area_ref = db.collection("area").stream()
    included_areas = []
    for area in area_ref:
        temp_dict = area.to_dict()
        included_areas.append(temp_dict['name'])


    for area in areas:
        if area not in included_areas:
            new_area_ref = db.collection('area').document()
            new_area_json = {
                "name": area,
                "areaId": new_area_ref.id,
                "restaurantId": [],
                "orderIdForPickup": []
            }

            new_area_ref.set(new_area_json)


def getDatabaseAreas():
    areaDatabase()

    areas_ref = db.collection('area').stream()
    areas = []

    for area in areas_ref:
        temp_dict = area.to_dict()
        areas.append(temp_dict)

    return areas

areas = getDatabaseAreas()