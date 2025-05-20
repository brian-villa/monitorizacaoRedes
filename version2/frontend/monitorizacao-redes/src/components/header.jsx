import React, { useState } from "react";
import Nethound from "../assets/NETHOUND.png"
import NethoundHover from "../assets/NETHOUNDHOVER.png"



function Header() {

  const [src,setSrc] = useState (Nethound)

  const scrollToCard = (id) => {
    const card = document.getElementById(id);
    const arrow = document.getElementById(`icon${id.replace('card', '')}`);

    if (card) {
      card.scrollIntoView({ behavior: 'smooth', block: 'center' });

      setTimeout(() => {
        card.classList.add('hovered');
        arrow.classList.add('hoveredArrow')
      }, 250); 
    
      setTimeout(() => {
        card.classList.remove('hovered');
        arrow.classList.remove('hoveredArrow')
      }, 1050); 
  }};
  return (
    <>
      <div className="flex w-full p-5 items-center justify-between">
        <img src={src}
          alt="Logo da marca Nethound"
          className="w-1/10 cursor-pointer mb-10 "
          onMouseOver={() => setSrc(NethoundHover)}
          onMouseLeave={() => setSrc(Nethound)}
          onClick={() => window.location.reload()}
        
        />
        <ul className="flex w-1/3 justify-around font-bold text-[#6da34d] text-center">
          <li className="hover:text-[#b5d6a1] cursor-pointer" onClick={() => scrollToCard("card1")}>
            HOW NETHOUND <br /> WORKS?
          </li>
          <li className="hover:text-[#b5d6a1] cursor-pointer" onClick={() => scrollToCard("card2")}>
            YOU FOUND AN <br />UNKNOWN IP?
          </li>
          <li className="hover:text-[#b5d6a1] cursor-pointer" onClick={() => scrollToCard("card3")}>
            ABOUT NETWORK <br /> SECURITY
          </li>
        </ul>
      </div>
    </>
  )
}


export default Header