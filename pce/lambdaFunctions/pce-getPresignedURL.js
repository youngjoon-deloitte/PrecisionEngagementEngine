"use strict";

const AWS = require("aws-sdk");
const { default: Campaign } = require("../src/pages/AllCampaigns");
AWS.config.update({ region: process.env.AWS_REGION });
const s3 = new AWS.S3();
const uploadBucket = "pce-upload";

//function to get Campaign parameter from api url

exports.handler = async (event) => {
  const { queryStringParameters } = event;
  const { campaignId } = queryStringParameters;

  const campaign = await getCampaign(campaignId);

  return {
    statusCode: 200,
    body: JSON.stringify(campaign),
  };
};

//capture parameter value from invoke api url and store in campaign variable

const getCampaign = async (campaignId) => {
  const campaign = await Campaign.getCampaign(campaignId);
  return campaign;
};

// Change this value to adjust the signed URL's expiration
const URL_EXPIRATION_SECONDS = 300;

// Main Lambda entry point
exports.handler = async (event) => {
  return await getUploadURL(event);
};

const getUploadURL = async function (event) {
  const randomID = parseInt(Math.random() * 10000000);
  const Key = `${randomID}.csv`;

  // Get signed URL from S3
  const s3Params = {
    Bucket: uploadBucket,
    Key,
    Expires: URL_EXPIRATION_SECONDS,
    ContentType: "text/csv",
  };

  console.log("Params: ", s3Params);
  const uploadURL = await s3.getSignedUrlPromise("putObject", s3Params);

  return JSON.stringify({
    uploadURL: uploadURL,
    Key,
  });
};
