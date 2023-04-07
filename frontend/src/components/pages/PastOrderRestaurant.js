import React, {useState, useEffect} from 'react';
import '../../App.css';

function PastOrderRestaurant(){
    const [orders,setorders] = useState([]);

    const handlemessage = (msg) => {
    setorders(msg)
    }


    useEffect(() => {fetch('/pastOrder' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            // console.log(message["user"])
            handlemessage(message["pastOrderlist"])
        ))},[])

    return(
        <>
            <div>
            <h2>Order Details</h2>
            <ul>
                {orders.map((pastOrder) => (
                <li key={['pastOrderlist']}>
                    <ul>
                        OrderId: {pastOrder["orderId"]}
                        Date&time: {pastOrder["orderDateTime"]}
                        {pastOrder.orderList.map((item) => (
                        <li key={['pastOrderlist']}>
                            Name: {item["name"]}
                            Quantity: {item["frequency"]}
                            pricePerItem: {item["pricePerItem"]}


                        </li>
                        
                    ))}
                        discount: {pastOrder["dicountValue"]}
                        delivery charge: {pastOrder["deliveryCharge"]}
                        Total : {pastOrder["orderValue"]}

                    </ul>
                </li>
                ))}
            </ul>
            </div>
        </>
    );

}
export default PastOrderRestaurant;