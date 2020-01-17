import React, {Component} from 'react';
import './App.css';
import axios from 'axios';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            result:null
        };
        this.fetchResult = this.fetchResult.bind(this);
        this.setResult = this.setResult.bind(this);
    }

    fetchResult() {
        fetch(
            // '127.0.0.1:8000/projects/'
                `https://hn.algolia.com/api/v1/search?query=redux`
        )
            .then(response => response.json())
            .then(result => this.setResult(result))
            .catch(error => error)
    }

    setResult(result) {
        // const {project_number, machinery_type, created, updated} = result;
        this.setState({
            result:result
        });
    }

    componentDidMount() {
        this.fetchResult();
    }


    render() {
        console.log('HEREEEE');
        console.log(this.state.result);
        return (
            this.state.result.hits.map(item =>
                <div>
                    {item}
                </div>
            )
        );
    }
}


export default App;
