from flask import Blueprint, session,request, redirect, url_for, render_template, jsonify
from .models import db,pyrebase_pb
from flask import request,json
from firebase_admin import firestore

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')
    
@views.route('/home')
def homie():
    return {"Hello":"World"}

@views.route('/customerDashboard')
def customerDashboard():
    user = session['user']
    if user['userType']=="customer":
        return user
    else:
        return redirect(url_for('Auth.logout'))



@views.route('/restaurantDashboard',methods=['POST'])
def restaurantDashboard():
    user = session['user']
    if user['userType']=="restaurant":
        return user
    else:
        return redirect(url_for('Auth.logout'))



@views.route('/deliveryAgentDashboard')
def deliveryAgentDashboard():
    user = session['user']
    if user['userType']=="deliveryAgent":
        return user
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

    user['ratingValue'] = db.collection('rating').document(user['ratingId']).get().to_dict()['rating']

    return user


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
        # temp_dict['areaName'] = db.collection('area').document(temp_dict['areaId']).get().to_dict()['name']
        temp_dict['ratingValue'] = db.collection('rating').document(temp_dict['ratingId']).get().to_dict()['rating']

        restaurantList.append(temp_dict)

    session['restaurantList'] = restaurantList

    return {"restaurantList":restaurantList}


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
        #temp_dict['areaName'] = db.collection('area').document(temp_dict['areaId']).get().to_dict()['name']
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
        #temp_dict['areaName'] = db.collection('area').document(temp_dict['areaId']).get().to_dict()['name']
        temp_dict['ratingValue'] = db.collection('rating').document(temp_dict['ratingId']).get().to_dict()['rating']

        session['deliveryAgentList'].append(temp_dict)

    return render_template('allDeliveryAgents.html',user=user)

@views.route('/menu',methods=['GET'])
def createMenu():
    user = session['user']
    if  not (user['userType']=='restaurant'):
        return {"msg":"hello"}
    try:
        ResMenuId= user['restaurantId']
        foodItemList=[]
        foodItems= db.collection('restaurant').document(ResMenuId).collection('foodItem').stream()
        for foodItem in foodItems :
            tdict= foodItem.to_dict()
        
            foodItemList.append(tdict)
        session['foodMessage']="False"
        return {"user":user,"menuList":foodItemList,"message":"success"}

    except Exception as e:
        return {"error":str(e)}
    # except:
    #     session['foodMessage']="False"
    #     message="False"
    #     return {"user":user,"menuList":foodItemList,"message":"error"}

# @views.route('/addFoodItem',methods=['POST'])
# def addFoodItem():
#     requestt = json.loads(request.data)
#     user= session['user']
#     if(user['userType']=='restaurant'):
#         message=session['foodMessage']
#         session['foodMessage']="False"
#         return render_template('addFoodItem.html',user=user,message=message)
#     else:
#         return redirect(url_for('Auth.logout'))
    
@views.route('/addFoodItem',methods=['POST'])
def Add():
    requestt = json.loads(request.data)
    print(requestt)
    if session['user']['userType'] != 'restaurant':
        return {"message":"Not A Restaurant"}
    name= requestt['name']
    price= requestt['price']
    user = session['user']
    # local file obj

    try:
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
        return {"message":"Success"}
    except:
        session['foodMessage'] = "Error adding food item text data in database"
        return {"message":session['foodMessage']}
    
@views.route('/finishMenu')
def finishMenu():
    user= session['user']
    if user['userType']=="restaurant" :
        return render_template('finishMenu.html',user=user)
    else:
        return redirect(url_for('Auth.logout'))


@views.route('/displayFoodItems/<restaurantUserId>',methods=['GET','POST'])
def FoodItems(restaurantUserId):
    rr=json.loads(request.data)
    restaurantUserId=rr['id']
    user= session['user']
    if not session['user']['userType']=='customer' and not session['user']['userType']=='admin':
        return redirect(url_for('Auth.logout'))
    session['ResMenuId']=restaurantUserId 
    foodItemList=[]
    foodItems= db.collection('restaurant').document(session['ResMenuId']).collection('foodItem').stream()
    for foodItem in foodItems:
        tdict= foodItem.to_dict()
        foodItemList.append(tdict)
    # print(foodItemList)
    # print(restaurantUserId)
    session['currentMenu']=foodItemList
    return {"menu":foodItemList}
    
@views.route('/order', methods=['POST','GET'])
def order():
    requestt = json.loads(request.data)
    foodItemList = session['currentMenu']

    cost=0
    orderList = []

    try:
        for i in range(len(foodItemList)):
            if not int(requestt[foodItemList[i]['name']]) == 0:
                foodItemList[i]['frequency'] = int(requestt[foodItemList[i]['name']])
                foodItemList[i]['pricePerItem'] = int(foodItemList[i]['pricePerItem'])
                orderList.append(foodItemList[i])
                cost += int(foodItemList[i]['pricePerItem']) * int(foodItemList[i]['frequency'])

        session['currentOrder'] = {
            'orderList': orderList,
            'isPending': True,
            'customerId': session['userId'],
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
        return {"message":"success"}
    except Exception as e:
        return {"message":"error", "error":str(e)}

    #return redirect(url_for('orderDetails'))


@views.route('/orderDetails')
def orderDetails():
    currentOrder = session['currentOrder']
    customerName = db.collection('customer').document(currentOrder)['customerId'].get().to_dict()['name']
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

@views.route('/placeOrder')
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
    user = session['user']
    currentOrder = session['currentOrder']
    customerId=currentOrder['customerId']
    listOrderId = db.collection('customer').document(customerId).get().to_dict()['pendingOrderId']
    docs = db.collection('order').stream()
    recentOrderList=[]
    for doc in docs:
        if doc.id in listOrderId:
            temp=doc.to_dict()
            temp['restaurantName']=db.collection('restaurant').document(temp['restaurantId']).get().to_dict()['name']
            recentOrderList.append(temp)
    session['presentOrderCustomer']=recentOrderList
    
    return render_template('recentOrderCustomer.html', recentOrderList=recentOrderList)

@views.route('/recentOrderRestaurant')

def recentOrderRestaurant():
    user=session['user']
    restaurantId = user['restaurantId']
    listOrderId = db.collection('restaurant').document(restaurantId).get().to_dict()['pendingOrderId']
    docs = db.collection('order').stream()
    recentOrderList = []
    
    for doc in docs:
        if doc.id in listOrderId:
            temp = doc.to_dict()
            print(temp['customerId'])
            temp['customerName']=db.collection('customer').document(temp['customerId']).get().to_dict()['name']
            recentOrderList.append(temp)
    session['presentOrderRestaurant'] = recentOrderList
    
        
    return render_template('recentOrderRestaurant.html', recentOrderList=recentOrderList)

@views.route('/orderDetailRestaurant<orderId>')

def orderDetailRestaurant(orderId):
    orderId=int(orderId)
    if orderId > len(session['presentOrderRestaurant']):
        return redirect(url_for('recentOrderRestaurant'))
    orderId=orderId-1
    currentOrder=session['presentOrderRestaurant'][orderId]['orderId']
    currentOrder=db.collection('order').document(currentOrder).get().to_dict()
    customerName = db.collection('customer').document(currentOrder['customerId']).get().to_dict()['name']
    restaurantName = db.collection('restaurant').document(currentOrder['restaurantId']).get().to_dict()['name']
    orderList=currentOrder['orderList']
    discount=currentOrder['discountValue']
    session['currentOrderUpdating']=currentOrder
    
    final=max(currentOrder['orderValue']+ currentOrder['deliveryCharge']- discount,0)
    return render_template('orderDetailsRestaurant.html', currentOrder = currentOrder, orderList=orderList, customerName=customerName, restaurantName=restaurantName, cost=currentOrder['orderValue'], deliveryCharge=currentOrder['deliveryCharge'], discount=discount, final=final, updateLevel=currentOrder['updateLevel'])

@views.route('/updateStatus0<val>')

def updateStatus0(val):
    if session['user']['userType'] != 'restaurant':
        return redirect(url_for('logout'))
    if val == "Reject":
        updateOrderDic = {'heading': "Rejected"}
        db.collection('order').document(session['currentOrderUpdating']['orderId']).update({'orderUpdates' : firestore.ArrayUnion([updateOrderDic])})
        db.collection('order').document(session['currentOrderUpdating']['orderId']).update({'isPending': False})
        db.collection('order').document(session['currentOrderUpdating']['orderId']).update({'updateMessage': "Rejected"})
        db.collection('order').document(session['currentOrderUpdating']['orderId']).update({'updateLevel': 1})
        db.collection('customer').document(session['currentOrderUpdating']['customerId']).update({'pendingOrderId' : firestore.ArrayRemove([session['currentOrderUpdating']['orderId']])})
        db.collection('restaurant').document(session['currentOrderUpdating']['restaurantId']).update({'pendingOrderId' : firestore.ArrayRemove([session['currentOrderUpdating']['orderId']])})
        return redirect('views.recentOrderRestaurant')
    else :
        return render_template('getEstimatedTime.html')

@views.route('/getEstimatedTime', methods=['POST','GET'])
def getEstimatedTime():
    if session['user']['userType'] != 'restaurant':
        return redirect(url_for('Auth.logout'))
    try:
        estimatedTime = request.form['time']
        updateOrderDic = {
            'heading': "Accepted",
            'time' : str(estimatedTime)+" min"
            
            }
        
    except Exception as e:
        print(str(e))

    try:
        db.collection('order').document(session['currentOrderUpdating']['orderId']).update({'updateMessage': "Accepted. Preparing Food"})
        db.collection('order').document(session['currentOrderUpdating']['orderId']).update({'updateLevel': 1})
        db.collection('order').document(session['currentOrderUpdating']['orderId']).update({'orderUpdates' : firestore.ArrayUnion([updateOrderDic])})
    except Exception as e:
        print(str(e))

    return redirect(url_for('views.recentOrderRestaurant'))

@views.route('/updateStatus1')
def updateStatus1():
    if session['user']['userType'] != 'restaurant':
        return redirect(url_for('Auth.logout'))
    return render_template('foodPrepared.html')

@views.route('/updateStatus3')
def updateStatus3():
    if session['user']['userType'] != 'restaurant':
        return redirect(url_for('logout'))
    currentOrder = session['currentOrderUpdating']
    db.collection('order').document(currentOrder['orderId']).update({'updateMessage': "Out for Delivery"})
    db.collection('order').document(currentOrder['orderId']).update({'updateLevel': 4})
    return redirect(url_for('views.recentOrderRestaurant'))

@views.route('/addPendingOrderId')
def addPendingOrderId():

    if session['user']['userType']!='restaurant':
        return redirect(url_for('logout'))

    pendingOrderId=session['currentOrderUpdating']['orderId'] #get from front end
    areaId=session['user']['areaId']

    #db.collection('area').document(areaId).update({'availableOrderIdForPickup':firestore.ArrayUnion([pendingOrderId])})
    db.collection('order').document(session['currentOrderUpdating']['orderId']).update({'updateMessage': "Food is Prepared"})
    db.collection('order').document(session['currentOrderUpdating']['orderId']).update({'updateLevel': 2})
    return redirect(url_for('views.recentOrderRestaurant'))

@views.route('/moreDetailsOrder<orderId>')
def moreDetailsOrder(orderId):
    if session['user']['userType'] != 'customer':
        return redirect(url_for('logout'))
    orderId=int(orderId)
    if orderId > len(session['presentOrderCustomer']):
        return redirect(url_for('recentOrderCustomer'))
    orderId=orderId-1
    currentOrder=session['presentOrderCustomer'][orderId]['orderId']
    currentOrder=db.collection('order').document(currentOrder).get().to_dict()
    customerName = db.collection('customer').document(currentOrder['customerId']).get().to_dict()['name']
    restaurantName = db.collection('restaurant').document(currentOrder['restaurantId']).get().to_dict()['name']
    session['customerCurrentOrderChanging']=currentOrder
    orderList=currentOrder['orderList']
    discount=currentOrder['discountValue']
    print(currentOrder['offerId'])
    if currentOrder['offerId'] == None:
        offerUsed=None
    else: 
        offerUsed=currentOrder['offerId']
        discount=min(int(int(currentOrder['orderValue'])*int(offerUsed['discount'])/100), int(offerUsed['upperLimit']))
    currentOrder['discountValue']=discount
    final=max(currentOrder['orderValue']+ currentOrder['deliveryCharge']- discount,0)
    deliveryAgentName=""
    if currentOrder['deliveryAgentId'] != "":
        deliveryAgentName=db.collection('deliveryAgent').document(currentOrder['deliveryAgentId']).get().to_dict()['name']
    return render_template('moreDetailsOrder.html',  orderList=orderList, customerName=customerName, restaurantName=restaurantName, offerUsed=offerUsed, cost=currentOrder['orderValue'], deliveryCharge=currentOrder['deliveryCharge'], discount=discount, final=final, updateLevel=currentOrder['updateLevel'], orderUpdate = currentOrder['orderUpdates'],restaurantId=currentOrder['restaurantId'],customerId= currentOrder['customerId'], deliveryAgentName=deliveryAgentName)

#offers walle code daalna baaki hai

@views.route('/redirectDashboard')
def redirectDashboard():
    if session['user']['userType']=='customer':
        return redirect(url_for('customerDashboard'))
    elif session['user']['userType']=='restaurant':
        return redirect(url_for('restaurantDashboard'))
    elif session['user']['userType']=='deliveryAgent':
        return redirect(url_for('deliveryAgentDashboard'))
    elif session['user']['userType']=='admin':
        return redirect(url_for('adminDashboard'))
    

@views.route('/deleteFoodItem<foodItemId>')

def deleteFoodItem(foodItemId):
    if session['user']['userType'] != 'restaurant':
        return redirect(url_for('Auth.logout'))
    restaurantId=session['userId']

    #command_to delete the id
    try:
        db.collection("restaurant").document(restaurantId).collection('foodItem').document(foodItemId).delete()
        session['foodMessage']="food item deletion from databse is successful"
    except Exception as e:
        # print(e)
        session['foodMessage']="Error deleting food item from databse"

    return redirect(url_for('views.createMenu'))

#recommended retaurant aur food item walle code baaki hai

@views.route('/pastOrder')

def pastOrder():
    if not session['user']['userType'] == 'restaurant' and not session['user']['userType'] == 'customer':
        return redirect(url_for('Auth.logout'))
    userId=session['userId']
    userType=session['user']['userType']

    pastOrderList=[]

    docs = db.collection('order').stream()
    for doc in docs:
        temp_dict=doc.to_dict()
        if not temp_dict['isPending'] :
            if userType=='customer' and userId==temp_dict['customerId']:
                temp_dict['restaurantName']=db.collection('restaurant').document(temp_dict['restaurantId']).get().to_dict()['name']
                pastOrderList.append(temp_dict)
            elif userType=='restaurant' and userId==temp_dict['restaurantId']:
                temp_dict['customerName']=db.collection('customer').document(temp_dict['customerId']).get().to_dict()['name']
                pastOrderList.append(temp_dict)

    if(userType=="customer"):
        session['presentOrderCustomer']= pastOrderList
        session.modified = True
        return render_template('pastOrderCustomer.html',pastOrderList=pastOrderList)
    if(userType=="restaurant"):
        session['presentOrderRestaurant']= pastOrderList
        
        return render_template('pastOrderRestaurant.html',pastOrderList=pastOrderList)


# This will show all the nearby delivery agent in the same area to the restaurant
@views.route('/nearbyDeliveryAgents')
def nearbyDeliveryAgents():

    if session['user']['userType']!='restaurant':
        return redirect(url_for('Auth.logout'))

    areaId=session['user']['areaId']

    nearbyDeliveryAgentsList=[]
    # Retrieving the data from the database
    doc_reference = db.collection('deliveryAgent').stream()

    for doc in doc_reference:
        temp_dict=doc.to_dict()
        if temp_dict['areaId']==areaId:
            #temp_dict['areaName'] = db.collection('area').document(temp_dict['areaId']).get().to_dict()['name']
            temp_dict['ratingValue']= db.collection('rating').document(temp_dict['ratingId']).get().to_dict()['rating']
            nearbyDeliveryAgentsList.append(temp_dict)
    return render_template('nearbyDeliveryAgent.html', nearbyDeliveryAgentsList = nearbyDeliveryAgentsList)

    


# This function will show all the delivery request for the customer in the region that are sent by the restaurants
@views.route('/seeDeliveryRequest')
def seeDeliveryRequest():

    if session['user']['userType']!='deliveryAgent':
        return redirect(url_for('Auth.logout'))
    
    area = session['user']['area']

    deliveryRequestList=[]

    restaurants = db.collection('restaurant').stream()
    for res in restaurants:
        temp = res.to_dict()
        if temp['area']!=area:
            continue

        for id in temp['pendingOrderId']:
            order_dict = db.collection('order').document(id).get().to_dict()
            if order_dict['updateLevel']==2:
                order_dict['restaurant']=db.collection('restaurant').document(order_dict['restaurantId']).get().to_dict()
                order_dict['customer']=db.collection('customer').document(order_dict['customerId']).get().to_dict()
                deliveryRequestList.append(order_dict)

    # areaId=session['user']['areaId']

    # orderIdForADeliveryAgent=db.collection('area').document(areaId).get().to_dict()['availableOrderIdForPickup']
    # deliveryRequestList=[]

    # for orderId in orderIdForADeliveryAgent:
    #     temp_dict=db.collection('order').document(orderId).get().to_dict()

    #     if temp_dict['isPending']==True: # it will be true , just doing it to be on the safe side
    #         temp_dict['restaurant']=db.collection('restaurant').document(temp_dict['restaurantId']).get().to_dict()
    #         temp_dict['customer']=db.collection('customer').document(temp_dict['customerId']).get().to_dict()
    #         #temp_dict['area']=db.collection('area').document(areaId).get().to_dict()
    #         deliveryRequestList.append(temp_dict)
    session['currentDeliveryRequest'] = deliveryRequestList
    session.modified = True
    return render_template("seeDeliveryRequest.html", deliveryRequestList = deliveryRequestList)



# This function will accept delivery request with getting the expected time of arrival and delivery from the delivery agent
# It will also update the status of the order to show to the customer
@views.route('/acceptDeliveryRequest', methods=['POST', 'GET'])
def acceptDeliveryRequest():
    
    if session['user']['userType']!='deliveryAgent':
        return redirect(url_for('logout'))
    
    user = session['user']
    timeToReachRestaurant = request.form['timeToRestaurant']
    timeToReachCustomer = request.form['timeToCustomer']
    updateOrderDic = {
        "timePickUp" : timeToReachRestaurant,
        "deliveryTime" : timeToReachCustomer
    }
    db.collection('order').document(session['currentOrderDeliveryAgent']['orderId']).update({'deliveryAgentId': user['deliveryAgentId']})
    db.collection('order').document(session['currentOrderDeliveryAgent']['orderId']).update({'updateMessage': "Order Accepted by Delivery Agent"})
    db.collection('order').document(session['currentOrderDeliveryAgent']['orderId']).update({'updateLevel': 3})
    db.collection('order').document(session['currentOrderDeliveryAgent']['orderId']).update({'orderUpdates' : firestore.ArrayUnion([updateOrderDic])})
    # print(session['currentOrderDeliveryAgent']['orderId'])
    # db.collection('area').document(session['sessionUser']['areaId']).update({'availableOrderIdForPickup' : firestore.ArrayRemove([session['currentOrderDeliveryAgent']['orderId']])})
    db.collection('deliveryAgent').document(user['deliveryAgentId']).update({"isAvailable" : not user['isAvailable']})
    db.collection('deliveryAgent').document(user['deliveryAgentId']).update({"currentOrderId" : session['currentOrderDeliveryAgent']['orderId']})

    return redirect(url_for('moreDetailsDeliveryRequest', status = "Details"))


@views.route('/markLocation',methods=['POST','GET'])
def markLocation():
    if session['user']['userType']!='deliveryAgent':
        return redirect(url_for('Auth.logout'))


















    