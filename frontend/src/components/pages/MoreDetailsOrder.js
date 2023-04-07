import React from 'react'
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function MoreDetailsOrder(){
    const id = useParams()

    const [details,setdetails] = useState([]);
    useEffect(() => {fetch('/moreDetailsOrder/:id' , {
        method:"POST",
        body:JSON.stringify(id),
      }).then(response => response.json())
        .then(message => (
            // console.log(message),
            setdetails(message)
        ))},[])



    return (
        <>
            <div>
            <h2>Order Details</h2>
            
                    <ul>
                        OrderId: {details["orderId"]}
                        Date&time: {details["orderDateTime"]}
                        Resturant Name: {details["restaurantName"]}
                        {details.orderList.map((item) => (
                        <li key={['pastOrderlist']}>
                            Name: {item["name"]}
                            Quantity: {item["frequency"]}
                            pricePerItem: {item["pricePerItem"]}


                        </li>
                        
                    ))}
                    </ul>
                        discount: {details["dicountValue"]}
                        delivery charge: {details["deliveryCharge"]}
                        Total : {details["orderValue"]}

             
            </div>

        </>
    )
}
export default MoreDetailsOrder;







