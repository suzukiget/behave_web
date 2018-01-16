# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given('we are on Hipchat Lobby Page')
def step_impl(context):
    context.authorized_page.enter_app()
    pass

@then('we create a room')
def step_impl(context):
    context.lobby_page.create_room()
    context.wait.until(EC.element_to_be_clickable((By.ID, 'create-room-name')))
    context.lobby_page.set_name()
    context.lobby_page.click_create_room()
    context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/ul/li[1]/div')))


@then('we invite member')
def step_impl(context):
    context.lobby_page.click_add_member()
    context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/a')))
    context.lobby_page.click_ask_to_join()
    context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#s2id_invite-users-people')))
    context.lobby_page.send_invite()
    context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="invite-users-dialog"]/footer/div[1]/button[1]')))
    context.lobby_page.invite()


@then('we relogin')
def step_impl(context):
    context.lobby_page.renavigate()
    context.login_page.enter_login('ighost1996+test@gmail.com')
    context.login_page.login()
    context.login_page.enter_pass('qwert12345')
    context.login_page.login()
    assert "Welcome," in context.authorized_page.get_page_head()
    context.authorized_page.enter_app()

@then('we accept the invitation')
def step_impl(context):
    context.lobby_page.accept_invite()

@then('we relogin again')
def step_impl(context):
    context.lobby_page.renavigate()
    context.login_page.enter_login(context.hipchat_login)
    context.login_page.login()
    context.login_page.enter_pass(context.hipchat_pass)
    context.login_page.login()
    assert "Welcome," in context.authorized_page.get_page_head()
    context.authorized_page.enter_app()

@then('we delete the room')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[2]/div/div/div/div[1]').click()
    context.driver.find_element_by_id('room-actions-btn').click()
    context.driver.find_element_by_css_selector('.delete-room-action').click()
    context.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/section/footer/div[1]/button[1]')))
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/footer/div[1]/button[1]').click()








