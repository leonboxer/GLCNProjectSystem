import React, {Component} from 'react';
import './App.css';
import axios from 'axios';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            result: [1]
        };
        this.setResult = this.setResult.bind(this);
    }

    componentDidMount() {
        axios(
            'http://127.0.0.1:8000/projects/'
            // 'localhost/users'
            // `${PATH_BASE}${PATH_SEARCH}?${PARAM_SEARCH}${searchTerm}`
            // 'https://hn.algolia.com/api/v1/search?query=redux'
        )
        // .then(response => response.json())
            .then(result => this.setResult(result.data))
            .then(error => error)
    }

    setResult(result) {
        this.setState({result})
    }


    render() {
        console.log('result:',this.state.result);
        return (
            this.state.result.map(item =>
               <div>
                <div>
                    {item.project_number}
                </div>
                <div>
                {item.created}
                </div>
               </div>
            )
        );
    }
}


export default App;
