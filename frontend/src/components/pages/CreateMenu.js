import React, {useState, useEffect} from 'react';
import '../../App.css';

function RestaurantDashboard() {
    
    // const [username,setusername] = useState('');

    // const handlemessage = (msg) => {
    // setusername(msg)
    // }

    // fetch('/restaurantDashboard' , {
    //     method:"POST",
    //   }).then(response => response.json())
    //     .then(message => (
    //         // console.log(message["user"])
    //         handlemessage(message["name"])
    //     ))

    const Redirect1 = (event) => {
        window.location.href='/AddFoodItem'
    }

    // const Redirect2 = (event) => {
    //     window.location.href='/createMenu'
    // }

    // const Redirect3 = (event) => {
    //     window.location.href='/presentOrdersforRestaurant'           //not in backend
    // }

    // const Redirect4 = (event) => {
    //     window.location.href='/pastOrdersforRestaurant'                      //not in backend
    // }

    return(
        <>
            <div className="Welcome">
            <h1>Create Menu</h1>    
            </div>     
            <div className="options">
                <button onClick={Redirect1}>Add Food Item</button>
            </div>
        </>
    );
}

export default RestaurantDashboard;