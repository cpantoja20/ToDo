import React from 'react';
import { useHistory } from 'react-router-dom';


const Delete = ({ id } ) => {

    const history = useHistory();

    const deleteTodo = () => {
        fetch(`/api/${id}`,{
            method : 'POST',
            body: JSON.stringify({
                id:id
            })
        }).then(response => response.json())
            .then(data => {
                console.log(data);
        })
        history.push('/');
    }

    return(
        <div>
            <button class="ui negative button" onClick={deleteTodo}>Delete</button>
        </div>
        
    );
};

export default Delete;