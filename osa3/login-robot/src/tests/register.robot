*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
	Input Credentials  lalle  kallenlaan1
        Output Should Contain  The username is already in use

Register With Already Taken Username And Valid Password
        Input Credentials  la  kallenlaan1
        Output Should Contain  The minimum username length is three characters

Register With Too Short Username And Valid Password
        Input Credentials  la  kallenlaan1
        Output Should Contain  The minimum username length is three characters

Register With Enough Long But Invalid Username And Valid Password
        Input Credentials  lal2  kallenlaan1
        Output Should Contain  The username can only contain characters a-z

Register With Valid Username And Too Short Password
        Input Credentials  lal2  kalan1
        Output Should Contain  The minimum password length is 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
        Input Credentials  lal  kalannnnnn
        Output Should Contain  The password must contain other characters besides alphabets

*** Keywords ***
Input New Command And Create User
    Create User  lalle  kallenlaan1
    Input New Command
