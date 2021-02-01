import React, { useState } from 'react';
import Accordion from './components/Accordion';
import Dropdown from './components/Dropdown';
import Search from './components/Search';
import Translate from './components/Translate';
import Route from './components/Route';
import Header from './components/Header';

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
        label: 'Rojo',
        value: 'red'
    },
    {
        label: 'Verde',
        value: 'green'
    },
    {
        label: 'Azul',
        value: 'blue'
    }
];

export default () => {

    const [selected, setSelected] = useState(options[0])

    return (
        <div>
            <Header />
            <Route path="/">
                <Accordion items={items} />
            </Route>
            <Route path="/list">
                <Search />
            </Route>
            <Route path="dropdown">
                <Dropdown 
                    label="Select a Color"
                    selected={selected} 
                    onSelectedChange={setSelected} 
                    options={options}  
                />
            </Route>
            <Route path="/translate">
                <Translate />
            </Route>
        </div>
    );
};