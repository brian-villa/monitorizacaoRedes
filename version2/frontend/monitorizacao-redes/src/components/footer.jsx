import React from "react";

function Footer (){
    return(
        <>
            <div className='w-full bg-[#6da34d] flex flex-col justify-center items-center p-5'>
                <div className="font-bold text-xl hover:text-[#101d2d] select-none cursor-default">
                    NETHOUND<span className="align-super text-sm ml-1">®</span>
                </div>
                <div className=" text-sm flex flex-col justify-center items-center w-full mt-4 pt-4 px-4 leading-relaxed font-light select-none cursor-default ">
                    <span> © 2024–2025 NETHOUND, LLC. All rights reserved. NETHOUND<span className="align-super text-xs ml-0.5">®</span></span>
                    <span> and related marks are federally registered trademarks of NETHOUND, LLC and may only be used with explicit written permission.</span>
                </div>
                <div className="border-t border-white/20 w-full mt-6 pt-4 text-sm text-center font-light select-none cursor-default">
                    &copy; {new Date().getFullYear()} NETHOUND. All rights reserved.
                </div>
            </div>
        </>
    )
}

export default Footer