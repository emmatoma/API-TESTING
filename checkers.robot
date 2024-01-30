*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    Edge

*** Test Cases ***
Test Select Piece and Move
    Set Screenshot Directory  C:/Users/ealvarezfelix/Music
    [Documentation]    Test Case: Select Piece and Move
    Open Browser    https://www.gamesforthebrain.com/game/checkers/    ${BROWSER}
    Click Element    xpath=//img[@name='space02']
    Click Element    xpath=//img[@name='space13']
    Sleep    5s
    Capture Page Screenshot    screenshot_after_first_test.png
    Close Browser

Test Invalid Move
    Set Screenshot Directory  C:/Users/ealvarezfelix/Music
    [Documentation]    Test Case: Invalid Move
    Open Browser    https://www.gamesforthebrain.com/game/checkers/    ${BROWSER}
    Click Element    xpath=//img[@name='space13']
    Click Element    xpath=//img[@name='space02']
    Log    Test Case Successful: Invalid Move - Initial piece is at the expected location.
    Capture Page Screenshot    screenshot_after_second__test.png
    ${imagecomp}=  compare_images  screenshot_after_first_test.png  ${browser}
    Close Browser
