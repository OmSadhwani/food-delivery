import React, {useState, useEffect} from 'react';
import '../../App.css';
import Cards from '../Cards';
import HeroSection from '../HeroSection';
import Footer from '../Footer';

function Home() {

  return (
    <>
      <HeroSection />
      <Cards />
      <Footer />
    </>
  );
}

// document.getElementById("Home").innerHTML = Home();
export default Home;
