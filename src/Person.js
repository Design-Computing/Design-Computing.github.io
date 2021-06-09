import React from "react";
import jsyaml from "js-yaml";

class Person extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: undefined,
      studentNumber: "z1234567",
      officialEmail: "noIdea@unsw.edu.au",
      contactEmail: "firstName.Lastname@whereIwork.com",
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
          a = jsyaml.load(atob(x.content));
          const e = a.contactEmail;
          if (e && e.firstBit && e.otherBit) {
            this.setState({
              name: a.name,
              studentNumber: a.studentNumber,
              officialEmail: a.officialEmail,
              contactEmail: `${e.firstBit}@${e.otherBit}`
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
        <p>{this.state.officialEmail}</p>
        <p>{this.state.contactEmail}</p>
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
