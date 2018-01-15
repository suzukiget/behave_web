
Feature: Entering the app

Scenario: Enter the app
    Given we are on Hipchat Lobby Page
    Then we create a room
    Then we invite member
    And we relogin
    And we accept the invitation
    And we relogin again
    And we delete the room