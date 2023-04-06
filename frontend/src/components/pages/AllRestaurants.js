import React,{useState} from 'react';
import '../../App.css';
import NavbarC from '../NavbarC'

export default function AllRestaurants() {

  const [details,setdetails] = useState({});


    fetch('/personalData' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            // console.log(message),
            setdetails(message)
        ))
  return (
    <>
    <NavbarC></NavbarC>
        
    </>
  )
}