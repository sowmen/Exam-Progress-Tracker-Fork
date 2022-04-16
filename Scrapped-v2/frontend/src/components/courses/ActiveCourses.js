/** @format */

import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TablePagination from "@material-ui/core/TablePagination";
import TableRow from "@material-ui/core/TableRow";
import Modal from "@material-ui/core/Modal";
import Backdrop from "@material-ui/core/Backdrop";
import Fade from "@material-ui/core/Fade";
const columns = [
	{
		id: "deadline",
		label: "Due Date",
		minWidth: 30,
		align: "center",
	},
	{
		id: "course",
		label: "Course Name",
		minWidth: 100,
		align: "center",
	},
	{
		id: "details",
		label: "Submission Details",
		minWidth: 100,
		align: "center",
	},
];

function createData(deadline, course, details) {
	return { deadline, course, details };
}

const rows = [
	createData("Tomorrow", "CSE 210", "Attendance Marks"),
	createData("Tomorrow", "CSE 220", "Attendance Marks"),
	createData("Tomorrow", "CSE 230", "Attendance Marks"),
	createData("Tomorrow", "CSE 240", "Attendance Marks"),
	createData("Tomorrow", "CSE 250", "Attendance Marks"),
	createData("Tomorrow", "CSE 260", "Attendance Marks"),
	createData("Tomorrow", "CSE 270", "Attendance Marks"),
];

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
  },
  container: {
    maxHeight: 440,
  },
  modal: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  paper: {
    backgroundColor: theme.palette.background.paper,
    border: "2px solid #000",
    boxShadow: theme.shadows[5],
    padding: theme.spacing(2, 4, 3),
  },
}));

const ActiveCourses = () => {
	const classes = useStyles();
	const [page, setPage] = React.useState(0);
	const [rowsPerPage, setRowsPerPage] = React.useState(5);
	const [open, setOpen] = React.useState(false);
	const [row, setRow] = React.useState(rows[0]);
	var courseCode = "";
	var courseName = "";
	var properties = "";
	const handleChangePage = (event, newPage) => {
		setPage(newPage);
	};

	const handleChangeRowsPerPage = (event) => {
		setRowsPerPage(+event.target.value);
		setPage(0);
	};

	const handleOpen = (row) => {
		setRow(row);
      	setOpen(true);
    };

    const handleClose = () => {
      setOpen(false);
    };

	return (
    <>
      <Paper className={classes.root}>
        <TableContainer className={classes.container}>
          <Table stickyHeader aria-label="sticky table">
            <TableHead>
              <TableRow>
                {columns.map((column) => (
                  <TableCell
                    key={column.id}
                    align={column.align}
                    style={{ minWidth: column.minWidth }}
                  >
                    {column.label}
                  </TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {rows
                .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                .map((row) => {
                  return (
                    <TableRow
                      hover
                      role="checkbox"
                      tabIndex={-1}
                      key={row.code}
                    >
                      {columns.map((column) => {
                        const value = row[column.id];
                        return (
                          <TableCell
                            key={column.id}
                            align={column.align}
                            onClick={()=> handleOpen(row)}
                          >
                            {column.format && typeof value === "number"
                              ? column.format(value)
                              : value}
                          </TableCell>
                        );
                      })}
                    </TableRow>
                  );
                })}
            </TableBody>
          </Table>
        </TableContainer>
        <TablePagination
          rowsPerPageOptions={[5, 10, 20]}
          component="div"
          count={rows.length}
          rowsPerPage={rowsPerPage}
          page={page}
          onChangePage={handleChangePage}
          onChangeRowsPerPage={handleChangeRowsPerPage}
        />
      </Paper>
      <Modal
        aria-labelledby="transition-modal-title"
        aria-describedby="transition-modal-description"
        className={classes.modal}
        open={open}
        onClose={handleClose}
        closeAfterTransition
        BackdropComponent={Backdrop}
        BackdropProps={{
          timeout: 500,
		}}
      >
        <Fade in={open}>
          <div className={classes.paper}>
            <h2 id="transition-modal-title">{row.course}</h2>
            <h4 id="transition-modal-title">{courseName}</h4>
            <p id="transition-modal-description">
              {properties}
            </p>
          </div>
        </Fade>
      </Modal>
    </>
  );
};

export default ActiveCourses;
