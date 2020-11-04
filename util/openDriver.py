# -*- coding:utf8 -*-
from selenium import webdriver
from util import config
from selenium.webdriver.chrome.options import Options
from util.logger import Logger
logger = Logger().getlog()


class OpenDriver(object):

    def __init__(self):
        self.config = config.Config()

    def driver(self):
        data = self.config.get_value("driver.conf", "driver", "driver")
        # mobile_emulation = eval(self.config.get_value("data.conf", "driver", "mobile_emulation"))
        chrome_options = Options()
        # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        browser = str(data)
        logger.info("You had select %s browser." % browser)
        # 主要是获取不同浏览器实例化的driver
        webdriver = self.get_driver(browser)
        return webdriver

    def get_driver(self,browser):
        '''
        Run class initialization method, the default is proper
        to drive the Firefox browser. Of course, you can also
        pass parameter for other browser, Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        '''
        if browser == "firefox" or browser == "ff":
            logger.info("Starting firefox browser.")
            return webdriver.Firefox()
        elif browser == "chrome":
            logger.info("Starting Chrome browser.")
            return webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            logger.info("Starting IE browser.")
            return webdriver.Ie()
        elif browser == "opera":
            logger.info("Starting Opera browser.")
            return webdriver.Opera()
        elif browser == "chrome_headless":
            logger.info("Starting Chrome headless browser.")
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            return webdriver.Chrome(chrome_options=chrome_options)
        elif browser == 'edge':
            logger.info("Starting Edge browser.")
            return webdriver.Edge()
        elif browser == 'hongqi':
            logger.info("Starting Hongqi browser.")
            return webdriver.Chrome()
        elif browser == '360':
            logger.info("Starting 360 browser.")
            return webdriver.Ie()

        else:
            raise NameError(
                    "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'edge', 'chrome' or 'chrome_headless'." % browser)


if __name__ == '__main__':
    Op = OpenDriver()
    driver = Op.driver()
