# Employee_and_Payroll_Management_System
A Python-based Employee Management &amp; Payroll System that streamlines employee records and payroll processing. Features include CRUD operations, automated salary calculations, allowances and deductions, payroll history, input validation, JSON-based data storage, reporting, payment tracking, and CSV export.
A console-based **Employee Management and Payroll System** developed using Python. The application allows users to manage employee records, generate monthly payroll, calculate salary components, view reports, store data in JSON files, and export reports to CSV files.

---

## 📌 Project Overview

Managing employee information and payroll calculations manually can be time-consuming and error-prone. This project provides a simple and efficient console-based solution to manage employee details and monthly salary records.

The system supports employee management, payroll generation, salary calculations, report generation, data persistence, and CSV exports.

---

## ✨ Features

### 👨‍💼 Employee Management

* Add new employees
* View all employees
* Search employees by Employee ID
* Update employee information
* Remove employees
* Prevent duplicate Employee IDs

### 💰 Payroll Management

* Generate monthly payroll records
* Calculate salary components automatically
* View payroll history
* Search salary details by Employee ID
* Prevent duplicate payroll for the same employee and month
* Track payment status as `Paid` or `Pending`

### 📊 Reports

* Employee report
* Department-wise employee report
* Payroll report
* Payment status report
* Payroll summary with total salary calculations

### 📁 Data Storage and Export

* Store employee data in `employees.json`
* Store payroll data in `payroll.json`
* Export employee data to CSV
* Export payroll data to CSV
* Export department report to CSV
* Export payment status report to CSV

### ✅ Validation and Error Handling

* Employee ID validation
* Email validation
* Indian mobile number validation
* Salary validation
* Payroll month validation
* Payment status validation
* Duplicate record prevention
* Handling of missing or corrupted JSON files
* Handling invalid numeric input

---

## 🛠️ Technologies Used

* **Python**
* **JSON File Handling**
* **CSV File Handling**
* **Regular Expressions**
* **Exception Handling**
* **Lists and Dictionaries**
* **Functions**
* **Console-Based User Interface**

### Python Modules

```python
import json
import re
import csv
```

---

## 🧮 Salary Calculation Policy

The project uses a simple salary calculation policy for learning and demonstration purposes.

| Component           | Calculation                     |
| ------------------- | ------------------------------- |
| Basic Salary        | Entered by the user             |
| HRA                 | 20% of Basic Salary             |
| Transport Allowance | 10% of Basic Salary             |
| Total Allowances    | HRA + Transport Allowance       |
| Gross Salary        | Basic Salary + Total Allowances |
| Deduction           | 5% of Basic Salary              |
| Net Salary          | Gross Salary - Deduction        |

### Formula

```text
Total Allowances = HRA + Transport Allowance

Gross Salary = Basic Salary + Total Allowances

Net Salary = Gross Salary - Deduction
```

> **Note:** The salary policy is a simplified calculation model and is not intended to represent actual statutory payroll rules.

---

## 📂 Project Structure

```text
Employee_Payroll_System/
│
├── main.py
├── employees.json
├── payroll.json
├── employee_report.csv
├── payroll_report.csv
├── department_report.csv
└── payment_status_report.csv
```

### File Description

| File                        | Description                      |
| --------------------------- | -------------------------------- |
| `main.py`                   | Main Python application          |
| `employees.json`            | Stores employee records          |
| `payroll.json`              | Stores payroll records           |
| `employee_report.csv`       | Exported employee report         |
| `payroll_report.csv`        | Exported payroll report          |
| `department_report.csv`     | Department-wise employee count   |
| `payment_status_report.csv` | Paid and pending payroll details |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/employee-payroll-system.git
```

### 2. Navigate to the Project Directory

```bash
cd employee-payroll-system
```

### 3. Run the Application

```bash
python main.py
```

---

## 🖥️ Application Menu

```text
========== Main Menu ==========

--- Employee Management ---
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Remove Employee

--- Payroll Management ---
6. Generate Payroll
7. View Payroll History
8. Search Employee Salary
9. Payroll Summary

--- Reports ---
10. Employee Report
11. Department Report
12. Payroll Report
13. Payment Status Report

--- Export Reports ---
14. Export Employee Report to CSV
15. Export Payroll Report to CSV
16. Export Department Report to CSV
17. Export Payment Status Report to CSV

18. Exit
```

---

## 🧾 Employee Data Fields

Each employee record contains:

* Employee ID
* Employee Name
* Department
* Designation
* Email
* Mobile Number
* Basic Salary

### Employee ID Format

```text
EMP001
EMP002
EMP003
```

### Payroll Month Format

```text
YYYY-MM
```

Example:

```text
2026-09
```

---

## 💳 Payroll Data Fields

Each payroll record contains:

* Payroll ID
* Employee ID
* Employee Name
* Month
* Basic Salary
* HRA
* Transport Allowance
* Total Allowances
* Gross Salary
* Deduction
* Net Salary
* Payment Status

### Payroll ID Format

```text
PAY001
PAY002
PAY003
```

---

## 🔐 Validation Rules

The application follows these validation rules:

1. Employee ID must follow the format `EMP001`.
2. Employee IDs must be unique.
3. Email must follow a valid email format.
4. Mobile number must contain a valid 10-digit Indian mobile number.
5. Salary cannot be negative.
6. Salary must be numeric.
7. Payroll can be generated only for an existing employee.
8. Duplicate payroll cannot be generated for the same employee and month.
9. Payroll month must follow the `YYYY-MM` format.
10. Payment status must be either `Paid` or `Pending`.

---

## 🧪 Testing Performed

The following scenarios were tested successfully:

* Adding a valid employee
* Adding an employee with a duplicate ID
* Entering an invalid email
* Entering an invalid mobile number
* Entering a negative salary
* Searching for an existing employee
* Searching for a nonexistent employee
* Updating employee details
* Removing an employee
* Generating payroll for an existing employee
* Generating payroll for a nonexistent employee
* Preventing duplicate monthly payroll
* Verifying salary calculations
* Loading data from JSON files
* Exporting reports to CSV files
* Handling invalid input and file errors

---

## 📸 Sample Workflow

```text
Add Employee
     ↓
Employee Data Saved to employees.json
     ↓
Generate Monthly Payroll
     ↓
Payroll Data Saved to payroll.json
     ↓
View Reports
     ↓
Export Reports to CSV
```

---

## 🎯 Learning Outcomes

Through this project, the following concepts were implemented:

* Python functions
* Conditional statements
* Loops
* Lists and dictionaries
* Modular programming
* Input validation
* Regular expressions
* Exception handling
* JSON file handling
* CSV file handling
* Data processing
* Payroll calculations
* Report generation
* Basic software testing

---

## 🔮 Future Enhancements

Possible future improvements include:

* Object-Oriented Programming implementation
* SQLite or MySQL database integration
* User login and role-based access
* Graphical User Interface using Tkinter
* Web application using Flask or Django
* Payslip generation in PDF format
* Attendance and leave management
* Tax and statutory deduction support
* Automated email delivery of payslips
* Advanced dashboard and visual analytics
* Unit testing using `unittest` or `pytest`

---

## 👨‍💻 Author

**Your Name**

* GitHub: [your-github-Shiva-Teja-Arva](https://github.com/Shiva-Teja-Arva)
* LinkedIn: [your-linkedin-shiva-teja-arva](https://www.linkedin.com/in/shiva-teja-arva/)

---

## 📄 License

This project is created for educational and portfolio purposes. You are free to use, modify, and improve the project according to your requirements.
