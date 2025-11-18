import React, {useState, useEffect} from 'react';
import { TimeService } from '../api';

function Home() {
    const [dateTime, setDateTime] = useState('Loading...');
    const [error, setError] = useState(null);

    useEffect( () => {
        const fetchDateTime = async () => {
            try {
                const response = await TimeService.getCurrentTime();
                setDateTime(response.current_date_time);
            }
            catch (err) {
                Console.error("Failed to fetch time: ", err);
                setError('Failed to fetch date and time from API.');
                setDateTime('N/A');
            }
        };
        fetchDateTime();
    }, []);

    return (
        <div className='page-container'>
            <h1>Welcome Home!</h1>
            <p>The current date and time is: <strong>{error ? error : dateTime}</strong></p>
        </div>
    )
}

export default Home