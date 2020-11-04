# @Author: 夭夭
# @Time: 五月 28, 2020
from selenium import webdriver
#定义关键字

from selenium.webdriver.support.wait import WebDriverWait
from tool.openDriver import OpenDriver
import time
from tool.element import ELEMENT
# 在这里面用的字典
# loc指的是sheet里面的元素这一列的值
# {'登录链接': ('xpath', "//div[@class='member-login']/a[text()='登录']"),
# '用户名': ('name', 'accounts'),
# '密码': ('name', 'pwd'),
# '登录': ('xpath', "//button[text()='登录']"),
# None: (None, None)}
class KeyWord(object):
    def __init__(self):
        self.driver = OpenDriver().driver('chrome')
        self.driver.maximize_window()

    def base_find_element(self, name, timeout=30, poll=0.5):
        # name是名称，就是loc对应的名称
        # name 就是‘登录链接’  loc是定位方法和值的元组
        loc = ELEMENT.get(name)
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_click(self,name):
        self.base_find_element(name).click()

    # 等待操作
    def base_wait(self,s):
        time.sleep(s)
    # 输入
    def base_input(self,name,value):

        el = self.base_find_element(name)
        el.clear()
        el.send_keys(value)

    # 打开
    def base_open(self,url):
        self.driver.get(url)

    def base_get_text(self,name):
        return self.base_find_element(name).text

    def base_screenshot(self):
        self.driver.get_screenshot_as_file("../img/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 断言
    def base_assert_contain_string(self):
        result = self.driver.page_source
        return result

    def base_quit_driver(self):
        self.driver.quit()

    # 切换窗口
    def base_switch_window(self, title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                print(f'入参的title值是{title}')
                print(f'window切换成功，当前的title名字是{self.driver.title}')
                break


