import React from 'react';
import Header from './components/header';
import Popup from './components/popup';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlay } from '@fortawesome/free-solid-svg-icons';

function App() {
  return (
    <>
      <div
        className="w-full min-h-screen text-white justify-items-center font-['Roboto'] bg-[#212529] "
      >
        <Header />

        <Popup />

        <div className='relative group w-40 h-40 flex justify-center items-center rounded-full mt-3 cursor-pointer bg-[#267a3c] hover:bg-[#219E45] transition-all transform hover:scale-105'>

          <span className="absolute w-full h-full rounded-full border-4 border-green-400 opacity-50 animate-slow-ping"></span>

          <span className='font-bold text-xl mr-2'>START</span>
          <FontAwesomeIcon icon={faPlay}  className=" text-3xl transform transition-transform duration-300 ease-in-out group-hover:rotate-180"/>
        </div>
       
      </div>
    </>
  );
}

export default App;
