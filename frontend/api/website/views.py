from flask import Blueprint, session,request, redirect, url_for, render_template, jsonify
from .models import db,pyrebase_pb
from flask import request,json

views = Blueprint('views',__name__)

@views.route('/')
def root():
    return redirect(url_for('views.home'))

@views.route('/home')
def home():
    return {"name":"apoorv", "status":1}

# @views.route('/create' , methods=['POST'])
# def create():
#     request_data = json.loads(request.data)
#     print(request_data)
#     return {"Name":"Apoorv"}
    

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

@views.route('/createMenu')
def createMenu():
    user = session['user']
    if(not user['userType']=='restaurant'):
        return redirect(url_for('Auth.logout'))
    ResMenuId= session['userId']
    foodItemList=[]
    foodItems= db.collection('restaurant').document(ResMenuId).collection('foodItem').stream()
    for foodItem in foodItems :
        tdict= foodItem.to_dict()
    
        foodItemList.append(tdict)
    try:
        message= session['foodMessage']
        session['foodMessage']="False"
    except:
        session['foodMessage']="False"
        message="False"
    return render_template('createMenu.html',user=user,menuList=foodItemList,message=message)

@views.route('/addFoodItem')
def addFoodItem():
    user= session['user']
    if(user['userType']=='restaurant'):
        message=session['foodMessage']
        session['foodMessage']="False"
        return render_template('addFoodItem.html',user=user,message=message)
    else:
        return redirect(url_for('Auth.logout'))
    
@views.route('addFoodItem/add',methods=['POST','GET'])
def Add():
    if session['user']['userType'] != 'restaurant':
        return redirect(url_for('Auth.logout'))
    name= request.form['name']
    price= request.form['price']
    # local file obj

    try:
        foodItem={
            "name": name,
            "pricePerItem": price,
            "isRecommended": False,
            "restaurantId": session["userId"],
            "picSrc": ""
        }
        doc = db.collection("restaurant").document(session["userId"]).collection("foodItem").document()
        doc.set(foodItem)
        db.collection("restaurant").document(session["userId"]).collection("foodItem").document(doc.id).update({"foodItemId":doc.id})
    except:
        session['foodMessage'] = "Error adding food item text data in database"
        return redirect(url_for('addFoodItem'))
    
@views.route('/finishMenu')
def finishMenu():
    user= session['user']
    if user['userType']=="restaurant" :
        return render_template('finishMenu.html',user=user)
    else:
        return redirect(url_for('Auth.logout'))


@views.route('/displayFoodItems/<restaurantUserId>')
def FoodItems(restaurantUserId):
    user= session['user']
    if not session['user']['userType']=='customer' and not session['user']['userType']=='admin':
        return redirect(url_for('Auth.logout'))
    session['ResMenuId']=restaurantUserId 
    foodItemList=[]
    foodItems= db.collection('restaurant').document(session['ResMenuId']).collection('foodItem').stream()
    for foodItem in foodItems:
        tdict= foodItem.to_dict()
        foodItemList.append(tdict)
    session['currentMenu']=foodItemList
    return render_template('allFoodItem.html',user=user,foodItemlist=foodItemList)


