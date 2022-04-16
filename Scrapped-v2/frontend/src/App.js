/** @format */

import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { makeStyles } from "@material-ui/core/styles";
import Navigation from "./components/navigation/Navigation";

import AuthWrapper from "./components/AuthWrapper";
import Dashboard from "./components/Dashboard";
import Courses from "./components/Courses";
import CommitteeDashboard from "./components/CommitteeDashboard";

const useStyles = makeStyles((theme) => ({
	root: {
		flexGrow: 1,
	},
	menuButton: {
		marginRight: theme.spacing(2),
	},
	title: {
		flexGrow: 1,
	},
}));

function App() {
	const isAuthorized = true;

	return (
		<Router>
			<div className="App">
				<Navigation classes={useStyles} isAuthorized={isAuthorized} />
				<Switch>
					<Route
						exact path="/"
						render={(props) =>
						(<
							Dashboard{...props} isAuthorized={isAuthorized} />
						)
						}
					/>
					<Route exact path="/courses" component={Courses} />
					<Route exact path="/committeeDashboard" component={CommitteeDashboard}/>
					<AuthWrapper />
				</Switch>
			</div>
		</Router>
	);
}

export default App;
