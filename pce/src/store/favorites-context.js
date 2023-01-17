import { createContext, useState } from "react";

const FavoritesContext = createContext({
  favorites: [],
  totalFavorites: 0,
  addFavorite: (favoritecampaign) => {},
  removeFavorite: (campaignId) => {},
  itemIsFavorite: (campaignId) => {},
});

export function FavoritesContextProvider(props) {
  const [userFavorites, setUserFavorites] = useState([]);

  function addFavoriteHandler(favoritecampaign) {
    setUserFavorites((prevUserFavorites) => {
      return prevUserFavorites.concat(favoritecampaign);
    });
  }

  function removeFavoriteHandler(campaignId) {
    setUserFavorites((prevUserFavorites) => {
      return prevUserFavorites.filter((campaign) => campaign.id !== campaignId);
    });
  }

  function itemIsFavoriteHandler(campaignId) {
    return userFavorites.some((campaign) => campaign.id === campaignId);
  }

  const context = {
    favorites: userFavorites,
    totalFavorites: userFavorites.length,
    addFavorite: addFavoriteHandler,
    removeFavorite: removeFavoriteHandler,
    itemIsFavorite: itemIsFavoriteHandler,
  };

  return (
    <FavoritesContext.Provider value={context}>
      {props.children}
    </FavoritesContext.Provider>
  );
}

export default FavoritesContext;
