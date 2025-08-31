# RPA-Task
This task utilizes Selenium & Python to automate registering, logging in, opening a bank account, requesting a loan, and creating a report for bank users.

The rpa-task-register.py is for the first part of the task
The rpa-task-loan-request is the first and second parts combined

The solution automates:
	•	Registering multiple customers from a CSV file.
	•	Handling cases where a username already exists.
	•	Logging in with existing credentials.
	•	Opening a new bank account (Checking or Savings).
	•	Requesting a loan with a calculated down payment.
	•	Exporting results into an Excel report.

Required Dependencies: selenium, pandas, openpyxl, webdriver-manager

Some challenges occurred during setup, such as some users skipping because of a misplaced continue statement, the script crashing when a user was already registered, some users remaining logged in while others were starting, and couldn't find some elements due to slow page load. All of these issues were resolved by the separation of registration and login logic, adding time.sleep and giving the page a second to load.

DOB, CVV, and Debit Cards columns are manually generated, since this information couldn't be found on the Parabank website
