import React from 'react'
import { useState, useEffect } from 'react';

export default function AdminDashboard(){




  const handleCustomersClick = () => {
    window.location.href='/allCustomers';
  };

  const handleRestaurantsClick = () => {
    window.location.href='/allRestaurantAdmin';
  };

  const handleAgentsClick = () => {
    window.location.href='/allDeliveryAgents';
  };

  const handleOffersClick = () => {
    window.location.href='/createOffer';
  };

    return (
        <div>
          <h1>Welcome to the Admin Dashboard</h1>
          <button onClick={handleCustomersClick}>List of Customers</button>
          <button onClick={handleRestaurantsClick}>List of Restaurants</button>
          <button onClick={handleAgentsClick}>List of Delivery Agents</button>
          <button onClick={handleOffersClick}>Promotional Offers</button>
        </div>
      );

}