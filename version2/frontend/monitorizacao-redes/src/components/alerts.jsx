import React, {useEffect, useState} from 'react';
import axios from 'axios';

const Alerts = () => {
    const [alerts, setAlerts] = useState([]);
    const [error, setError] = useState(null);

    const apiKey = import.meta.env.VITE_API_KEY;

    useEffect(() => {
        axios.get('http://localhost:5000/api/alerts', {
            headers: {
                'X-API-Key': apiKey,
            }
        })
        .then(response => {
            setAlerts(response.data);
        })
        .catch(error => {
            console.error('Error finding alerts:', error);
            setError(error.message);
        });
    }, []);

    const formatDate = (isoString) => {
        const date = new Date(isoString);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short', 
            day: '2-digit',
        });
    };

    const getSeverityColor = (severity) => {
        switch (severity?.toLowerCase()) {
            case 'low':
                return 'bg-[#6da34d]';    
            case 'medium':
                return 'bg-yellow-400';    
            case 'high':
                return 'bg-red-500';       
        }
    };

    return (
        <>
            {error && <p>ERROR: {error}</p>}
            <ul className='w-full flex flex-col h-73 overflow-y-auto px-4 styled-scrollbar'>
                {alerts.map(alert => (
                    <li
                        key={alert.mac}
                        className={`text-white rounded mb-3 p-4 flex flex-col items-center justify-center transition-all duration-300 hover:scale-103 select-none ${getSeverityColor(alert.severity)}`}
                    >
                        <h1 className='font-bold text-xl mb-1'>{alert.title}</h1>  
                        <span className='mb-3 text-center'>{alert.description}</span> 
                        <span className='font-light text-sm'>{formatDate(alert.alert_generated_at)}</span>              
                    </li>
                ))}
            </ul>
        </>
    );
};

export default Alerts;
