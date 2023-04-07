import React from 'react'
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function Order(){
    const id = useParams()

    const [menu,setmenu] = useState([]);
    
    // console.log(id)

    
    useEffect(() => {fetch('/displayFoodItems/:id' , {
        method:"POST",
        body:JSON.stringify(id),
      }).then(response => response.json())
        .then(message => (
            // console.log(message),
            setmenu(message["menu"])
        ))},[])


        const [inputs, setInputs] = useState({});
        // const [issuccess,setissuccess] = useState('');
      
        // const handleChange = (event) => {
        //   const name = event.target.name;
        //   const value = event.target.value;
        //   setInputs(values => ({...values , [name]:value}))
        // }
      
        // const handleSuccess = (msg) => {
        //   setissuccess(msg)
        //   if(msg=='Success'){
        //     window.location.href = '/customerLogin'
        //   }
        //   else{
      
        //   }
        // }
      
        // const handleSubmit = (event) => {
        //   event.preventDefault()
        //   console.log(inputs)
        //   fetch('/customerSignup' , {
        //     method:"POST",
        //     body:JSON.stringify(inputs),
        //   }).then(response => response.json())
        //     .then(message => (
        //         handleSuccess(message['message'])
        //     ))    
        // }

    return (
<>
    <div>
      <h2>Menu</h2>
      {/* <form onSubmit={handleSubmit}> */}
      <ul>
        {menu.map((m) => (
          <li key={m['foodItemId']}>
            {m['name']}{' '}
            {/* restid=restaurant['restaurantId']
             */}
            
            {m['pricePerItem']}{' '}
            {/* <button onClick={() => handleButtonClick(restaurant['restaurantId'])}>Menu</button> */}
           { <input type="number" name="{{ m['name']}}" value="" min="0"></input>}
          </li>
        ))}
      </ul>
      {/* </form> */}
    </div>
</>
    );
}

export default Order;