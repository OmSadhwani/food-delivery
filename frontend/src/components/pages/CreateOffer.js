import React from 'react'
import { useState, useEffect } from 'react';

export default function CreateOffer(){
        const [details,setdetails] = useState([]);
        const handlemessage = (msg) => {
            setdetails(msg)
        }
    
        
        useEffect(() => {fetch('/createOffer' , {
            method:"GET",
          }).then(response => response.json())
            .then(message => (
                // console.log(message["user"])
                handlemessage(message['offerList'])
            ))},[])
        
                
        const handleRestaurantsClick = () => {
            window.location.href='/addOffer';
        };



          return(
            <>
                <h1>
                    Promotional Offers
                </h1>

                <div>
                <ul>
                    {details.map((item) => (
                    <li>
                        Name: {item["name"]}
                        Dicount: {item["discount"]}
                        Upper Limit: {item["price"]}
                        Offer Id :{ item["offerId"]}
                        
                    </li>
                    ))}
                    <button onClick={handleRestaurantsClick}>Create Offer</button>
                </ul>
                </div>

            </>
            
          )



}