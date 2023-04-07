import React, {useState,useEffect} from 'react'
import { useParams } from 'react-router-dom'

function SendDeliveryRequest(){
    const temp = useParams()
    // console.log(temp)
    

    const [deliveryagents,setdeliveryagents]=useState([])
    // const [inputs, setInputs] = useState({});
    // const handleChange = (event) => {
    //     const name = event.target.name;
    //     const value = event.target.value;
    //     setInputs(values => ({...values , [name]:value}))
    //   }

    const handlemessage = (msg) => {
        // console.log(msg)
        if (msg == "Success"){
            window.location.href='/pendingOrdersRestaurant'
        }
        else{

        }
    }

    const handleClick = (event) => {
        // console.log(temp.id)
        fetch('/sendDeliveryRequest/'.concat(temp.id) , {
            method:"POST",
            body:JSON.stringify({'id':temp.id}),
          }).then(response => response.json())
            .then(message => (
                // setdeliveryagents(message['deliveryAgentList'])
                // console.log(message['message']),
                handlemessage(message['message'])
            ))
    }


        useEffect(() => {fetch('/nearbyDeliveryAgents/'.concat(temp.id) , {
          method:"GET",
        //   body:JSON.stringify(inputs),
        }).then(response => response.json())
          .then(message => (
                // console.log(message['deliveryAgentList']),
              setdeliveryagents(message['deliveryAgentList'])
          ))},[])
      

    return (
        <>

    <ul>
    {deliveryagents.map((m) => (
      <li key={m['name']}>
        Name : {m['name']}{' '}
        Mobile Number : {m['mobileNumber']}{' '}
        Rating Value : {m['ratingValue']}{' '}
        Area : {m['area']}{' '}
      </li>
    ))}
  </ul>
        <div class="footer">
            <button type="submit" className="btn1" onClick={handleClick}>Send Delivery Request</button>
        </div>
  </>

    );
}

export default SendDeliveryRequest