# -*- coding: UTF-8 -*-

from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LobbyPage(Page):
    """
    Start page for logged in user
    """
    url = '/chat'

    def create_room(self):
        self.find_btn().click()

    def find_btn(self):
        return self.context.driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[1]/nav/div[2]/div[1]/ul/li[6]')


    def find_set_name(self):
        return self.context.driver.find_element_by_id('create-room-name')

    def set_name(self):
        self.find_set_name().send_keys('TestRoomIvan')

    def find_create_btn(self):
        return self.context.driver.find_element_by_xpath('//*[@id="create-room-dialog"]/footer/div[1]/button[1]')

    def click_create_room(self):
        self.find_create_btn().click()




