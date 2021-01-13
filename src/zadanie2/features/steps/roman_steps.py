from behave import *
from src.zadanie2.roman import Roman
from assertpy import assert_that

use_step_matcher("re")


@given("Create class Roman")
def step_impl(context):
    context.roman = Roman()


@when("convert 1 to Roman number")
def step_impl(context):
    context.roman.roman(1)


@then("output should be I")
def step_impl(context):
    assert_that(context.roman.roman(1)).is_equal_to("I")


@when("convert 6 to Roman number")
def step_impl(context):
    context.roman.roman(6)


@then("output should be VI")
def step_impl(context):
    assert_that(context.roman.roman(6)).is_equal_to("VI")


@when("convert 27 to Roman number")
def step_impl(context):
    context.roman.roman(27)


@then("output should be XXVII")
def step_impl(context):
    assert_that(context.roman.roman(27)).is_equal_to("XXVII")


@when("convert 59 to Roman number")
def step_impl(context):
    context.roman.roman(59)


@then("output should be LIX")
def step_impl(context):
    assert_that(context.roman.roman(59)).is_equal_to("LIX")


@when("convert 93 to Roman number")
def step_impl(context):
    context.roman.roman(93)


@then("output should be XCIII")
def step_impl(context):
    assert_that(context.roman.roman(93)).is_equal_to("XCIII")


@when("convert 163 to Roman number")
def step_impl(context):
    context.roman.roman(163)


@then("output should be CLXIII")
def step_impl(context):
    assert_that(context.roman.roman(163)).is_equal_to("CLXIII")


@when("convert 402 to Roman number")
def step_impl(context):
    context.roman.roman(402)


@then("output should be CDII")
def step_impl(context):
    assert_that(context.roman.roman(402)).is_equal_to("CDII")


@when("convert 1024 to Roman number")
def step_impl(context):
    context.roman.roman(1024)


@then("output should be MXXIV")
def step_impl(context):
    assert_that(context.roman.roman(1024)).is_equal_to("MXXIV")


@when("convert 3000 to Roman number")
def step_impl(context):
    context.roman.roman(3000)


@then("output should be MMM")
def step_impl(context):
    assert_that(context.roman.roman(3000)).is_equal_to("MMM")
