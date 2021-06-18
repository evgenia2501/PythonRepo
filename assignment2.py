from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= 'drivers/chromedriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
#continue_btn = driver.find_element_by_xpath("//body/div[2]")



wd_wait = WebDriverWait(driver,10)
continue_btn = wd_wait.until(EC.element_to_be_clickable((By.XPATH,"//body/div[2]")))
continue_btn.click()



