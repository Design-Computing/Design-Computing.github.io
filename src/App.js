import React from "react";
import ReactDOM from "react-dom";
import Person from "./Person";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { repos: [{ things: "coming", id: 0 }] };
  }

  componentDidMount() {
    fetch("https://api.github.com/repos/Design-Computing/me/forks", {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    })
      .then(x => x.json())
      .then(x => {
        this.setState({ repos: x });
      });
  }

  render() {
    return (
      <div>
        {this.state.repos.map(r => {
          if ("owner" in r) {
            return <Person key={r.id} forkData={r.owner} />;
          }
        })}
        {/* <pre>{JSON.stringify(this.state.repos, null, 2)}</pre> */}
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
