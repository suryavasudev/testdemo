from selenium.webdriver.common.by import By


class Snap_deal_page:

    textbox_search_name = "keyword"
    btn_search_xpath = "//span[@class='searchTextSpan']"


    def __init__(self,driver):
        self.driver = driver


    def enter_search_box(self,name):
        self.driver.find_element(By.NAME,self.textbox_search_name).send_keys(name)


    def click_search_btn(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()

    def click_airwave_shoe_white(self):
        self.driver.find_element(By.XPATH,self.click_notstyle_gray_xpath).click()

