import React, {useState, useEffect} from 'react';
import '../../App.css';

function RestaurantDashboard() {
    
    const [username,setusername] = useState('');

    const handlemessage = (msg) => {
    setusername(msg)
    }

    fetch('/restaurantDashboard' , {
        method:"POST",
      }).then(response => response.json())
        .then(message => (
            // console.log(message["user"])
            handlemessage(message["name"])
        ))

    const Redirect1 = (event) => {
        window.location.href='/personalData'
    }

    const Redirect2 = (event) => {
        window.location.href='/createMenu'
    }

    const Redirect3 = (event) => {
        window.location.href='/presentOrdersforRestaurant'           //not in backend
    }

    const Redirect4 = (event) => {
        window.location.href='/pastOrdersforRestaurant'                      //not in backend
    }
    
    const Redirect5 = (event) => {
        window.location.href='/CurrentMenu'                      //not in backend
    }

    return(
        <>
            <div className="Welcome">
            <h1>Welcome {username}</h1>    
            </div>     
            <div className="options">
                <button onClick={Redirect1}>Personal Details</button>
            </div>
            <div className="options">
                <button onClick={Redirect2}>Create Menu</button>
            </div>
            <div className="options">
                <button onClick={Redirect3}>Pending Orders</button>
            </div>
            <div className="options">
                <button onClick={Redirect4}>Past Orders</button>
            </div>
            <div className="options">
                <button onClick={Redirect5}>See Current Menu</button>
            </div>
        </>
    );
}

export default RestaurantDashboard;