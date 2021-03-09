import React, { useState } from 'react';
import { Link } from 'react-router-dom'

const Acordion = ({ todos }) =>{

    const [activeIndex, setActiveIndex] = useState(null);

    const onIconClick = (index) => {
        setActiveIndex(index);
    };

    const renderedTodos = todos.map( (todo,index) => {

        const active = index === activeIndex ? 'active':'';

        return (
            <React.Fragment key ={todo.id}>  
                <div className= {`title ${active}`} onClick ={()=> onIconClick(index)}>
                    <i className="dropdown icon"></i>
                    <Link to = {`${todo.id}`}>
                        {todo.name}
                    </Link>
                </div>
                <div className={`content ${active}`}>
                    <p>{todo.content}</p>
                </div>
            </React.Fragment>
        );
    });

    return(
        <div className = "ui styled accordion">
            {renderedTodos}
        </div>
    );
}

export default Acordion;

