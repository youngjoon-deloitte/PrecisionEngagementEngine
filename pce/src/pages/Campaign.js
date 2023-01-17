import { useState, useEffect } from "react";
import { useContext } from "react";
import CampaignList from "../components/Campaigns/CampaignList";
import AuthContext from "../store/auth-context";
import Uploader from "../components/s3Upload/Uploader";
import Card from "../components/ui/Card";
import classes from "../components/Campaigns/CampaignItem.module.css";

function CampaignDetail() {
  const url = window.location.href;
  const campaignId = url.split("/").pop();
  const [isLoading, setIsLoading] = useState(true);
  const [loadedCampaigns, setLoadedCampaigns] = useState([]);
  const campaign = { campaignId: campaignId };
  useEffect(() => {
    setIsLoading(true);
    fetch("https://85uu8de1h1.execute-api.us-east-1.amazonaws.com/dev", {
      method: "POST",
      body: JSON.stringify(campaign),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        console.log("Response:", response);
        return response.json();
      })
      .then((data) => {
        console.log("Data:", data);
        setLoadedCampaigns(data);
        setIsLoading(false);
      });
  }, []);

  if (isLoading) {
    return (
      <section>
        <p>Loading...</p>
      </section>
    );
  }
  const campaignName = loadedCampaigns.map((campaign) => campaign.campaignName);
  const campaignDescription = loadedCampaigns.map(
    (campaign) => campaign.campaignDescription
  );
  const campaignStartDateTime = loadedCampaigns.map(
    (campaign) => campaign.campaignStartDateTime
  );
  const campaignEndDateTime = loadedCampaigns.map(
    (campaign) => campaign.campaignEndDateTime
  );
  const campaignQuietStartTime = loadedCampaigns.map(
    (campaign) => campaign.campaignQuietStartTime
  );
  const campaignQuietEndTime = loadedCampaigns.map(
    (campaign) => campaign.campaignQuietEndTime
  );

  return (
    <section>
      <h1>All campaigns</h1>
      <li className={classes.item}>
        <Card>
          <div>
            <div className={classes.content}>
              <h1>{campaignName}</h1>
            </div>
            <div className={classes.content}>
              <h3>{campaignDescription}</h3>
            </div>
            <div className={classes.content}>
              <div className="columns">
                <h3>Scheduled Start: {campaignStartDateTime}</h3>
              </div>
              <div className="columns">
                <h3>Scheduled End: {campaignEndDateTime}</h3>
              </div>
            </div>
            <div className={classes.content}>
              <div className="columns">
                <h3>Quiet Hours Start: {campaignQuietStartTime}</h3>
              </div>
              <div className="columns">
                <h3>Quiet Hours End: {campaignQuietEndTime}</h3>
              </div>
            </div>
            <Uploader />
          </div>
        </Card>
      </li>
    </section>
  );
}

export default CampaignDetail;
