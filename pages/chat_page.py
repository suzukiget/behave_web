from .base_page import Page
from selenium.webdriver.common.by import By

class ChatPage(Page):

    url = 'chat/'



    def find_chat(self):
        self.context.wait.until(lambda driver: driver.find_element_by_id('status_dropdown'))
        return self.context.driver.find_element_by_xpath("//span[text()='Alias room']")

    def find_plus_butt(self):
        self.context.wait.until(lambda driver: driver.find_element_by_id('input_actions_dropdown-trigger'))
        return self.context.driver.find_element_by_id("input_actions_dropdown-trigger")

    def find_butt_in_dropdown_menu(self):
        self.context.wait.until(
        lambda driver: driver.find_element_by_css_selector("#input_actions_dropdown > div > ul > li:nth-child(1) > a"))
        return self.context.driver.find_element_by_css_selector("#input_actions_dropdown > div > ul > li:nth-child(1) > a")


    #def switch_to_frame(self):
        #self.context.wait.until(lambda driver: driver.find_element_by_class_name('hc-addon-iframe'))
     #   frame = self.context.driver.find_element_by_class_name('hc-addon-iframe')
      #  return self.context.driver.switch_to.frame(frame)

    def find_config(self):

        self.context.wait.until(lambda driver: driver.find_element(By.XPATH, '//*[@id="react-app"]/div/div/a'))
        self.context.driver.find_element(By.XPATH, '//*[@id="react-app"]/div/div/a').click()

    def find_alias_form(self):
        return self.context.driver.find_element_by_name('alias')

    def find_form_name(self):
        return self.context.driver.find_element(By.XPATH, '//*[@id="react-app"]/div/form/div/div[2]/div/div/div/input')


    def find_input_but(self):
        return self.context.driver.find_element_by_css_selector\
            ('#react-app > div > form > div > div.aui-item.actions > input')

    def find_added_el(self):
        self.context.wait.until(lambda driver: self.context.driver.find_elements_by_css_selector('.aui>.aliases>.alias>.mentions'))
        tabledata = self.context.driver.find_elements_by_css_selector('.aui>.aliases>.alias>.mentions')
        print(tabledata)
        result = False
        for element in tabledata:
            if element.text == "@HenaYamkoviy":
                print(element.text)
                result = True
        return result


    def input_data_in_alias_form(self):
        self.find_alias_form().send_keys("@test")

    def input_data_in_alias_name_form(self):
        self.find_form_name().send_keys('@HenaYamkoviy')
        self.find_form_name().send_keys(u'\ue007')
        self.find_form_name().send_keys(u'\ue007')
        try: self.context.wait.until(
            lambda driver: self.context.driver.find_elements_by_css_selector('.aui>.aliases>.alias>.mentions'))
        except:
            self.find_form_name().send_keys('@HenaYamkoviy')
            self.find_form_name().send_keys(u'\ue007')
            self.find_form_name().send_keys(u'\ue007')


    def open_config(self):
        #self.switch_to_frame()
        self.find_config()
    def open_menu(self):
        self.find_butt_in_dropdown_menu().click()


    def open_chat(self):
        self.find_chat().click()

    def open_alias_menu(self):
        self.find_plus_butt().click()