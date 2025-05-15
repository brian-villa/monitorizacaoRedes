import React, {useState} from 'react';
import Header from './components/header';
import Popup from './components/popup';
import StartBut from './components/startBut';
import Footer from './components/footer';
import Info from './components/info';

function App() {

  return (
    <>
      <div
        className="w-full min-h-screen text-white justify-items-center font-['Roboto'] bg-[#101d2d] overflow-y-hidden"
      >
        <Popup />

        <Header />

        <StartBut />

        <Info />

        <Footer />
       
      </div>
    </>
  );
}

export default App;
