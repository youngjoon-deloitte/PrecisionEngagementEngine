import { useState, useRef, useContext } from "react";
import { useNavigate } from "react-router-dom";
import UserPool from "./UserPool";
import {
  CognitoUserPool,
  CognitoUserAttribute,
  CognitoUser,
  AuthenticationDetails,
} from "amazon-cognito-identity-js";

import AuthContext from "../../store/auth-context";
import classes from "./AuthForm.module.css";

const AuthForm = () => {
  const history = useNavigate();
  const usernameInputRef = useRef();
  const emailInputRef = useRef();
  const phone_numberInputRef = useRef();
  const passwordInputRef = useRef();
  const profileInputRef = useRef();

  const authCtx = useContext(AuthContext);
  console.log("Auth1", authCtx);

  const [isLogin, setIsLogin] = useState(true);
  const [isLoading, setIsLoading] = useState(false);

  const switchAuthModeHandler = () => {
    setIsLogin((prevState) => !prevState);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    var attributeList = [];
    const enteredUserName = usernameInputRef.current.value;
    const enteredPassword = passwordInputRef.current.value;
    if (!isLogin) {
      const enteredProfile = profileInputRef.current.value;
      const enteredEmail = emailInputRef.current.value;
      const enteredPhoneNumber = phone_numberInputRef.current.value;
      var dataProfile = {
        Name: "profile",
        Value: enteredProfile,
      };
      var dataEmail = {
        Name: "email",
        Value: enteredEmail,
      };
      var dataPhoneNumber = {
        Name: "phone_number",
        Value: enteredPhoneNumber,
      };
      attributeList.push(dataProfile);
      attributeList.push(dataEmail);
      attributeList.push(dataPhoneNumber);
      UserPool.signUp(
        enteredUserName,
        enteredPassword,
        attributeList,
        null,
        (err, data) => {
          if (err) {
            console.error(err);
          }
          console.log(data);
          //history("/auth");
        }
      );
    } else {
      const user = new CognitoUser({
        Username: enteredUserName,
        Pool: UserPool,
      });
      const authDetails = new AuthenticationDetails({
        Username: enteredUserName,
        Password: enteredPassword,
      });

      user.authenticateUser(authDetails, {
        onSuccess: (data) => {
          //console.log("onSuccess: ", data);
          console.log("Profile: ", data.idToken.payload.profile);
          const expirationTime = new Date(
            new Date().getTime() + data.idToken.payload.exp * 1000
          );
          console.log("Profile: ", data.idToken.payload.profile);
          console.log("UserName: ", data.accessToken.payload.username);
          console.log("Expiration Time", expirationTime);
          authCtx.login(
            data.idToken.jwtToken,
            data.idToken.payload.profile,
            data.accessToken.payload.username,
            expirationTime.toISOString()
          );
          console.log("AuthCTX", authCtx);
          history("/");
        },
        onFailure: (err) => {
          console.error("onFailure :", err);
        },
        newPasswordRequired: (data) => {
          console.log("newPassword Required: ", data);
        },
      });
    }
  };

  return (
    <section className={classes.auth}>
      <h1>{isLogin ? "Login" : "Sign Up"}</h1>
      <form onSubmit={submitHandler}>
        <div className={classes.control}>
          <label htmlFor="username">Your Username</label>
          <input
            type="username"
            id="username"
            required
            ref={usernameInputRef}
          />
        </div>
        <div className={classes.control}>
          <label htmlFor="password">Your Password</label>
          <input
            type="password"
            id="password"
            required
            ref={passwordInputRef}
          />
        </div>
        <div className={classes.control}>
          {isLogin ? (
            ""
          ) : (
            <>
              <label htmlFor="email">Your Email</label>
              <input type="email" id="email" required ref={emailInputRef} />
            </>
          )}
        </div>
        <div className={classes.control}>
          {isLogin ? (
            ""
          ) : (
            <>
              <label htmlFor="phone_number">Your Phone Number</label>
              <input
                type="phone_number"
                id="phone_number"
                required
                ref={phone_numberInputRef}
              />
            </>
          )}
        </div>
        <div className={classes.control}>
          {isLogin ? (
            ""
          ) : (
            <>
              <label htmlFor="profile">Your Profile</label>
              <input
                type="profile"
                id="profile"
                required
                ref={profileInputRef}
              />
            </>
          )}
        </div>
        <div className={classes.actions}>
          {!isLoading && (
            <button>{isLogin ? "Login" : "Create Account"}</button>
          )}
          {isLoading && <p>Sending request...</p>}
          <button
            type="button"
            className={classes.toggle}
            onClick={switchAuthModeHandler}
          >
            {isLogin ? "Create new account" : "Login with existing account"}
          </button>
        </div>
      </form>
    </section>
  );
};

export default AuthForm;
