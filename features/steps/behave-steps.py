import tkinter
from unittest.mock import patch, MagicMock

from behave import *
from pytest import approx


@given('unputed "{text}" in entry')
def step_impl(context, text):
    context.view.entry.insert(0, text)
    assert context.view.entry.get() == text


@when('we press calculate button')
def step_impl(context):
    context.view.calculate_button.invoke()


@then('we will get "{expected_number}" in result')
def step_impl(context, expected_number):
    actual_text = context.view.result_label.cget("text")
    expected_num = float(expected_number)
    actual_num = float(actual_text)
    assert actual_num == approx(expected_num)


@then('we will get "{text}" exception')
def step_impl(context, text):
    context.view.display_error.assert_called_once_with(text)
