import React from "react";
import ReactDOM from "react-dom";
// import { Router, Link } from "@reach/router";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { repos: undefined };
  }

  componentDidMount() {
    fetch("https://api.github.com/repos/Design-Computing/me/forks", {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        access_token: this.state.idToken
      }
    }).then(x => this.setState({ repos: x }));
  }

  render() {
    return (
      <div>
        <h1>hey!</h1>
        <pre>{JSON.stringify(this.state.repos, null, 2)}</pre>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
