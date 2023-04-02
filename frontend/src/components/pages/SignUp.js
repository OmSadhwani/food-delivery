import React, { useState } from 'react';
import '../../App.css';
import {RegistrationForm} from '../RegistrationForm';


function SignUp() {

  const [inputs, setInputs] = useState({});

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values , [name]:value}))
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    console.log(inputs)
    fetch('/create' , {
      method:"POST",
      body:JSON.stringify(inputs),
    }).then(response => response.json())
      .then(message => console.log(message))
    
  }

  // const handleSubmit
  return(
    <>
      <div className="form">
        <h1>Sign Up Form</h1>
          <form onSubmit={handleSubmit}>
              <div className="Name">
                  <input className="form__input" type="text" id="name" name="name" placeholder="Name" required value={inputs.name || ""} onChange={handleChange}/>
              </div>
              <br/>
              <div className="email">
                  <input  type="email" id="email" name="email" className="form__input" placeholder="Email" value={inputs.email || ""} onChange={handleChange}/>
              </div>
              <br/>
              <div className="gender">
                  <select id="gender" name="gender" className="form__input" value={inputs.gender} onChange={handleChange}>
                    <option value="" disabled selected hidden>Gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
                  </select>
              </div>
              <br/>
              <div className="mobile">
                  <input className="form__input" type="tel" name="mobile" id="mobile" placeholder="Mobile Number" value={inputs.mobile || ""} onChange={handleChange}/>
              </div>
              <br/>
              <div className="area">
                  <input  type="text" name="area" id="area"  className="form__input"placeholder="Area" value={inputs.area || ""} onChange={handleChange}/>
              </div>
              <br/>
              <div className="address">
                  <input className="form__input" type="text" name="address"  id="address" placeholder="Address" value={inputs.address || ""} onChange={handleChange}/>
              </div>
              <br/>
              <div className="password">
                  <input className="form__input" name="password" type="password" id="password" required placeholder="Password" value={inputs.password} onChange={handleChange}/>
              </div>
              <br/>
              {/* <div className="confirm-password">
                  <input className="form__input" name="confirm-password" type="password" id="confirm-password" placeholder="Confirm Password" value={inputs.confirm-password} onChange={handleChange}/>
              </div> */}
          <div class="footer">
              <a href='/customerLogin'>
              <button type="submit" className="btn1">Register</button>
              </a>
          </div>
          </form>
      </div>
    </>
  );
}

export default SignUp;