import React, { useState, useEffect } from 'react';
import {FaTypo3} from "react-icons/fa";
import {FaTimes} from "react-icons/fa";
import {FaBars} from "react-icons/fa";
import { Button } from './Button';
import { Link } from 'react-router-dom';
import './Navbar.css';

function NavbarC() {
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
          <Link to='/customerDashboard' className='navbar-logo' onClick={closeMobileMenu}>
            Home <FaTypo3/>
          </Link>
          <div className='menu-icon' onClick={handleClick}>
            {click ? <FaTimes/> : <FaBars/>}
          </div>
          {/* {button && <Button linkto='customerLogin' buttonSize='btn--large' buttonStyle='btn--outline'>Login</Button>}
          {button && <Button linkto='customerSignup' buttonSize='btn--large' buttonStyle='btn--outline'>SignUp</Button>} */}
        </div>
      </nav>
    </>
  );
}

export default NavbarC;