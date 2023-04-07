import React from 'react'
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

export default function MoreDetailsDeliveryRequest(){

    const id= useParams()
    const [details,setdetails] = useState({});
    console.log(id["id"])
    useEffect(() => {fetch('/moreDetailsDeliveryRequest/'.concat(id["id"]) , {
        method:"POST",

        body:JSON.stringify(id),
      }).then(response => response.json())
        .then(message => (
            console.log(message),
            setdetails(message)
        ))},[])

        const handleSubmit = (event) => {
            
            
            window.location.href ='/ratingDeliveryAgent/'.concat(id["id"])
    
            
           
                  
        }

    
        return (
            <>

                <div>
                <h2>Order Details</h2>
                <p>Restaurant Name: {details["restaurantName"]}</p>
                <p>Customer Name: {details["customerName"]}</p>
                <p>Customer Address: {details["address"]}</p>
                <h3>Order List</h3>
                <ul>
                    {details["orderList"].map((item) => (
                    <li>
                        Name: {item["name"]}
                        Quantity: {item["frequency"]}
                    </li>
                    ))}
                </ul>
                            
                </div>
                <div class="footer">
                <button type="submit" className="btn1" onClick={handleSubmit}>Order Delivered</button>
                </div>
            </>
        )



}