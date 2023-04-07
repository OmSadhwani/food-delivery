import React from 'react'
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';


export default function AcceptDeliveryRequest() {
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
          window.location.href = '/customerDashboard'
        }
        else{
            window.location.href = '/customerLogin'
        }
      }

    const handleSubmit = (event) => {
        event.preventDefault()
        inputs["id"]=id
        console.log(inputs)

        fetch('/acceptDeliveryRequest/:id' , {
          method:"POST",
          body:JSON.stringify(inputs),
        }).then(response => response.json())
          .then(message => (
              handleSuccess(message['message'])
          ))
    }



    
    
  
    //   useEffect(() => {fetch('/acceptDeliveryRequest/:id' , {
    //     method:"POST",
    //     body:JSON.stringify(id),
    //   }).then(response => response.json())
    //     .then(message => (
            
    //         setrequests(message["deliveryRequestList"])
    //     ))},[])
    
        return(
            <div className="form">
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
            <div className="form-body">
                <div className="estimated time to reach customer">
                    <input  type="number" min="0" id="email" name="email" className="form__input" placeholder="Email" value={inputs.restaurant || ""} onChange={handleChange}/>
                </div>
                <br/>
                <div className="estimated time to reach customer">
                    <input className="form__input" type="number" min="0" name="password" id="password" placeholder="Password" value={inputs.customer || ""} onChange={handleChange}/>
                </div>
            </div>
            <div class="footer">
                <button type="submit" className="btn1">Accept</button>
            </div>
            </form>
        </div>
        )
}