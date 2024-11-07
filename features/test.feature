Feature: solving expression

  Scenario: solve simple expression
    Given unputed "4/2" in entry
    When we press calculate button
    Then we will get "2.0" in result