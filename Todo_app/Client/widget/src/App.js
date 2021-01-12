import React from 'react';
import Accordion from './components/Accordion';

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

export default () => {
    return (
        <div>
            <Accordion items={items}/>
        </div>
    );
};