from selenium import webdriver

driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")
newregistrantbtn = driver.find_element_by_xpath("//a[contains(text(),'Continue')]")
newregistrantbtn.click()
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Evgenia")

#lastname field
lastname_field = driver.find_element_by_xpath("//fieldset/div[2]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Vorobeva")

#email field
email_field = driver.find_element_by_xpath("//fieldset/div[2]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class

email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("ev@gmail.com")

#password field
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("ev1234")

#telephone field
telephone_field = driver.find_element_by_xpath("//fieldset/div[2]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("123-456")

#fax field
fax_input = driver.find_element_by_id("input-fax")
fax_input.clear()
fax_input.send_keys(412-458)

#company field
company_input = driver.find_element_by_id("input-company")
company_input.clear()
company_input.send_keys("Book store")

#address 1
address1_field = driver.find_element_by_xpath("//fieldset/div[2]")
address1_field_class = address1_field.get_attribute("class")
assert "required" in address1_field_class

address1_input = driver.find_element_by_id("input-address1")
address1_input.clear()
address1_input.send_keys("123 Main st")

#address 2
address2_input = driver.find_element_by_id("input-address2")
address2_input.clear()
address2_input.send_keys("345 Emmy Str")
