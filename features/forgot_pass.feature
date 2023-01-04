Feature: Jules forgot password tests

  # before every test
  Background:
    Given sign_in: I am a user on jules sign in page

    @jules
    Scenario: Wrong email validation message
      When sign_in: I click on forgot password link
      When forgot_pass: I set my email "abc"
      Then forgot_pass: I verify that email validation message is correct

    @jules
    Scenario Outline: Wrong email validation message with table data
      When sign_in: I click on forgot password link
      When forgot_pass: I set my email "<email>"
      Then forgot_pass: I verify that email validation message is correct

      Examples:
        | email         |
        | abcd@yahoo.com |
        | a1b2c@yahoo.com|