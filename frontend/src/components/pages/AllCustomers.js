import React,{useState,useEffect} from 'react';
import '../../App.css';
import NavbarA from '../NavbarA'

export default function AllCustomers() {

    const [customers,setcustomers] = useState([]);
    
    
  
      useEffect(() => {fetch('/allCustomers' , {
          method:"GET",
        }).then(response => response.json())
          .then(message => (
              console.log(message),
              setcustomers(message['customerList'])
          ))},[])
  
          function handleButtonClick(menuURL,menu) {
            window.location.href = "/delete/".concat(menuURL).concat(menu)
          }
    return (
      <>
      <div className="AllCustomers">
      <NavbarA></NavbarA>
        <h1>Customers</h1>
              <table className='my-table'>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Mobile</th>
                    <th>Gender</th>
                    <th>Area</th>
                    <th>Address</th>
                    <th>Remove Customer</th>
                  </tr>
                </thead>
                <tbody>

                {customers.map((customer) => (
                      <tr>
                      <td>{customer['name']}</td>
                      <td>{customer['email']}</td>
                      <td>{customer['mobileNumber']}</td>
                      <td>{customer['gender']}</td>
                      <td>{customer['area']}</td>
                      <td>{customer['address']}</td>
                      <td><button onClick={() => handleButtonClick("customer/",customer["customerId"])} className='btn1'>Delete</button></td>
                    </tr>

          ))}
                </tbody>
              </table>

      </div>
  
          
      </>
    )
  }