import React,{ useState } from 'react';

const Form = ({ onFormChange, onFormSubmit}) => {

    const [todo, setTodo] = useState({
        name:'',
        content:''
    });

    const handleInputChange = (event) => {
        setTodo({
            ...todo,
            [event.target.name]: event.target.value
        });
        onFormChange(todo)
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        onFormSubmit();
        setTodo({
            name:'',
            content:''
        });
        document.getElementById("insertForm").reset();
    }



    return (
        <div>
            <h3 class="ui dividing header">New Task</h3>  
            <form id ="insertForm" class="ui form" onSubmit={handleSubmit}>
                <div class="field">
                    <label>Task:</label>
                    <input 
                        type="text" 
                        name = "name"
                        required 
                        onChange={handleInputChange}/>
                </div>
                <div class="field">
                    <label>Description:</label>
                    <textarea 
                        name="content" 
                        required
                        onChange={handleInputChange}/>
                </div>                
                <button class="ui positive button" type="submit">Submit</button>
            </form>
        </div>
    );

};

export default Form;