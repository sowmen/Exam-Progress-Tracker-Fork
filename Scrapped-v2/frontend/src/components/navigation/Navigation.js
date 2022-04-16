/** @format */

import React from "react";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";

import NavAuthorized from './NavAuthorized';
import NavLoginPrompt from './NavLoginPrompt';

const Navigation = ({ isAuthorized }) => {
	return (
		<AppBar position="static" style={{ background: '#2E3B55' }}>
			<Toolbar>
				{isAuthorized? <NavAuthorized/>: <NavLoginPrompt/>}
			</Toolbar>
		</AppBar>
	);
};

export default Navigation;
