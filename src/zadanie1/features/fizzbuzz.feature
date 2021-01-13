Feature: Friendships


  Scenario: Fizzbuzz output Buzz
    Given Create class MyFizzBuzz
    When only is number / 5
    Then get Buzz

  Scenario: Fizzbuzz output Fizz
    Given Create class MyFizzBuzz
    When only is number / 3
    Then get Fizz

  Scenario: Fizzbuzz output FizzBuzz
    Given Create class MyFizzBuzz
    When only is number / 15
    Then get FizzBuzz

  Scenario: Fizzbuzz output number type str
    Given Create class MyFizzBuzz
    When number is not / by 5,3
    Then get number type str

  Scenario: Fizzbuzz output number type float
    Given Create class MyFizzBuzz
    When number is not / by 5,3 and not type int
    Then get number type float

  Scenario: Fizzbuzz output error
    Given Create class MyFizzBuzz
    When input in not type float and int
    Then get error
