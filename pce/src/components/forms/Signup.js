import React, { Component } from "react";
import AddMessage from "./AddMessage";
import CampaignDetails from "./CampaignDetails";
import OutreachChannel from "./OutreachChannel";
import OutreachDetails from "./OutreachDetails";
import ReviewAndValidate from "./ReviewAndValidate";
import ScheduleCampaign from "./ScheduleCampaign";
import Success from "./Success";

export default class Signup extends Component {
  state = {
    step: 1,
    campaignName: "",
    campaignDescription: "",
    outreachType: "",
    outreachChannel: "",
    templateType: "",
    message: "",
    templateName: "",
    journeyName: "",
    campaignStartDateTime: "",
    campaignEndDateTime: "",
    campaignQuietStartTime: "",
    campaignQuietEndTime: "",
    timeZone: "",
    reviewAndValidate: false,
  };

  // go back to previous step
  prevStep = () => {
    const { step } = this.state;
    this.setState({ step: step - 1 });
  };

  // proceed to the next step
  nextStep = () => {
    const { step } = this.state;
    this.setState({ step: step + 1 });
  };

  // handle field change
  handleChange = (input) => (e) => {
    console.log(e.target.value);
    this.setState({ [input]: e.target.value });
  };

  handleChangeTemplateName = (settemplateName) => {
    this.setState({ templateName: settemplateName });
  };

  handleChangeJourneyName = (setJourneyName) => {
    this.setState({ journeyName: setJourneyName });
  };

  render() {
    const { step } = this.state;
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
      campaignId,
      campaignStatus,
      campaignCreationDate,
      userName,
    } = this.state;
    const values = {
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
    };

    switch (step) {
      case 1:
        return (
          <CampaignDetails
            nextStep={this.nextStep}
            handleChange={this.handleChange}
            values={values}
          />
        );
      case 2:
        return (
          <OutreachDetails
            prevStep={this.prevStep}
            nextStep={this.nextStep}
            handleChange={this.handleChange}
            values={values}
          />
        );
      case 3:
        return (
          <AddMessage
            prevStep={this.prevStep}
            nextStep={this.nextStep}
            handleChange={this.handleChange}
            values={values}
            handleChangeTemplateName={this.handleChangeTemplateName}
            handleChangeJourneyName={this.handleChangeJourneyName}
          />
        );
      case 4:
        return (
          <ScheduleCampaign
            prevStep={this.prevStep}
            nextStep={this.nextStep}
            handleChange={this.handleChange}
            values={values}
          />
        );
      case 5:
        return (
          <ReviewAndValidate
            prevStep={this.prevStep}
            nextStep={this.nextStep}
            handleChange={this.handleChange}
            values={values}
          />
        );
      case 6:
        return <Success />;
      // never forget the default case, otherwise VS code would be mad!
      default:
      // do nothing
    }
  }
}
