@login_tag
Feature: User login

    Background: login screen
        Given user is on the login page
        When user enter "username" and "password"
    # And clicks on login button

    @scenario_1
    Scenario Outline: User login with correct details
        Then user successfully logs in and redirected to their profile page
        Examples:
            # | username         | password             |
            | correct_username | correct_passowrd123@ |
    @scenario_2
    Scenario Outline: User login with incorrect details
        Then popup error message is displayed
        Examples:
            # | username           | password           |
            | incorrect_username | wrong_passowrd123@ |