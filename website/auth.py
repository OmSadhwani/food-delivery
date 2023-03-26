from flask import Blueprint

auth = Blueprint('auth',__name__)


@auth.route('/customerLogin')
def customerLogin():
    return "<p>customer login page</p>"

@auth.route('/customerSignup')
def customerSignup():
    return "<p>customer sign up page</p>"



@auth.route('/restaurantLogin')
def customerLogin():
    return "<p>restaurant login page</p>"

@auth.route('/restaurantSignup')
def customerSignup():
    return "<p>restaurant sign up page</p>"



@auth.route('/deliveryAgentLogin')
def customerLogin():
    return "<p>deliveryAgent login page</p>"

@auth.route('/deliveryAgentSignup')
def customerSignup():
    return "<p>deliveryAgent sign up page</p>"



@auth.route('/managementLogin')
def customerLogin():
    return "<p>management login page</p>"

@auth.route('/managementSignup')
def customerSignup():
    return "<p>management sign up page</p>"