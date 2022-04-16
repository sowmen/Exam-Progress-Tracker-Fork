/** @format */

import React from "react";
import ActiveCourses from "./courses/ActiveCourses";
import PastCourses from "./courses/PastCourses";

const Courses = () => {
	return (
		<>
			<div className="container">
			<p> Active Courses</p>
			<ActiveCourses />
			</div>
			<div className="container">
			<p> Past Courses</p>
			<PastCourses />
			</div>
		</>
	);
};

export default Courses;
