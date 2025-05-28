import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.Read_properties import Read_config
from Base_Page.Login_Page import Snap_deal_page
from Utilities.custom_logger import log_maker



class Test_01_snap_deal:

    snap_deal_page = Read_config.get_snapdeal_url()
    product_name = Read_config.get_shoe_name()
    logger = log_maker.log_gen()



    def test_verify_title(self,setup):
        self.logger.info("****************----- test_verify_title -----****************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(self.snap_deal_page)
        act_title = self.driver.title
        exp_title = "Shop Online for Men, Women & Kids Clothing, Shoes, Home Decor Items"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            assert False


    def test_search_product(self,setup):
        self.logger.info("***************----- test_search_product -------***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(self.snap_deal_page)
        self.search_prod = Snap_deal_page(self.driver)
        self.search_prod.enter_search_box(self.product_name)
        time.sleep(10)
        self.search_prod.click_search_btn()
        self.driver.close()

    def test_white_shoe(self):
        self.logger.info("**************----- test_white_shoe ------*******************")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(self.snap_deal_page)
        self.search_prod = Snap_deal_page(self.driver)
        self.search_prod.enter_search_box(self.product_name)
        self.driver.implicitly_wait(20)
        self.search_prod.click_search_btn()
        time.sleep(5)
        self.driver.close()









