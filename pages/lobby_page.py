# -*- coding: UTF-8 -*-

from .base_page import Page
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LobbyPage(Page):
    """
    Start page for logged in user
    """
    url = '/chat'

    def create_room(self):

        self.find_btn().click()
        self.context.wait.until(EC.element_to_be_clickable((By.ID, 'create-room-name')))


    def find_btn(self):
        return self.context.driver.find_element_by_css_selector('#page > div.hc-layout > div.hc-left-sidebar-col > nav > div.aui-navgroup-inner > div:nth-child(2) > ul > li.hc-tab.hc-add-item-link')


    def find_set_name(self):
        return self.context.driver.find_element_by_id('create-room-name')

    def set_name(self):
        rand = random.randint(1, 999)
        self.find_set_name().send_keys(rand)
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create-room-dialog"]/footer/div[1]/button[1]')))

    def find_create_btn(self):
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create-room-dialog"]/footer/div[1]/button[1]')))
        return self.context.driver.find_element_by_xpath('//*[@id="create-room-dialog"]/footer/div[1]/button[1]')

    def click_create_room(self):
        self.find_create_btn().click()


    def find_add_member(self):
        return self.context.driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/ul/li[1]/div')

    def click_add_member(self):
        self.find_add_member().click()

    def find_ask_to_join(self):
        return self.context.driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/a')

    def click_ask_to_join(self):
        self.find_ask_to_join().click()

    def send_invite(self):
        self.context.driver.find_element_by_css_selector('#s2id_invite-users-people').click()
        self.context.driver.find_element_by_xpath('//*[@id="select2-drop"]/ul/li[3]').click()

    def find_invite(self):
        return self.context.driver.find_element_by_xpath('//*[@id="invite-users-dialog"]/footer/div[1]/button[1]')

    def invite(self):
        self.find_invite().click()






