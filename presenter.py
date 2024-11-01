import math

import numpy as np

from model import Model
from view import View


class CalculatorException(Exception):
    pass


class CalculatorToken:
    priority_dict = {"+": 1, "-": 1, "/": 2, "*": 2, "^": 3, "~": 4}

    def __init__(self, t_type, t_value):
        self.t_type = t_type
        self.t_value = t_value

        if t_type == "Operator":
            self.t_priority = self.priority_dict[t_value]


def save_number_buff(tokenized_input: list, number_buff: str, add_mult=False) -> tuple[list, str]:
    tokenized_input.append(CalculatorToken("Digit", number_buff))
    if add_mult:
        tokenized_input.append(CalculatorToken("Operator", "*"))
    return tokenized_input, ""


def save_letter_buff(tokenized_input: list, letter_buff: str) -> tuple[list, str]:
    tokenized_input.append(CalculatorToken("Function", letter_buff))
    return tokenized_input, ""


def save_constants(tokenized_input: list, letter_buff: str) -> tuple[list, str] | CalculatorException:
    if letter_buff == "pi" or letter_buff == "π":
        tokenized_input.append(CalculatorToken("Digit", np.pi))
    elif letter_buff == "e":
        tokenized_input.append(CalculatorToken("Digit", 2.71))
    else:
        raise CalculatorException(f"invalid value: {letter_buff}")
    return tokenized_input, ""


class Presenter:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def evaluate(self, expression):
        stack = []
        unary_dict = {"~": lambda a: -a, "sin": lambda a: np.sin(a)}
        binary_dict = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "/": lambda a, b: a / b,
                       "*": lambda a, b: a * b, "^": lambda a, b: a ** b, "log": lambda a, b: math.log(b, a)}
        for token in expression:
            print(stack)
            if token.t_type == "Digit":
                stack.append(float(token.t_value))
            else:
                if token.t_value in binary_dict:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(binary_dict[token.t_value](b, a))
                else:
                    stack.append(unary_dict[token.t_value](stack.pop()))

        return stack.pop()

    def input_tokenize(self, input_string: str) -> list:
        tokenized_input = []
        operators = ["+", "-", "*", "/", "%", "^"]

        number_buffer = ""
        letter_buffer = ""
        try:
            for i, symbol in enumerate(input_string.replace(" ", "")):
                if symbol.isdigit():
                    # if len(tokenized_input) > 0 and tokenized_input[-1].t_type == "CloseBracket":
                    #     tokenized_input.append(CalculatorToken("Operator", "*"))
                    number_buffer += symbol

                elif symbol.isalpha():
                    if len(number_buffer) > 0:
                        tokenized_input, number_buffer = save_number_buff(tokenized_input, number_buffer, add_mult=True)
                    letter_buffer += symbol

                elif symbol in operators:
                    if len(number_buffer) > 0:
                        tokenized_input, number_buffer = save_number_buff(tokenized_input, number_buffer)

                    if len(letter_buffer) > 0:
                        tokenized_input, letter_buffer = save_constants(tokenized_input, letter_buffer)

                    # check for unary minus
                    if symbol == "-" and (
                            i == 0 or (i > 1 and input_string.replace(" ", "")[i - 1] in operators + ["(", ")"])):
                        symbol = "~"
                    tokenized_input.append(CalculatorToken("Operator", symbol))

                elif symbol == "(":
                    if len(tokenized_input) > 0 and tokenized_input[-1].t_type == "CloseBracket":
                        tokenized_input.append(CalculatorToken("Operator", "*"))

                    if len(letter_buffer) > 0:
                        tokenized_input, letter_buffer = save_letter_buff(tokenized_input, letter_buffer)

                    elif len(number_buffer) > 0:
                        tokenized_input, number_buffer = save_number_buff(tokenized_input, number_buffer, add_mult=True)
                    tokenized_input.append(CalculatorToken("OpenBracket", symbol))

                elif symbol == ")":
                    if len(number_buffer) > 0:
                        tokenized_input, number_buffer = save_number_buff(tokenized_input, number_buffer)
                    if len(letter_buffer) > 0:
                        tokenized_input, letter_buffer = save_constants(tokenized_input, letter_buffer)
                    tokenized_input.append(CalculatorToken("CloseBracket", symbol))

                elif symbol == ".":
                    number_buffer += "."
                elif symbol == ",":
                    if len(number_buffer) > 0:
                        tokenized_input, number_buffer = save_number_buff(tokenized_input, number_buffer)
                    if len(letter_buffer) > 0:
                        tokenized_input, letter_buffer = save_constants(tokenized_input, letter_buffer)
                    tokenized_input.append(CalculatorToken("Separator", symbol))
                else:
                    raise CalculatorException(f'incorrect symbol - {symbol}')

            if len(number_buffer) > 0:
                tokenized_input, number_buffer = save_number_buff(tokenized_input, number_buffer)
            if len(letter_buffer) > 0:
                tokenized_input, letter_buffer = save_constants(tokenized_input, letter_buffer)
        except CalculatorException as e:
            print(f'exception: {e}')
            return []
        print(*[i.t_type for i in tokenized_input], sep=' ')
        print(*[i.t_value for i in tokenized_input], sep='')
        return tokenized_input

    def sort_machine_algo(self, parsed_tokens: list[CalculatorToken]):
        queue = []
        stack = []
        for token in parsed_tokens:
            print(f"token: {token.t_value}")
            print("queue:", end=" ")
            print([item.t_value for item in queue], sep=" ")
            print("stack:", end=" ")
            print([item.t_value for item in stack], sep=" ")
            print()
            match token.t_type:
                case "Digit":
                    queue.append(token)

                case "Function":
                    stack.append(token)

                case "OpenBracket":
                    stack.append(token)

                case "CloseBracket":
                    while stack[-1].t_type != "OpenBracket":
                        queue.append(stack.pop())
                    else:
                        stack.pop()
                    if len(stack) > 0 and stack[-1].t_type == "Function":
                        queue.append(stack.pop())

                case "Separator":
                    while stack[-1].t_type != "OpenBracket":
                        queue.append(stack.pop())

                case "Operator":
                    while len(stack) > 0 and stack[-1].t_type == "Operator" and stack[-1].t_priority >= token.t_priority:
                        queue.append(stack.pop())
                    stack.append(token)

        while len(stack) > 0:
            queue.append(stack.pop())
        return queue

    # def check_input(self, parsed_command: list) -> bool:
    #     """
    #     Validating input
    #     :param parsed_command: list of parsed input_string into nums and operators
    #     :return: boolean value if input is valid
    #     """
    #     if len(parsed_command) != 3 or parsed_command[1] not in list(self._model.operations.keys()):
    #         self._view.display_error("Invalid input\n")
    #         return False
    #     try:
    #         for i, num in enumerate(parsed_command):
    #             if i != 1:
    #                 if "." in num or "," in num:
    #                     parsed_command[i] = float(num.replace(",", "."))
    #                     if abs(parsed_command[i]) < 10 ** -6:
    #                         raise CalculatorException("Small number exception!")
    #                 else:
    #                     parsed_command[i] = int(num)
    #         return True
    #     except Exception as e:
    #         self._view.display_error(str(e))
    #         return False
    #
    # def execute(self):
    #     """
    #     Function to execute calculator app
    #     """
    #     # get expression string from view
    #     input_string = self._view.get_input()
    #     self._view.entry.delete(0, tkinter.END)
    #     self._view.set_output("calculate>")
    #     # parse expression string
    #     parsed_command = self.parse_input(input_string)
    #
    #     # validating parsed command
    #     if self.check_input(parsed_command):
    #         try:
    #             result = self._model.calculate(parsed_command[0], self._model.operations[parsed_command[1]],
    #                                            parsed_command[2])
    #             self._view.set_output(str(result) + "\n")
    #         except Exception as err:
    #             self._view.display_error(str(err))

    def solve(self, in_str):
        tokens = self.input_tokenize(in_str)
        parsed = self.sort_machine_algo(tokens)
        #print(" ".join([item.t_value for item in parsed]))
        return self.evaluate(parsed)
