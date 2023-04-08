import React from 'react';
import { useState, useEffect } from 'react';
import '../../App.css';

export default function SeeDeliveryRequest() {

    const [requests,setrequests] = useState([]);
    
    
  
      useEffect(() => {fetch('/seeDeliveryRequest' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            
            setrequests(message["deliveryRequestList"])
        ))},[])

        function handleButtonClick(menuURL) {
            window.location.href = "/acceptDeliveryRequest/".concat(menuURL)
          }

    return (
        <div>
            <h1>
                Delivery Requests
            </h1>
            <ul>
                {requests.map((request) => (
                <li>
                    {request['restaurant']["name"]}{' '}
                    {/* restid=restaurant['restaurantId']
                    */}
                    {request['customer']['address']}
                    {request['customer']['name']}
                    {/* {order['updateMessage']} */}
                    <button onClick={() => handleButtonClick(request['orderId'])}>Accept</button>
                </li>
                ))}
            </ul>
        </div>
    );


}