import { useContext } from "react";
import { Link } from "react-router-dom";

import classes from "./MainNavigation.module.css";
import FavoritesContext from "../../store/favorites-context";
import AuthContext from "../../store/auth-context";

function MainNavigation() {
  const favoritesCtx = useContext(FavoritesContext);
  const authCtx = useContext(AuthContext);

  const isLoggedIn = authCtx.isLoggedIn;
  const userProfile = authCtx.profile;
  console.log("authCTX Log", authCtx.profile);
  const logoutHandler = () => {
    authCtx.logout();
    // optional: redirect the user
  };

  return (
    <header className={classes.header}>
      <div className={classes.logo}>Precision Clinical Engine</div>
      <nav>
        <ul>
          <li>
            <Link to="/">All Campaigns</Link>
          </li>
          <li>
            <Link to="/new-campaign">Add New Campaign</Link>
          </li>
          <li>
            <Link to="/favorites">
              My Favorites
              <span className={classes.badge}>
                {favoritesCtx.totalFavorites}
              </span>
            </Link>
          </li>
          {isLoggedIn && userProfile == "Admin" && (
            <li>
              <Link to="/new-campaign">Admin</Link>
            </li>
          )}
          {!isLoggedIn && (
            <li>
              <Link to="/auth">Login</Link>
            </li>
          )}
          {isLoggedIn && (
            <li>
              <button onClick={logoutHandler}>
                {authCtx.userName} (LogOut)
              </button>
            </li>
          )}
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;
