# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given('we are on login page')
def step_impl(context):
    context.login_page.navigate()
    context.login_page.enter_login(context.hipchat_login)
    context.login_page.login()
    context.login_page.enter_pass(context.hipchat_pass)
    context.login_page.login()
    assert "Welcome," in context.authorized_page.get_page_head()

@when('we create new Alias')
def step_impl(context):

    context.authorized_page.enter_web_chat()
    context.chat_page.open_chat()
    context.chat_page.open_alias_menu()
    #context.lobby_page.open_drop_down_menu()
    context.chat_page.open_menu()
    context.wait.until(lambda driver: driver.find_element_by_class_name('hc-addon-iframe'))
    #time.sleep(4)
    context.driver.switch_to.frame(context.driver.find_element_by_class_name('hc-addon-iframe'))
    try:
        context.chat_page.open_config()
    except:
        context.driver.switch_to.frame(context.driver.find_element_by_class_name('hc-addon-iframe'))
        context.chat_page.open_config()
    context.chat_page.input_data_in_alias_form()
    context.chat_page.input_data_in_alias_name_form()

    pass


@then('we check our data')
def step_impl(context):
    assert context.chat_page.find_added_el()

