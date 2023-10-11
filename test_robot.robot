*** Settings ***
Library    RequestsLibrary

*** Keywords ***
Check Is Prime
    [Arguments]    ${x}    ${expested_result}
    ${resp}    GET On Session    session    /is_prime/${x}
    Should Be Equal As Strings    ${resp.text}    ${expested_result}

*** Test Cases ***
true_when_x_is_7
    Create Session    session    http://192.168.17.133:5000/
    Check Is Prime    17    True

false_when_x_is_36
    Check Is Prime    36    False
    
false_when_x_is_13219
    Check Is Prime    13219    True
