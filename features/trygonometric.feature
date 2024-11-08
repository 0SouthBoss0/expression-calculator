Feature: solving trygonometric expression

  Scenario: solve hard trygonometric expression
    Given unputed "(sin(2pi * (3 + (4 / (5 - 2)))) ^ 2) / (1 + (sin(pi / 4)) ^ 3)" in entry
    When we press calculate button
    Then we will get "0.5540970937771961" in result