import React, {useState, useEffect} from 'react';
import '../../App.css';

function PendingOrderRestaurant(){
    const [orders,setorders] = useState([]);

    const handlemessage = (msg) => {
        setorders(msg)
    }

    
    useEffect(() => {fetch('/recentOrderRestaurant' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            console.log(message),
            handlemessage(message['recentOrders'])
        ))},[])
    
        function handleButtonClick(menuURL) {
            window.location.href = "/orderDetailRestaurant/".concat(menuURL)
          }
          
    
    
    return(
        <>
        
            <div>
            <h2>Pending Orders</h2>
            <ul>
                {orders.map((order) => (
                <li key={order['orderId']}>
                    {order['customerName']}{' '}
                    {order['orderValue']}{' '}
                    {order['updateMessage']}{' '}
                    <button onClick={() => handleButtonClick(order['orderId'])}>More Details</button>
                </li>
                ))}
            </ul>
            </div>

        </>
    )

}

export default PendingOrderRestaurant;