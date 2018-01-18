# -*- coding: UTF-8 -*-

from .base_page import Page


class AuthorizedPage(Page):
    """
    Start page for logged in user
    """

    url = '/home'

    def label_page_head(self):
        return self.context.driver.find_element_by_css_selector("div.aui-page-header-main > h1")

    def get_page_head(self):
        return self.label_page_head().text

    def current_url(self):
        return self.context.driver.current_url

    def edit_profile_click(self):
        self.context.driver.find_element_by_link_text('Edit Profile').click()
