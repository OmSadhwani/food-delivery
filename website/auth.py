from flask import Blueprint, request, redirect, url_for
from . import db


auth = Blueprint('auth',__name__)


@auth.route('/customerLogin',methods=['GET','POST'])
def customerLogin():
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     password = request.form.get('password')

    #     #....to complete..

    return "<p>customer login page</p>"

@auth.route('/customerSignup',methods=['GET','POST'])
def customerSignup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #checks...
        if len(email)<4:
            pass
        elif len(name)<2:
            pass
        elif password1!=password2:
            pass
        elif len(password1)<7:
            pass
        else:
            #add user to database
            try:
                customer_ref = db.collection("customer")
                query = customer_ref.where('email','==',email).get()
                if len(query) > 0:
                    pass #????
                else:
                    customer = db.collection("customer").document()
            except:
                pass #???
            
            try:
                rating_ref = db.collection("rating").document()
                rating_json_data = {"inputs":0, "sum":0.0, "rating":0.0, "ratingId":rating_ref.id}
                rating_ref.set(rating_json_data)

                customer_json_data = {
                    "name": name,
                    "email": email,

                    "customerId":customer.id,
                    "ratingId":rating_ref.id,

                    "pendingOrderId": []
                    #fill it up....
                }
                customer.set(customer_json_data)
            except:
                pass #???

            #signup successful
            #redirect to the next page
            return redirect(url_for('customerDashboard'))



        #....to complete..
     
    return "<p>customer sign up page</p>"



@auth.route('/restaurantLogin',methods=['GET','POST'])
def restaurantLogin():
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     password = request.form.get('password')

    #     #....to complete..
     
    return "<p>restaurant login page</p>"

@auth.route('/restaurantSignup',methods=['GET','POST'])
def restaurantSignup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        area = request.form.get('area')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        #checks...
        if len(email)<4:
            pass
        elif len(name)<2:
            pass
        elif password1!=password2:
            pass
        elif len(password1)<7:
            pass
        else:
            #add user to database
            try:
                restaurant_ref = db.collection("restaurant")
                query = restaurant_ref.where('name','==',name).get()
                if len(query) > 0:
                    pass #????
                else:
                    restaurant = db.collection("restaurant").document()
            except:
                pass #???
            
            try:
                rating_ref = db.collection("rating").document()
                rating_json_data = {"inputs":0, "sum":0.0, "rating":0.0, "ratingId":rating_ref.id}
                rating_ref.set(rating_json_data)

                restaurant_json_data = {
                    "name": name,
                    "email": email,

                    "restaurantId":restaurant.id,
                    "ratingId":rating_ref.id,

                    "areaId" : area,

                    "pendingOrderId": [],

                    "isRecommended":False
                    #fill it up....
                }
                restaurant.set(restaurant_json_data)
            except:
                pass #???

            #signup successful
            #redirect to the next page
            return redirect(url_for('restaurantDashboard'))


        #....to complete..
     
    return "<p>restaurant sign up page</p>"



@auth.route('/deliveryAgentLogin',methods=['GET','POST'])
def deliveryAgentLogin():
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     password = request.form.get('password')

    #     #....to complete..
     
    return "<p>deliveryAgent login page</p>"

@auth.route('/deliveryAgentSignup',methods=['GET','POST'])
def deliveryAgentSignup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        area = request.form.get('area')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        #checks...
        if len(email)<4:
            pass
        elif len(name)<2:
            pass
        elif password1!=password2:
            pass
        elif len(password1)<7:
            pass
        else:
            #add user to database
            try:
                delivery_ref = db.collection("deliveryAgent")
                query = delivery_ref.where('email','==',email).get()
                if len(query) > 0:
                    pass #????
                else:
                    deliveryAgent = db.collection("deliveryAgent").document()
            except:
                pass #???
            
            try:
                rating_ref = db.collection("rating").document()
                rating_json_data = {"inputs":0, "sum":0.0, "rating":0.0, "ratingId":rating_ref.id}
                rating_ref.set(rating_json_data)

                del_agent_json_data = {
                    "name": name,
                    "email": email,

                    "deliveryAgentId":deliveryAgent.id,
                    "ratingId":rating_ref.id,

                    "areaId" : area,

                    "pendingOrderId": [],

                    "isAvailable":True,
                    "currentOrderId":""
                    #fill it up....
                }
                deliveryAgent.set(del_agent_json_data)
            except:
                pass #???

            #signup successful
            #redirect to the next page
            return redirect(url_for('deliveryAgentDashboard'))


        #....to complete..
     
    return "<p>deliveryAgent sign up page</p>"



@auth.route('/managementLogin',methods=['GET','POST'])
def managementLogin():
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     password = request.form.get('password')

    #     #....to complete..
     
    return "<p>management login page</p>"

@auth.route('/managementSignup',methods=['GET','POST'])
def managementSignup():
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     password = request.form.get('password')

    #     #....to complete..
     
    return "<p>management sign up page</p>"