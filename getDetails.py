#A program that automatically gets the upcoming class and the number of assigned projects remaining.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

email = input("Enter Email: ")
pwd = input("Enter Password: ")

options = Options()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(executable_path="C://ProgramData/chromedriver.exe", options=options)
driver.get("https://code.whitehatjr.com/s/login")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'LOGIN WITH PASSWORD')]")))
driver.find_element_by_xpath("//*[contains(text(), 'LOGIN WITH PASSWORD')]").click()

driver.find_element_by_id("emailOrMobile").send_keys(email)
driver.find_element_by_id("password").send_keys(pwd)
driver.find_element_by_xpath("//*[text()='Login']").click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'eQGIGU')))
next_class = driver.find_elements_by_class_name("eQGIGU")[0].text

driver.get("https://code.whitehatjr.com/s/my-projects/listing")

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'col-md-6')))

print("\nUpcoming Class: " + next_class)
print("Projects Assigned: " + str(len(driver.find_elements_by_class_name("col-md-6"))))

driver.quit()
input("\nPress ENTER to exit.")

