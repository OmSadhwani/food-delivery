import React, {useState, useEffect} from 'react';
import '../../App.css';

function RecentOrderCustomer(){
    const [orders,setorders] = useState({});

    const handlemessage = (msg) => {
    setorders(msg)
    }

    
    useEffect(() => {fetch('/recentOrderCustomer' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            // console.log(message["user"])
            handlemessage(message)
        ))},[])
    
        function handleButtonClick(menuURL) {
            window.location.href = "/moreDetailsOrder/".concat(menuURL)
          }
    
    return(
        <>
        
            <div>
            <h2>Restaurants</h2>
            <ul>
                {orders.map((order) => (
                <li key={order['orderId']}>
                    {order['restaurantName']}{' '}
                    {/* restid=restaurant['restaurantId']
                    */}
                    {order['orderValue']}
                    {order['updateMessage']}
                    <button onClick={() => handleButtonClick(order['orderId'])}>More Details</button>
                </li>
                ))}
            </ul>
            </div>

        </>
    )

}

export default RecentOrderCustomer;