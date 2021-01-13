from behave import *
from src.zadanie1.fizzbuzz import MyFizzBuzz
from assertpy import assert_that

use_step_matcher("re")


@given("Create class MyFizzBuzz")
def step_impl(context):
    context.fizzbuzz = MyFizzBuzz()


@when("only is number / 5")
def step_impl(context):
    context.fizzbuzz.game(25)


@then("get Buzz")
def step_impl(context):
    assert_that(context.fizzbuzz.game(25)).is_equal_to("Buzz")


@when("only is number / 3")
def step_impl(context):
    context.fizzbuzz.game(9)


@then("get Fizz")
def step_impl(context):
    assert_that(context.fizzbuzz.game(9)).is_equal_to("Fizz")


@when("only is number / 15")
def step_impl(context):
    context.fizzbuzz.game(30)


@then("get FizzBuzz")
def step_impl(context):
    assert_that(context.fizzbuzz.game(30)).is_equal_to("FizzBuzz")


@when("number is not / by 5,3")
def step_impl(context):
    context.fizzbuzz.game(17)


@then("get number type str")
def step_impl(context):
    assert_that(context.fizzbuzz.game(17)).is_type_of(str)


@when("number is not / by 5,3 and not type int")
def step_impl(context):
    context.fizzbuzz.game(3.11)


@then("get number type float")
def step_impl(context):
    assert_that(context.fizzbuzz.game(3.11)).is_type_of(float)


@when("input in not type float and int")
def step_impl(context):
    context.fizzbuzz.game(False)


@then("get error")
def step_impl(context):
    assert_that(context.fizzbuzz.game(False)).is_equal_to("Error in FizzBuzz")
