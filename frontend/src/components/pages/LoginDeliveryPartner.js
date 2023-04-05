import React, {useState, useEffect} from 'react';
import '../../App.css';

function Login() {

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
            // window.location.href = '/deliveryAgentLogin'
        }
      }

    const handleSubmit = (event) => {
        event.preventDefault()
        console.log(inputs)
        fetch('/deliveryAgentLogin' , {
          method:"POST",
          body:JSON.stringify(inputs),
        }).then(response => response.json())
          .then(message => (
              handleSuccess(message['message'])
          ))
    }

    return(
        <>
        <div className="form">
        <h1>Login</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-body">
              <div className="email">
                  <input  type="email" id="email" name="email" className="form__input" placeholder="Email" value={inputs.email || ""} onChange={handleChange}/>
              </div>
              <br/>
              <div className="password">
                  <input className="form__input" type="password" name="password" id="password" placeholder="Password" value={inputs.password || ""} onChange={handleChange}/>
              </div>
          </div>
          <div class="footer">
              <button type="submit" className="btn1">Login</button>
          </div>
        </form>
        <div>
            <h2>{issuccess}</h2>
        </div>
      </div>      
        </>
    );
}

export default Login;