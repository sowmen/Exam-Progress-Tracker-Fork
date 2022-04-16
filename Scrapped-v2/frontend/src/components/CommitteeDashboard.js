import React from "react";
import Button from "@material-ui/core/Button";
import ActiveCoursesCD from "./committeeDashboard/ActiveCoursesCD";
import CommitteeMember from "./committeeDashboard/CommitteeMember";

const buttonStyle = {
  position: "absolute",
  left: "50%",
  top: "10%",
  transform: "translate(-50%, -10%)",
};

const activeCourseStyle = {
  position: "absolute",
  left: "50%",
  top: "50%",
  transform: "translate(-50%, -50%)",
};

const committeeMemberStyle = {
  position: "absolute",
  right: "18%",
  top: "50%",
  transform: "translate(80%, -50%)",
};
const CommitteeDashboard = () => {
  return (
    <>
      <div className="container" style={buttonStyle}>
        <Button variant="contained" color="primary">
          Create New Course
        </Button>
      </div>
      <div className="container" style={activeCourseStyle}>
        <ActiveCoursesCD />
      </div>
      <div className="container" style={committeeMemberStyle}>
        <CommitteeMember />
      </div>
    </>
  );
};

export default CommitteeDashboard;
