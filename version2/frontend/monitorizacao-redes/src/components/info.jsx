import React from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";

function Info() {
    return (
        <div className="flex flex-col items-center w-full p-10">
            <div className="flex w-full justify-around gap-4 flex-wrap">

                {/* Card 1 */}
                <div id="card1" className="group flex flex-col items-center w-full sm:w-[32%] bg-[#101d2d] border border-[#6da34d] rounded p-4 
                    transition-all duration-300 transform hover:scale-105 hover:bg-[#18293f] select-none">
                    <div className="flex items-center justify-center w-full mb-3">
                        <h2 className="text-[#6da34d] font-bold text-2xl text-center">HOW NETHOUND WORKS?</h2>
                        <div id="icon1" className="flex items-center justify-center w-10 h-10 ml-3 border border-[#6da34d] rounded-full 
                            transition-transform duration-300 group-hover:-rotate-90 ">
                            <FontAwesomeIcon icon={faArrowLeft} className="text-white text-xl" />
                        </div>
                    </div>
                    <div className="w-full bg-[#6da34d] rounded h-[2px] mb-3"></div>
                    <p className="text-center text-white text-lg font-light px-3">
                        NetHound performs a real-time scan of your local network using a Python-based engine powered by Nmap and Scapy. It identifies all connected devices, collects data such as IP addresses, MAC addresses, hostnames, and manufacturers, and monitors for new or suspicious activity. If unknown or inactive devices are detected, the system generates alerts to keep your network secure and transparent.
                    </p>
                </div>

                {/* Card 2 */}
                <div id="card2" className="group flex flex-col items-center w-full sm:w-[32%] bg-[#101d2d] border border-[#6da34d] rounded p-4 
                    transition-all duration-300 transform hover:scale-105 hover:bg-[#18293f] select-none">
                    <div className="flex items-center justify-center w-full mb-3">
                        <h2 className="text-[#6da34d] font-bold text-2xl text-center">FOUND AN UNKNOWN IP?</h2>
                        <div id="icon2" className="flex items-center justify-center w-10 h-10 ml-3 border border-[#6da34d] rounded-full 
                            transition-transform duration-300 group-hover:-rotate-90 ">
                            <FontAwesomeIcon icon={faArrowLeft} className="text-white text-xl" />
                        </div>
                    </div>
                    <div className="w-full bg-[#6da34d] rounded h-[2px] mb-3"></div>
                    <p className="text-center text-white text-lg font-light px-3">
                        If you detect an unfamiliar IP address, first verify if it's a legitimate device (smart TV, guest phone, etc). If it's unrecognized, change your Wi-Fi password immediately and reboot your router. You can also block the MAC address on your router or use NetHound to track its behavior and status in future scans.
                    </p>
                </div>

                {/* Card 3 */}
                <div id="card3" className="group flex flex-col items-center w-full sm:w-[32%] bg-[#101d2d] border border-[#6da34d] rounded p-4 
                    transition-all duration-300 transform hover:scale-105 hover:bg-[#18293f] select-none">
                    <div className="flex items-center justify-center w-full mb-3">
                        <h2 className="text-[#6da34d] font-bold text-2xl text-center">ABOUT NETWORK SECURITY</h2>
                        <div id="icon3" className="flex items-center justify-center w-10 h-10 ml-3 border border-[#6da34d] rounded-full 
                            transition-transform duration-300 group-hover:-rotate-90 ">
                            <FontAwesomeIcon icon={faArrowLeft}  className="text-white text-xl" />
                        </div>
                    </div>
                    <div className="w-full bg-[#6da34d] rounded h-[2px] mb-3"></div>
                    <p className="text-center text-white text-lg font-light px-3">
                        Securing your home network is essential. Ensure your router firmware is up to date, use strong passwords, and disable WPS. Tools like NetHound help you stay aware of every connection in real time, giving you more control over your digital environment and protecting your data.
                    </p>
                </div>

            </div>
        </div>
    );
}

export default Info;
