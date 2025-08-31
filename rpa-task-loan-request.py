from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time


customers = pd.read_csv("ParaBank users.csv")

driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm")
driver.maximize_window()

results = []

for idx, row in customers.iterrows():

      driver.find_element(By.LINK_TEXT, "Register").click()
      time.sleep(1)
      driver.find_element(By.ID, "customer.firstName").send_keys(str(row["First Name"]))
      driver.find_element(By.ID, "customer.lastName").send_keys(str(row["Last Name"]))
      driver.find_element(By.ID, "customer.address.street").send_keys(str(row["Address"]))
      driver.find_element(By.ID, "customer.address.city").send_keys(str(row["City"]))
      driver.find_element(By.ID, "customer.address.state").send_keys(str(row["State"]))
      driver.find_element(By.ID, "customer.address.zipCode").send_keys(str(row["Zip Code"]))
      driver.find_element(By.ID, "customer.phoneNumber").send_keys(str(row["Phone Number"]))
      driver.find_element(By.ID, "customer.ssn").send_keys(str(row["SSN"]))
      driver.find_element(By.ID, "customer.username").send_keys(str(row["Username"]))
      driver.find_element(By.ID, "customer.password").send_keys(str(row["Password"]))
      driver.find_element(By.ID, "repeatedPassword").send_keys(str(row["Password"]))

      driver.find_element(By.XPATH, "//input[@value='Register']").click()
      time.sleep(2)


      try:
          error_msg = driver.find_element(By.ID, "customer.username.errors")
          if "This username already exists" in error_msg.text:
            print(f" Username {row['Username']} already exists")
            driver.get("https://parabank.parasoft.com/parabank/index.htm")
      except:
          driver.find_element(By.LINK_TEXT, "Log Out").click()
    
      driver.find_element(By.XPATH, "//input[@name='username']").send_keys(str(row["Username"]))
      driver.find_element(By.XPATH, "//input[@name='password']").send_keys(str(row["Password"]))
      driver.find_element(By.XPATH, "//input[@value='Log In']").click()
      time.sleep(2)

      driver.find_element(By.LINK_TEXT, "Open New Account").click()
      time.sleep(1)

      acc_dropdown = Select(driver.find_element(By.ID, "type"))
      acc_type =str(row["Account Type"]).strip().upper()
      if acc_type in ["CHECKING", "SAVINGS"]:
         acc_dropdown.select_by_visible_text(acc_type)
      else:
         acc_dropdown.select_by_visible_text("CHECKING")

      driver.find_element(By.XPATH, "//input[@value='Open New Account']").click()
      time.sleep(2)

      new_acc_number = driver.find_element(By.ID, "newAccountId").text

      driver.find_element(By.LINK_TEXT, "Request Loan").click()
      time.sleep(1)

      driver.find_element(By.ID, "amount").send_keys("10000")
      initial_deposit = row.get("Initial Deposit", 0)
      try:
          initial_deposit = float(initial_deposit)
      except (ValueError, TypeError):
          initial_deposit = 0

      down_payment = initial_deposit * 0.2 if initial_deposit > 0 else 0
      driver.find_element(By.ID, "downPayment").send_keys(str(down_payment))
      from_acc_dropdown = Select(driver.find_element(By.ID, "fromAccountId"))
      from_acc_dropdown.select_by_visible_text(new_acc_number)

      driver.find_element(By.XPATH, "//input[@value='Apply Now']").click()
      time.sleep(2)

      loan_status = driver.find_element(By.ID, "loanStatus").text

      dob = "01/01/1990"
      debit_card = "4000123412341234"
      cvv = "123"

      results.append({
         "First Name": row["First Name"],
         "Last Name": row["Last Name"],
         "DOB": dob,
         "Debit Card": debit_card,
         "CVV": cvv,
         "Username": row["Username"],
         "Account Type": acc_type,
         "New Account Number": new_acc_number,
         "Initial Deposit": row["Initial Deposit"],
         "Loan Requested (USD)": 10000,
         "Down Payment (USD)": 2000,
         "Loan Status": loan_status,
         "Loan in EUR": round(10000*0.82, 2)

      })

      try:
        driver.find_element(By.LINK_TEXT, "Log Out").click()
        time.sleep(2)
      except:
        pass    

      df = pd.DataFrame(results)
      df.to_excel("Parabank_Report.xlsx", index=False)



driver.quit()
