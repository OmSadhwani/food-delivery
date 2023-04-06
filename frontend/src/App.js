import React, {useState, useEffect} from 'react';
import Navbar from './components/Navbar';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/pages/Home';
import SignUp from './components/pages/SignUp';
import Login from './components/pages/Login';
import AboutUs from './components/pages/AboutUs';
import SignUpRestaurant from './components/pages/SignUpRestaurant';
import LoginRestaurant from './components/pages/LoginRestaurant';
import SignUpDeliveryPartner from './components/pages/SignUpDeliveryPartner';
import LoginDeliveryPartner from './components/pages/LoginDeliveryPartner';
import CustomerDashboard from './components/pages/CustomerDashboard';
import RestaurantDashboard from './components/pages/RestaurantDashboard';
import Menu from './components/pages/Menu';
import AddFoodMenu from './components/pages/AddFoodItem';
import DeliveryAgentDashboard from './components/pages/DeliveryAgentDashboard'
import PersonalDataDeliveryAgent from './components/pages/PersonalDataDeliveryAgent'
import PersonalDataRestaurant from './components/pages/PersonalDataRestaurant'
import PersonalData from './components/pages/PersonalData'
import AllRestaurants from './components/pages/AllRestaurants'
import Order from './components/pages/Order'

function App() {
  // const [initialData, setInitialData] = useState([{}])

  // useEffect(() => {
  //   fetch('/').then(
  //     response => response.json()
  //   ).then(data => setInitialData(data))
  // }, []);

  return (
    <>
      <Router>
        <Routes>
          <Route exact path='/' element={<Home/>} />
          <Route exact path='/home' element={<Home/>} />
          <Route exact path='/about-us' element={<AboutUs/>} />
          <Route exact path='/customerLogin' element={<Login/>} />
          <Route exact path='/customerSignup' element={<SignUp/>} />
          <Route exact path='/restaurantSignup' element={<SignUpRestaurant/>} />
          <Route exact path='/restaurantLogin' element={<LoginRestaurant/>} />
          <Route exact path='/deliveryAgentSignup' element={<SignUpDeliveryPartner/>} />
          <Route exact path='/deliveryAgentLogin' element={<LoginDeliveryPartner/>} />
          <Route exact path='/customerDashboard' element={<CustomerDashboard/>} />
          <Route exact path='/restaurantDashboard' element={<RestaurantDashboard/>} />
          <Route exact path='/menu' element={<Menu/>} />
          <Route exact path='/addFoodItem' element={<AddFoodMenu/>} />
          <Route exact path='/deliveryAgentDashboard' element={<DeliveryAgentDashboard/>} />
          <Route exact path='/personalDataAgent' element={<PersonalDataDeliveryAgent/>} />
          <Route exact path='/personalData' element={<PersonalData/>} />
          <Route exact path='/personalDataRestaurant' element={<PersonalDataRestaurant/>} />
          <Route exact path='/allRestaurants' element={<AllRestaurants/>} />
          <Route exact path='/order' element={<Order/>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;