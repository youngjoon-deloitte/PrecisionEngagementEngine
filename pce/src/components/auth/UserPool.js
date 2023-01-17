import { CognitoUserPool } from "amazon-cognito-identity-js";

const poolData = {
  UserPoolId: "us-east-1_nvwxM0lXo",
  ClientId: "6kaledf056h4bab9c2uvgv2eqn",
};

export default new CognitoUserPool(poolData);
