import { useState, useEffect } from "react";
import { useContext } from "react";
import CampaignList from "../components/Campaigns/CampaignList";
import AuthContext from "../store/auth-context";

function Campaign() {
  const [isLoading, setIsLoading] = useState(true);
  const [loadedCampaigns, setLoadedCampaigns] = useState([]);
  const authCtx = useContext(AuthContext);
  const userName = { UserName: authCtx.userName };
  useEffect(() => {
    setIsLoading(true);
    fetch("https://f3fi8dc437.execute-api.us-east-1.amazonaws.com/dev", {
      method: "POST",
      body: JSON.stringify(userName),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        console.log("Response:", response);
        return response.json();
      })
      .then((data) => {
        const campaigns = [];

        for (const key in data) {
          const campaign = {
            campaignId: key,
            ...data[key],
          };
          console.log("Campaign", campaign);
          campaigns.push(campaign);
        }

        setIsLoading(false);
        setLoadedCampaigns(campaigns);
      });
  }, []);

  if (isLoading) {
    return (
      <section>
        <p>Loading...</p>
      </section>
    );
  }

  return (
    <section>
      <h1>All campaigns</h1>
      <CampaignList campaigns={loadedCampaigns} />
    </section>
  );
}

export default Campaign;
