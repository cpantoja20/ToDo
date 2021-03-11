// Client/src/Components/Card.js
import React from 'react';


const Card = ({ key, tName, tContent }) => {

    return (
        <div class="ui centered cards">
            <div class="card">
                <div class="content">
                    <div class="header"> {tName} </div>
                    <div class="description"> {tContent} </div>
                </div>
            </div>                    
        </div>
    );

};

export default Card;