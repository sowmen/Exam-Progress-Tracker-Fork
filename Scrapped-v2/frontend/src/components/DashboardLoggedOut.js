import React from 'react'

import Login from './Login';

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

const DashboardLoggedOut = () => {
    const classes = useStyles();
    return (
        <>

			<div className="auth-wrapper">
                <div className="auth-inner">
                    <Login />
                </div>
            </div>
        </>
    );
}

export default DashboardLoggedOut
