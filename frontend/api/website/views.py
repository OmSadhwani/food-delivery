from flask import Blueprint, session, redirect, url_for, render_template, jsonify
from .models import db,pyrebase_pb

views = Blueprint('views',__name__)

@views.route('/')
def home():
    # return  render_template('home.html')
    pass


@views.route('/customerDashboard')
def customerDashboard():
    user = session['user']
    if user['userType']=="customer":
        return render_template('customer-dashboard.html',user=user)
    else:
        return redirect(url_for('Auth.logout'))



@views.route('/restaurantDashboard')
def restaurantDashboard():
    user = session['user']
    if user['userType']=="restaurant":
        return render_template('restaurant-dashboard.html',user=user)
    else:
        return redirect(url_for('Auth.logout'))



@views.route('/deliveryAgentDashboard')
def deliveryAgentDashboard():
    user = session['user']
    if user['userType']=="deliveryAgent":
        return render_template('deliveryAgent-dashboard.html',user=user)
    else:
        return redirect(url_for('Auth.logout'))



@views.route('/adminDashboard')
def adminDashboard():
    # user = session['user']
    # if user['userType']=="admin":
    #     return render_template('adminDashboard',user=user)
    # else:
    #     return redirect(url_for('logout'))

    
    return "<h2>this is admin dashboard</h2>"

#show personal data of the user
@views.route('/personalData')
def personalData():
    user = session['user']
    user['areaName'] = db.collection('area').document(user['areaId']).get().to_dict()['name']
    user['ratingValue'] = db.collection('rating').document(user['areaId']).get().to_dict()['rating']

    return render_template('personalData.html',user=user)


#list of the restaurants
@views.route('/allRestaurant')
def allRestaurant():
    user = session['user']
    if (not user['userType'] == 'admin') and (not user['userType'] == 'customer'):
        return redirect(url_for('Auth.logout'))
    
    restaurantList = []
    restaurant_ref = db.collection('restaurant').stream()
    for res in restaurant_ref:
        temp_dict = res.to_dict()
        temp_dict['userId'] = res.id
        temp_dict['areaName'] = db.collection('area').document(temp_dict['areaId']).get().to_dict()['name']
        temp_dict['ratingValue'] = db.collection('rating').document(temp_dict['ratingId']).get().to_dict()['rating']

        restaurantList.append(temp_dict)

    session['restaurantList'] = restaurantList

    return render_template('allRestaurant.html', user=user, restaurantList=restaurantList)


#list of the customers
@views.route('/allCustomers')
def allCustomers():
    user = session['user']
    if not user['userType']=='admin':
        return redirect(url_for('Auth.logout'))
    
    session['customerList'] = []
    customer_ref = db.collection('customer').stream()
    for cust in customer_ref:
        temp_dict = cust.to_dict()
        temp_dict['userId'] = cust.id
        temp_dict['areaName'] = db.collection('area').document(temp_dict['areaId']).get().to_dict()['name']
        temp_dict['ratingValue'] = db.collection('rating').document(temp_dict['raringId']).get().to_dict()['rating']

        session['customerList'].append(temp_dict)

    return render_template('allCustomers.html', user=user)


#list of the deliveryAgents
@views.route('/allDeliveryAgents')
def allDeliveryAgents():
    user = session['user']
    if (not user['userType']=='admin') and (not user['userType']=='restaurant'):
        return redirect(url_for('Auth.logout'))
    
    session['deliveryAgentList'] = []

    deliveryAgent_ref = db.collection('deliveryAgent').stream()
    for agent in deliveryAgent_ref:
        temp_dict = agent.to_dict()
        temp_dict['userId'] = agent.id
        temp_dict['areaName'] = db.collection('area').document(temp_dict['areaId']).get().to_dict()['name']
        temp_dict['ratingValue'] = db.collection('rating').document(temp_dict['ratingId']).get().to_dict()['rating']

        session['deliveryAgentList'].append(temp_dict)

    return render_template('allDeliveryAgents.html',user=user)

