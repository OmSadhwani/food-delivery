import React from 'react';
import './Cards.css';
import CardItem from './CardItem';
import { Link } from 'react-router-dom';

function Cards() {
  return (
    <div className='cards'>
      <h1>Partner With Us!</h1>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <li className='cards__item'>
              <Link className='cards__item__link' to='/login'>
                <figure className='cards__item__pic-wrap' data-category='Restaurant'>
                  <img
                    className='cards__item__img'
                    alt='img'
                    src={require('../images/img2.jpg')}
                  />
                </figure>
                <div className='cards__item__info'>
                <h5 className='cards__item__text'>Register as a Restaurant</h5>
                </div>
              </Link>
            </li>
          </ul>
          <ul className='cards__items'>
            <li className='cards__item'>
                <Link className='cards__item__link' to='/login'>
                  <figure className='cards__item__pic-wrap' data-category='Delivery Partner'>
                    <img
                      className='cards__item__img'
                      alt='img'
                      src={require('../images/img8.jpg')}
                    />
                  </figure>
                  <div className='cards__item__info'>
                  <h5 className='cards__item__text'>Register as a Delivery Partner</h5>
                  </div>
                </Link>
              </li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards;