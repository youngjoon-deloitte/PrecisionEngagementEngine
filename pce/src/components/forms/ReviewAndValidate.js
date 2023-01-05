import Card from "../ui/Card";
import classes from "./Form.module.css";
import React from "react";

const ReviewAndValidate = ({ prevStep, nextStep, values }) => {
  console.log(values);
  //console.log(values1);
  const {
    campaignName,
    campaignDescription,
    outreachType,
    outreachChannel,
    templateType,
    message,
    templateName,
    journeyName,
    campaignStartDateTime,
    campaignEndDateTime,
    campaignQuietStartTime,
    campaignQuietEndTime,
    timeZone,
    reviewAndValidate,
  } = values;
  const Continue = (e) => {
    e.preventDefault();
    nextStep();
  };

  const Previous = (e) => {
    e.preventDefault();
    prevStep();
  };
  return (
    <Card>
      <div>
        <ul>
          <li>Campaign Name: {campaignName}</li>
          <li>Campaign Description: {campaignDescription}</li>
          <li>Outreach Type: {outreachType}</li>
          <li>Outreach Channel: {outreachChannel}</li>
          <li>Template Type: {templateType}</li>
          <li>Message: {message}</li>
          <li>Template Name: {templateName}</li>
          <li>Journey Name: {journeyName}</li>
          <li>Campaign Start Date Time: {campaignStartDateTime}</li>
          <li>Campaign End Date Time: {campaignEndDateTime}</li>
          <li>Campaign Quiet Start Time: {campaignQuietStartTime}</li>
          <li>Campaign Quiet End Time: {campaignQuietEndTime}</li>
          <li>Time Zone: {timeZone}</li>
        </ul>
      </div>
      <div className={classes.actions}>
        <button onClick={Previous}>Previous</button>
      </div>
      <div className={classes.actions}>
        <button onClick={Continue}>Next</button>
      </div>
    </Card>
  );
};

export default ReviewAndValidate;
