from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.jjshouse.com/')
driver.maximize_window()
driver.find_element_by_class_name('sign-in-label').click()
time.sleep(3)
driver.find_element_by_class_name('signInBtn').click()
driver.find_element_by_id('email').clear()
driver.find_element_by_id('email').send_keys('tst5@tetx.com')
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('password_again').clear()
driver.find_element_by_id('password_again').send_keys('123456')
driver.find_element_by_class_name('signUpBtn').click()
time.sleep(5)
driver.get_screenshot_as_file("C:\\test\\register.png")
try:
    txt = driver.find_element_by_class_name('ga-my-account-link').get_attribute('textContent')
    print(txt)
    if txt == " tst5's Account":
        print("注册成功")
except:
    print("注册失败")
driver.quit()