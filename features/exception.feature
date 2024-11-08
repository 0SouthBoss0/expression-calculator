Feature: raising exceptions

  Scenario: solve wrong expression
    Given unputed "2/0" in entry
    When we press calculate button
    Then we will get error with "Ошибка во время вычисления / !" message