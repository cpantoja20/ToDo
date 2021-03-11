// Client/src/App.js
import {BrowserRouter as Router, Switch,Route, Link} from "react-router-dom";
import ListTodos from './Components/ListTodos';
import Todo from './Components/Todo';

const App = () => {
  return ( 
    <div>
      <Router>
        <Switch>
          <Route exact path='/'>
            <ListTodos/>
          </Route>
          <Route  path='/:id'>
            <Todo/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
