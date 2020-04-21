from selenium import webdriver
from selenium.webdriver.common import keys
import time

driver = webdriver.Chrome(executable_path = r"C:\Users\Abhijith\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.flipkart.com/?gclid=Cj0KCQjw3qzzBRDnARIsAECmryo9YfCxSwSS3rA-nlPwHHa0U-v-VLcPoDepstabzfY9riNG0l2UlkkaAvc3EALw_wcB&ef_id=Cj0KCQjw3qzzBRDnARIsAECmryo9YfCxSwSS3rA-nlPwHHa0U-v-VLcPoDepstabzfY9riNG0l2UlkkaAvc3EALw_wcB:G:s&s_kwcid=AL!739!3!326505318642!e!!g!!flipkart&semcmpid=sem_8024046704_brand_eta_goog")
use = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
driver.implicitly_wait(10)
if use.is_enabled():
    use.send_keys("9037950074")
pas = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
if pas.is_enabled():
    pas.send_keys("Sarayu1994@")
login = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button/span")
if login.is_enabled():
    login.click()
cart = driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[5]/div/div/a/span")
