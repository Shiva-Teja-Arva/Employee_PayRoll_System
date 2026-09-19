# Importing necessary libraries and modules
import re
import json
import csv

# -------------------------------GLOBAL DATA----------------------------------
# Store all employee records
employees = []
# Store all payroll records
payroll_records = []


# -------------------------------VALIDATION FUNCTIONS-------------------------------
# Function to validate employee ID, email, and mobile number using regex patterns
def validate_employee_id(employee_id):
    pattern = r"^EMP[0-9]{3,}$"
    return bool(re.fullmatch(pattern, employee_id))

# Function to validate email using regex pattern
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, email))

# Function to validate mobile number using regex pattern
def validate_mobile(mobile):
    pattern = r"^[6-9][0-9]{9}$"
    return bool(re.fullmatch(pattern, mobile))

# Function to validate month and year for payroll generation
def validate_month(month):
    pattern = r"^[0-9]{4}-(0[1-9]|1[0-2])$"
    return bool(re.fullmatch(pattern, month))

def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_valid_employee_id():
    while True:
        employee_id = input(
            "Enter Employee ID: "
        ).strip().upper()

        if validate_employee_id(employee_id):
            return employee_id

        print("Invalid Employee ID!")
        print("Example: EMP001")


def get_valid_email():
    while True:
        email = input("Enter Email: ").strip()

        if validate_email(email):
            return email

        print("Invalid email format!")
        print("Example: example@gmail.com")


def get_valid_mobile():
    while True:
        mobile = input(
            "Enter Mobile Number: "
        ).strip()

        if validate_mobile(mobile):
            return mobile

        print("Invalid mobile number!")
        print("Enter a valid 10-digit Indian mobile number.")


def get_non_negative_salary(message):
    while True:
        try:
            salary = float(input(message).strip())

            if salary < 0:
                print("Salary cannot be negative!")
                continue

            return round(salary, 2)

        except ValueError:
            print("Please enter a valid numeric salary!")


def get_valid_month():
    while True:
        month = input(
            "Enter Payroll Month (YYYY-MM): "
        ).strip()

        if validate_month(month):
            return month

        print("Invalid month format!")
        print("Example: 2026-09")


def get_payment_status():
    while True:
        status = input(
            "Enter Payment Status (Paid/Pending): "
        ).strip().capitalize()

        if status in ["Paid", "Pending"]:
            return status

        print("Invalid payment status!")
        print("Please enter either Paid or Pending.")

def format_currency(amount):
    return f"₹{amount:,.2f}" # we can also use unicode the print the rupee symbol in the console as \u20B9


# -------------------------------EMPLOYEE FILE HANDLING---------------------------------------

def save_employees():
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)


def load_employees():
    global employees

    try:
        with open("employees.json", "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                employees = data
            else:
                print("Invalid employee data format!")
                employees = []

    except FileNotFoundError:
        employees = []

    except json.JSONDecodeError:
        print("Employee data file is corrupted!")
        employees = []

    except OSError:
        print("Unable to read employee data file!")
        employees = []

#-------------------------------PAYROLL FILE HANDLING---------------------------------------

def save_payroll():
    with open("payroll.json", "w") as file:
        json.dump(payroll_records, file, indent=4)

def load_payroll():
    global payroll_records

    try:
        with open("payroll.json", "r") as file:
            data = json.load(file)

            if not isinstance(data, list):
                print("Invalid payroll data format!")
                payroll_records = []
                return

            valid_records = []

            for payroll in data:
                if isinstance(payroll, dict):
                    if is_valid_payroll_record(payroll):
                        valid_records.append(payroll)
                    else:
                        print(
                            "Skipped an invalid payroll record."
                        )
                else:
                    print(
                        "Skipped a malformed payroll record."
                    )

            payroll_records = valid_records

    except FileNotFoundError:
        payroll_records = []

    except json.JSONDecodeError:
        print("Payroll data file is corrupted!")
        payroll_records = []

    except OSError:
        print("Unable to read payroll data file!")
        payroll_records = []

# --------------------------------MENU DISPLAY--------------------------------
def display_menu():

    print("\n" + "=" * 62)
    print("|       EMPLOYEE MANAGEMENT & PAYROLL SYSTEM                 |")
    print("=" * 62)

    print(f"| {'No.':<5} | {'Operation':<50} |")
    print("-" * 62)

    print("| ---------------- Employee Management --------------------- |")

    print(f"| {'1':<5} | {'Add Employee':<50} |")
    print(f"| {'2':<5} | {'View Employees':<50} |")
    print(f"| {'3':<5} | {'Search Employee':<50} |")
    print(f"| {'4':<5} | {'Update Employee':<50} |")
    print(f"| {'5':<5} | {'Remove Employee':<50} |")
 
    print("| ---------------- Payroll Management ---------------------- |")

    print(f"| {'6':<5} | {'Generate Payroll':<50} |")
    print(f"| {'7':<5} | {'View Salary History':<50} |")
    print(f"| {'8':<5} | {'Search Employee Salary':<50} |")
    print(f"| {'9':<5} | {'Payroll Summary':<50} |")

    print("| ---------------------- Reports --------------------------- |")

    print(f"| {'10':<5} | {'Employee Report':<50} |")
    print(f"| {'11':<5} | {'Department Report':<50} |")
    print(f"| {'12':<5} | {'Payroll Report':<50} |")
    print(f"| {'13':<5} | {'Payment Status Report':<50} |")

    print("| --------------- Export Reports to CSV -------------------- |")

    print(f"| {'14':<5} | {'Export Employee Report':<50} |")
    print(f"| {'15':<5} | {'Export Payroll Report':<50} |")
    print(f"| {'16':<5} | {'Export Department Report':<50} |")
    print(f"| {'17':<5} | {'Export Payment Status Report':<50} |")

    print(f"| {'18':<5} | {'Exit':<50} |")

    print("=" * 62)


# -------------------------------EMPLOYEE MANAGEMENT FUNCTIONS-------------------------------
# -------------------------------ADD EMPLOYEE-------------------------------
# Function to add a new employee
# =========================================================
# ADD EMPLOYEE
# =========================================================

def add_employee():
    print("\n========== Add Employee ==========")

    employee_id = get_valid_employee_id()

    for employee in employees:
        if employee["employee_id"] == employee_id:
            print("Employee ID already exists!")
            return

    employee_name = get_non_empty_input(
        "Enter Employee Name: "
    )

    department = get_non_empty_input(
        "Enter Department: "
    )

    designation = get_non_empty_input(
        "Enter Designation: "
    )

    email = get_valid_email()

    mobile = get_valid_mobile()

    basic_salary = get_non_negative_salary(
        "Enter Basic Salary: "
    )

    employee = {
        "employee_id": employee_id,
        "employee_name": employee_name,
        "department": department,
        "designation": designation,
        "email": email,
        "mobile": mobile,
        "basic_salary": basic_salary
    }

    employees.append(employee)
    save_employees()

    print("\nEmployee added successfully!")

# --------------------------------ADDING REUSABLE EMPLOYEE LOOKUP---------------------------

def find_employee_by_id(employee_id):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            return employee

    return None

# -------------------------------VIEW EMPLOYEES-------------------------------
# Function to view all employees
def view_employees():
    print("\n" + "-" * 40)
    print("           ALL EMPLOYEES")
    print("-" * 40)

    if len(employees) == 0:
        print("No employees found!")
        return

    for employee in employees:
        display_employee(employee)

# -------------------------------SEARCH EMPLOYEE------------------------------------
# Function to search for an employee by ID
def search_employee():
    print("\n========== Search Employee ==========")

    employee_id = get_valid_employee_id()
    employee = find_employee_by_id(employee_id)

    if employee is None:
        print("Employee not found!")
        return

    display_employee(employee)

# -------------------------------DISPLAY EMPLOYEE DETAILS------------------------------------
# Common Function to display employee details for all operations
def display_employee(employee):
    print("\n" + "=" * 55)
    print("Employee Details".center(55))
    print("=" * 55)

    print(f"{'Employee ID':<20}: {employee['employee_id']}")
    print(f"{'Name':<20}: {employee['employee_name']}")
    print(f"{'Department':<20}: {employee['department']}")
    print(f"{'Designation':<20}: {employee['designation']}")
    print(f"{'Email':<20}: {employee['email']}")
    print(f"{'Mobile':<20}: {employee['mobile']}")
    print(
        f"{'Basic Salary':<20}: "
        f"{format_currency(employee['basic_salary'])}"
    )

    print("=" * 55)

# -------------------------------UPDATE EMPLOYEE------------------------------------
def update_employee():
    print("\n========== Update Employee ==========")

    employee_id = get_valid_employee_id()

    for employee in employees:
        if employee["employee_id"] == employee_id:
            print("\nExisting Employee Details:")
            display_employee(employee)

            employee_name = get_non_empty_input(
                "Enter New Name: "
            )

            department = get_non_empty_input(
                "Enter New Department: "
            )

            designation = get_non_empty_input(
                "Enter New Designation: "
            )

            email = get_valid_email()

            mobile = get_valid_mobile()

            basic_salary = get_non_negative_salary(
                "Enter New Basic Salary: "
            )

            employee["employee_name"] = employee_name
            employee["department"] = department
            employee["designation"] = designation
            employee["email"] = email
            employee["mobile"] = mobile
            employee["basic_salary"] = basic_salary

            save_employees()

            print("Employee updated successfully!")
            return

    print("Employee not found!")

# -------------------------------REMOVE EMPLOYEE------------------------------------
def remove_employee():
    print("\n========== Remove Employee ==========")

    employee_id = get_valid_employee_id()

    for employee in employees:
        if employee["employee_id"] == employee_id:
            display_employee(employee)

            while True:
                confirmation = input(
                    "Are you sure you want to remove this employee? "
                    "(yes/no): "
                ).strip().lower()

                if confirmation == "yes":
                    employees.remove(employee)
                    save_employees()

                    print("Employee removed successfully!")
                    return

                elif confirmation == "no":
                    print("Employee removal cancelled!")
                    return

                else:
                    print("Please enter only yes or no.")

    print("Employee not found!")

# -------------------------------PAYROLL MANAGEMENT FUNCTIONS-------------------------------
# -------------------------------DISPLAY PAYROLL DETAILS------------------------------------
def display_payroll(payroll):
    print("\n" + "=" * 60)
    print("Payroll Details".center(60))
    print("=" * 60)

    print(f"{'Payroll ID':<25}: {payroll['payroll_id']}")
    print(f"{'Employee ID':<25}: {payroll['employee_id']}")
    print(f"{'Employee Name':<25}: {payroll['employee_name']}")
    print(f"{'Month':<25}: {payroll['month']}")

    print(
        f"{'Basic Salary':<25}: "
        f"{format_currency(payroll['basic_salary'])}"
    )

    print(
        f"{'HRA':<25}: "
        f"{format_currency(payroll['hra'])}"
    )

    print(
        f"{'Transport Allowance':<25}: "
        f"{format_currency(payroll['transport_allowance'])}"
    )

    print(
        f"{'Total Allowances':<25}: "
        f"{format_currency(payroll['total_allowances'])}"
    )

    print(
        f"{'Gross Salary':<25}: "
        f"{format_currency(payroll['gross_salary'])}"
    )

    print(
        f"{'Deduction':<25}: "
        f"{format_currency(payroll['deduction'])}"
    )

    print(
        f"{'Net Salary':<25}: "
        f"{format_currency(payroll['net_salary'])}"
    )

    print(f"{'Payment Status':<25}: {payroll['payment_status']}")

    print("=" * 60)

# -------------------------------GENERATE PAYROLL ID-------------------------------

def generate_payroll_id():
    highest_number = 0

    for payroll in payroll_records:
        payroll_id = payroll.get("payroll_id", "")

        if payroll_id.startswith("PAY"):
            number_part = payroll_id[3:]

            if number_part.isdigit():
                number = int(number_part)

                if number > highest_number:
                    highest_number = number

    return f"PAY{highest_number + 1:03d}"

# -------------------------------VALIDATE PAYROLL RECORD------------------------------------

def is_valid_payroll_record(payroll):
    required_fields = [
        "payroll_id",
        "employee_id",
        "employee_name",
        "month",
        "basic_salary",
        "hra",
        "transport_allowance",
        "total_allowances",
        "gross_salary",
        "deduction",
        "net_salary",
        "payment_status"
    ]

    for field in required_fields:
        if field not in payroll:
            return False

    if not validate_employee_id(payroll["employee_id"]):
        return False

    if not validate_month(payroll["month"]):
        return False

    if payroll["payment_status"] not in ["Paid", "Pending"]:
        return False

    return True

# -------------------------------ADDING REUSABLE PAYROLL LOOKUP---------------------------

def find_payroll_by_id(payroll_id):
    for payroll in payroll_records:
        if payroll["payroll_id"] == payroll_id:
            return payroll

    return None

# -------------------------------CALCULATE SALARY------------------------------------

def calculate_salary(basic_salary):
    hra = round(basic_salary * 0.20, 2)

    transport_allowance = round(
        basic_salary * 0.10,
        2
    )

    total_allowances = round(
        hra + transport_allowance,
        2
    )

    gross_salary = round(
        basic_salary + total_allowances,
        2
    )

    deduction = round(
        basic_salary * 0.05,
        2
    )

    net_salary = round(
        gross_salary - deduction,
        2
    )

    return {
        "hra": hra,
        "transport_allowance": transport_allowance,
        "total_allowances": total_allowances,
        "gross_salary": gross_salary,
        "deduction": deduction,
        "net_salary": net_salary
    }

# -------------------------------CHECK DUPLICATE PAYROLL------------------------------------

def payroll_already_exists(employee_id, month):
    for payroll in payroll_records:
        if (
            payroll["employee_id"] == employee_id
            and payroll["month"] == month
        ):
            return True

    return False

# -------------------------------GENERATE PAYROLL------------------------------------

def generate_payroll():
    print("\n========== Generate Payroll ==========")

    employee_id = get_valid_employee_id()

    employee = find_employee_by_id(employee_id)

    if employee is None:
        print("Employee not found!")
        return

    month = get_valid_month()

    if payroll_already_exists(employee_id, month):
        print("Payroll already exists for this employee and month!")
        return

    try:
        basic_salary = round(
            float(employee["basic_salary"]),
            2
        )

        salary_details = calculate_salary(basic_salary)

        hra = salary_details["hra"]
        transport_allowance = salary_details["transport_allowance"]
        total_allowances = salary_details["total_allowances"]
        gross_salary = salary_details["gross_salary"]
        deduction = salary_details["deduction"]
        net_salary = salary_details["net_salary"]

    except (ValueError, TypeError):
        print("Invalid salary data found for this employee!")
        return

    payment_status = get_payment_status()

    payroll = {
        "payroll_id": generate_payroll_id(),
        "employee_id": employee_id,
        "employee_name": employee["employee_name"],
        "month": month,
        "basic_salary": basic_salary,
        "hra": hra,
        "transport_allowance": transport_allowance,
        "total_allowances": total_allowances,
        "gross_salary": gross_salary,
        "deduction": deduction,
        "net_salary": net_salary,
        "payment_status": payment_status
    }

    payroll_records.append(payroll)
    save_payroll()

    print("\nPayroll generated successfully!")
    display_payroll(payroll)

    
# -------------------------------VIEW PAYROLL HISTORY------------------------------------

def view_payroll_history():
    print("\n========== Payroll History ==========")

    if not payroll_records:
        print("No payroll records found!")
        return

    for payroll in payroll_records:
        display_payroll(payroll)

# -------------------------------SEARCH EMPLOYEE SALARY------------------------------------

def search_employee_salary():
    print("\n========== Search Employee Salary ==========")

    employee_id = get_valid_employee_id()

    if not validate_employee_id(employee_id):
        print("Invalid Employee ID!")
        return

    employee_exists = False

    for employee in employees:
        if employee["employee_id"] == employee_id:
            employee_exists = True
            break

    if not employee_exists:
        print("Employee not found!")
        return

    found_records = []

    for payroll in payroll_records:
        if payroll["employee_id"] == employee_id:
            found_records.append(payroll)

    if not found_records:
        print("No salary records found for this employee!")
        return

    print("\nSalary History for Employee:", employee_id)
    print("=" * 50)

    for payroll in found_records:
        display_payroll(payroll)

# -------------------------------PAYROLL SUMMARY------------------------------------

def payroll_summary():
    print("\n========== Payroll Summary ==========")

    if not payroll_records:
        print("No payroll records found!")
        return

    total_basic_salary = 0
    total_allowances = 0
    total_gross_salary = 0
    total_deductions = 0
    total_net_salary = 0

    paid_count = 0
    pending_count = 0

    for payroll in payroll_records:
        total_basic_salary += payroll["basic_salary"]
        total_allowances += payroll["total_allowances"]
        total_gross_salary += payroll["gross_salary"]
        total_deductions += payroll["deduction"]
        total_net_salary += payroll["net_salary"]

        if payroll["payment_status"] == "Paid":
            paid_count += 1

        elif payroll["payment_status"] == "Pending":
            pending_count += 1

    print("\nTotal Payroll Records :", len(payroll_records))
    print("-" * 45)

    print("Total Basic Salary    :", round(total_basic_salary, 2))
    print("Total Allowances      :", round(total_allowances, 2))
    print("Total Gross Salary    :", round(total_gross_salary, 2))
    print("Total Deductions      :", round(total_deductions, 2))
    print("Total Net Salary      :", round(total_net_salary, 2))

    print("-" * 45)

    print("Paid Payrolls         :", paid_count)
    print("Pending Payrolls      :", pending_count)

    print("-" * 45)

# -------------------------------EMPLOYEE REPORT----------------------------------

def employee_report():
    print("\n========== Employee Report ==========")

    if not employees:
        print("No employee records found!")
        return

    print("Total Employees:", len(employees))
    print("-" * 60)

    for employee in employees:
        print("Employee ID  :", employee["employee_id"])
        print("Name         :", employee["employee_name"])
        print("Department   :", employee["department"])
        print("Designation  :", employee["designation"])
        print("Basic Salary :", employee["basic_salary"])
        print("-" * 60)

# -------------------------------DEPARTMENT-WISE EMPLOYEE REPORT----------------------------------

def department_report():
    print("\n========== Department Report ==========")

    if not employees:
        print("No employee records found!")
        return

    department_counts = {}

    for employee in employees:
        department = employee["department"]

        if department not in department_counts:
            department_counts[department] = 0

        department_counts[department] += 1

    print("\nEmployees by Department:")
    print("-" * 40)

    for department, count in department_counts.items():
        print(f"{department:<25} : {count}")

# -------------------------------PAYROLL REPORT----------------------------------

def payroll_report():
    print("\n========== Payroll Report ==========")

    if not payroll_records:
        print("No payroll records found!")
        return

    print("Total Payroll Records:", len(payroll_records))
    print("-" * 70)

    for payroll in payroll_records:
        print("Payroll ID     :", payroll["payroll_id"])
        print("Employee ID    :", payroll["employee_id"])
        print("Employee Name  :", payroll["employee_name"])
        print("Month          :", payroll["month"])
        print("Gross Salary   :", payroll["gross_salary"])
        print("Net Salary     :", payroll["net_salary"])
        print("Payment Status :", payroll["payment_status"])
        print("-" * 70)

# -------------------------------PAYMENT STATUS REPORT----------------------------------

def payment_status_report():
    print("\n========== Payment Status Report ==========")

    if not payroll_records:
        print("No payroll records found!")
        return

    paid_records = []
    pending_records = []

    for payroll in payroll_records:
        if payroll["payment_status"] == "Paid":
            paid_records.append(payroll)

        elif payroll["payment_status"] == "Pending":
            pending_records.append(payroll)

    print("\nPaid Payrolls:", len(paid_records))
    print("-" * 50)

    for payroll in paid_records:
        print(
            payroll["payroll_id"],
            "|",
            payroll["employee_id"],
            "|",
            payroll["month"],
            "| Net:",
            payroll["net_salary"]
        )

    print("\nPending Payrolls:", len(pending_records))
    print("-" * 50)

    for payroll in pending_records:
        print(
            payroll["payroll_id"],
            "|",
            payroll["employee_id"],
            "|",
            payroll["month"],
            "| Net:",
            payroll["net_salary"]
        )

# -------------------------------EXPORT EMPLOYEE REPORT TO CSV------------------------------------

def export_employees_to_csv():
    print("\n========== Export Employee Report ==========")

    if not employees:
        print("No employee records available to export!")
        return

    try:
        with open("employee_report.csv", "w", newline="") as file:
            fieldnames = [
                "employee_id",
                "employee_name",
                "department",
                "designation",
                "email",
                "mobile",
                "basic_salary"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(employees)

        print("Employee report exported successfully!")
        print("File created: employee_report.csv")

    except OSError:
        print("Error while exporting employee report!")

# --------------------------------EXPORT PAYROLL REPORT TO CSV------------------------------------

def export_payroll_to_csv():
    print("\n========== Export Payroll Report ==========")

    if not payroll_records:
        print("No payroll records available to export!")
        return

    try:
        with open("payroll_report.csv", "w", newline="") as file:
            fieldnames = [
                "payroll_id",
                "employee_id",
                "employee_name",
                "month",
                "basic_salary",
                "hra",
                "transport_allowance",
                "total_allowances",
                "gross_salary",
                "deduction",
                "net_salary",
                "payment_status"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
                extrasaction="ignore"
            )

            writer.writeheader()
            writer.writerows(payroll_records)

        print("Payroll report exported successfully!")
        print("File created: payroll_report.csv")

    except OSError:
        print("Error while exporting payroll report!")

# -------------------------------EXPORT DEPARTMENT REPORT TO CSV------------------------------------

def export_department_report_to_csv():
    print("\n========== Export Department Report ==========")

    if not employees:
        print("No employee records available to export!")
        return

    department_counts = {}

    for employee in employees:
        department = employee["department"]

        if department not in department_counts:
            department_counts[department] = 0

        department_counts[department] += 1

    try:
        with open("department_report.csv", "w", newline="") as file:
            fieldnames = [
                "department",
                "employee_count"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for department, count in department_counts.items():
                writer.writerow({
                    "department": department,
                    "employee_count": count
                })

        print("Department report exported successfully!")
        print("File created: department_report.csv")

    except OSError:
        print("Error while exporting department report!")

# -------------------------------EXPORT PAYMENT STATUS REPORT TO CSV------------------------------------

def export_payment_status_report_to_csv():
    print("\n========== Export Payment Status Report ==========")

    if not payroll_records:
        print("No payroll records available to export!")
        return

    try:
        with open("payment_status_report.csv", "w", newline="") as file:
            fieldnames = [
                "payroll_id",
                "employee_id",
                "employee_name",
                "month",
                "net_salary",
                "payment_status"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
                extrasaction="ignore"
            )

            writer.writeheader()

            for payroll in payroll_records:
                writer.writerow({
                    "payroll_id": payroll["payroll_id"],
                    "employee_id": payroll["employee_id"],
                    "employee_name": payroll["employee_name"],
                    "month": payroll["month"],
                    "net_salary": payroll["net_salary"],
                    "payment_status": payroll["payment_status"]
                })

        print("Payment status report exported successfully!")
        print("File created: payment_status_report.csv")

    except OSError:
        print("Error while exporting payment status report!")


# -------------------------------MAIN FUNCTION------------------------------------

"""
Employee Management and Payroll System

A console-based Python application for managing employee records,
generating monthly payroll, calculating salaries, storing data in JSON
files, and exporting reports to CSV files.

Technologies:
- Python
- JSON
- CSV
- Regular Expressions
- File Handling
"""

def main():
    load_employees()  # Load existing employee data from file
    load_payroll()  # Load existing payroll data from file

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_employee()

            elif choice == 2:
                view_employees()

            elif choice == 3:
                search_employee()

            elif choice == 4:
                update_employee()

            elif choice == 5:
                remove_employee()

            elif choice == 6:
                generate_payroll()

            elif choice == 7:
                view_payroll_history()

            elif choice == 8:
                search_employee_salary()

            elif choice == 9:
                payroll_summary()

            elif choice == 10:
                employee_report()

            elif choice == 11:
                department_report()

            elif choice == 12:
                payroll_report()

            elif choice == 13:
                payment_status_report()

            elif choice == 14:
                export_employees_to_csv()

            elif choice == 15:
                export_payroll_to_csv()

            elif choice == 16:
                export_department_report_to_csv()

            elif choice == 17:
                export_payment_status_report_to_csv()

            elif choice == 18:
                print("Thank you for using the Employee Payroll System!")
                break

            else:
                print("Invalid choice! Please select 1 to 18.")

        except ValueError:
            print("Please enter a valid numeric choice.")


if __name__ == "__main__":
    main()