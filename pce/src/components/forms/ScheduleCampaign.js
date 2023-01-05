import Card from "../ui/Card";
import classes from "./Form.module.css";
import React from "react";

const ScheduleCampaign = ({ prevStep, nextStep, handleChange, values }) => {
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
      <h1>Schedule Campaign</h1>
      <form>
        <div className={classes.control}>
          <label>
            Campaign Start Date and Time
            <input
              name="campaignStartDateTime"
              type="datetime-local"
              required
              value={values.campaignStartDateTime}
              onChange={handleChange("campaignStartDateTime")}
            />
          </label>
        </div>
        <div className={classes.control}>
          <label>
            Campaign End Date and Time
            <input
              name="campaignEndDateTime"
              type="datetime-local"
              required
              value={values.campaignEndDateTime}
              onChange={handleChange("campaignEndDateTime")}
            />
          </label>
        </div>
        <div className={classes.control}>
          <label>
            Quiet Hours Start Time (Optional)
            <input
              name="campaignQuietStartTime"
              type="time"
              required
              value={values.campaignQuietStartTime}
              onChange={handleChange("campaignQuietStartTime")}
            />
          </label>
        </div>
        <div className={classes.control}>
          <label>
            Quiet Hours End Time (Optional)
            <input
              name="campaignQuietEndTime"
              type="time"
              required
              value={values.campaignQuietEndTime}
              onChange={handleChange("campaignQuietEndTime")}
            />
          </label>
        </div>
        <div className={classes.control}>
          <label>timeZone</label>
          <select onChange={handleChange("timeZone")} value={values.timeZone}>
            <option value="utc">UTC</option>
            <option value="utc+01">UTC+01</option>
            <option value="utc+02">UTC+02</option>
            <option value="utc+03">UTC+03</option>
            <option value="utc+03:30">UTC+03:30</option>
            <option value="utc+04">UTC+04</option>
            <option value="utc+04:30">UTC+04:30</option>
            <option value="utc+05">UTC+05</option>
            <option value="utc+05:30">UTC+05:30</option>
            <option value="utc+05:45">UTC+05:45</option>
            <option value="utc+06">UTC+06</option>
            <option value="utc+06:30">UTC+06:30</option>
            <option value="utc+07">UTC+07</option>
            <option value="utc+08">UTC+08</option>
            <option value="utc+09">UTC+09</option>
            <option value="utc+09:30">UTC+09:30</option>
            <option value="utc+10">UTC+10</option>
            <option value="utc+10:30">UTC+10:30</option>
            <option value="utc+11">UTC+11</option>
            <option value="utc+12">UTC+12</option>
            <option value="utc+13">UTC+13</option>
            <option value="utc-01">UTC-01</option>
            <option value="utc-02">UTC-02</option>
            <option value="utc-03">UTC-03</option>
            <option value="utc-04">UTC-04</option>
            <option value="utc-05">UTC-05</option>
            <option value="utc-06">UTC-06</option>
            <option value="utc-07">UTC-07</option>
            <option value="utc-08">UTC-08</option>
            <option value="utc-09">UTC-09</option>
            <option value="utc-10">UTC-10</option>
            <option value="utc-11">UTC-11</option>
          </select>
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

export default ScheduleCampaign;
