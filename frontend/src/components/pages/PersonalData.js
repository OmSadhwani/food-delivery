import React,{useState} from 'react';
import '../../App.css';
import Navbar from '../Navbar';

export default function PersonalData() {

  const [details,setdetails] = useState({});


    fetch('/personalData' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            // console.log(message),
            setdetails(message)
        ))
  return (
    <>
          <div>
        Address<br/>
        {details['address']}
      </div>
      <br/>
      <div>
        Area ID <br/>
        {details['areaId']}
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