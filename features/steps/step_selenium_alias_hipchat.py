# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
import selenium

@given('we are on login page')
def step_impl(context):
    context.login_page.navigate()
    context.login_page.enter_login(context.hipchat_login)
    context.login_page.login()
    context.login_page.enter_pass(context.hipchat_pass)
    context.login_page.login()



@when('we create new Alias')
def step_impl(context):
    context.lobby_page.navigate()
    context.lobby_page.open_chat()
    context.lobby_page.open_alias_menu()
    context.lobby_page.pen_drop_down_menu()
    context.lobby_page.open_menu()
    context.lobby_page.open_config()
    context.lobby_page.input_data_in_alias_form()
    context.lobby_page.input_data_in_alias_name_form()


@then('we check our data')
def step_impl(context):
    context.lobby_page.check_input()

