import React,{useState,useEffect} from 'react';
import '../../App.css';
import NavbarC from '../NavbarC'

export default function AllRestaurantAdmin() {

  const [restaurants,setrestaurants] = useState([]);
  const [restid,setrestid]=useState('')

    // useEffect(() => {
  //   fetch('/').then(
  //     response => response.json()
  //   ).then(data => setInitialData(data))
  // }, []);


    useEffect(() => {fetch('/allRestaurant' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            // console.log(message),
            setrestaurants(message['restaurantList'])
        ))},[])

        function handleButtonClick(menuURL) {
          window.location.href = "/menuAdmin/".concat(menuURL)
        }
        function handleDeleteClick(menuURL,menu) {
            window.location.href = "/delete/".concat(menuURL).concat(menu)
        }
        function handleChangeClick(menuURL) {
            window.location.href = "/changeRecommendRestaurant/".concat(menuURL)
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
            <button onClick={() => handleDeleteClick("restaurant/",restaurant["restaurantId"])}>Delete</button>
            {String(restaurant['isRecommended'])}{' '}
            <button onClick={() => handleChangeClick(restaurant['restaurantId'])}>Change</button>
          </li>
        ))}
      </ul>
    </div>

        
    </>
  )
}