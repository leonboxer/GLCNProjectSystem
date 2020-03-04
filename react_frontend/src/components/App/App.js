import React, {Component} from 'react';
import './App.css';
import Navbar from '../App Bar'
import axios from 'axios';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import About from '../About'
import Users from '../Users'

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            result: null
            // result: []
        };
        this.fetchResult = this.fetchResult.bind(this)
    }

    fetchResult() {
        axios(
            'http://127.0.0.1:8000/projects/'
            // 'https://hn.algolia.com/api/v1/search?query=redux'
        )
        // .then(response => response.json())
            .then(result => this.setState({
                    // result: result
                    result: result.data
                    // result: result.data.hits
                })
            )
    }

    componentDidMount() {
        this.fetchResult()
    }

    render() {
        const {result} = this.state;
        console.log('result:', this.state.result);
        if (!result) {
            return null;
        }
        return (
            <Router>
                <div>
                    <nav>
                        <ul>
                            <li>
                                <Link to="/">Home</Link>
                            </li>
                            <li>
                                <Link to="/about">About</Link>
                            </li>
                            <li>
                                <Link to="/users">Users</Link>
                            </li>
                        </ul>
                    </nav>

                    {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
                    <Switch>
                        <Route path="/about">
                            <About/>
                        </Route>
                        <Route path="/users">
                            <Users/>
                        </Route>
                        {/*<Route path="/">*/}
                        {/*    <Home />*/}
                        {/*</Route>*/}
                    </Switch>
                </div>
            </Router>
        );
    }
}


export default App;
