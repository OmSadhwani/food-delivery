import React from 'react'
import { useState, useEffect } from 'react';
import { redirect, useParams } from 'react-router-dom';


export default function RatingDeliveryAgent() {
    const id= useParams()
    const [inputs, setInputs] = useState({});
    const [issuccess,setissuccess] = useState('');

    const handleChange = (event) => {
      const name = event.target.name;
      const value = event.target.value;
      setInputs(values => ({...values , [name]:value}))
    }

    const handleSuccess = (msg) => {
        setissuccess(msg)
        if(msg=='Success'){
          window.location.href = '/deliveryAgentDashboard'
        }
        else{
            // window.location.reload()
        }
      }

    const handleSubmit = (event) => {
        event.preventDefault()
        inputs["id"]=id
        
        console.log(inputs)
        // console.log()

        fetch('/ratingDeliveryAgent/'.concat(id) , {
          method:"POST",
          body:JSON.stringify(inputs),
        }).then(response => response.json())
          .then(message => (
            console.log(message),
            handleSuccess(message['message'])
              ))
              
    }

    return(
        <div className="form">
        <h1>Give rating to the customer</h1>
        <form onSubmit={handleSubmit}>
        <div className="form-body">
            <div className="rating">
                <input  type="number" min="0" id="number" name="rating" className="form__input" placeholder="rate the customer out of 5" value={inputs.rating} onChange={handleChange}/>
            </div>
            <br/>
           
        </div>
        <div class="footer">
            <button type="submit" className="btn1">Submit</button>
        </div>
        </form>
    </div>
    )
}