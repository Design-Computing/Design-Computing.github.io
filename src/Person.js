import React from "react";
import jsyaml from "js-yaml";

class Person extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "Your Name",
      studentNumber: "z1234567",
      officialEmail: "noIdea@unsw.edu.au",
      contactEmail: "firstName.Lastname@whereIwork.com"
    };
  }

  componentDidMount() {
    // GET /repos/:owner/:repo/contents/:path
    const url = `https://api.github.com/repos/${
      this.props.forkData.login
    }/me/contents/aboutMe.yml`;
    fetch(url, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    })
      .then(x => x.json())
      .then(x => {
        const a = jsyaml.load(atob(x.content));
        this.setState({
          name: a.name,
          studentNumber: a.studentNumber,
          officialEmail: a.officialEmail,
          contactEmail: `${a.contactEmail.firstBit}@${a.contactEmail.otherBit}`
        });
      });
  }

  render() {
    if (this.props.forkData) {
      return (
        <div className="person">
          <img
            alt={`${this.state.name}'s face`}
            src={`https://avatars.githubusercontent.com/${
              this.props.forkData.login
            }`}
          />
          <div className="info">
            <h1>
              <a href={this.props.forkData.html_url}>{this.state.name}</a>
            </h1>
            <p>{this.state.studentNumber}</p>
            <p>{this.state.officialEmail}</p>
            <p>{this.state.contactEmail}</p>

            {/* <pre>{JSON.stringify(this.props, null, 2)}</pre> */}
          </div>
        </div>
      );
    } else {
      return null;
    }
  }
}

export default Person;
