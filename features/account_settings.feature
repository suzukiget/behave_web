
Feature: Checking account settings

Scenario: Check account settings
    When we are on Account settings Page
    When we enter login
    And we enter password
    Then we see filled account settings