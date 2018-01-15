# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
import time

@given('we are on Hipchat Home Page')
def step_impl(context):
    context.login_page.navigate()
    context.login_page.enter_login(context.hipchat_login)
    context.login_page.login()
    context.login_page.enter_pass(context.hipchat_pass)
    context.login_page.login()
    assert "Welcome," in context.authorized_page.get_page_head()


@when('we edit profile')
def step_impl(context):
    context.authorized_page.edit_profile()
    assert '/account' in context.authorized_page.current_url()


@then('we see filled account settings')
def step_impl(context):
    assert context.authorized_page.get_acc_settings()


