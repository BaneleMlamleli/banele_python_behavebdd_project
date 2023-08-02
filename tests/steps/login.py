from behave import Given, When, Then
from hamcrest import assert_that, equal_to
from login_domain import LoginDomain

@Given('user is on the login page')
def user_is_on_the_login_page(context):
    context.login_domain = LoginDomain
    context.login_domain.login

@When('user enter "{username}" and "{password}"')
def user_enter_username_and_password(context, username, password):
    context.login_domain = LoginDomain(username, password)
    context.login_domain.enter_credentials

# @And('clicks on login button')
# def clicks_on_login_button(context):
#     context.login_domain = LoginDomain
#     context.login_domain.login_button

@Then('user successfully logs in and redirected to their profile page')
def user_successfully_logs_in_and_redirected_to_their_profile_page(context):
    context.login_domain = LoginDomain
    context.login_domain.correct_login_details

@Then('popup error message is displayed')
def popup_error_message_is_displayed(context):
    context.login_domain = LoginDomain
    context.login_domain.incorrect_login_details