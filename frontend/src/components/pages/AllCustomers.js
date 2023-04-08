import React,{useState,useEffect} from 'react';
import '../../App.css';
import NavbarC from '../NavbarC'

export default function AllCustomers() {

    const [customers,setcustomers] = useState([]);
    
    
  
      useEffect(() => {fetch('/allCustomers' , {
          method:"GET",
        }).then(response => response.json())
          .then(message => (
              // console.log(message),
              setcustomers(message['customerList'])
          ))},[])
  
          function handleButtonClick(menuURL,menu) {
            window.location.href = "/delete/".concat(menuURL).concat(menu)
          }
          function handleClick(menuURL) {
            window.location.href = "/allOffer/".concat(menuURL)
          }
    return (
      <>
      <NavbarC></NavbarC>
      <div>
        <h2>Customers</h2>
        <ul>
          {customers.map((customer) => (
            <li>
              {customer['name']}{' '}
              {customer['email']}{' '}
              {customer['mobile']}{' '}
              {customer['gender']}{' '}
              {customer['area']}{' '}
              {customer['address']}{' '}
              
              {/* restid=restaurant['restaurantId']
               */}
  
              {/* <button onClick={() => handleButtonClick("customer/",customer["customerId"])}>Promotional Offers</button> */}
              <button onClick={() => handleButtonClick("customer/",customer["customerId"])}>Delete</button>
              <button onClick={() => handleClick(customer["customerId"])}>Offers</button>
            </li>
          ))}
        </ul>
      </div>
  
          
      </>
    )
  }