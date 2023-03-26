from flask import Flask, render_template, request
import json
import firebase_admin
from firebase_admin import credentials, firestore, storage
from firebase_admin import db
import pyrebase

#check for bitly

cred = credentials.Certificate('fbadminconfig.json')


def create_app():
    app = Flask(__name__)
    app.config["SECRET KEY"] = "a very long secret key"
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.config['SESSION_TYPE']="filesystem"

    firebase = firebase_admin.initialize_app(cred, json.load(open('fbconfig.json')))
    pyrebase_pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))
    db = firestore.client()
    bucket = storage.bucket()

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    return app