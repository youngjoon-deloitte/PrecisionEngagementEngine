import { useNavigate } from "react-router-dom";

import NewCampaignForm from "../components/Campaigns/NewCampaignForm";
import Signup from "../components/forms/Signup";

function NewCampaignPage() {
  const history = useNavigate();

  function addCampaignHandler(campaignData) {
    fetch(
      "https://react-getting-started-48dec-default-rtdb.firebaseio.com/campaigns.json",
      {
        method: "POST",
        body: JSON.stringify(campaignData),
        headers: {
          "Content-Type": "application/json",
        },
      }
    ).then(() => {
      history.replace("/");
    });
  }

  return (
    <section>
      <h1>Add New Campaign</h1>
      <Signup />
      {/* <NewCampaignForm onAddCampaign={addCampaignHandler} /> */}
    </section>
  );
}

export default NewCampaignPage;
