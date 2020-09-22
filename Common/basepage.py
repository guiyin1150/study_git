"""
 1）日志？失败截图？
      什么样子的日志：记录用例的执行过程。
      失败截图：用例失败了，在失败的操作截取当前的页面。

      用例当中每一个步骤 === 调页面对象的行为 + 测试数据
                                ||
                              页面对象
                                ||
                        selenium webdriver API
                             日志/失败截图
                                ||
                            1、等待可见
                            2、查找元素
                            3、点击 - 必然的前提：等待和查找
                            4、输入 - 必然的前提：等待和查找
                            5、获取属性 - 必然的前提：等待和查找
                            6、获取文本 - 必然的前提：等待和查找
"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class Basepage:

    def __init__(self, driver: WebDriver):
        # 初始化driver
        self.driver = driver

    # 1、等待可见
    def wait_ele_visible(self,loc,img_name,timeout=20,poll_fre=0.5):
        """
        :param loc:
        :param img_name:
        :param timeout:
        :param poll_fre:
        :return:
        等待开始的时候，记录一下当前时间。等待结束的时候，记录一下当前时间。时间差就是等待时长。
        """
        logging.info("{} 等待 {} 元素可见。".format(img_name,loc))
        # 等待开始的时候，记录一下当前时间
        try:
            WebDriverWait(self.driver, timeout,poll_frequency=poll_fre).until(EC.visibility_of_element_located(loc))
        except:
            # 失败截图 - 写入日志
            self.save_page_shot(img_name)
            logging.exception("等待元素可见失败：")
            raise
        else:
            # 等待结束的时候，记录一下当前时间。
            pass

    # 2、查找元素
    def get_element(self):
        pass

    def click_element(self):
        pass

    def input_text(self):
        pass

    def get_ele_attribute(self):
        pass

    def get_ele_text(self):
        pass

    def save_page_shot(self,img_name):
        """
        :param img_name: {页面名称_页面行为}
        :return:
        """
        # 将图片存储到Outputs的screenshots下。唯一不同的是，图片命名
        # 命名规范：{页面名称_页面行为}_时间.png
        # 文件完整名称 = Outputs的screenshots + {页面名称_页面行为}_时间.png
        file_name = "{}_{}.png".format(img_name,"当前时间")
        self.driver.save_screenshot("图片存储图片" + file_name)
        logging.info("页面图片保存在：{}".format("图片存储图片" + file_name))


if __name__ == '__main__':
    pass