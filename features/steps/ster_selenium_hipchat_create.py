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
    #context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/a')))
    import time
    time.sleep(2)






