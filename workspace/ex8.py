from selenium import webdriver #pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.naver.com")
driver.implicitly_wait(0.5)
query_text="한국 시간"
search_box=driver.find_element(by=By.CSS_SELECTOR,value="#query")
search_box.send_keys(query_text)
search_button=driver.find_element(by=By.ID,value="search-btn")
search_button.click()
temp_div=driver.find_element(by=By.CSS_SELECTOR,value="#_worldtime_area > div.c_worldtime._worldtime_calc > div.left_city._left_citytimer > div.digital_timer._timer")
print(temp_div.text)
time.sleep(10)
#20315 배준우
