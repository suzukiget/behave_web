# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

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

    time.sleep(2)


@then('we relogin')
def step_impl(context):
    context.lobby_page.renavigate()
    context.login_page.enter_login('ighost1996+test@gmail.com')
    context.login_page.login()
    context.login_page.enter_pass('qwert12345')
    context.login_page.login()
    assert "Welcome," in context.authorized_page.get_page_head()
    context.authorized_page.enter_app()
    #time.sleep(2)

@then('we accept the invitation')
def step_impl(context):
    #context.wait.until(EC.element_to_be_clickable((By.XPATH, '/div[1]/div[2]/div/div/div/div[@data-reactid=".0.1.1.1.1.0.$431487_111@conf=1hipchat=1com"]')))
    context.driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[2]/div/div/div/div[1]').click()
    #context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/form/table/tbody/tr/td[2]/div[2]/div')))
    from selenium.webdriver.common.keys import Keys
    context.driver.find_element_by_id('hc-message-input').send_keys('@all', Keys.RETURN, Keys.RETURN)
    time.sleep(3)

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
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[2]/div/div/div/div[1]').click()
    context.driver.find_element_by_id('room-actions-btn').click()
    time.sleep(1)
    context.driver.find_element_by_css_selector('.delete-room-action').click()
    #context.wait.until(EC.element_to_be_clickable(By.XPATH, '/html/body/div[2]/div/div[2]/section/footer/div[1]/button[1]'))
    #context.wait.until(lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/footer/div[1]/button[1]'))
    time.sleep(1)
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/footer/div[1]/button[1]').click()
    time.sleep(2)








