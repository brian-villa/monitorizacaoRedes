import React, { useState, useEffect } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlay, faSpinner } from '@fortawesome/free-solid-svg-icons';

function StartBut() {
  const [isLarge, setIsLarge] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [loadingMessage, setLoadingMessage] = useState("getting your neighbor ip address");
  const [messageIndex, setMessageIndex] = useState(0);

  const loadingMessages = [
    "getting your neighbor ip address",
    "scanning devices on the network",
    "checking for unauthorized connections",
    "gathering information",
    "analyzing data"
  ];

  useEffect(() => {
    let interval;

    if (isLarge && isLoading) {

      interval = setInterval(() => {
        setMessageIndex(prev => (prev + 1) % loadingMessages.length);
        setLoadingMessage(loadingMessages[messageIndex]);
      }, 1000);
      setTimeout(() => {
        setIsLoading(false);
        clearInterval(interval);
      }, 5000);
    }

    return () => clearInterval(interval); 
  }, [isLarge, isLoading, messageIndex]);

  const handleClick = () => {
    if (!isLarge) {
      setIsLarge(true);
      setIsLoading(true);
    }
  };

  return (
    <>  
      <div 
        className={`relative group mb-60 ${isLarge ? 'w-250 h-100 rounded ' : 'w-40 h-40 rounded-full cursor-pointer hover:bg-[#6da34d] transition-all transform hover:scale-105'}  flex justify-center items-center mt-3  border-2 border-[#6da34d] transition-[width,height] duration-500 ease-in-out `}
        onClick={handleClick}
      >
        {isLarge ? (
          <div className="flex flex-col items-center">
            {isLoading ? (
              <>
                <FontAwesomeIcon icon={faSpinner} className="text-3xl text-white animate-spin mb-1" />
                <span className="font-bold text-xl text-white">{loadingMessage}</span>
              </>
            ) : (
              <span className="font-bold text-xl text-white">Conteúdo carregado</span>
            )}
          </div>
        ) : (
          <>
            <span className="absolute w-full h-full rounded-full border-1 border-[#6da34d] opacity-50 animate-slow-ping"></span>
            <span className='font-bold text-xl text-[#ffffff] mr-2'>START</span>
            <FontAwesomeIcon icon={faPlay}  className=" text-3xl text-[#ffffff] transform transition-transform duration-300 ease-in-out group-hover:rotate-180 "/>
          </>    
        )}
      </div>
    </>   
  );
}

export default StartBut;
