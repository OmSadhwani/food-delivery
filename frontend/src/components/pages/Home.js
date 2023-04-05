import React, {useState, useEffect} from 'react';
import '../../App.css';
import Navbar from '../Navbar';
import Cards from '../Cards';
import HeroSection from '../HeroSection';
import Footer from '../Footer';

function Home() {

  const [initialData, setInitialData] = useState([{}])

  useEffect(() => {
    fetch('/home').then(
      response => response.json()
    ).then(data => setInitialData(data))
  }, []);


  return (
    <>
      <Navbar/>
      <HeroSection />
      <Cards />
      <Footer />
    </>
  );
}

// document.getElementById("Home").innerHTML = Home();
export default Home;
