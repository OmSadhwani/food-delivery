import React from 'react';
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

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route exact path='/' element={<Home/>} />
          <Route exact path='/about-us' element={<AboutUs/>} />
          <Route exact path='/login-customer' element={<Login/>} />
          <Route exact path='/sign-up-customer' element={<SignUp/>} />
          <Route exact path='/sign-up-restaurant' element={<SignUpRestaurant/>} />
          <Route exact path='/login-restaurant' element={<LoginRestaurant/>} />
          <Route exact path='/sign-up-delivery-partner' element={<SignUpDeliveryPartner/>} />
          <Route exact path='/login-delivery-partner' element={<LoginDeliveryPartner/>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;