// import React, {useState} from 'react';
// import {Link} from 'react-router-dom';
// import {FaTypo3} from "react-icons/fa";
// import {FaTimes} from "react-icons/fa";
// import {FaBars} from "react-icons/fa";

// function Navbar(){
//     const [click,setClick] = useState(false);

//     const handleClick = () => setClick(!click);
//     const closeMobileMenu = () => setClick(false)
//     return (
//         <>
//             <nav className="navbar">
//                 <div className="navbar-container">
//                     <Link to="/" className="navbar-logo">
//                         DoorDine <FaTypo3 />
//                     </Link>
//                     <div className='menu-icon' onClick={handleClick}>
//                         {click ? <FaTimes/> : <FaBars/>}
//                     </div>
//                     <ul className={click ? 'nav-menu active' : 'nav-menu'}>
//                         <li className='nav-item'>
//                             <Link to='/' className='nav-links' onClick={closeMobileMenu}>
//                                 Home
//                             </Link>
//                         </li>
//                         <li className='nav-item'>
//                             <Link to='/aboutus' className='nav-links' onClick={closeMobileMenu}>
//                                 About Us
//                             </Link>
//                         </li>
//                         <li className='nav-item'>
//                             <Link to='/aboutus' className='nav-links-mobile' onClick={closeMobileMenu}>
//                                 Sign Up
//                             </Link>
//                         </li>
//                     </ul>
//                 </div>
//             </nav>
//         </>
//     );
// }

// export default Navbar


import React, { useState, useEffect } from 'react';
import { Button } from './Button';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
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
          <Link to='/' className='navbar-logo' onClick={closeMobileMenu}>
            TRVL
            <i class='fab fa-typo3' />
          </Link>
          <div className='menu-icon' onClick={handleClick}>
            <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
          </div>
          <ul className={click ? 'nav-menu active' : 'nav-menu'}>
            <li className='nav-item'>
              <Link to='/' className='nav-links' onClick={closeMobileMenu}>
                Home
              </Link>
            </li>
            <li className='nav-item'>
              <Link
                to='/services'
                className='nav-links'
                onClick={closeMobileMenu}
              >
                Services
              </Link>
            </li>
            <li className='nav-item'>
              <Link
                to='/products'
                className='nav-links'
                onClick={closeMobileMenu}
              >
                Products
              </Link>
            </li>

            <li>
              <Link
                to='/sign-up'
                className='nav-links-mobile'
                onClick={closeMobileMenu}
              >
                Sign Up
              </Link>
            </li>
          </ul>
          {button && <Button buttonStyle='btn--outline'>SIGN UP</Button>}
        </div>
      </nav>
    </>
  );
}

export default Navbar;