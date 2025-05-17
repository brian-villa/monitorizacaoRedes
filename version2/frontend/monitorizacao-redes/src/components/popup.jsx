import React, { useState, useEffect } from "react";

function Popup() {
  const [isVisible, setIsVisible] = useState(true);
  const [isClosing, setIsClosing] = useState(false);

  useEffect(() => {
    document.body.style.overflowY = isVisible ? "hidden" : "auto";
  }, [isVisible]);

  const handleAgreeClick = () => {
    setIsClosing(true);
    setTimeout(() => setIsVisible(false), 100);
  };

  if (!isVisible) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
      <div
        className={`w-2/5 max-w-lg p-6 rounded shadow-lg bg-[#1f1f1f] text-white transform transition-all duration-100 ${
          isClosing ? "opacity-0 scale-90" : "opacity-100 scale-100"
        }`}
      >
        <h1 className="font-bold text-2xl text-[#6da34d] mb-2">How we work?</h1>
        <p className="font-light text-base mb-4">
          We use a Python-based script to scan all devices connected to your network,
          making it easier to identify any unauthorized presence. All collected data is used
          for informational purposes only and is automatically removed from our database after 24 hours.
        </p>
        <div
          className="px-4 py-2 rounded cursor-pointer bg-[#6da34d] hover:bg-[#219E45] transition-all transform hover:scale-105 font-bold text-center"
          onClick={handleAgreeClick}
        >
          I agree
        </div>
      </div>
    </div>
  );
}

export default Popup;
