import Card from "../ui/Card";
import classes from "./Form.module.css";
import React from "react";

const OutreachChannel = ({ prevStep, nextStep, handleChange, values }) => {
  const componentDidMount = () => {
    if ((values.outreachType = "Journey Based Outreach")) {
      document.getElementById("ContinueDefault").click();
    }
  };

  const checkClick = () => {
    console.log("clicked!");
  };
  const Previous = (e) => {
    e.preventDefault();
    prevStep();
  };
  const Continue = (e) => {
    e.preventDefault();
    nextStep();
  };

  return (
    <Card>
      <h1>Outreach Channel</h1>
      <form>
        <div className={classes.control}>
          <label>
            SMS
            <input
              name="outreachChannel"
              type="radio"
              required
              value="SMS"
              onChange={handleChange("outreachChannel")}
            />
          </label>
        </div>
        <div className={classes.control}>
          <label>
            Email
            <input
              name="outreachChannel"
              type="radio"
              required
              value="Email"
              onChange={handleChange("outreachChannel")}
            />
          </label>
        </div>
        <div className={classes.actions}>
          <button onClick={Previous}>Previous</button>
        </div>
        <div className={classes.actions}>
          <button onClick={Continue}>Next</button>
        </div>
      </form>
    </Card>
  );
};

export default OutreachChannel;
