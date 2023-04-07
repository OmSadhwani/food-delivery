import React, {useState, useEffect} from 'react';
import '../../App.css';
import Navbar from '../Navbar';

function ConfirmOrder() {

    const [details, setdetails] = useState({});
    const [issuccess,setissuccess] = useState("");
    const [orderList,setorderList] = useState([]);

    // const handleChange = (event) => {
    //   const name = event.target.name;
    //   const value = event.target.value;
    //   setInputs(values => ({...values , [name]:value}))
    // }

    const handleSuccess = (msg) => {
        setissuccess(msg)
        if(msg=="Success"){
          window.location.href = '/customerDashboard'
        }
        else{

        }
      }

    const handleSubmit = (event) => {
        fetch('/placeOrder' , {
          method:"GET",
        }).then(response => response.json())
          .then(message => (
              handleSuccess(message["message"])
          ))
    }


      useEffect(() => {
    fetch('/orderDetails').then(
      response => response.json()
    ).then(message => (
      console.log(message),
      setdetails(message),
      setorderList(message['orderList'])
    ))
  }, []);

    return(
        <>
        <Navbar/>
        <div className="form">
        <h1>Order Details</h1>
          <div>
            Customer Name : {details['customerName']}
          </div> 
          <div>
            Restaurant Name : {details['restaurantName']}
          </div> 
          <div>
            Base Price : {details['cost']}
          </div> 
          <div>
            Delivery Charge : {details['deliveryCharge']}
          </div> 
          <div>
            Discount : {details['discount']}
          </div> 
          <div>
            Total amount to pay : {details['final']}
          </div> 
          <div>
            Offer Used : {String(details['offerUsed'])}
          </div> 

          <div>
          <ul>
        {orderList.map((m) => (
          <li key={m['foodItemId']}>
            {m['name']}{' '}
            {m['pricePerItem']}{' '}
            {m['frequency']}{' '}
          </li>
        ))}
      </ul>
          </div>


          <div class="footer">
              <button type="submit" className="btn1" onClick={handleSubmit}>Confirm and Pay</button>
          </div>

      </div>      
        </>
    );
}

export default ConfirmOrder;