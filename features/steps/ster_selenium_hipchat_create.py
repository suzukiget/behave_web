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
import time

@given('we are on Hipchat Lobby Page')
def step_impl(context):
    context.authorized_page.enter_app()
    time.sleep(8)
    pass

@then('we create a room')
def step_impl(context):
    context.lobby_page.create_room()
    time.sleep(5)
    context.lobby_page.set_name()
    context.lobby_page.click_create_room()
    time.sleep(2)

