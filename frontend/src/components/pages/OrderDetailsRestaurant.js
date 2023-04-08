import React, {useState, useEffect} from 'react';
import '../../App.css';
import { useParams } from 'react-router-dom';


function AcceptReject(props){

    const handlemessage = (msg) => {
        if(msg == "Success"){
            window.location.href='/pendingOrdersRestaurant'
        }
        else{
            
        }
    }
    const handleClick1 = (event) => {
        const id=props.det

        window.location.href='/giveEstimatedTime/'.concat(id)
    }
    const handleClick2 = (event) => {
        fetch('/updateStatus0' , {
            method:"POST",
            body:JSON.stringify({'ordid':props.det})
          }).then(response => response.json())
            .then(message => (
                handlemessage(message['message'])
            ))
        
        
    }
    return(
        <>
            <button onClick={handleClick1}>Accept</button>
            <br/>
            <button onClick={handleClick2}>Reject</button>
        </>
    );
}

function FoodPrepared(props){
    const handleClick3 = (event) => {
        window.location.href='/sendDeliveryRequest/'.concat(props.det)
    }
    return(
        <button onClick={handleClick3}>Food Prepared</button>
    );
}

function OutforDelivery(props){

    const [success,setsuccess]=useState('')

    const handleSuccess = (msg) => {
        setsuccess(msg)
        // console.log(msg)
        if (msg == "Success"){
            window.location.href='/pendingOrdersRestaurant'
        }
        else{

        }
    }

    const handleClick4 = (event) => {

        console.log(props.det)
        fetch('/updateStatus3' , {
            method:"POST",
            body:JSON.stringify(props.det),
          }).then(response => response.json())
            .then(message => (
                console.log(message['message']),
                handleSuccess(message['message'])
            ))

    }
    return(
        <button onClick={handleClick4}>Out For Delivery</button>
    );
}


// 0 - ask for accept reject
// 1 - accepted or rejected show updateMessage if updateMessage = 'Accepted. Preparing Food'  'Rejected'
// 2 - if delivery request sent then state 2 
// 3 - out for delivery 
//4 - when delivered



function OrderDetailsRestaurant(){

    const id = useParams()

    const [details,setdetails] = useState({});
    const [orderList,setorderList] = useState([]);
    const [level,setlevel] = useState('')

    const handlemessage = (msg) => {
        setdetails(msg)
        setorderList(msg['orderList'])
        setlevel(msg['currentOrder']['updateLevel'])
    }

    
    useEffect(() => {fetch('/orderDetailRestaurant/:id' , {
        method:"POST",
        body:JSON.stringify(id),
      }).then(response => response.json())
        .then(message => (
            // console.log(message['currentOrder']['orderId']),
            handlemessage(message)
        ))},[])
    
        // function handleButtonClick(menuURL) {
        //     window.location.href = "/orderDetailRestaurant/".concat(menuURL)
        //   }
    
    let message;

    if(level == '0'){
        message = <AcceptReject det={details['currentOrder']['orderId']}/>
    }
    else if(level == '1'){
        message=<FoodPrepared det={details['currentOrder']['orderId']}/>
    }
    else if(level == '2'){
        message=<h2>Delivery Request Sent</h2>
    }
    else if(level == '3'){
        message=<OutforDelivery det={details['currentOrder']['orderId']}/>
    }
    else if(level == '4'){
        message=<h1>Order on its Way!!</h1>
    }
    
    return(
        <>
        
            <div>
            <h2>Order Details</h2>
            </div>
            <div>
                Customer : {details['customerName']}
            </div>
            <br/>
            <div>
                <table class='my-table'>
                    <tr>
                    <th>
                        Item
                    </th>
                    <th>
                        Price per Item
                    </th>
                    <th>
                        Quantity
                    </th>
                    <th>
                        Cost
                    </th>
                    </tr>
                    
                    {orderList.map((m) => (
          <tr>
            <td>{m['name']}</td>
            <td>{m['pricePerItem']}</td>
            <td>{m['frequency']}</td>
            <td>{m['frequency']*m['pricePerItem']}</td>
            </tr>
      ))}


                </table>
                <br/>
                <table class='my-table'>
                    <tr>
                        <th>Base Price</th>
                        <th>Delivery Charge</th>
                        <th>Discount</th>
                        <th>Amount to Pay</th>
                    </tr>
                    <tr>
                        <td>{details['cost']}</td>
                        <td>{details['deliveryCharge']}</td>
                        <td>{details['discount']}</td>
                        <td>{details['final']}</td>
                    </tr>
                </table>
            </div>
            <div>
                {message}
            </div>
        </>
    )

}

export default OrderDetailsRestaurant;