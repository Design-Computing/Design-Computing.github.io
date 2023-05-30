import jsyaml from "js-yaml";
// import { parse } from "yaml";
import React from "react";

class Person extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: undefined,
      studentNumber: "z1234567",
      errorMessage: undefined
    };
  }

  componentDidMount() {
    // GET /repos/:owner/:repo/contents/:path
    const url = `https://api.github.com/repos/${this.props.forkData.login}/me/contents/aboutMe.yml`;
    fetch(url, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "User-Agent": "notionparallax"
      }
    })
      .then(x => x.json())
      .then(x => {
        let a;
        try {
          let fileContent = atob(x.content);
          // try {
          a = jsyaml.load(fileContent);
          // } catch (e) {
          //   a = parse(fileContent);
          // }
          if (a.first_name) {
            this.setState({
              name: a.first_name,
              studentNumber: a.studentNumber
            });
          } else {
            this.setState({
              errorMessage: "aboutMe.yml not updated " + JSON.stringify(a)
            });
          }
        } catch (error) {
          this.setState({ errorMessage: error });
        }
      });
  }

  render() {
    const goodInfo = (
      <div>
        <p>{this.state.studentNumber}</p>
        <h1>
          <a href={this.props.forkData.html_url}>
            {this.state.name || this.props.forkData.html_url}
          </a>
        </h1>
      </div>
    );
    const badInfo = (
      <div>
        <p>{this.errorMessage}</p>
        <pre>{JSON.stringify(this.props, null, 2)}</pre>
        <h1>
          <a href={this.props.forkData.html_url}>
            {this.props.forkData.html_url.split("/")[3]}
          </a>
        </h1>
      </div>
    );

    if (this.props.forkData) {
      try {
        return (
          <div className="person">
            <img
              alt={`${this.state.name}'s face`}
              src={`https://avatars.githubusercontent.com/${this.props.forkData.login}`}
            />
            <div className="info">{this.state.name ? goodInfo : badInfo}</div>
          </div>
        );
      } catch (error) {
        console.log(error);
        return (
          <div className="person">
            {JSON.stringify(this.props.forkData, null, 2)}
          </div>
        );
      }
    } else {
      return null;
    }
  }
}

export default Person;
