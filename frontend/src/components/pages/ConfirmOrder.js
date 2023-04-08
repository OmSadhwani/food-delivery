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
        <div className="ConfirmOrder">
        <Navbar/>
        <h1>Order Details</h1>

        <table className='my-table'>
          <thead>
            <tr>
              <th>Customer Name</th>
              <th>{details['customerName']}</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Restaurant Name</td>
              <td>{details['restaurantName']}</td>
            </tr>
            <tr>
              <td>Base Price</td>
              <td>{details['cost']}</td>
            </tr>
            <tr>
              <td>Delivery Charge</td>
              <td>{details['deliveryCharge']}</td>
            </tr>
            <tr>
              <td>Discount</td>
              <td>{details['discount']}</td>
            </tr>
            <tr>
              <td>Taotal amount to pay</td>
              <td>{details['final']}</td>
            </tr>
            <tr>
              <td>Offer Used</td>
              <td>{String(details['offerUsed'])}</td>
            </tr>
          </tbody>
          
          
        </table>

        <br/><br/><br/><br/><br/><br/>
        <h2>Order List</h2>

        <table className='my-table'>
          <thead>
            <tr>
              <th>Item Name</th>
              <th>Price per Item</th>
              <th>Quantity</th>
            </tr>
          </thead>
          <tbody>

            {orderList.map((m) => (
            <tr>
              <td>{m['name']}</td>
              <td>{m['pricePerItem']}</td>
              <td>{m['frequency']}</td>
            </tr>
            ))}
          </tbody>
        </table>
          <div class="footer">
              <button type="submit" className="btn1" onClick={handleSubmit} style={{width:'10%'}}>Confirm and Pay</button>
          </div>



      </div>    
        </>
    );
}

export default ConfirmOrder;