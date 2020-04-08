from selenium import webdriver
import unittest
import time
class LoginCase(unittest.TestCase):
    def login(self,email,password):
        '''定义登录方法'''
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.jjshouse.com/')
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('sign-in-label').click()
        time.sleep(3)
        self.driver.find_element_by_id('_email').clear()
        self.driver.find_element_by_id('_email').send_keys(email)
        time.sleep(2)
        self.driver.find_element_by_id('_password').clear()
        self.driver.find_element_by_id('_password').send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_class_name('sign-in-btn-td').click()
    def test_login_success(self):
        '''账号密码正确'''
        self.login('lpd@tetx.com','123456')
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:\\test\\login\\login_success.png")
        try:
            txt = self.driver.find_element_by_class_name('ga-my-account-link').get_attribute('textContent')
            print(txt)
            if txt == " lpd's Account":
                print("登录成功")
        except:
            print("登录失败")
        # self.driver.quit()
    def test_login_email_error(self):
        '''账号正确,密码错误'''
        self.login('lpd@tetx.com', '111111')
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:\\test\\login\\login_email_error.png")
        try:
            txt = self.driver.find_element_by_id('_msg').get_attribute('textContent')
            print(txt)
            if txt == 'The email address or password you entered is incorrect.':
                print('验证成功')
        except:
            print('验证失败')
        # self.driver.quit()
    def test_login_pwd_error(self):
        '''账号错误,密码正确'''
        self.login('lp@tetx.com', '123456')
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:\\test\\login\\login_pwd_error.png")
        try:
            txt = self.driver.find_element_by_id('_msg').get_attribute('textContent')
            print(txt)
            if txt == 'The email address or password you entered is incorrect.':
                print('验证成功')
        except:
            print('验证失败')
        # self.driver.quit()
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
    print("登录测试结束")























