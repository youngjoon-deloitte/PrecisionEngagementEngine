import React from "react";
export const CustomDropdownJourney = (props) => (
  <div>
    <strong>{props.username}</strong>
    <select name="{props.username}" onChange={props.onChange}>
      <option defaultValue>Select {props.name}</option>
      {props.options.map((item, index) => (
        <option key={index} value={item.username}>
          {item.username}
        </option>
      ))}
    </select>
  </div>
);
export default class JourneyListDropDown extends React.Component {
  constructor() {
    super();
    this.state = {
      collection: [],
      value: "",
    };
  }
  componentDidMount() {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((res) => this.setState({ collection: res }));
  }
  onChange = (event) => {
    this.setState({ value: event.target.value });
    this.props.getJourneyName(event.target.value);
  };

  render() {
    return (
      <div>
        Select the Template
        <CustomDropdownJourney
          name={this.state.username}
          options={this.state.collection}
          onChange={this.onChange}
        />
      </div>
    );
  }
}
