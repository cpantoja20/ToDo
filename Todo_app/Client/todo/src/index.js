//import React and reactDom libraries
import React from 'react';
import ReactDom from 'react-dom';
// import faker from 'faker';
// Components
// import CommentDetail from './CommentDetail';
// import ApprovalCard from './ApprovalCard';


//Create a react component
// const App = () => {
    
//     return (
//         <div>
//             {/* Comentarios y approval */}
//             <div className="ui container comments">
//                 <ApprovalCard>
//                     <CommentDetail 
//                         author="Nena" 
//                         timeAgo="Today at 4:45AM"
//                         content="Nice work"
//                         avatar={faker.image.image()}/>
//                 </ApprovalCard>
//                 <ApprovalCard>
//                     <CommentDetail 
//                         author="Cyndy" 
//                         timeAgo="Today at 3:15PM"
//                         content="You're the best"
//                         avatar={faker.image.image()}/>
//                 </ApprovalCard>
//                 <ApprovalCard>
//                     <CommentDetail 
//                         author="Ivon" 
//                         timeAgo="Yesterday at 5:24AM"
//                         content="Do not give up"
//                         avatar={faker.image.image()}/>
//                 </ApprovalCard>
//             </div>
//         </div>
//     );
// };

class App extends React.Component{
    constructor(props){
        super(props);
        this.state = {lat:null, errorMessage: ''};

        window.navigator.geolocation.getCurrentPosition(
            position => {
                this.setState({lat: position.coords.latitude});
            },
            err => {
                this.setState({errorMessage: err.message});
            }
        );
    };
    render() {
        
        return (
            <div>
                <h3>Position Geografica</h3>
                <h4>Latitud: </h4>{this.state.lat}
                <h4>Error: </h4>{this.state.errorMessage}           
            </div>
        );
    };
};

//show react component in the screen
ReactDom.render(<App/>, document.querySelector('#root'));