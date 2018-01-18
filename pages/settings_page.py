# -*- coding: UTF-8 -*-

from .base_page import Page


class SettingsPage(Page):
    """
    Page for Account settings
    """

    url = '/account'

    def mention_name(self):
        return self.context.driver.find_element_by_id('mention_name').get_attribute('value')

    def full_name(self):
        return self.context.driver.find_element_by_id('name').get_attribute('value')

    def email(self):
        return self.context.driver.find_element_by_id('email').get_attribute('value')
