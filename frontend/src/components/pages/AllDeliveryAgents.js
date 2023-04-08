import React,{useState,useEffect} from 'react';
import '../../App.css';
import NavbarC from '../NavbarC'

export default function AllDeliveryAgents() {

    const [deliveryAgents,setdeliveryAgents] = useState([]);
    
    
  
      useEffect(() => {fetch('/allDeliveryAgents' , {
          method:"GET",
        }).then(response => response.json())
          .then(message => (
              // console.log(message),
              setdeliveryAgents(message['deliveryAgentList'])
          ))},[])
  
          function handleButtonClick(menuURL,menu) {
            window.location.href = "/delete/".concat(menuURL).concat(menu)
          }
    return (
      <>
      <NavbarC></NavbarC>
      <div>
        <h2>Delivery Agents</h2>
        <ul>
          {deliveryAgents.map((deliveryAgents) => (
            <li>
              {deliveryAgents['name']}{' '}
              {deliveryAgents['email']}{' '}
              {deliveryAgents['mobile']}{' '}
              {deliveryAgents['gender']}{' '}
              {deliveryAgents['area']}{' '}
              {deliveryAgents['address']}{' '}
              
              {/* restid=restaurant['restaurantId']
               */}
  
              {/* <button onClick={() => handleButtonClick("deliveryAgents/",deliveryAgents["deliveryAgentsId"])}>Promotional Offers</button> */}
              <button onClick={() => handleButtonClick("deliveryAgent/",deliveryAgents["deliveryAgentId"])}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
  
          
      </>
    )
  }