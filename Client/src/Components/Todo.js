// Client/src/Components/Todo.js
import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import Card from './Card';
import Delete from './Delete';


const Todo = () =>{

    const { id } = useParams();

    const [todo, setTodo] = useState([]);

    useEffect( () => {
        fetch(`/api/${id}`)
        .then(response => response.json())
        .then(data => setTodo(data))
    },[id])

    return (
        <div class="ui center aligned basic segment">
            <div class="ui">
                {todo.length > 0 && todo.map(data =><Card key ={id} tName={data.name} tContent={data.content}/>)}
            </div>
            <br/>
            <div class="ui buttons">
                <Delete id={id}/>
                <div class="or"></div>
                <button class="ui button">
                    <Link to='/'>Back to List</Link>
                </button>
            </div>            
        </div>
    );
};

export default Todo;