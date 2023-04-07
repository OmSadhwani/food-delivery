import React, {useState,useEffect} from 'react'
import { useParams } from 'react-router-dom'

function GiveEstimatedTime(){
    const temp = useParams()
    console.log(temp)
    
    const [inputs, setInputs] = useState({});
    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values , [name]:value}))
      }

    const handlemessage = (msg) => {
        if (msg == "Success"){
            window.location.href='/pendingOrdersRestaurant'
        }
        else{

        }
    }

    const handleSubmit = (event) => {
        event.preventDefault()
        // console.log(inputs)
        inputs['id']=temp.id


        fetch('/getEstimatedTime/'.concat(temp.id) , {
          method:"POST",
          body:JSON.stringify(inputs),
        }).then(response => response.json())
          .then(message => (
            console.log(message),
              handlemessage(message['message'])
          ))    
      }

    return (
        <form onSubmit={handleSubmit}>
        <div className="form-body">
            <div className="time">
                <input  type="number" id="time" name="time" className="form__input" placeholder="Estimated Time" min="0" value={inputs.time} onChange={handleChange}/>
            </div>
        </div>
        <div class="footer">
            <button type="submit" className="btn1">Confirm</button>
        </div>
      </form>
    );
}

export default GiveEstimatedTime