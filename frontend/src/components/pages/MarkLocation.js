import React from 'react';
import { useState, useEffect } from 'react';
import '../../App.css';

export default function MarkLocation() {

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
              window.location.reload()
            //   console.log()
          }
        }
  
      const handleSubmit = (event) => {
          event.preventDefault()
          
          console.log(inputs)
  
          fetch('/markLocation' , {
            method:"POST",
            body:JSON.stringify(inputs),
          }).then(response => response.json())
            .then(message => (
              handleSuccess(message['message'])
                ))
                
      }

      return (
        <>
            <div className="form">
            <h1>Mark Your Location</h1>
            <form onSubmit={handleSubmit}>
            <div className="form-body">
                <div className="Location">
                    <input  type="text" min="0" id="Location" name="location" className="form__input" placeholder="Your Location" value={inputs.location} onChange={handleChange}/>
                </div>
                <br/>
                
            </div>
            <div class="footer">
                <button type="submit" className="btn1">Submit</button>
            </div>
            </form>
            </div>
        </>
      );

}