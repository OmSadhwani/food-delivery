from flask import Blueprint

views = Blueprint('views',__name__)


@views.route('/')
def home():
    return "<h1>ask if he's a customer or restaurant or delivery agent.</h1>"

