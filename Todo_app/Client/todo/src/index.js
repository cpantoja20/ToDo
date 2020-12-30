//import React and reactDom libraries
import React from 'react';
import ReactDom from 'react-dom';

//Create a react component
const App = () => {
    return <div>Hi there!</div>
};

//show react component in the screen
ReactDom.render(<App/>, document.querySelector('#root'));