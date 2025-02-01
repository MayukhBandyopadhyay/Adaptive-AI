import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

function Profile() {
  return (
    <div className="container mt-5">
      <h2 className="text-center text-primary">👤 User Profile</h2>
      <div className="card p-4 shadow">
        <h4>John Doe</h4>
        <p>Email: johndoe@example.com</p>
        <p>Courses Completed: 5</p>
        <p>Current Learning Path: Data Science</p>
      </div>
    </div>
  );
}

export default Profile;
