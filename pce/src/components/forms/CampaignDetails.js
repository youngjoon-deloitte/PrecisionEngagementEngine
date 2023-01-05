import Card from "../ui/Card";
import classes from "./Form.module.css";
import React from "react";

const CampaignDetails = ({ nextStep, handleChange, values }) => {
  const Continue = (e) => {
    e.preventDefault();
    nextStep();
  };
  return (
    <Card>
      <h1>Campaign Details</h1>
      <form>
        <div className={classes.control}>
          <label>
            Campaign Name
            <input
              type="text"
              required
              placeholder="Campaign Name"
              value={values.campaignName}
              onChange={handleChange("campaignName")}
            />
          </label>
        </div>
        <div className={classes.control}>
          <label>Campaign Description</label>
          <textarea
            required
            rows="5"
            placeholder="Campaign Description"
            value={values.campaignDescription}
            onChange={handleChange("campaignDescription")}
          ></textarea>
        </div>
        <div className={classes.actions}>
          <button onClick={Continue}>Next</button>
        </div>
      </form>
    </Card>
  );
};

export default CampaignDetails;
