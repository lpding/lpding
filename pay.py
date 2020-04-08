from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.jjshouse.com/-g4044')
driver.maximize_window()
driver.find_element_by_class_name('order-status-icon')    #判断页面是否存在订单状态查询按钮
print('please login in first!')
'''rose账号登录'''
driver.find_element_by_class_name('sign-in-label').click()
time.sleep(3)
driver.find_element_by_id('_email').send_keys("rose_te@tetx.com")
driver.find_element_by_id('_password').send_keys('leqee.com')
driver.find_element_by_class_name('sign-in-btn-td').click()
time.sleep(5)
driver.find_element_by_id('_add_to_cart').click()
time.sleep(5)
driver.find_element_by_class_name('cart_car').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="shopping-cart-float-right"]/a').click()
time.sleep(3)
driver.find_element_by_id('coupon_code').clear()
driver.find_element_by_id('coupon_code').send_keys('DevTestRose')
time.sleep(3)
driver.find_element_by_id('apply_btn').click()
grand_total = driver.find_element_by_xpath('//*[@id="span_order_amount"]').get_attribute('textContent')
print(grand_total)
if float(grand_total) <= 0.01:
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(3)
    '''信用卡支付'''
    driver.find_element_by_id('payment-radio-157').click()
    driver.find_element_by_id('creditCardNumber').send_keys('4392260032028506')
    driver.find_element_by_id('EXPIRYDATE_MM').click()
    driver.find_element_by_xpath('// *[ @ id = "EXPIRYDATE_MM"] / option[3]').click()
    driver.find_element_by_id('EXPIRYDATE_YY').click()
    driver.find_element_by_xpath('//*[@id="EXPIRYDATE_YY"]/option[3]').click()
    driver.find_element_by_id('CVV').send_keys('511')
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    driver.find_element_by_id('btn_sbmt_order').click()
    time.sleep(3)
    driver.get_screenshot_as_file("C:\\test\\pay\\creditcard.png")
    driver.quit()
else:
    print('超出金额')
    driver.quit()









