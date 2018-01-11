# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given('we are on Hipchat Lobby Page')
def step_impl(context):
    context.authorized_page.enter_app()
    try:
        element = EC.presence_of_element_located((By.XPATH, '//*[@id="page"]/div[1]/div[1]/nav/div[2]/div[1]/ul/li[6]'))
        WebDriverWait(context.driver, 5).until(element)
    except TimeoutException:
        print("zaebalo")
    pass


    #context.driver.get('https://bortnik.hipchat.com/chat')



@when('we creating the room')
def step_impl(context):
    try:
        element = EC.presence_of_element_located((By.XPATH, '//*[@id="page"]/div[1]/div[1]/nav/div[2]/div[1]/ul/li[6]'))
        WebDriverWait(context.driver, 5).until(element)
        context.lobby_page.create_room()
        context.lobby_page.set_name()
        context.lobby_page.click_create_room()
    except TimeoutException:
        print("zaebalo")
    '''context.lobby_page.create_room()
    context.lobby_page.set_name()
    context.lobby_page.click_create_room()'''
