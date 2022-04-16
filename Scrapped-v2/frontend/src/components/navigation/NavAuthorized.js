/** @format */

import React from "react";
import { Link } from "react-router-dom";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";

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

const NavAuthorized = () => {
	const classes = useStyles();

	return (
		<>
			<Button component={Link} to={"/"} color="inherit">
				Dashboard
			</Button>
			<Button component={Link} to={"/courses"} color="inherit">
				Courses
			</Button>
			<Button component={Link} to={"/committeeDashboard"} color="inherit">
				Committee Dashboard
			</Button>
			<Typography variant="h6" className={classes.title}>
				SUST Exam Progress Tracker
			</Typography>
			<Button component={Link} to={"/"} color="inherit">
				Profile
			</Button>
		</>
	);
};

export default NavAuthorized;
