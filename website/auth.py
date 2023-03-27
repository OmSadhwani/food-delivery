from flask import Blueprint, request, redirect, url_for, session, render_template
from . import db,pyrebase_pb
from firebase_admin import auth
import time


Auth = Blueprint('Auth',__name__)


@Auth.route('/customerLogin',methods=['GET','POST'])
def customerLogin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            # #user = pyrebase_pb.Auth().sign_in_with_email_and_password(email,password)
            # print("s1")
            # # user = auth.get_user_by_email(email)
            # time.sleep(0.05)
            # user = pyrebase_pb.auth().sign_in_with_email_and_password(email, password)
            # print('s2')
            # # if pyrebase_pb.auth().verify_password(password, user.password_hash)==False:
            # #     print("pass")
            # #     pass #wrong password

            # if user.custom_claims.get("userType") != "customer":
            #     print("cust")
            #     pass #not a customer
            time.sleep(0.01)
            auth_user = auth.get_user_by_email(email)
            uid = auth_user.uid
            auth_user = auth.update_user(uid,email=email,password=password)

            custom_claims = {"userType":"customer"}

            if not (auth.get_user(uid).custom_claims == custom_claims):
                #wrong credentials
                print("wrong credentials!")
                return redirect(url_for('customerLogin'))

            json_data = db.collection("customer").document(uid).get().to_dict()

            session['user'] = json_data
            session['user']['userType'] = "customer"

            return redirect(url_for('views.customerDashboard'))


        except Exception as e:
            #print(e)
            print("Unable to process request")
            return render_template('customer-login.html')

    return render_template('customer-login.html')



@Auth.route('/customerSignup',methods=['GET','POST'])
def customerSignup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password')
        # password2 = request.form.get('password2')

        #checks...
        if len(email)<4:
            pass
        elif len(name)<2:
            pass
        # elif password1!=password2:
        #     pass
        elif len(password1)<3:
            pass
        else:
            #add user to database
            try:
                customer_ref = db.collection("customer")
                query = customer_ref.where('email','==',email).get()
                if len(query) > 0:
                    print("An account with the same email already exists!")
                    return redirect(url_for('customerSignup'))
                else:
                    user = auth.create_user(email=email,password=password1)
                    custom_claims={"userType":"customer"}
                    auth.set_custom_user_claims(user.uid, custom_claims)
            except Exception as e:
                #print(e)
                print("Unable to process request")
                return render_template('customer-signup.html')
            
            try:
                rating_ref = db.collection("rating").document()
                rating_json_data = {"inputs":0, "sum":0.0, "rating":0.0, "ratingId":rating_ref.id}
                rating_ref.set(rating_json_data)

                customer_json_data = {
                    "name": name,
                    "email": email,

                    "customerId":user.uid,
                    "ratingId":rating_ref.id,

                    "pendingOrderId": []
                    #fill it up....
                }
                db.collection("customer").document(user.uid).set(customer_json_data)
                
            except Exception as e:
                #print(e)
                print("Unable to process request")
                return render_template('customer-signup.html')

            #signup successful
            session['user'] = customer_json_data
            session['user']['userType'] = "customer"
            #redirect to the next page
            return redirect(url_for('views.customerDashboard'))
     
    return render_template('customer-signup.html')



@Auth.route('/restaurantLogin',methods=['GET','POST'])
def restaurantLogin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            # #user = pyrebase_pb.Auth().sign_in_with_email_and_password(email,password)
            # print("s1")
            # # user = auth.get_user_by_email(email)
            # time.sleep(0.05)
            # user = pyrebase_pb.auth().sign_in_with_email_and_password(email, password)
            # print('s2')
            # # if pyrebase_pb.auth().verify_password(password, user.password_hash)==False:
            # #     print("pass")
            # #     pass #wrong password

            # if user.custom_claims.get("userType") != "customer":
            #     print("cust")
            #     pass #not a customer
            time.sleep(0.01)
            auth_user = auth.get_user_by_email(email)
            uid = auth_user.uid
            auth_user = auth.update_user(uid,email=email,password=password)

            custom_claims = {"userType":"restaurant"}

            if not (auth.get_user(uid).custom_claims == custom_claims):
                #wrong credentials
                print("wrong credentials!")
                return redirect(url_for('restaurantLogin'))

            json_data = db.collection("restaurant").document(uid).get().to_dict()

            session['user'] = json_data
            session['user']['userType'] = "restaurant"

            return redirect(url_for('views.restaurantDashboard'))


        except Exception as e:
            #print(e)
            print("Unable to process request")
            return render_template('restaurant-login.html')

    return render_template('restaurant-login.html')


@Auth.route('/restaurantSignup',methods=['GET','POST'])
def restaurantSignup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        area = request.form.get('area')
        password1 = request.form.get('password1')
        # password2 = request.form.get('password2')


        #checks...
        if len(email)<4:
            pass
        elif len(name)<2:
            pass
        # elif password1!=password2:
        #     pass
        elif len(password1)<3:
            pass
        else:
            #add user to database
            try:
                restaurant_ref = db.collection("restaurant")
                query = restaurant_ref.where('email','==',email).get()
                if len(query) > 0:
                    print("An account with the same email already exists!")
                    return redirect(url_for('restaurantSignup'))
                else:
                    user = auth.create_user(email=email,password=password1)
                    custom_claims={"userType":"restaurant"}
                    auth.set_custom_user_claims(user.uid, custom_claims)
            except Exception as e:
                #print(e)
                print("Unable to process request")
                return render_template('restaurant-signup.html')
            
            try:
                rating_ref = db.collection("rating").document()
                rating_json_data = {"inputs":0, "sum":0.0, "rating":0.0, "ratingId":rating_ref.id}
                rating_ref.set(rating_json_data)

                restaurant_json_data = {
                    "name": name,
                    "email": email,

                    "restaurantId":user.uid,
                    "ratingId":rating_ref.id,

                    "areaId" : area,

                    "pendingOrderId": [],

                    "isRecommended":False
                    #fill it up....
                }
                db.collection("restaurant").document(user.uid).set(restaurant_json_data)
            except:
                #print(e)
                print("Unable to process request")
                return render_template('restaurant-signup.html')

            #signup successful
            session['user'] = restaurant_json_data
            session['user']['userType'] = "restaurant"
            #redirect to the next page
            return redirect(url_for('restaurantDashboard'))

    return render_template('restaurant-signup.html')



@Auth.route('/deliveryAgentLogin',methods=['GET','POST'])
def deliveryAgentLogin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            # #user = pyrebase_pb.Auth().sign_in_with_email_and_password(email,password)
            # print("s1")
            # # user = auth.get_user_by_email(email)
            # time.sleep(0.05)
            # user = pyrebase_pb.auth().sign_in_with_email_and_password(email, password)
            # print('s2')
            # # if pyrebase_pb.auth().verify_password(password, user.password_hash)==False:
            # #     print("pass")
            # #     pass #wrong password

            # if user.custom_claims.get("userType") != "customer":
            #     print("cust")
            #     pass #not a customer
            time.sleep(0.01)
            auth_user = auth.get_user_by_email(email)
            uid = auth_user.uid
            auth_user = auth.update_user(uid,email=email,password=password)

            custom_claims = {"userType":"deliveryAgent"}

            if not (auth.get_user(uid).custom_claims == custom_claims):
                #wrong credentials
                print("wrong credentials!")
                return redirect(url_for('deliveryAgentLogin'))

            json_data = db.collection("deliveryAgent").document(uid).get().to_dict()

            session['user'] = json_data
            session['user']['userType'] = "deliveryAgent"

            return redirect(url_for('views.deliveryAgentDashboard'))


        except Exception as e:
            #print(e)
            print("Unable to process request")
            return render_template('deliveryAgent-login.html')

    return render_template('deliveryAgent-login.html')

@Auth.route('/deliveryAgentSignup',methods=['GET','POST'])
def deliveryAgentSignup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        area = request.form.get('area')
        password1 = request.form.get('password1')
        # password2 = request.form.get('password2')


        #checks...
        if len(email)<4:
            pass
        elif len(name)<2:
            pass
        # elif password1!=password2:
        #     pass
        elif len(password1)<3:
            pass
        else:
            #add user to database
            try:
                delivery_ref = db.collection("deliveryAgent")
                query = delivery_ref.where('email','==',email).get()
                if len(query) > 0:
                    #print(e)
                    print("An account with the same email already exists!")
                    return render_template('deliveryAgent-signup.html')
                else:
                    user = auth.create_user(email=email,password=password1)
                    custom_claims={"userType":"deliveryAgent"}
                    auth.set_custom_user_claims(user.uid, custom_claims)
            except:
               #print(e)
                print("Unable to process request")
                return render_template('deliveryAgent-signup.html')
            
            try:
                rating_ref = db.collection("rating").document()
                rating_json_data = {"inputs":0, "sum":0.0, "rating":0.0, "ratingId":rating_ref.id}
                rating_ref.set(rating_json_data)

                del_agent_json_data = {
                    "name": name,
                    "email": email,

                    "deliveryAgentId":user.uid,
                    "ratingId":rating_ref.id,

                    "areaId" : area,

                    "pendingOrderId": [],

                    "isAvailable":True,
                    "currentOrderId":""
                    #fill it up....
                }
                db.collection("deliveryAgent").document(user.uid).set(del_agent_json_data)
            except:
               #print(e)
                print("Unable to process request")
                return render_template('deliveryAgent-signup.html')

            #signup successful
            session['user'] = del_agent_json_data
            session['user']['userType'] = "deliveryAgent"
            #redirect to the next page
            return redirect(url_for('deliveryAgentDashboard'))

     
    return render_template('deliveryAgent-signup.html')



@Auth.route('/managementLogin',methods=['GET','POST'])
def managementLogin():
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     password = request.form.get('password')

    #     #....to complete..
     
    return "<p>management login page</p>"

@Auth.route('/managementSignup',methods=['GET','POST'])
def managementSignup():
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     password = request.form.get('password')

    #     #....to complete..
     
    return "<p>management sign up page</p>"


@Auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))