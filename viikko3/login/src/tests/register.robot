*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  pilkunviilaaja42
    Set Password  salasana1234
    Set Password Confirmation  salasana1234
    Click  button >> text=Register
    Register Should Succeed

Register With Password Confirmation That Does Not Match
    Set Username  passwordmismatch
    Set Password  salasana1234
    Set Password Confirmation  toinen1234
    Click  button >> text=Register
    Register Should Fail With Message  password confirmation mismatch

Register With Too Short Username And Valid Password
    Set Username  op
    Set Password  nullnull95
    Set Password Confirmation  nullnull95
    Click  button >> text=Register
    Register Should Fail With Message  Username too short must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  devaaja69
    Set Password  blober2
    Set Password Confirmation  blober2
    Click  button >> text=Register
    Register Should Fail With Message  Password too short must be at least 8 characters

Register With Password Containing Numbers
    Set Username  passwordnumbers
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Special Characters
    Set Username  passwordspecial
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Only Lowercase Letters
    Set Username  passwordlowercase
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  passwordmixedcase
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Get Text  body  *=  ${message}
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
