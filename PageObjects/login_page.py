# from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PO.PageLocators.login_page_locs import LoginPageLocs as loc

class LoginPage:


    def __init__(self,driver:WebDriver):
        # 初始化driver
        self.driver = driver
        # self.driver = webdriver.Chrome() # 打开了一个浏览器，开始了一个新会话

    # 登陆  - 元素操作 - 不知道用例在什么情况下会调用我？？
    def login(self,username,passwd):
        # 等待？？

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.login_button))
        self.driver.find_element(*loc.user_input).send_keys(username)
        self.driver.find_element(*loc.passwd_input).send_keys(passwd)
        self.driver.find_element(*loc.login_button).click()


    # 获取登陆区域的提示信息
    def get_msg_from_login_form(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.msg_from_login_form))
        eles =  self.driver.find_elements(*loc.msg_from_login_form)
        if len(eles) == 1:
            return eles[0].text
        elif len(eles) > 1:
            text_list = []
            for el in eles:
                text_list.append(el.text)
            return text_list

