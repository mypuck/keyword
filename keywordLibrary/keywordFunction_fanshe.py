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

    def base_find_element(self, el,timeout=30, poll=0.5):
        # name是名称，就是loc对应的名称

        loc = ELEMENT.get(el)
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_click(self, el, data):
        self.base_find_element(el).click()


    def base_wait(self,el,data):
        time.sleep(int(data))

    def base_input(self, el, data):

        el = self.base_find_element(el)
        el.clear()
        el.send_keys(data)


    def base_open(self, el, data):
        self.driver.get(data)

    def base_get_text(self,el,data):
        return self.base_find_element(el).text

    def base_screenshot(self,el,data):
        self.driver.get_screenshot_as_file("../img/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 断言如何封装呢？因为self.assertIn只能在unittest框架里面用
    def base_assert_contain_string(self, el, data):
        result = self.driver.page_source
        assert data in result

    def base_quit_driver(self):
        self.driver.quit()

    def base_switch_window(self, el, data):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == data:
                break


