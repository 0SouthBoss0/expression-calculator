Feature: solving simple expression

  Scenario: solve divizion expression
    Given unputed "4/2" in entry
    When we press calculate button
    Then we will get "2.0" in result

  Scenario: solve long expression
    Given unputed "15/(7-(1+1))*3-(2+(1+1))*15/(7-(200+1))*3-(2+(1+1))*(15/(7-(1+1))*3-(2+(1+1))+15/(7-(1+1))*3-(2+(1+1)))" in entry
    When we press calculate button
    Then we will get "-30.072164948453608" in result


