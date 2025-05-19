import React, { useState, useEffect } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlay, faSpinner } from '@fortawesome/free-solid-svg-icons';
import { motion, AnimatePresence } from 'framer-motion';
import Devices from "./devices";
import Alerts from "./alerts";

function StartBut() {
  const [isLarge, setIsLarge] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [showAlerts, setShowAlerts] = useState(false); 
  const [isSwitching, setIsSwitching] = useState(false)
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
      setShowAlerts(false);
    }
  };

  const handleToggleAlerts = () => {
    setShowAlerts(prev => !prev);
    setIsSwitching(true);
    setTimeout(() => {
      setIsSwitching(false); 
    }, 1000);
  };

  return (
    <>  
      <div 
        className={`relative group mb-60 ${isLarge ? 'w-250 h-100 rounded ' : 'w-40 h-40 rounded-full cursor-pointer hover:bg-[#6da34d] transition-all transform hover:scale-105'}  flex justify-center items-center mt-3  border-2 border-[#6da34d] transition-[width,height] duration-500 ease-in-out `}
        onClick={handleClick}
      >
        {isLarge ? (
          <div className="relative flex flex-col items-center justify-center w-full h-full overflow-hidden">


            <AnimatePresence>
              {isLoading && (
                <motion.div
                  key="loading"
                  initial={{ opacity: 1 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  transition={{ duration: 0.3 }}
                  className="absolute z-10 flex flex-col items-center justify-center w-full h-full bg-[#6da34d]"
                >
                  <FontAwesomeIcon icon={faSpinner} className="text-3xl text-white animate-spin mb-2" />
                  <span className="font-bold text-xl text-white text-center">{loadingMessage}</span>
                </motion.div>
              )}
            </AnimatePresence>

            <AnimatePresence>
              {isSwitching && (
                <motion.div
                  key="switching"
                  initial={{ opacity: 0.7 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  transition={{ duration: 0.6 }}
                  className="absolute z-20 flex flex-col items-center justify-center w-full h-full bg-[#6da34d]"
                >
                  <span className="text-white text-xl font-bold">loading...</span>
                </motion.div>
              )}
            </AnimatePresence>

            <div className="w-full h-full px-1 bg-[#18293f]">
              <div className="flex flex-col items-center px-3 mt-1">
                <h1 className="text-2xl font-bold text-white mb-1">
                  {showAlerts ? 'Alerts' : 'Devices'}
                </h1>
                <div className="mb-2 cursor-pointer" onClick={handleToggleAlerts}>
                  <FontAwesomeIcon icon={faPlay} className="text-white text-xl rotate-180 mr-2 hover:scale-105" />
                  <FontAwesomeIcon icon={faPlay} className="text-white text-xl hover:scale-105" />
                </div>
                <div className="w-full bg-[#6da34d] rounded h-[2px] mb-3"></div>
              </div>
              {showAlerts ? <Alerts /> : <Devices />}
            </div>
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
