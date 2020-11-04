# @Author: 夭夭
# @Time: 五月 28, 2020
from selenium import webdriver
#定义关键字

from selenium.webdriver.support.wait import WebDriverWait
from tool.openDriver import OpenDriver
import time
from tool.element import ELEMENT

# loc指的是sheet里面的元素这一列的值

class KeyWord(object):
    def __init__(self):
        self.driver = OpenDriver().driver('chrome')
        self.driver.maximize_window()

    def base_find_element(self, name, timeout=30, poll=0.5):
        # name是名称，就是loc对应的名称

        loc = ELEMENT.get(name)
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_click(self,name):
        self.base_find_element(name).click()


    def base_wait(self,s):
        time.sleep(s)

    def base_input(self,name,value):

        el = self.base_find_element(name)
        el.clear()
        el.send_keys(value)


    def base_open(self,url):
        self.driver.get(url)

    def base_get_text(self,name):
        return self.base_find_element(name).text

    def base_screenshot(self):
        self.driver.get_screenshot_as_file("../img/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    def base_assert_contain_string(self):
        result = self.driver.page_source
        return result

    def base_quit_driver(self):
        self.driver.quit()

    def base_switch_window(self, title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                print(f'入参的title值是{title}')
                print(f'window切换成功，当前的title名字是{self.driver.title}')
                break


