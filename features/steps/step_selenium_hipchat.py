# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then





@given('we are on Hipchat Login Page')
def step_impl(context):
    context.login_page.navigate()
    assert context.login_page.at()


@when('we enter login')
def step_impl(context):
    context.login_page.enter_login(context.hipchat_login)
    context.login_page.login()
    pass


@when('we enter password')
def step_impl(context):
    context.login_page.enter_pass(context.hipchat_pass)
    context.login_page.login()
    pass


@then('we see welcome title')
def step_impl(context):
    assert "Welcome," in context.authorized_page.get_page_head()
    context.driver.implicitly_wait(10)


'''@given('we are on Hipchat Lobby Page')
def step_impl(context):
    context.authorized_page.enter_app()
    context.driver.implicitly_wait(5)
    pass
    #context.driver.get('https://bortnik.hipchat.com/chat')


@then('we creating the room')
def step_impl(context):
    context.lobby_page.create_room()
    context.lobby_page.set_name()
    context.lobby_page.click_create_room()'''




'''@then('we entered')
def step_impl(context):
    assert context.lobby_page.new_url()
'''
