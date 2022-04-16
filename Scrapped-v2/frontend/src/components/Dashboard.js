/** @format */

import React from "react";

import DashboardLoggedIn from "./DashboardLoggedIn";
import DashboardLoggedOut from "./DashboardLoggedOut";

const Dashboard = ({ isAuthorized }) => {
	console.log(isAuthorized);
	return (
		<>
			{isAuthorized? <DashboardLoggedIn/> : <DashboardLoggedOut/>}
		</>
	);
};

export default Dashboard;
