import React from 'react'

import DeadlineTable from "./dashboardComponents/DeadlineTable";
import DashboardNotifications from "./dashboardComponents/DashboardNotifications";

const DashboardLoggedIn = () => {
    return (
      <>
        <div className="container">
          <DeadlineTable />
        </div>
        <div className="container">
          <DashboardNotifications />
        </div>
      </>
    );
}

export default DashboardLoggedIn
