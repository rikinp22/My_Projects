INSERT TABLE titles (
	"title_id" varchar(10),
	"title" varchar(50)
);

SELECT * FROM titles;

INSERT TABLE employees (
	"emp_no" int PRIMARY KEY,
	"emp_title_id" varchar(10),
	"birth_date" date,
	"first_name" varchar(50),
	"last_name" varchar(50),
	"sex" varchar(10),
	"hire_date" date,
	FOREIGN KEY (emp_title_id) REFERENCES titles (title_id) 
);

SELECT * FROM employees;

INSERT TABLE departments (
	"dept_no" varchar(10),
	"dept_name" varchar(50)
);

SELECT * FROM departments;

INSERT TABLE dept_emp (
	"emp_no" int PRIMARY KEY,
	"dept_no" varchar(10),
	FOREIGN KEY (dept_no) REFERENCES departments (dept_no)
);

SELECT * FROM dept_emp;

INSERT TABLE dept_manager (
	"dept_no" varchar(10),
	"emp_no" int PRIMARY KEY
);

SELECT * FROM dept_manager;

INSERT TABLE salaries (
	"emp_no" int PRIMARY KEY,
	"salary" int
);

SELECT * FROM salaries;