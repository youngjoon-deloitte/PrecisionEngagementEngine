import Card from "../ui/Card";
import classes from "./Form.module.css";
import React, { Component } from "react";
import { useState } from "react";
import TemplateListDropDown from "./TemplateListDropDown";
import JourneyListDropDown from "./JourneyListDropDown";

const AddMessage = ({
  prevStep,
  nextStep,
  handleChange,
  values,
  handleChangeTemplateName,
  handleChangeJourneyName,
}) => {
  const CallbackFunction = (childData) => {
    handleChangeTemplateName(childData);
  };
  const CallbackFunctionJourney = (childData) => {
    handleChangeJourneyName(childData);
    console.log(childData);
  };
  const Previous = (e) => {
    e.preventDefault();
    prevStep();
  };
  const Continue = (e) => {
    e.preventDefault();
    nextStep();
  };
  const [isNewTemplate, setIsNewTemplate] = useState(false);
  const setIsNewTemplateHandler = () => {
    setIsNewTemplate(true);
  };
  const setIsExistingTemplateHandler = () => {
    setIsNewTemplate(false);
  };
  if (values.outreachType === "Single Message Outreach") {
    return (
      <Card>
        <h1>Add Message</h1>
        <form>
          <div className={classes.control}>
            <label>
              Create New Template
              <input
                name="templateType"
                type="radio"
                required
                value="Create New Template"
                onChange={handleChange("templateType")}
                onClick={setIsNewTemplateHandler}
              />
            </label>
          </div>
          <div className={classes.control}>
            <label>
              Use Existing Template
              <input
                name="templateType"
                type="radio"
                required
                value="Use Existing Template"
                onChange={handleChange("templateType")}
                onClick={setIsExistingTemplateHandler}
              />
            </label>
          </div>
          {isNewTemplate ? (
            <div className={classes.control}>
              <label>
                Enter Message
                <input
                  type="text"
                  required
                  placeholder="Enter Message"
                  value={values.message}
                  onChange={handleChange("message")}
                />
              </label>
            </div>
          ) : (
            <TemplateListDropDown getTemplateName={CallbackFunction} />
          )}
          <div className={classes.actions}>
            <button onClick={Previous}>Previous</button>
          </div>
          <div className={classes.actions}>
            <button onClick={Continue}>Next</button>
          </div>
        </form>
      </Card>
    );
  }
  {
    return (
      <Card>
        <h1>Select Journey</h1>
        <form>
          <JourneyListDropDown getJourneyName={CallbackFunctionJourney} />
          <div className={classes.actions}>
            <button onClick={Previous}>Previous</button>
          </div>
          <div className={classes.actions}>
            <button onClick={Continue}>Next</button>
          </div>
        </form>
      </Card>
    );
  }
};

export default AddMessage;
