import CampaignItem from "./CampaignItem";
import classes from "./CampaignList.module.css";

function CampaignList(props) {
  return (
    <ul className={classes.list}>
      {props.campaigns.map((campaign) => (
        <CampaignItem
          key={campaign.campaignId}
          campaignId={campaign.campaignId}
          campaignName={campaign.campaignName}
          campaignDescription={campaign.campaignDescription}
          campaignCreationDate={campaign.campaignCreationDate}
          campaignStartDateTime={campaign.campaignStartDateTime}
          campaignEndDateTime={campaign.campaignEndDateTime}
        />
      ))}
    </ul>
  );
}

export default CampaignList;
