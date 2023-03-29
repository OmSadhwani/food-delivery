import React from 'react';
import '../../App.css';

export default function SignUpRestaurant() {
  return(
  <div className="form">
        <h1>Sign Up Form</h1>
          <div className="form-body">
              <div className="Name">
                  <input className="form__input" type="text" id="name" placeholder="Name"/>
              </div>
              <br/>
              <div className="email">
                  <input  type="email" id="email" className="form__input" placeholder="Email"/>
              </div>
              <br/>
              <div className="area">
                  <input  type="text" name="" id="area"  className="form__input"placeholder="Area"/>
              </div>
              <br/>
              <div className="password">
                  <input className="form__input" type="password" id="confirmPassword" placeholder="Password"/>
              </div>
              <br/>
              <div className="confirm-password">
                  <input className="form__input" type="password" id="confirm-password" placeholder="Confirm Password"/>
              </div>
          </div>
          <div class="footer">
              <button type="submit" className="btn1">Register</button>
          </div>
      </div>
  );
}