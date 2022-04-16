/** @format */

import React from "react";
import { Route } from "react-router-dom";
import Login from "./Login";
import SignUp from "./Signup";

const AuthWrapper = () => {
	return (
			<div className="auth-wrapper">
				<div className="auth-inner">
					<Route exact path="/login" component={Login} />
					<Route exact path="/signup" component={SignUp} />
				</div>
			</div>
	);
};

export default AuthWrapper;
