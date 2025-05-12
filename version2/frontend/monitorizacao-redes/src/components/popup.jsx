import React, { useState } from "react";

function Popup(){
    
    const [isVisible, setIsVisible] = useState(true);
    const handleAgreeClick = () => {
        setIsVisible(false);
    };

    return(
        <>
            {isVisible && (
                <div className='w-2/5 p-2 m-1 rounded flex flex-col items-center' style={{ backgroundColor: 'rgba(0, 0, 0, 0.7)'}}>
                    <h1 className="font-bold text-2xl w-full text-[#20C74F]"> How we work?</h1>
                    <p className="font-light text-base">
                    We use a Python-based script to scan all devices connected to your network, making it easier to identify any unauthorized presence.
                    All collected data is used for informational purposes only and is automatically removed from our database after 24 hours.
                    </p>
                    <div
                    className="w-1/7 rounded flex justify-center p-1 mt-3 cursor-pointer bg-[#267a3c] hover:bg-[#219E45] transition-all transform hover:scale-105"
                    onClick={handleAgreeClick} 
                    >
                    <p className="font-normal text-base">I agree</p>
                    </div>
                </div>
            )}
        </>
    )
}

export default Popup;