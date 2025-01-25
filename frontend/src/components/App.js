import React, { Component } from 'react';
import ReactDOM from 'react-dom/client';

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <h1>Testing React Code</h1>
            </div>
        )
    }
}

const appDiv = ReactDOM.createRoot(document.getElementById('app'));
appDiv.render(<App />);