from flask import Blueprint, session,request, redirect, url_for, render_template, jsonify
from .models import db,pyrebase_pb
from flask import request,json
from firebase_admin import firestore

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')
    

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
        try:
            temp_dict = res.to_dict()
            temp_dict['userId'] = res.id
            #temp_dict['areaName'] = db.collection('area').document(temp_dict['areaId']).get().to_dict()['name']
            temp_dict['ratingValue'] = db.collection('rating').document(temp_dict['ratingId']).get().to_dict()['rating']

            restaurantList.append(temp_dict)
        except:
            #print(temp_dict)
            pass

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
    ResMenuId= user['restaurantId']
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
    return render_template('menu.html',user=user,menuList=foodItemList,message=message)

@views.route('/addFoodItem')
def addFoodItem():
    user= session['user']
    if(user['userType']=='restaurant'):
        message=session['foodMessage']
        session['foodMessage']="False"
        return render_template('addFoodItem.html',user=user,message=message)
    else:
        return redirect(url_for('Auth.logout'))
    
@views.route('/addFoodItem/add',methods=['POST','GET'])
def Add():
    if session['user']['userType'] != 'restaurant':
        return redirect(url_for('Auth.logout'))
    name= request.form['name']
    price= request.form['price']
    # local file obj

    try:
        user = session['user']
        foodItem={
            "name": name,
            "pricePerItem": price,
            "isRecommended": False,
            "restaurantId": user['restaurantId'],
            #"picSrc": ""
        }
        doc = db.collection("restaurant").document(user['restaurantId']).collection("foodItem").document()
        doc.set(foodItem)
        db.collection("restaurant").document(user['restaurantId']).collection("foodItem").document(doc.id).update({"foodItemId":doc.id})
        return redirect(url_for('views.createMenu'))
    except:
        session['foodMessage'] = "Error adding food item text data in database"
        print(session['foodMessage'])
        return redirect(url_for('views.addFoodItem'))
    
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
    return render_template('allFoodItem.html',user=user,foodItemList=foodItemList)
    
@views.route('/order', methods=['POST','GET'])
def order():
    foodItemList = session['currentMenu']
    user = session['user']

    cost=0
    orderList = []

    for i in range(len(foodItemList)):
        if not int(request.form.get(str(i+1))) == 0:
            foodItemList[i]['frequency'] = int(request.form.get(str(i+1)))
            foodItemList[i]['pricePerItem'] = int(foodItemList[i]['pricePerItem'])
            orderList.append(foodItemList[i])
            cost += int(foodItemList[i]['pricePerItem']) * int(foodItemList[i]['frequency'])

    session['currentOrder'] = {
        'orderList': orderList,
        'isPending': True,
        'customerId': user['customerId'],
        'restaurantId': foodItemList[0]['restaurantId'],
        'orderValue': cost,
        'offerId': None,
        'discountValue': 0,
        'paidValue': 0,
        'deliveryCharge': 50,
        'orderDateTime': "",
        'deliveryAgentId': "",
        'updateLevel': 0,
        'updateMessage': "Accept/Reject",
        'orderUpdates': [],
        'orderId': ''
    }

    return redirect(url_for('views.orderDetails'))


@views.route('/orderDetails')
def orderDetails():
    currentOrder = session['currentOrder']
    customerName = db.collection('customer').document(currentOrder['customerId']).get().to_dict()['name']
    restaurantName = db.collection('restaurant').document(currentOrder['restaurantId']).get().to_dict()['name']
    orderList = currentOrder['orderList']
    discount = currentOrder['discountValue']
    if currentOrder['offerId'] == None:
        offerUsed = None
        discount = 0
    else:
        offerUsed = db.collection('customer').document(currentOrder['customerId']).collection('promotionalOfferId').document(currentOrder['offerId']).get().to_dict()
        discount = min(int(int(currentOrder['orderValue'])*int(offerUsed['discount'])/100), int(offerUsed['upperLimit']))

    currentOrder['discountValue'] = discount

    final = max(currentOrder['orderValue'] + currentOrder['deliveryCharge'] - discount, 0)
    currentOrder['paidValue'] = final

    return render_template('orderDetails.html', orderList=orderList, customerName=customerName, restaurantName=restaurantName, offerUsed=offerUsed, cost=currentOrder['orderValue'], deliveryCharge=currentOrder['deliveryCharge'], discount=discount, final=final)

@views.route('/placeOrder', methods = ['POST','GET'])
def placeOrder():
    currentOrder = session['currentOrder']

    doc_ref = db.collection('order').document()
    doc_ref.set(currentOrder)

    db.collection('order').document(doc_ref.id).update({'orderId': doc_ref.id})

    orderId = doc_ref.id
    session['currentOrder']['orderId'] = orderId

    restaurantId = currentOrder['restaurantId']
    restaurantDoc_ref = db.collection('restaurant').document(restaurantId)
    restaurantDoc_ref.update({'pendingOrderId': firestore.ArrayUnion([orderId])})

    customerId = currentOrder['customerId']
    customerDoc_ref = db.collection('customer').document(customerId)
    customerDoc_ref.update({'pendingOrderId': firestore.ArrayUnion([orderId])})

    if not currentOrder['offerId'] == None:
        db.collection('order').document(orderId).update({'offerId': db.collection('customer').document(customerId).collection('promotionalOfferId').document(currentOrder['offerId']).get().to_dict()})
        db.collection('customer').document(customerId).collection('prmotionalOfferId').document(currentOrder['offerId']).delete()

    return redirect(url_for('views.recentOrderCustomer'))

@views.route('/recentOrderCustomer')
def recentOrderCustomer():
    return "Order has been placed"















    