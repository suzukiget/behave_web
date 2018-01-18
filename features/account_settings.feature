
Feature: Checking account settings

Scenario: Login to HipChat
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title


Scenario: Check account settings
    When we are on Account settings Page
    Then we see filled account settings