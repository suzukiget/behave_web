# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import when, then


@when('we are on Account settings Page')
def step_impl(context):
    context.settings_page.navigate()


@then('we see filled account settings')
def step_impl(context):
    #assert len(context.settings_page.name()) > 0
    for i in [context.settings_page.mention_name(),
              context.settings_page.full_name(),
              context.settings_page.email()]:
        assert len(i) > 0
