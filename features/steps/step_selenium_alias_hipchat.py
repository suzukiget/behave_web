# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import when, then


@when('we create new Alias')
def step_impl(context):

    context.authorized_page.enter_web_chat()
    context.chat_page.open_alias_room()
    context.chat_page.open_alias_menu()
    context.chat_page.open_menu()
    context.chat_page.open_config()
    context.chat_page.input_data_in_alias_form()
    context.chat_page.input_data_in_alias_name_form()


@then('we check our data')
def step_impl(context):
    assert context.chat_page.find_added_element
