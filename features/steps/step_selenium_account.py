# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@when('we are on Account settings Page')
def step_impl(context):
    # context.settings_page.navigate()
    # assert context.settings_page.at()
    pass

@then('we see filled account settings')
def step_impl(context):
    #assert context.settings_page.filled_acc_settings()
    pass
