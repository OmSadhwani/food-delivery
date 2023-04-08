import React, { useState, useEffect } from 'react';
import {FaTypo3} from "react-icons/fa";
import {FaTimes} from "react-icons/fa";
import {FaBars} from "react-icons/fa";
import {RxDashboard} from "react-icons/rx"
import { Button } from './Button';
import { Link } from 'react-router-dom';
import './Navbar.css';

function NavbarD() {
  const [click, setClick] = useState(false);
  const [button, setButton] = useState(true);
  const handleClick = () => setClick(!click);
  const closeMobileMenu = () => setClick(false);

  const showButton = () => {
    if (window.innerWidth <= 960) {
      setButton(false);
    } else {
      setButton(true);
    }
  };

  useEffect(() => {
    showButton();
  }, []);

  window.addEventListener('resize', showButton);

  return (
    <>
      <nav className='navbar'>
        <div className='navbar-container'>
          <Link to='/deliveryAgentDashboard' className='navbar-logo' onClick={closeMobileMenu}>
            DashBoard &nbsp; <RxDashboard/>
          </Link>
        </div>
      </nav>
    </>
  );
}

export default NavbarD;