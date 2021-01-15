import React, { useState } from 'react';
import Accordion from './components/Accordion';
import Dropdown from './components/Dropdown';
import Search from './components/Search';
import Translate from './components/Translate';

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
            <Translate />
        </div>
    );
};