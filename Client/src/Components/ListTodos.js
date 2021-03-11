// Client/src/Components/ListTodo.js
import React, { useEffect, useState } from 'react';
import Acordion from './Acordion';
import Form from './Form';

const ListTodos = () => {

    const [todos, setTodos] = useState([]);
    const [addTodo, setAddTodo] = useState({name:'', content:''});

    useEffect(() => {
        fetch('/api').then(response => {
            if (response.ok) {
                return response.json()
            }
        }).then(data => setTodos(data))
    });

    const handleFormChange = (inputsValue) => {
        setAddTodo(inputsValue);
    }

    const handleFormSubmit = () => {
        fetch('/api/create', {
            method: 'POST',
            body: JSON.stringify(addTodo),
            headers: {
                'Content-type': 'aplication/json; charset=UTF-8'
            }
        }).then(response => response.json())
            .then(message => {
                console.log(message);
                setAddTodo({name:'', content:''});
                getLatestTodos();
            })
    }

    const getLatestTodos = () => {
        fetch('/api').then(response => {
            if (response.ok) {
                return response.json()
            }
        }).then(data => setTodos(data))
    }

    return (
        <div class="ui placeholder segment">
            <div class="ui two column very relaxed stackable grid">
                <div class="column">
                    <Form  onFormSubmit={handleFormSubmit} onFormChange={handleFormChange} />
                </div>
                <div class="aligned column">
                    <h3 class="ui dividing header">List of Todos</h3>    
                    <Acordion todos={todos} />
                </div>              
            </div>
        <div/>
                
                
            </div>
    );
}

export default ListTodos;