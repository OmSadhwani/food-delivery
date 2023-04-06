import React,{useState} from 'react';
import '../../App.css';
import Navbar from '../Navbar';

export default function PersonalDataRestaurant() {

  const [details,setdetails] = useState({});


    fetch('/personalData' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            console.log(message)
            // setdetails(message)
        ))
  return (
    <>
      {/* <div>
        Area ID <br/>
        {details['areaId']}
      </div>
      <br/>
      <div>
        CurrentOrderId <br/>
        {details['currentOrderId']}
      </div>    <br/>   <div>
        Delivery Agent ID <br/>
        {details['deliveryAgentId']}
      </div>     <br/>  <div>
        Email <br/>
        {details['email']}
      </div>    <br/>   <div>
        Gender <br/>
        {details['gender']}
      </div>     <br/>  <div>
        Status (Availability) <br/>
        {details['isAvailable'].toString()}
      </div>    <br/>   <div>
        Mobile Number <br/>
        {details['mobileNumber']}
      </div>    <br/>   <div>
        Name <br/>
        {details['name']}
      </div>    <br/>   <div>
        Rating ID <br/>
        {details['ratingId']}
      </div>
      <br/>   <div>
        userType <br/>
        {details['userType']}
        </div> */}
    </>
  )
}