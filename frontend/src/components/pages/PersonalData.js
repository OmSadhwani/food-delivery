import React from 'react';
import { useState, useEffect } from 'react';
import '../../App.css';
import Navbar from '../Navbar';
import NavbarC from '../NavbarC'

export default function PersonalData() {

  const [details,setdetails] = useState({});

  // useEffect(() => {
  //   fetch('/').then(
  //     response => response.json()
  //   ).then(data => setInitialData(data))
  // }, []);

    useEffect (() => { fetch('/personalData' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            // console.log(message),
            setdetails(message)
        ))},[])
  return (
    <>
    <NavbarC></NavbarC>
          <div>
        Address<br/>
        {details['address']}
      </div>
      <br/>
      <div>
        Area <br/>
        {details['area']}
      </div>
      <br/>
      <div>
        customerID <br/>
        {details['customerId']}
      </div>
      <br/>
      <div>
        Email <br/>
        {details['email']}
      </div>    <br/>   <div>
        Gender <br/>
        {details['gender']}
      </div>     <br/>     <div>
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
        Pending Order ID <br/>
        {details['pendingOrderId']}
      </div>
      <br/>   <div>
        userType <br/>
        {details['userType']}
        </div>
        {/* <div>Hello World</div> */}
    </>
  )
}