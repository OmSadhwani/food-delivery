import React,{useState,useEffect} from 'react';
import '../../App.css';
import { useParams } from 'react-router-dom';

export default function AllOffer() {
    const {id}= useParams()
    const [offers,setoffers] = useState([]);
    const [restid,setrestid]=useState('')
  
      // useEffect(() => {
    //   fetch('/').then(
    //     response => response.json()
    //   ).then(data => setInitialData(data))
    // }, []);
  
  
      useEffect(() => {fetch('/allOffer/'.concat(id) , {
          method:"GET",
        }).then(response => response.json())
          .then(message => (
              // console.log(message),
              setoffers(message['offerList'])
          ))},[])
  
        //   function handleButtonClick(menuURL) {
        //     window.location.href = "/menuAdmin/".concat(menuURL)
        //   }
          function handleAddClick(customerId,offerId) {
              window.location.href = "/giveOffer/".concat(customerId).concat('/').concat(offerId)
          }
        //   function handleChangeClick(menuURL) {
        //       window.location.href = "/changeRecommendRestaurant/".concat(menuURL)
        //   }
    return (
      <>
    
      <div>
        <h2>Offers</h2>
        <ul>
          {offers.map((offer) => (
            <li>
              {offer['name']}{' '}
              {offer['discount']}{' '}
              {offer['upperLimit']}{' '}
              
  
              {/* <button onClick={() => handleButtonClick(restaurant['restaurantId'])}>Menu</button>
              <button onClick={() => handleDeleteClick("restaurant/",restaurant["restaurantId"])}>Delete</button>
              {String(restaurant['isRecommended'])}{' '}
              <button onClick={() => handleChangeClick(restaurant['restaurantId'])}>Change</button> */}
                <button class="btn1" onClick={() => handleAddClick(id,offer["offerId"])}>Add Offer</button>
            </li>
          ))}
        </ul>
      </div>
  
          
      </>
    )
  }