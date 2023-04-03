from flask import Flask

app = Flask(__name__)

@app.route('/apid')
def api():
    return {"name":"apoorv", "status":1}