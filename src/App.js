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
    let url = `${api}/repos/${org}/me/forks?per_page=40`;
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

    url = `${api}/repos/${org}/Design-Computing.github.io/contents/md/general.md`;
    fetch(url, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    })
      .then(x => x.json())
      .then(x => {
        if(x.message && x.message.includes("API rate limit exceeded")){
          // general is looking for a markdown string
          this.setState({ general:
`# Well, this is embarrasing, we're being ratelimited 😬

It happens when a lot of people are trying to hit the GitHub API at the same time from this page.

You can still get to the content through these links:

1. [What's supposed to be on this page](https://design-computing.github.io/md/general)
1. [Week 1](https://design-computing.github.io/md/week1)
1. [Week 2](https://design-computing.github.io/md/week2)
1. [Week 3](https://design-computing.github.io/md/week3)
1. [Week 4](https://design-computing.github.io/md/week4)
1. [Week 5](https://design-computing.github.io/md/week5)
1. [Week 6](https://design-computing.github.io/md/week6)
1. [Week 7](https://design-computing.github.io/md/week7)
1. [Week 8+](https://design-computing.github.io/md/theRest)
` });
        }else{
          this.setState({ general: atob(x.content) });
        }
      });
  }

  render() {
    return (
      <div>
        <ReactMarkdown source={this.state.general} className="writing" />
        <div className="facebook">
          {this.renderPeople(this.state)}
        </div>
        {/* <pre>{JSON.stringify(this.state.repos, null, 2)}</pre> */}
      </div>
    );
  }

  renderPeople(state) {
    if (state && state.repos && state.repos.map){
      return state.repos.map(r => {
        if ("owner" in r) {
          return <Person key={r.id} forkData={r.owner} />;
        }
      });
    }else{
      return "<div>😬</div>"
    }
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
