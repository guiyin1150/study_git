from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PO.PageLocators.bid_page_locs import BidPageLocs as locs

class BidPage:

    def __init__(self, driver: WebDriver):
        # 初始化driver
        self.driver = driver

    # 11、标页面 - 获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locs.money_input))
        return self.driver.find_element(*locs.money_input).get_attribute("data-amount")

    # 111、标页面 - 获取标的余额
    def get_bid_money(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locs.bid_money_text))
        return self.driver.find_element(*locs.bid_money_text).text

    # 2、标页面 - 输入金额2000，点投标
    def invest(self,invest_money):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locs.money_input))
        self.driver.find_element(*locs.money_input).send_keys(invest_money)
        self.driver.find_element(*locs.invest_button).click()

    # 3、标页面 - 在投标成功的弹出框里，点击查看并激活按钮
    def click_active_button_in_success_popup(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locs.active_button_on_successPop))
        self.driver.find_element(*locs.active_button_on_successPop).click()