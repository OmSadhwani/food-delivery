import React,{useState,useEffect} from 'react';
import '../../App.css';
import NavbarC from '../NavbarC'

export default function AllRestaurants() {

  const [restaurants,setrestaurants] = useState([]);
  const [restid,setrestid]=useState('')

    fetch('/allRestaurant' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            // console.log(message),
            setrestaurants(message['restaurantList'])
        ))

        function handleButtonClick(menuURL) {
          window.location.href = "/displayFoodItems/".concat(menuURL)
        }
  return (
    <>
    <NavbarC></NavbarC>
    <div>
      <h2>Restaurants</h2>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant['restaurantId']}>
            {restaurant['name']}{' '}
            {/* restid=restaurant['restaurantId']
             */}

            <button onClick={() => handleButtonClick(restaurant['restaurantId'])}>Menu</button>
          </li>
        ))}
      </ul>
    </div>

        
    </>
  )
}