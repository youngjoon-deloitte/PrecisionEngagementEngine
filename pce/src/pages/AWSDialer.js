import React from "react";

const Dialer = () => {
  const [data, setData] = React.useState([]);

  return (
    <div
      style={{
        backgroundImage: "url(/HIP1.jpg)",
        width: "100%",
        height: "100%",
      }}
    >
      <h1>Real-time Data</h1>
      {data.map((item) => (
        <div key={item.memberId}>
          Name: {item.name}
          <br />
          Phone Number: {item.phoneNumber}
          <br />
          Status: {item.status}
        </div>
      ))}
      <button>AWS Connect Phone</button>
    </div>
  );
};

export default Dialer;
