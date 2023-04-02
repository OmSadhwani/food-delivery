from flask import Blueprint, request, redirect, url_for, session, render_template
from .models import db,pyrebase_pb,areas
from firebase_admin import auth
import time


Auth = Blueprint('Auth',__name__)


@Auth.route('/customerLogin',methods=['GET','POST'])
def customerLogin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:

            time.sleep(0.01)
            user = pyrebase_pb.auth().sign_in_with_email_and_password(email, password)

            type_json = db.collection("userType").document(user["localId"]).get().to_dict()
            print(type_json)
            if (type_json["type"]!="customer"):
                print("Invalid credentials!")
                return redirect(url_for('Auth.customerLogin'))

            json_data = db.collection("customer").document(user["localId"]).get().to_dict()
            session['user'] = json_data
            session['user']['userType'] = "customer"

            return redirect(url_for('views.customerDashboard'))


        except Exception as e:
            print(e)
            print("Unable to process request")
            return redirect(url_for('Auth.customerLogin'))

    return render_template('customer-login.html')



@Auth.route('/customerSignup',methods=['GET','POST'])
def customerSignup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        gender = request.form.get('email')
        mobile = request.form.get('mobile')
        area = request.form.get('area')
        address = request.form.get('address')

        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        #checks...
        if len(name)<2 or len(address)<2 or password!=confirm_password:
            if(len(name))<2:
                print("Name is too short")
            elif len(address)<2:
                print("Address is too short")
            elif password!=confirm_password:
                print("Both the passwords don't match")

            return render_template('customer-signup.html',
                            name=name,
                            email=email,
                            gender=gender,
                            mobile=mobile,
                            area=area,
                            address=address,
                            areas=areas)

        elif area=="Other":
            print("We currently don't deliver in your area.")
            return redirect(url_for("Auth.customerSignup"))
        else:
            #add user to database
            try:

                user = auth.create_user(email=email, password=password)

            except ValueError as v:
                print("Error: "+str(v))
                return render_template('customer-signup.html',
                                            name=name,
                                            email=email,
                                            gender=gender,
                                            mobile=mobile,
                                            area=area,
                                            address=address,
                                            areas=areas)

            except Exception as e:
                print("Error: "+str(e))
                print("Unable to process request!")
                return render_template('customer-signup.html',
                                            name=name,
                                            email=email,
                                            gender=gender,
                                            mobile=mobile,
                                            area=area,
                                            address=address,
                                            areas=areas)
            
            try:
                rating_ref = db.collection("rating").document()
                rating_json_data = {"inputs":0, "sum":0.0, "rating":0.0, "ratingId":rating_ref.id}
                rating_ref.set(rating_json_data)

                customer_json_data = {
                    "name": name,
                    "email": email,
                    "customerId":user.uid,
                    "ratingId":rating_ref.id,
                    "gender": gender,
                    "mobileNumber": mobile,
                    "areaId": area,
                    "address": address,
                    "pendingOrderId": []
                    #fill it up....
                }
                db.collection("customer").document(user.uid).set(customer_json_data)
                db.collection("userType").document(user.uid).set({"type":"customer"})
                
            except Exception as e:
                print("Error: "+str(e))
                print("Unable to process request!")
                return redirect(url_for('Auth.customerSignup'))

            print("Successfully signed up. Now login with the same credentials!")
            return redirect(url_for('Auth.customerLogin'))
     
    return render_template('customer-signup.html',areas=areas)



@Auth.route('/restaurantLogin',methods=['GET','POST'])
def restaurantLogin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:

            time.sleep(0.01)
            user = pyrebase_pb.auth().sign_in_with_email_and_password(email, password)

            type_json = db.collection("userType").document(user["localId"]).get().to_dict()
            if (type_json["type"]!="restaurant"):
                print("Invalid credentials!")
                return redirect(url_for('Auth.restaurantLogin'))


            json_data = db.collection("restaurant").document(user["localId"]).get().to_dict()

            session['user'] = json_data
            session['user']['userType'] = "restaurant"

            return redirect(url_for('views.restaurantDashboard'))


        except Exception as e:
            print(e)
            print("Unable to process request")
            return redirect(url_for('Auth.restaurantLogin'))

    return render_template('restaurant-login.html')


@Auth.route('/restaurantSignup',methods=['GET','POST'])
def restaurantSignup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        area = request.form.get('area')

        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        #checks...
        if len(name)<2 or password!=confirm_password:
            if len(name)<2:
                print("Name is too short")
            else:
                print("Both the passwords don't match!")

            return render_template('restaurant-signup.html',
                            name=name,
                            email=email,
                            area=area,
                            areas=areas)
        elif area=="Other":
            print("We currently don't have service in your area.")
            return redirect(url_for('Auth.restaurantSignup'))
        else:
            #add user to database
            try:

                user = auth.create_user(email=email, password=password)

            except ValueError as v:
                print("Error: "+str(v))
                return render_template('restaurant-signup.html',
                                name=name,
                                email=email,
                                area=area,
                                areas=areas)

            except Exception as e:
                print("Error: "+str(e))
                print("Unable to process request!")
                return render_template('restaurant-signup.html',
                                name=name,
                                email=email,
                                area=area,
                                areas=areas)
            
            try:
                rating_ref = db.collection("rating").document()
                rating_json_data = {"inputs":0, "sum":0.0, "rating":0.0, "ratingId":rating_ref.id}
                rating_ref.set(rating_json_data)

                restaurant_json_data = {
                    "name": name,
                    "email": email,
                    "restaurantId":user.uid,
                    "ratingId":rating_ref.id,
                    "areaId": area,
                    "pendingOrderId": [],
                    "isRecommended": False
                    #fill it up....
                }
                db.collection("restaurant").document(user.uid).set(restaurant_json_data)
                db.collection("userType").document(user.uid).set({"type":"restaurant"})
                
            except Exception as e:
                print("Error: "+str(e))
                print("Unable to process request!")
                return redirect(url_for('Auth.restaurantSignup'))

            print("Successfully signed up. Now login with the same credentials!")
            return redirect(url_for('Auth.restaurantLogin'))
     
    return render_template('restaurant-signup.html',areas=areas)



@Auth.route('/deliveryAgentLogin',methods=['GET','POST'])
def deliveryAgentLogin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:

            time.sleep(0.01)
            user = pyrebase_pb.auth().sign_in_with_email_and_password(email, password)

            type_json = db.collection("userType").document(user["localId"]).get().to_dict()
            if (type_json["type"]!="deliveryAgent"):
                print("Invalid credentials!")
                return redirect(url_for('Auth.deliveryAgentLogin'))


            json_data = db.collection("deliveryAgent").document(user["localId"]).get().to_dict()

            session['user'] = json_data
            session['user']['userType'] = "deliveryAgent"

            return redirect(url_for('views.deliveryAgentDashboard'))


        except Exception as e:
            print(e)
            print("Unable to process request")
            return redirect(url_for('Auth.deliveryAgentLogin'))

    return render_template('deliveryAgent-login.html')

@Auth.route('/deliveryAgentSignup',methods=['GET','POST'])
def deliveryAgentSignup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        gender = request.form.get('gender')
        area = request.form.get('area')
        mobile = request.form.get('mobile')

        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        #checks...
        if len(name)<2 or password!=confirm_password:
            if len(name)<2:
                print("Name is too short")
            elif password!=confirm_password:
                print("Both the passwords don't match!")

            return render_template('deliveryAgent-signup.html',
                            name=name,
                            email=email,
                            gender=gender,
                            area=area,
                            mobile=mobile,
                            areas=areas)
        
        elif area=="Other":
            print("We currently don't have service in your area.")
            return redirect(url_for('Auth.deliveryAgentSignup'))
        
        else:
            #add user to database
            try:

                user = auth.create_user(email=email, password=password)

            except ValueError as v:
                print("Error: "+str(v))
                return render_template('deliveryAgent-signup.html',
                                name=name,
                                email=email,
                                gender=gender,
                                area=area,
                                mobile=mobile,
                                areas=areas)

            except Exception as e:
                print("Error: "+str(e))
                print("Unable to process request!")
                return render_template('deliveryAgent-signup.html',
                                name=name,
                                email=email,
                                gender=gender,
                                area=area,
                                mobile=mobile,
                                areas=areas)
            
            try:
                rating_ref = db.collection("rating").document()
                rating_json_data = {"inputs":0, "sum":0.0, "rating":0.0, "ratingId":rating_ref.id}
                rating_ref.set(rating_json_data)

                deliveryAgent_json_data = {
                    "name": name,
                    "email": email,
                    "deliveryAgentId":user.uid,
                    "ratingId":rating_ref.id,
                    "mobileNumber": mobile,
                    "gender": gender,
                    "areaId": area,
                    "isAvailable": True,
                    "currentOrderId": ""
                    #fill it up....
                }
                db.collection("deliveryAgent").document(user.uid).set(deliveryAgent_json_data)
                db.collection("userType").document(user.uid).set({"type":"deliveryAgent"})
                
            except Exception as e:
                print("Error: "+str(e))
                print("Unable to process request!")
                return redirect(url_for('Auth.deliveryAgentSignup'))

            print("Successfully signed up. Now login with the same credentials!")
            return redirect(url_for('Auth.deliveryAgentLogin'))
     
    return render_template('deliveryAgent-signup.html',areas=areas)



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
    return redirect(url_for('views.home'))