// import React, {useState, useEffect} from 'react';
// import '../../App.css';
// import { useParams } from 'react-router-dom';




// function AcceptReject(){
// // if accept open form to give estimated time

//     const handleClick1 = (event) => {
//         window.location.href='/giveEstimatedTime'
//     }
//     const handleClick2 = (event) => {
//         window.location.href='/pendingOrdersRestaurant'
//     }
//     return(
//         <>
//             <button onClick={handleClick1}>Accept</button>
//             <br/>
//             <button onClick={handleClick2}>Reject</button>
//         </>
//     );
// }

// function FoodPrepared(){
//     const handleClick3 = (event) => {
//         window.location.href='/sendDeliveryRequest'
//     }
//     return(
//         <button onClick={handleClick3}>Food Prepared</button>
//     );
// }

// function OutforDelivery(){
//     const handleClick4 = (event) => {
//         window.location.href='/restaurantDashboard'
//     }
//     return(
//         <button onClick={handleClick4}>Out For Delivery</button>
//     );
// }

// function Done(){
//     return(

//     );
// }

// // 0 - ask for accept reject
// // 1 - accepted or rejected show updateMessage if updateMessage = 'Accepted. Preparing Food'  'Rejected'
// // 2 - if delivery request sent then state 2 
// // 3 - out for delivery 
// //4 - when delivered



// function OrderDetailsRestaurant(){

//     const id = useParams()

//     const [details,setdetails] = useState({});
//     const [orderList,setorderList] = useState([]);

//     const handlemessage = (msg) => {
//         setdetails(msg)
//         setorderList(msg['orderList'])
//     }

    
//     useEffect(() => {fetch('/orderDetailRestaurant/:id' , {
//         method:"POST",
//         body:JSON.stringify(id),
//       }).then(response => response.json())
//         .then(message => (
//             console.log(message),
//             handlemessage(message)
//         ))},[])
    
//         // function handleButtonClick(menuURL) {
//         //     window.location.href = "/orderDetailRestaurant/".concat(menuURL)
//         //   }
    
//     let message;

//     if(details['updateLevel'] == '0'){
//         message = <AcceptReject/>
//     }
//     else if(details['updateLevel'] == '1'){
//         message=<FoodPrepared/>
//     }
//     else if(details['updateLevel'] == '2'){
//         message=<OutforDelivery/>
//     }
//     else if(details['updateLevel'] == '3'){
//         message=<Done/>
//     }
    
//     return(
//         <>
        
//             <div>
//             <h2>Order Details</h2>
//             </div>
//             <div>
//                 Customer : {details['customerName']}
//             </div>
//             <br/>
//             <div>
//                 <table class='my-table'>
//                     <tr>
//                     <th>
//                         Item
//                     </th>
//                     <th>
//                         Price per Item
//                     </th>
//                     <th>
//                         Quantity
//                     </th>
//                     <th>
//                         Cost
//                     </th>
//                     </tr>
                    
//                     {orderList.map((m) => (
//           <tr>
//             <td>{m['name']}</td>
//             <td>{m['pricePerItem']}</td>
//             <td>{m['frequency']}</td>
//             <td>{m['frequency']*m['pricePerItem']}</td>
//             </tr>
//       ))}


//                 </table>
//                 <br/>
//                 <table class='my-table'>
//                     <tr>
//                         <th>Base Price</th>
//                         <th>Delivery Charge</th>
//                         <th>Discount</th>
//                         <th>Amount to Pay</th>
//                     </tr>
//                     <tr>
//                         <td>{details['cost']}</td>
//                         <td>{details['deliveryCharge']}</td>
//                         <td>{details['discount']}</td>
//                         <td>{details['final']}</td>
//                     </tr>
//                 </table>
//             </div>
//             <div>
//                 {message}
//             </div>
//         </>
//     )

// }

// export default OrderDetailsRestaurant;