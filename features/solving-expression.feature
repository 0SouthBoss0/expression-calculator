Feature: solving expression

  Scenario Outline: Calculate <expression>
    Given unputed "<expression>" in entry
    When we press calculate button
    Then we will get "<result>" in result

    Examples: one operation expressions
      | expression | result            |
      | 2+3        | 5.0               |
      | 3-2        | 1.0               |
      | 2-3        | -1.0              |
      | 2*3        | 6.0               |
      | 4/2        | 2.0               |
      | 3*3        | 9.0               |
      | 4%3        | 1.0               |
      | 2^3        | 8.0               |
      | 2^3        | 8.0               |
      | -1-3       | -4.0              |
      | (0.9)π     | 2.827433388230814 |

    Examples: many operation expressions
      | expression  | result |
      | 2+3+4       | 9.0    |
      | 3-2+5       | 6.0    |
      | 3-(2+5)     | -4.0   |
      | (2-3)+(3-4) | -2.0   |
      | 4*(2+3)     | 20.0   |
      | 4(2+3)      | 20.0   |
      | -4(-2+3)    | -4.0   |
      | 4(-2-(-3))  | 4.0    |
      | 2+2*2       | 6.0    |

    Examples: long expressions
      | expression                                                                                              | result              |
      | 15/(7-(1+1))*3-(2+(1+1))*15/(7-(200+1))*3-(2+(1+1))*(15/(7-(1+1))*3-(2+(1+1))+15/(7-(1+1))*3-(2+(1+1))) | -30.072164948453608 |

    Examples: trigonometric expressions
      | expression                                                     | result             |
      | (sin(2pi * (3 + (4 / (5 - 2)))) ^ 2) / (1 + (sin(pi / 4)) ^ 3) | 0.5540970937771961 |

    Examples: function expressions
      | expression | result |
      | fact(3)    | 6      |
      | 3!         | 6      |
      | min(2, 5)  | 2.0    |
      | max(-2, 5) | 5.0    |
      | log(2, 64) | 6.0    |
      | ln(e)      | 1.0    |

    Examples: basic arithmetic variations
      | expression | result |
      | 0+0        | 0.0    |
      | 0-5        | -5.0   |
      | 5-0        | 5.0    |
      | 0*5        | 0.0    |
      | 5*0        | 0.0    |
      | 0/5        | 0.0    |
      | 1/1        | 1.0    |
      | 10/2       | 5.0    |
      | 2^0        | 1.0    |
      | 2^1        | 2.0    |
      | 0^5        | 0.0    |
      | 5%2        | 1.0    |
      | 5%5        | 0.0    |

    Examples: negative numbers operations
      | expression | result |
      | -5+3       | -2.0   |
      | -5-3       | -8.0   |
      | -5*-3      | 15.0   |
      | -5*3       | -15.0  |
      | -10/2      | -5.0   |
      | -10/-2     | 5.0    |
      | (-2)^3     | -8.0   |
      | (-2)^4     | 16.0   |

    Examples: decimal operations
      | expression | result |
      | 0.5+0.5    | 1.0    |
      | 1.5-0.5    | 1.0    |
      | 0.5*4      | 2.0    |
      | 1.5/0.5    | 3.0    |
      | 0.1+0.2    | 0.3    |
      | 2.5^2      | 6.25   |
      | 0.25*0.25  | 0.0625 |

    Examples: order of operations
      | expression    | result |
      | 2+3*4         | 14.0   |
      | (2+3)*4       | 20.0   |
      | 10-4/2        | 8.0    |
      | (10-4)/2      | 3.0    |
      | 2^3*4         | 32.0   |
      | 2^(3*4)       | 4096.0 |
      | 4+3*2^2       | 16.0   |
      | 4+3*(2^2)     | 16.0   |
      | 100/10^2      | 1.0    |
      | (100/10)^2    | 100.0  |
      | 2+3*4-5/1     | 9.0    |
      | (2+3)*(4-5)/1 | -5.0   |

    Examples: parentheses combinations
      | expression          | result |
      | ((2+3))             | 5.0    |
      | (((2+3)*4))         | 20.0   |
      | (2+(3*4))           | 14.0   |
      | ((2+3)*(4-1))       | 15.0   |
      | (2*(3+(4*5)))       | 46.0   |
      | ((((5))))           | 5.0    |
      | (1+((2*3)+4))       | 11.0   |
      | ((1+2)*(3+4)*(5+6)) | 231.0  |

    Examples: implicit multiplication
      | expression  | result            |
      | 2(3+4)      | 14.0              |
      | (2+3)4      | 20.0              |
      | 3(2)        | 6.0               |
      | (3)(4)      | 12.0              |
      | 2(3+4)5     | 70.0              |
      | -2(3+4)     | -14.0             |
      | 2(-3+4)     | 2.0               |
      | 0.5(10)     | 5.0               |
      | 2π          | 6.283185307179586 |
      | 2(3+4)(5+6) | 154.0             |

    Examples: trigonometric functions basic
      | expression | result |
      | sin(0)     | 0.0    |
      | sin(pi/2)  | 1.0    |
      | sin(pi)    | 0.0    |
      | cos(0)     | 1.0    |
      | cos(pi/2)  | 0.0    |
      | cos(pi)    | -1.0   |
      | tan(0)     | 0.0    |
      | tan(pi/4)  | 1.0    |


    Examples: advanced trigonometric
      | expression            | result             |
      | sin(pi/6)             | 0.5                |
      | cos(pi/3)             | 0.5                |
      | tan(pi/3)             | 1.7320508075688767 |
      | sin(pi/4)^2           | 0.5                |
      | sin(pi/6)+cos(pi/3)   | 1.0                |
      | 2*sin(pi/4)*cos(pi/4) | 1.0                |
      | sin(pi/2)+cos(pi/2)   | 1.0                |
      | tan(pi/4)+tan(pi/4)   | 2.0                |

    Examples: logarithmic functions
      | expression    | result |
      | log(10, 100)  | 2.0    |
      | log(2, 8)     | 3.0    |
      | log(5, 25)    | 2.0    |
      | ln(1)         | 0.0    |
      | ln(e^2)       | 2.0    |
      | log(10, 1000) | 3.0    |
      | log(2, 1)     | 0.0    |
      | ln(e^10)      | 10.0   |
      | log(0.5, 2)   | -1.0   |

    Examples: factorial and combinations
      | expression      | result |
      | fact(0)         | 1      |
      | fact(1)         | 1      |
      | fact(5)         | 120    |
      | 0!              | 1      |
      | 1!              | 1      |
      | 5!              | 120    |
      | fact(2)+fact(3) | 8      |
      | 2!*3!           | 12     |
      | fact(4)/fact(2) | 12     |

    Examples: min/max functions
      | expression        | result |
      | min(1, 2)         | 1.0    |
      | min(-5, 5)        | -5.0   |
      | min(0, 0)         | 0.0    |
      | min(2.5, 3.7)     | 2.5    |
      | max(1, 2)         | 2.0    |
      | max(-5, 5)        | 5.0    |
      | max(0, 0)         | 0.0    |
      | max(2.5, 3.7)     | 3.7    |
      | min(1, min(2, 3)) | 1.0    |
      | max(1, max(2, 3)) | 3.0    |
      | min(max(1,5), 10) | 5.0    |

    Examples: constants usage
      | expression | result             |
      | π          | 3.141592653589793  |
      | e          | 2.718281828459045  |
      | 2π         | 6.283185307179586  |
      | π/2        | 1.5707963267948966 |
      | e^1        | 2.718281828459045  |
      | π+e        | 5.859874482048838  |
      | 2e         | 5.43656365691809   |
      | π*π        | 9.869604401089358  |

    Examples: complex expressions mixing functions
      | expression                | result |
      | sin(π/2)+cos(0)           | 2.0    |
      | 2*sin(π/4)*cos(π/4)       | 1.0    |
      | fact(3)+log(2,8)          | 9.0    |
      | min(5,max(2,10))          | 5.0    |
      | sqrt(4)+2^3               | 10.0   |
      | sin(π/6)*2                | 1.0    |
      | log(2,8)*fact(2)          | 6.0    |
      | (sin(π/2))^2+(cos(π/2))^2 | 1.0    |

    Examples: edge cases and error prevention
      | expression | result |
      | 1+2+3+4+5  | 15.0   |
      | 1-2-3-4    | -8.0   |
      | 2*2*2*2    | 16.0   |
      | 100/2/2/5  | 5.0    |
      | 2^2^2      | 16.0   |
      | 1+-1       | 0.0    |
      | -(-5)      | 5.0    |
      | 3!+2!      | 8.0    |

    Examples: square roots and powers
      | expression     | result             |
      | sqrt(4)        | 2.0                |
      | sqrt(9)        | 3.0                |
      | sqrt(2)        | 1.4142135623730951 |
      | sqrt(25)       | 5.0                |
      | sqrt(0)        | 0.0                |
      | sqrt(1)        | 1.0                |
      | 4^(1/2)        | 2.0                |
      | 8^(1/3)        | 2.0                |
      | sqrt(sqrt(16)) | 2.0                |
      | (sqrt(4))^2    | 4.0                |

    Examples: modulo calculations
      | expression  | result |
      | 17 % 5      | 2      |
      | 100 + 7%4   | 103    |
      | 50 * 3%2    | 50     |
      | 10%3 + 20%6 | 3      |




    Examples: mixed complex expressions
      | expression              | result |
      | 2+3*4-5/1+2^3           | 17.0   |
      | (2+3)*(4-1)+10/2        | 20.0   |
      | sin(π/2)*cos(0)+fact(3) | 7.0    |
      | min(5,10)+max(2,8)*2    | 21.0   |
      | sqrt(16)+log(2,8)!      | 10.0   |
      | (2+3)*(4-1)/(5-2)       | 5.0    |
      | 2^(3+1)-sqrt(16)*2      | 8.0    |
      | fact(4)/2+log(10,100)   | 14.0   |