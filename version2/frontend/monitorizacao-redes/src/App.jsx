import React from 'react';
import Header from './components/header';
import Popup from './components/popup';
import StartBut from './components/startBut';
import Footer from './components/footer';
import Info from './components/info';

function App() {

  return (
    <>
      <div
        className="min-w-screen min-h-screen text-white flex flex-col justify-center items-center font-['Roboto'] bg-[#101d2d] overflow-y-hidden"
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
