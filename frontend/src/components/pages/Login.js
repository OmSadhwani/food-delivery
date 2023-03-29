import React from 'react';
import '../../App.css';

function Login() {
    return(
        <>
        <div className="form">
        <h1>Login</h1>
          <div className="form-body">
              <div className="email">
                  <input  type="email" id="email" className="form__input" placeholder="Email"/>
              </div>
              <br/>
              <div className="password">
                  <input className="form__input" type="password" id="confirmPassword" placeholder="Password"/>
              </div>
          </div>
          <div class="footer">
              <button type="submit" className="btn1">Login</button>
          </div>
      </div>      
        </>
    );
}

export default Login;