import math

import numpy as np


class CalculatorException(Exception):
    pass


class CalculatorToken:
    priority_dict = {"+": 1, "-": 1, "%": 1, "/": 2, "*": 2, "^": 3, "~": 4}

    def __init__(self, t_type, t_value):
        self.t_type = t_type
        self.t_value = t_value

        if t_type == "Operator":
            self.t_priority = self.priority_dict[t_value]

    def __eq__(self, other):
        return self.t_type == other.t_type and self.t_value == other.t_value


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
        tokenized_input.append(CalculatorToken("Digit", np.e))
    else:
        raise CalculatorException(f"invalid value: {letter_buff}")
    return tokenized_input, ""


def factorial_check(a):
    if a.is_integer():
        return math.factorial(int(a))
    else:
        raise CalculatorException("factorial not int error")


class Model:
    def __init__(self):
        pass

    def evaluate(self, expression: list[CalculatorToken]):
        stack = []
        unary_dict = {"~": lambda a: -a, "sin": lambda a: np.sin(a), "cos": lambda a: np.cos(a),
                      "tan": lambda a: np.tan(a), "cot": lambda a: 1 / np.tan(a), "sqrt": lambda a: math.sqrt(a),
                      "ln": lambda a: math.log(a), "fact": factorial_check,
                      "!": factorial_check}
        binary_dict = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "/": lambda a, b: a / b,
                       "*": lambda a, b: a * b, "^": lambda a, b: a ** b, "log": lambda a, b: math.log(b, a),
                       "min": lambda a, b: min(a, b), "max": lambda a, b: max(a, b), "%": lambda a, b: a % b}
        for token in expression:
            if token.t_type == "Digit":
                stack.append(float(token.t_value))
            else:
                if token.t_value in binary_dict:
                    try:
                        a = stack.pop()
                        b = stack.pop()
                    except IndexError as err:
                        raise CalculatorException(f"exception with expression - {err}")
                    try:
                        stack.append(binary_dict[token.t_value](b, a))
                    except Exception as err:
                        raise CalculatorException(f"exception while calculation - {err}")
                else:
                    try:
                        stack.append(unary_dict[token.t_value](stack.pop()))
                    except Exception as err:
                        raise CalculatorException(f"exception while calc - {err}")

        try:
            return stack.pop()
        except Exception as err:
            raise CalculatorException(f"exception with expression - {err}")

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
                elif symbol == "!":
                    if len(number_buffer) > 0:
                        tokenized_input, number_buffer = save_number_buff(tokenized_input, number_buffer)
                    tokenized_input.append(CalculatorToken("Function", symbol))
                elif symbol in operators:
                    if len(number_buffer) > 0:
                        tokenized_input, number_buffer = save_number_buff(tokenized_input, number_buffer)

                    if len(letter_buffer) > 0:
                        tokenized_input, letter_buffer = save_constants(tokenized_input, letter_buffer)

                    # check for unary minus
                    if symbol == "-" and (
                            i == 0 or (i > 1 and input_string.replace(" ", "")[i - 1] in operators + ["("])):
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
        # print(*[i.t_type for i in tokenized_input], sep=' ')
        # print(*[i.t_value for i in tokenized_input], sep='')
        return tokenized_input

    def sort_machine_algo(self, parsed_tokens: list[CalculatorToken]):
        queue = []
        stack = []
        for token in parsed_tokens:
            # print(f"token: {token.t_value}")
            # print("queue:", end=" ")
            # print([item.t_value for item in queue], sep=" ")
            # print("stack:", end=" ")
            # print([item.t_value for item in stack], sep=" ")
            # print()
            match token.t_type:
                case "Digit":
                    queue.append(token)

                case "Function":
                    if token.t_value == "!":
                        queue.append(token)
                    else:
                        stack.append(token)

                case "OpenBracket":
                    stack.append(token)

                case "CloseBracket":
                    try:
                        while stack[-1].t_type != "OpenBracket":
                            queue.append(stack.pop())
                        else:
                            stack.pop()
                        if len(stack) > 0 and stack[-1].t_type == "Function":
                            queue.append(stack.pop())
                    except IndexError as err:
                        raise CalculatorException(
                            f"в выражении либо неверно поставлен разделитель, либо не согласованы скобки - {err}")

                case "Separator":
                    try:
                        while stack[-1].t_type != "OpenBracket":
                            queue.append(stack.pop())
                    except IndexError as err:
                        raise CalculatorException(
                            f"Проблема с разделителем - вероятно, использована десятичная запятая вместо точки!")
                case "Operator":
                    while len(stack) > 0 and stack[-1].t_type == "Operator" and stack[
                        -1].t_priority >= token.t_priority:
                        queue.append(stack.pop())
                    stack.append(token)

        while len(stack) > 0:
            temp = stack.pop()
            if temp.t_type != "Operator":
                raise CalculatorException("в выражении не согласованы скобки")
            else:
                queue.append(temp)
        return queue
