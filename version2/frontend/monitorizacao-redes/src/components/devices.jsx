import React, {useEffect,useState} from 'react';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

import {
  faMobileAlt,
  faLaptop,
  faPrint,
  faWifi,
  faQuestionCircle
} from '@fortawesome/free-solid-svg-icons';

const Devices = () => {
    const [devices, setDevices] = useState([]);
    const [error, setError] = useState(null);

    const apiKey = import.meta.env.VITE_API_KEY;

    useEffect(() => {
        axios.get('http://localhost:5000/api/devices', {
        headers: {
            'X-API-Key': apiKey,
        }
        })
        .then(response => {
            setDevices(response.data);
        })
        .catch(error => {
            console.error('Error finding devices:', error);
            setError(error.message);
        });
    }, []);

    const getDeviceTypeIcon = (host, manufacturer) => {
    const h = host?.toLowerCase() || '';
    const m = manufacturer?.toLowerCase() || '';

    if (h.includes('iphone') || h.includes('android') || m.includes('samsung') || m.includes('huawei') || m.includes('apple')) {
        return faMobileAlt;
    }
    if (h.includes('mac') || h.includes('desktop') || h.includes('laptop') || h.includes('pc') || m.includes('dell') || m.includes('hp') || m.includes('asus')|| m.includes('laptop')) {
        return faLaptop;
    }
    if (h.includes('printer') || m.includes('epson') || m.includes('canon')) {
        return faPrint;
    }
    if (h.includes('router') || m.includes('ubiquiti') || m.includes('tp-link') || m.includes('cisco')) {
        return faWifi;
    }
    return faQuestionCircle;
    };

    const formatDate = (isoString) => {
    const date = new Date(isoString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short', 
        day: '2-digit',
    });
    };
    
    return(
        <>  
            {error && <p>ERROR: {error}</p>}
            <ul className=' w-full flex flex-col h-73 overflow-y-auto px-4 styled-scrollbar' >
                {devices.map(device =>(
                  <li key={device.mac} className='bg-white text-black rounded mb-3 p-4 flex items-center transition-all duration-300 hover:scale-103 select-none'>
                    <div className='w-12 h-12 flex items-center justify-center mr-7'>
                        <FontAwesomeIcon icon={getDeviceTypeIcon(device.host, device.manufacturer)} className='text-[#6da34d] text-5xl ' />
                    </div>
                    <div className='w-full'>
                        <div className='w-full flex justify-between mb-2'>
                            <h1 className=' text-[#6da34d] font-bold text-xl'> {device.host} </h1>
                        <div
                            className={`w-12 h-7 flex items-center justify-center rounded text-white text-xs font-semibold ${
                            device.status === 'active' ? 'bg-[#6da34d]' : 'bg-red-500'}`}
                        >
                            {device.status}
                        </div>
                        </div>
                        <div>
                            <div className='flex'>
                                <h2 className='mr-1 font-bold text-[#6da34d]'>IP:</h2>
                                {device.ip}  
                            </div>
                            <div className="flex text-sm">
                                <h2 className="mr-1 font-bold text-[#6da34d]">First seen:</h2>
                                {formatDate(device.first_seen)}
                            </div>

                            <div className="flex text-sm">
                                <h2 className="mr-1 font-bold text-[#6da34d]">Last seen:</h2>
                                {formatDate(device.last_seen)}
                            </div>
                            <div className="flex text-sm">
                                <h2 className="mr-1 font-bold text-[#6da34d]">Manufacturer:</h2>
                                {device.manufacturer}
                            </div>  
                        </div>
                    </div>
                     
                </li>
                ))}
            </ul>
        </>
    )
}

export default Devices;