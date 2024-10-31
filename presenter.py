import tkinter

from model import Model
from view import View


class CalculatorException(Exception):
    pass


class Presenter:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def parse_input(self, input_string: str) -> list:
        """
        Parsing calculator input string to list
        :param input_string: string with expression to calculate
        :return: list of parsed input_string into nums and operators
        """
        expression_splitted = []
        buff = ""
        # flag not to split first operation character like minus in "-2"
        first_flag = False
        for item in "".join(input_string.split()):
            if item in list(self._model.operations.keys()) and first_flag:
                if buff:
                    expression_splitted.append(buff)
                expression_splitted.append(item)
                buff = ""
            else:
                buff += item
                first_flag = True
        # saving buff if need
        if buff:
            expression_splitted.append(buff)
        return expression_splitted

    def check_input(self, parsed_command: list) -> bool:
        """
        Validating input
        :param parsed_command: list of parsed input_string into nums and operators
        :return: boolean value if input is valid
        """
        if len(parsed_command) != 3 or parsed_command[1] not in list(self._model.operations.keys()):
            self._view.display_error("Invalid input\n")
            return False
        try:
            for i, num in enumerate(parsed_command):
                if i != 1:
                    if "." in num or "," in num:
                        parsed_command[i] = float(num.replace(",", "."))
                        if abs(parsed_command[i]) < 10 ** -6:
                            raise CalculatorException("Small number exception!")
                    else:
                        parsed_command[i] = int(num)
            return True
        except Exception as e:
            self._view.display_error(str(e))
            return False

    def execute(self):
        """
        Function to execute calculator app
        """
        # get expression string from view
        input_string = self._view.get_input()
        self._view.entry.delete(0, tkinter.END)
        self._view.set_output("calculate>")
        # parse expression string
        parsed_command = self.parse_input(input_string)

        # validating parsed command
        if self.check_input(parsed_command):
            try:
                result = self._model.calculate(parsed_command[0], self._model.operations[parsed_command[1]],
                                               parsed_command[2])
                self._view.set_output(str(result) + "\n")
            except Exception as err:
                self._view.display_error(str(err))
