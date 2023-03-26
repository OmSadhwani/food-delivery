from flask import Blueprint

views = Blueprint('views',__name__)


@views.route('/')
def home():
    return "<h1>ask if he's a customer or restaurant or delivery agent.</h1>"


@views.route('/customerDashboard')
def customerDashboard():


    return "<h2>this is customer dashboard</h2>"


@views.route('/restaurantDashboard')
def restaurantDashboard():

    
    return "<h2>this is restaurant dashboard</h2>"


@views.route('/deliveryAgentDashboard')
def deliveryAgentDashboard():

    
    return "<h2>this is deliveryAgent dashboard</h2>"


@views.route('/adminDashboard')
def adminDashboard():

    
    return "<h2>this is admin dashboard</h2>"