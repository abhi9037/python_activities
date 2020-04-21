from selenium import webdriver
from selenium.webdriver.common import keys
import time

driver = webdriver.Chrome(executable_path = r"C:\Users\Abhijith\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.flipkart.com/?gclid=Cj0KCQjw3qzzBRDnARIsAECmryo9YfCxSwSS3rA-nlPwHHa0U-v-VLcPoDepstabzfY9riNG0l2UlkkaAvc3EALw_wcB&ef_id=Cj0KCQjw3qzzBRDnARIsAECmryo9YfCxSwSS3rA-nlPwHHa0U-v-VLcPoDepstabzfY9riNG0l2UlkkaAvc3EALw_wcB:G:s&s_kwcid=AL!739!3!326505318642!e!!g!!flipkart&semcmpid=sem_8024046704_brand_eta_goog")

driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

time.sleep(5)
driver.close()