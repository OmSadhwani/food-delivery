import React, {useState, useEffect} from 'react';
import '../../App.css';

function DeliveryAgentDashboard() {
    
    const [username,setusername] = useState('');

    const handlemessage = (msg) => {
    setusername(msg)
    }

    fetch('/deliveryAgentDashboard' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            // console.log(message["user"])
            handlemessage(message["name"])
        ))

    const Redirect1 = (event) => {
        window.location.href='/personalDataAgent'
    }

    const Redirect2 = (event) => {
        window.location.href='/markLocation'                       //not in backend
    }

    const Redirect3 = (event) => {
        window.location.href='/seeDeliveryRequest'        //not in backend
    }

    const Redirect4 = (event) => {
        window.location.href='/acceptDeliveryRequest'     //not in backend
    }

    const Redirect5 = (event) => {
        window.location.href='/currentOrder'           //not in backend
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
                <button onClick={Redirect2}>Mark Location</button>
            </div>
            <div className="options">
                <button onClick={Redirect3}>See Delivery Request</button>
            </div>
            <div className="options">
                <button onClick={Redirect4}>Accept Delivery Request</button>
            </div>
            <div className="options">
                <button onClick={Redirect5}>See Current Order</button>
            </div>
        </>
    );
}

export default DeliveryAgentDashboard;