import React, { useState, useEffect, useCallback, Profiler } from "react";

let logoutTimer;

const AuthContext = React.createContext({
  token: "",
  isLoggedIn: false,
  profile: "",
  userName: "",
  expirationTime: "",
  login: (token, profile, userName, expirationTime) => {},
  logout: () => {},
});

const calculateRemainingTime = (expirationTime) => {
  const currentTime = new Date().getTime();
  const adjExpirationTime = expirationTime; //new Date(expirationTime).getTime();
  console.log("current time", currentTime);
  const remainingDuration = adjExpirationTime - currentTime;
  console.log("Remaining Duration", remainingDuration);
  return remainingDuration;
};

const retrieveStoredToken = () => {
  const storedToken = localStorage.getItem("token");
  const storedExpirationDate = localStorage.getItem("expirationTime");
  const storedProfile = localStorage.getItem("profile");
  const storedUserName = localStorage.getItem("userName");

  const remainingTime = calculateRemainingTime(storedExpirationDate);

  if (remainingTime <= 3600) {
    localStorage.removeItem("token");
    localStorage.removeItem("expirationTime");
    localStorage.removeItem("profile");
    localStorage.removeItem("userName");
    return null;
  }

  return {
    token: storedToken,
    expirationTime: remainingTime,
    profile: storedProfile,
    userName: storedUserName,
  };
};

export const AuthContextProvider = (props) => {
  const tokenData = retrieveStoredToken();
  console.log("token", tokenData);
  let initialToken;
  let initialUserProfile;
  let initialUserName;
  let initialExpirationTime;
  if (tokenData) {
    initialToken = tokenData.token;
    initialUserProfile = tokenData.profile;
    initialUserName = tokenData.userName;
    initialExpirationTime = tokenData.expirationTime;
  }

  const [token, setToken] = useState(initialToken);
  const [profile, setProfile] = useState(initialUserProfile);
  const [userName, setUserName] = useState(initialUserName);
  const [expirationTime, setExpirationTime] = useState(initialExpirationTime);

  const userIsLoggedIn = !!token;
  //const userProfile = tokenData.profile;
  //const userName = tokenData.userName;

  const logoutHandler = useCallback(() => {
    setToken(null);
    setProfile(null);
    setUserName(null);
    setExpirationTime(null);
    localStorage.removeItem("token");
    localStorage.removeItem("expirationTime");
    localStorage.removeItem("profile");
    localStorage.removeItem("userName");
    if (logoutTimer) {
      clearTimeout(logoutTimer);
    }
  }, []);

  const loginHandler = (token, profile, userName, expirationTime) => {
    setToken(token);
    setProfile(profile);
    setUserName(userName);
    setExpirationTime(expirationTime);
    localStorage.setItem("token", token);
    localStorage.setItem("expirationTime", expirationTime);
    localStorage.setItem("profile", profile);
    localStorage.setItem("userName", userName);

    const remainingTime = calculateRemainingTime(expirationTime);

    //logoutTimer = setTimeout(logoutHandler, remainingTime);
  };

  /*useEffect(() => {
    if (tokenData) {
      console.log("Expiration Time", tokenData.expirationTime);
      logoutTimer = setTimeout(logoutHandler, tokenData.expirationTime);
    }
  }, [tokenData, logoutHandler]);
  */

  const contextValue = {
    token: token,
    isLoggedIn: userIsLoggedIn,
    profile: profile,
    userName: userName,
    expirationTime: expirationTime,
    login: loginHandler,
    logout: logoutHandler,
  };

  return (
    <AuthContext.Provider value={contextValue}>
      {props.children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
