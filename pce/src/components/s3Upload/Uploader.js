import React from "react";
import "react-dropzone-uploader/dist/styles.css";
import Dropzone from "react-dropzone-uploader";

const Uploader = () => {
  const axios = require("axios").default;
  const url = window.location.href;
  const campaignId = url.split("/").pop();

  const API_ENDPOINT =
    "https://7cr0b7ym2l.execute-api.us-east-1.amazonaws.com/pce-getPresignedURLs?Campaign=MedicaidLier";
  const handleChangeStatus = ({ meta, remove }, status) => {
    console.log(status, meta);
  };

  const handleSubmit = async (files) => {
    const f = files[0];
    console.log(f["file"]);
    // * GET request: presigned URL
    const response = await axios({
      method: "GET",
      url: API_ENDPOINT,
    });

    console.log("Response: ", response);

    // * PUT request: upload file to S3
    const result = await fetch(response.data.uploadURL, {
      method: "PUT",
      body: f["file"],
    });
    console.log("Result: ", result, "Status", result.status);
    if (result.status === 200) {
      alert("File Uploaded Successfully");
      window.location.reload(true);
    } else {
      alert("File Upload Failed");
    }
  };

  return (
    <Dropzone
      onChangeStatus={handleChangeStatus}
      onSubmit={handleSubmit}
      hjello
      maxFiles={1}
      multiple={false}
      canCancel={false}
      inputContent="Upload Users"
      styles={{
        dropzone: { width: 400, height: 200 },
        dropzoneActive: { borderColor: "green" },
      }}
    />
  );
};

<Uploader />;

export default Uploader;
