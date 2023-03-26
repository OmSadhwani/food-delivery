# import pyrebase

from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# apiKey: "AIzaSyBbGuiRdaQ_Kpe89OwS2cqTJbdFWkGtU4A",
# authDomain: "proj-6e66c.firebaseapp.com",
# projectId: "proj-6e66c",
# storageBucket: "proj-6e66c.appspot.com",
# messagingSenderId: "135795766531",
# appId: "1:135795766531:web:ba68bf6a5427d59a202536",
# measurementId: "G-GD73T1PWVM"

app = Flask(__name__)

FirbaseConfig = {
     'apiKey': "AIzaSyD5KiB_WEyAF0uzrVU6aO1h5C1WURpxJ6o",
  'authDomain': "fdms-382f8.firebaseapp.com",
  'databaseURL': "https://fdms-382f8-default-rtdb.firebaseio.com",

  'projectId': "fdms-382f8",
  'storageBucket': "fdms-382f8.appspot.com",
  'messagingSenderId': "661144916661",
  'appId': "1:661144916661:web:8c050285e9edfe7873a4fc",
  'measurementId': "G-F3ZZZ5DCVG"
}


cred = credentials.Certificate("fbadminconfig.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fdms-382f8-default-rtdb.firebaseio.com'
})
# firebase = firebase_admin.initialize_app(FirbaseConfig)
# db = firebase.database()


@app.route('/')
def index():
    return render_template('form.html')

# Create a route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Extract the form data
    name = request.form['name']
    email = request.form['email']

    # Write the data to Firebase Realtime Database
    ref = db.reference('users')
    ref.push({
        'name': name,
        'email': email
    })

    # Redirect the user to a thank you page
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)