import Card from "../ui/Card";
import classes from "./Form.module.css";
import React from "react";
import { useState } from "react";
import OutreachChannel from "./OutreachChannel";

const OutreachDetails = ({ prevStep, nextStep, handleChange, values }) => {
  const [isSingleMessage, setIsSingleMessage] = useState(false);
  const setIsSingleMessageHandler = () => {
    setIsSingleMessage(true);
  };
  const setIsJourneyMessageHandler = () => {
    setIsSingleMessage(false);
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
      <h1>Outreach Type</h1>
      <form>
        <div className={classes.control}>
          <label>
            Single Message Outreach
            <input
              name="outreachType"
              type="radio"
              required
              value="Single Message Outreach"
              onChange={handleChange("outreachType")}
              onClick={setIsSingleMessageHandler}
            />
          </label>
        </div>
        {isSingleMessage ? (
          <div>
            Select Channel
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
          </div>
        ) : (
          ""
        )}
        ;
        <div className={classes.control}>
          <label>
            Journey Based Outreach
            <input
              name="outreachType"
              type="radio"
              required
              value="Journey Based Outreach"
              onChange={handleChange("outreachType")}
              onClick={setIsJourneyMessageHandler}
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

export default OutreachDetails;
