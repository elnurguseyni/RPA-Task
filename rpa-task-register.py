from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

customers = pd.read_csv("ParaBank users.csv")

driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm")
driver.maximize_window()

for idx, row in customers.iterrows():
  driver.find_element(By.LINK_TEXT, "Register").click()

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

  try:
    error = driver.find_element(By.ID, "customer.username.errors").text
    if "This username already exists" in error:
      print(f"Username {row['Username']} already exists.")
      time.sleep(5)
      continue
  except:
    time.sleep(5)
    pass

  try:
    driver.find_element(By.LINK_TEXT, "Log Out").click()
  except:
    pass                      

  time.sleep(2)