from flask import Blueprint, session, redirect, url_for, render_template

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
        return redirect(url_for('logout'))

    # return "<h2>this is customer dashboard</h2>"


@views.route('/restaurantDashboard')
def restaurantDashboard():
    user = session['user']
    if user['userType']=="restaurant":
        return render_template('restaurant-dashboard.html',user=user)
    else:
        return redirect(url_for('logout'))

    
    # return "<h2>this is restaurant dashboard</h2>"


@views.route('/deliveryAgentDashboard')
def deliveryAgentDashboard():
    user = session['user']
    if user['userType']=="deliveryAgent":
        return render_template('deliveryAgent-dashboard.html',user=user)
    else:
        return redirect(url_for('logout'))

    
    # return "<h2>this is deliveryAgent dashboard</h2>"


@views.route('/adminDashboard')
def adminDashboard():
    # user = session['user']
    # if user['userType']=="admin":
    #     return render_template('adminDashboard',user=user)
    # else:
    #     return redirect(url_for('logout'))

    
    return "<h2>this is admin dashboard</h2>"