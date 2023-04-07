import React from 'react';
import { useState, useEffect } from 'react';
import '../../App.css';
import Navbar from '../Navbar';

export default function PersonalDataDeliveryAgent() {

  const [details,setdetails] = useState({});
  // useEffect(() => {
  //   fetch('/').then(
  //     response => response.json()
  //   ).then(data => setInitialData(data))
  // }, []);

    useEffect(() => {fetch('/personalData' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
          // console.log(message)
          setdetails(message)
        ))},[])
  return (
    <>
      <div>
        Area <br/>
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
        {String(details['isAvailable'])}
      </div>    <br/>   <div>
        Mobile Number <br/>
        {details['mobileNumber']}
      </div>    <br/>   <div>
        Name <br/>
        {details['name']}
      </div>    
      <br/>   <div>
        userType <br/>
        {details['userType']}
        </div>
        <br/>   <div>
        Rating <br/>
        {details['ratingValue']}
        </div>

    </>
  )
}