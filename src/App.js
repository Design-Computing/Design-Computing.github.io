import React from "react";
import ReactDOM from "react-dom";
import ReactMarkdown from "react-markdown";
import Person from "./Person";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      repos: [{ things: "coming", id: 0 }],
      general: "# Loading Content"
    };
  }

  componentDidMount() {
    const api = "https://api.github.com";
    const org = "design-computing";
    let url = `${api}/repos/${org}/me/forks`;
    fetch(url, {
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

    url = `${api}/repos/${org}/Design-Computing.github.io/contents/general.md`;
    fetch(url, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    })
      .then(x => x.json())
      .then(x => {
        this.setState({ general: atob(x.content) });
      });
  }

  render() {
    return (
      <div>
        <ReactMarkdown source={this.state.general} className="writing" />
        <div className="facebook">
          {this.state.repos.map(r => {
            if ("owner" in r) {
              return <Person key={r.id} forkData={r.owner} />;
            }
          })}
        </div>
        {/* <pre>{JSON.stringify(this.state.repos, null, 2)}</pre> */}
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
