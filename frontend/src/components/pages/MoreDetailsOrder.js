import React from 'react'
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function MoreDetailsOrder(){
    const id = useParams()

    const [details,setdetails] = useState({});
    const [orderList,setorderList] = useState([])
    useEffect(() => {fetch('/moreDetailsOrder/:id' , {
        method:"POST",
        body:JSON.stringify(id),
      }).then(response => response.json())
        .then(message => (
            console.log(message),
            setdetails(message),
            setorderList(message['orderList'])
        ))},[])



    return (
        <>
            <div>
            <h2>Order Details</h2>
            
                    <ul>
                        {/* <li>OrderId: {details["orderId"]}</li> */}
                        <li>Date&time: {details["orderDateTime"]}</li>
                        <li>Resturant Name: {details["restaurantName"]}</li>
                        {orderList.map((item) => (
                        <li>
                            Name: {item["name"]}
                            Quantity: {item["frequency"]}
                        </li>
                        
                    ))}
                        <li>discount: {details["discount"]}</li>
                        <li>delivery charge: {details["deliveryCharge"]}</li>
                        <li>Total : {details["cost"]}</li>
                    </ul>

             
            </div>

        </>
    )
}
export default MoreDetailsOrder;







