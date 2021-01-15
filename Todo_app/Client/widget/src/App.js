import React, { useState } from 'react';
import Accordion from './components/Accordion';
import Dropdown from './components/Dropdown';
import Search from './components/Search';

const items = [
    {
        title : 'titulo1',
        content : 'este es el contenido del titulo 1'
    },
    {
        title : 'titulo2',
        content : 'este es el contenido del titulo 2'
    },
    {
        title : 'titulo3',
        content : 'este es el contenido del titulo 3'
    }
];

const options = [
    {
        label: 'Red',
        value: 'red'
    },
    {
        label: 'Green',
        value: 'green'
    },
    {
        label: 'Blue',
        value: 'blue'
    }
];


export default () => {
    const [selected, setSelected] = useState(options[0]);
    return (
        <div>
            <Dropdown 
                selected={selected} 
                onSelectedChange={setSelected} 
                options={options} 
            />
        </div>
    );
};