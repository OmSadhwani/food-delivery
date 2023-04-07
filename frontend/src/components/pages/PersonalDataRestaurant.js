import React from 'react';
import { useState, useEffect } from 'react';
import '../../App.css';
import Navbar from '../Navbar';

export default function PersonalDataRestaurant() {

  const [details,setdetails] = useState({});

  // useEffect(() => {
  //   fetch('/').then(
  //     response => response.json()
  //   ).then(data => setInitialData(data))
  // }, []);
  useEffect(() => {
    fetch('/personalData' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            console.log(message)
            // setdetails(message)
        ))},[])
  return (
    <>
      <div>
        Area <br/>
        {details['area']}
      </div>
      <br/>
      <div>
        CurrentOrderId <br/>
        {details['currentOrderId']}
      </div> 
      <br/>   <div>
        Is Recommended <br/>
        {String(details['isRecommended'])}
      </div>     <br/>  <div>
        Email <br/>
        {details['email']}
      </div>   <br/>   <div>
        Name <br/>
        {details['name']}
      </div>
      <br/>   <div>
        Rating Value <br/>
        {details['ratingValue']}
      </div>
      <div>
        restaurantId <br/>
        {details['restaurantId']}
      </div>
    </>
  )
}