import React, {useState, useEffect} from 'react';
import '../../App.css';

function PastOrders(){
    const [orders,setorders] = useState([]);

    const handlemessage = (msg) => {
    setorders(msg)
    }


    useEffect(() => {fetch('/pastOrder' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            console.log(message["pastOrderist"]),
            handlemessage(message["pastOrderlist"])
        ))},[])

    return(
        <>
            <div className="PastOrders">
            <h1>Order Details</h1><br/><br/><br/>
            <ul>
                {orders.map((pastOrder) => (
                <li key={['pastOrderlist']}>
                    <ul>
                        <h3>
                        OrderId: {pastOrder["orderId"]} &nbsp;&nbsp;
                        Date&time: {pastOrder["orderDateTime"]}
                        </h3>
                        

                        <table className='my-table'>
                            <thead>
                                <tr>
                                    <th>Item Name</th>
                                    <th>Quantity</th>
                                    <th>Price per Item</th>
                                </tr>
                            </thead>

                            <tbody>
                            {pastOrder.orderList.map((item) => (
                                <tr>
                                    <td>{item['name']}</td>
                                    <td>{item['frequency']}</td>
                                    <td>{item['pricePerItem']}</td>
                                </tr>
                        
                    ))}

                            </tbody>
                        </table>
                        <br/><br/>
                        <h3>                        Discount: {pastOrder["dicountValue"]}&nbsp;
                        Delivery charge: {pastOrder["deliveryCharge"]}&nbsp;
                        Base Price : {pastOrder["orderValue"]}</h3>

                    </ul>
                    <br/><br/>
                    <h6 className="gradient" >&nbsp;</h6>
                    <br/><br/>
                </li>
                ))}
                <br/><br/><br/>
                
            </ul>

            
            </div>
        </>
    );

}
export default PastOrders;