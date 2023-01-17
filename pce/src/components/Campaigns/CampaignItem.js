import { useContext } from "react";

import Card from "../ui/Card";
import classes from "./CampaignItem.module.css";
import FavoritesContext from "../../store/favorites-context";
import { useNavigate } from "react-router-dom";

function CampaignItem(props) {
  const favoritesCtx = useContext(FavoritesContext);
  const history = useNavigate();
  const itemIsFavorite = favoritesCtx.itemIsFavorite(props.id);
  const onClickHandler = () => {
    history("/campaign/" + props.campaignId);
  };

  function toggleFavoriteStatusHandler() {
    if (itemIsFavorite) {
      favoritesCtx.removeFavorite(props.id);
    } else {
      favoritesCtx.addFavorite({
        key: props.id,
        campaignName: props.campaignName,
        campaignDescription: props.campaignDescription,
        campaignCreationDate: props.campaignCreationDate,
        campaignStartDateTime: props.campaignStartDateTime,
        campaignEndDateTime: props.campaignEndDateTime,
      });
    }
  }

  return (
    <li className={classes.item}>
      <Card>
        <div onClick={onClickHandler}>
          <div className={classes.content}>
            <h1>{props.campaignName}</h1>
          </div>
          <div className={classes.content}>
            <h3>{props.campaignDescription}</h3>
          </div>
          <div className={classes.content}>
            <div className="columns">
              <h3>Scheduled Start: {props.campaignStartDateTime}</h3>
            </div>
            <div className="columns">
              <h3>Scheduled End: {props.campaignEndDateTime}</h3>
            </div>
          </div>
          <div className={classes.actions}>
            <button onClick={toggleFavoriteStatusHandler}>
              {itemIsFavorite ? "Remove from Favorites" : "To Favorites"}
            </button>
          </div>
        </div>
      </Card>
    </li>
  );
}

export default CampaignItem;
