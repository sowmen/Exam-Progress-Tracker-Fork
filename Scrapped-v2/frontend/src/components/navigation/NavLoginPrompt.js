/** @format */

import React from "react";
import { Link } from "react-router-dom";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
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

const NavLoginPrompt = () => {
	const classes = useStyles();

	return (
		<>
			<Typography variant="h6" className={classes.title}>
				SUST Exam Progress Tracker
			</Typography>
			<Button component={Link} to={"/login"} color="inherit">
				Login
			</Button>
			<Button component={Link} to={"/signup"} color="inherit">
				Signup
			</Button>
		</>
	);
};

export default NavLoginPrompt;
