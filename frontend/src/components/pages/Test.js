import { useState, useEffect } from 'react';

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    // Fetch restaurant data from the database
    fetch('/api/restaurants')
      .then(response => response.json())
      .then(data => setRestaurants(data));
  }, []);

  function handleButtonClick(menuURL) {
    window.location.href = menuURL;
  }

  return (
    <div>
      <h2>Restaurants</h2>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            {restaurant.name}{' '}
            <button onClick={() => handleButtonClick(restaurant.menuURL)}>Menu</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RestaurantList;