import React from 'react'
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TablePagination from "@material-ui/core/TablePagination";
import TableRow from "@material-ui/core/TableRow";

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
		minWidth: 30,
		align: "center",
	},
];

function createData(deadline, course ) {
	return { deadline, course };
}

const rows = [
	createData("Tomorrow", "CSE 210"),
	createData("Tomorrow", "CSE 210"),
	createData("Tomorrow", "CSE 210"),
	createData("Tomorrow", "CSE 210"),
	createData("Tomorrow", "CSE 210"),
	createData("Tomorrow", "CSE 210"),
	createData("Tomorrow", "CSE 210"),
	createData("Tomorrow", "CSE 210"),
	createData("Tomorrow", "CSE 210"),
	createData("Tomorrow", "CSE 210"),
];

const useStyles = makeStyles({
	root: {
		width: "65%",
	},
	container: {
		maxHeight: 440,
	},
});

const ActiveCoursesCD = () => {
	const classes = useStyles();
	const [page, setPage] = React.useState(0);
	const [rowsPerPage, setRowsPerPage] = React.useState(5);

	const handleChangePage = (event, newPage) => {
		setPage(newPage);
	};

	const handleChangeRowsPerPage = (event) => {
		setRowsPerPage(+event.target.value);
		setPage(0);
	};
	return (
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
							.slice(
								page * rowsPerPage,
								page * rowsPerPage + rowsPerPage
							)
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
												>
													{column.format &&
													typeof value === "number"
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
	);
};

export default ActiveCoursesCD
