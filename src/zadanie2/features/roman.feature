Feature: Roman


  Scenario: create roman number with 1
    Given Create class Roman
    When convert 1 to Roman number
    Then output should be I

  Scenario: create roman number with 6
    Given Create class Roman
    When convert 6 to Roman number
    Then output should be VI

  Scenario: create roman number with 27
    Given Create class Roman
    When convert 27 to Roman number
    Then output should be XXVII

  Scenario: create roman number with 59
    Given Create class Roman
    When convert 59 to Roman number
    Then output should be LIX

  Scenario: create roman number with 93
    Given Create class Roman
    When convert 93 to Roman number
    Then output should be XCIII

  Scenario: create roman number with 163
    Given Create class Roman
    When convert 163 to Roman number
    Then output should be CLXIII

  Scenario: create roman number with 402
    Given Create class Roman
    When convert 402 to Roman number
    Then output should be CDII

  Scenario: create roman number with 1024
    Given Create class Roman
    When convert 1024 to Roman number
    Then output should be MXXIV

  Scenario: create roman number with 3000
    Given Create class Roman
    When convert 3000 to Roman number
    Then output should be MMM