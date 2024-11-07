from behave import *
import tkinter as tk

@given('unputed "{text}" in entry')
def step_impl(context, text):
    context.view.entry.delete(0, tk.END)
    context.view.entry.insert(0, text)


@when('we press calculate button')
def step_impl(context):
    context.view.calculate_button.invoke()


@then('we will get "{text}" in result')
def step_impl(context, text):
    assert context.view.result_label.cget("text") == text