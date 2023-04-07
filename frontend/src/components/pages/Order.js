import React from 'react'
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function Order(){
    const id = useParams()

    const [menu,setmenu] = useState([]);
    
    // console.log(id)

    // fetch('/displayFoodItems/:id' , {
    //     method:"POST",
    //     body:JSON.stringify(id),
    //   }).then(response => response.json())
    //     .then(message => (
    //         // console.log(message),
    //         setmenu(message["menu"])
    //     ),[])

    return (
<>
    <div>
      <h2>Menu</h2>
      <ul>
        {menu.map((m) => (
          <li key={m['foodItemId']}>
            {m['name']}{' '}
            {/* restid=restaurant['restaurantId']
             */}
            
            {m['pricePerItem']}{' '}
            {/* <button onClick={() => handleButtonClick(restaurant['restaurantId'])}>Menu</button> */}
           { <input type="number" name="{{ m['foodItemId']}}" value="0" min="0"></input>}
          </li>
        ))}
      </ul>
    </div>
</>
    );
}

export default Order;