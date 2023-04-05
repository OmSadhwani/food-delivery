import React, {useState, useEffect} from 'react';
import '../../App.css';

function CustomerDashboard() {
    
    const [username,setusername] = useState('');

    const handlemessage = (msg) => {
    setusername(msg)
    }

    fetch('/customerDashboard' , {
        method:"POST",
      }).then(response => response.json())
        .then(message => (
            // console.log(message["user"])
            handlemessage(message["name"])
        ))

    const Redirect1 = (event) => {
        window.location.href='/order'
    }

    const Redirect2 = (event) => {
        window.location.href='/personalData'
    }

    const Redirect3 = (event) => {
        window.location.href='/recommendedRestaurant'        //not in backend
    }

    const Redirect4 = (event) => {
        window.location.href='/allRestaurant'
    }

    const Redirect5 = (event) => {
        window.location.href='/presentOrders'           //not in backend
    }

    const Redirect6 = (event) => {
        window.location.href='/pastOrders'                      //not in backend
    }

    return(
        <>
            <div className="Welcome">
            <h1>Welcome {username}</h1>    
            </div>     
            <div className="options">
                <button onClick={Redirect1}>Order Now</button>
            </div>
            <div className="options">
                <button onClick={Redirect2}>Personal Details</button>
            </div>
            <div className="options">
                <button onClick={Redirect3}>Recommeded Restaurants</button>
            </div>
            <div className="options">
                <button onClick={Redirect4}>All Restaurants</button>
            </div>
            <div className="options">
                <button onClick={Redirect5}>Present Orders</button>
            </div>
            <div className="options">
                <button onClick={Redirect6}>Past Orders</button>
            </div>
        </>
    );
}

export default CustomerDashboard;