*** Settings ***
Library  RequestsLibrary
Library  BuiltIn

*** Variables ***
${BASE_URL}  http://localhost:5000

*** Test Cases ***
be_0_when_x_is_0
    ${response}  Get  ${BASE_URL}/mul5/0
    Should Be Equal As Strings  ${response.status_code}  200
    Should Be Equal As Strings  ${response.text}  0

be_15_when_x_is_3
    ${response}  Get  ${BASE_URL}/mul5/3
    Should Be Equal As Strings  ${response.status_code}  200
    Should Be Equal As Strings  ${response.text}  15

be_1dot5_when_x_is_7dot5
    ${response}  Get  ${BASE_URL}/mul5/7.5
    Should Be Equal As Strings  ${response.status_code}  200
    Should Be Equal As Strings  ${response.text}  37.5
