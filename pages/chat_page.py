from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ChatPage(Page):

    url = 'chat/'

    def open_alias_room(self):
        self.find_alias_room().click()

    def find_alias_room(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'status_dropdown')))
        return self.context.driver.find_element_by_xpath("//a[@aria-label='Alias room']")

    def open_alias_menu(self):
        self.find_plus_button().click()

    def find_plus_button(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'input_actions_dropdown-trigger')))
        return self.context.driver.find_element_by_id("input_actions_dropdown-trigger")

    def open_menu(self):
        self.find_button_in_dropdown_menu().click()

    def find_button_in_dropdown_menu(self):
        self.context.wait.until(lambda driver: driver.find_element_by_css_selector(
            "#input_actions_dropdown > div > ul > li:nth-child(1) > a"))
        return self.context.driver.find_element_by_css_selector(
            "#input_actions_dropdown > div > ul > li:nth-child(1) > a")

    def open_config(self):
        try:
            self.context.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hc-addon-iframe")))
            self.context.driver.switch_to.frame(self.context.driver.find_element_by_class_name('hc-addon-iframe'))
            self.find_config().click()
        except:
            self.context.driver.switch_to.frame(self.context.driver.find_element_by_class_name('hc-addon-iframe'))
            self.find_config().click()

    def find_config(self):
        self.context.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-app"]/div/div/a')))
        return self.context.driver.find_element(By.XPATH, '//*[@id="react-app"]/div/div/a')

    def input_data_in_alias_form(self):
        self.find_alias_form().send_keys("@test")

    def find_alias_form(self):
        self.context.wait.until(EC.presence_of_element_located((By.NAME, 'alias')))
        return self.context.driver.find_element_by_name('alias')

    def input_data_in_alias_name_form(self):
        self.find_form_name().send_keys('HenaYamkoviy')
        self.context.wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="@HenaYamkoviy"]')))
        self.adding_data()

    def adding_data(self):
        self.find_form_name().send_keys(u'\ue007')
        self.find_form_name().send_keys(u'\ue007')

    def find_form_name(self):
        return self.context.driver.find_element(By.XPATH, '//input[@tabindex="0"]')

    def find_added_element(self):
        self.context.wait.until(
            lambda driver: self.context.driver.find_elements_by_css_selector('.aui>.aliases>.alias>.mentions'))
        table = self.context.driver.find_elements_by_css_selector('.aui>.aliases>.alias>.mentions')

        result = False
        for element in table:
            if element.text == "@HenaYamkoviy":
                result = True
        return result
