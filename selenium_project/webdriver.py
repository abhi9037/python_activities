from selenium import webdriver
# from selenium.webdriver.common.keys import keys
import time

driver = webdriver.Chrome(executable_path = r"C:\Users\Abhijith\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.udemy.com/")
print(driver.current_url)
print(driver.title)

time.sleep(5)
driver.close()