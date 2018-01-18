
Feature: Check Alias Functional

Scenario: Login, Open Alias Room, Create Alias, Check

    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    When we create new Alias
    Then we check our data

