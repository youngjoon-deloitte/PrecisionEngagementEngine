import { Route, Routes, Navigate } from "react-router-dom";
import { useContext } from "react";
import AuthContext from "./store/auth-context";

import AllCampaignsPage from "./pages/AllCampaigns";
import NewCampaignPage from "./pages/NewCampaign";
import CampaignDetail from "./pages/Campaign";
import AuthPage from "./pages/AuthPage";
import FavoritesPage from "./pages/Favorites";
import Layout from "./components/layout/Layout";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const authCtx = useContext(AuthContext);
  console.log(
    "Auth Status",
    authCtx.isLoggedIn,
    authCtx.userName,
    authCtx.profile
  );
  return (
    <Layout>
      <Routes>
        <Route path="/" exact element={<AllCampaignsPage />}></Route>
        <Route path="/campaign/:id" element={<CampaignDetail />} exact></Route>
        {!authCtx.isLoggedIn && (
          <Route path="/auth" element={<AuthPage />}></Route>
        )}
        <Route path="/new-campaign" element={<NewCampaignPage />}></Route>
        <Route path="/favorites" element={<FavoritesPage />}></Route>
      </Routes>
    </Layout>
  );
}

export default App;
