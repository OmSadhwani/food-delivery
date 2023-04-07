import React, {useState, useEffect} from 'react';
import '../../App.css';

function customerDashboard(){
    const [past,setpast] = useState({});

    const handlemessage = (msg) => {
    setpast(msg)
    }

      // useEffect(() => {
  //   fetch('/').then(
  //     response => response.json()
  //   ).then(data => setInitialData(data))
  // }, []);


    useEffect(() => {fetch('/pastOrder' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            // console.log(message["user"])
            handlemessage(message)
        ))},[])

    return(
        <>
            
        </>
    );

}