# -*- coding: UTF-8 -*-

from .base_page import Page


class SettingsPage(Page):
    """
    Page for Account settings
    """

    url = '/account'

    def filled_acc_settings(self):
        ment_name = self.context.driver.find_element_by_id('mention_name').get_attribute('value')
        name = self.context.driver.find_element_by_id('name').get_attribute('value')
        email = self.context.driver.find_element_by_id('email').get_attribute('value')
        if len(ment_name) > 0 and len(name) > 0 and len(email) > 0:
            return True
        else:
            return False
