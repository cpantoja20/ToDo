import React from 'react';
import Card from './Card';
import { useEffect, useState } from 'react';

const App = () => {

    const [todo, setTodo] = useState([]);

    useEffect(() => {
        fetch('/api').then(response => {
            if(response.ok){
                return(
                    response.json()
                );
            };
        }).then(data => console.log(data))
    });

    
    return (
        <div>
            <Card/>
        </div>
    );

};

export default App;