import unittest
from unittest.mock import patch, MagicMock, Mock, call

from model import Model
from presenter import Presenter
from view import View
from model import CalculatorToken
from model import CalculatorException


class TestModel(unittest.TestCase):
    def setUp(self) -> None:
        self.model = Model()

    def test_input_tokenize(self):
        self.assertEqual(self.model.input_tokenize("2+2"),
                         [CalculatorToken("Digit", "2"), CalculatorToken("Operator", "+"),
                          CalculatorToken("Digit", "2")])

    def test_sort_machine_algo(self):
        self.assertEqual(self.model.sort_machine_algo(
            [CalculatorToken("Digit", "2"), CalculatorToken("Operator", "+"), CalculatorToken("Digit", "2")]),
            [CalculatorToken("Digit", "2"), CalculatorToken("Digit", "2"),
             CalculatorToken("Operator", "+")])

    def test_evaluate(self):
        self.assertEqual(self.model.evaluate([CalculatorToken("Digit", "2"), CalculatorToken("Digit", "2"),
                                              CalculatorToken("Operator", "+")]), 4)
        with self.assertRaises(CalculatorException):
            self.model.evaluate([CalculatorToken("Digit", "2"), CalculatorToken("Operator", "+")])


class TestPresenter(unittest.TestCase):
    def setUp(self):
        self._view = Mock()
        self._model = Mock()
        self._presenter = Presenter(self._view, self._model)

    def test_execute(self):
        """
        Testing execute function of presenter with no errors
        """
        self._view.get_input = MagicMock(return_value="2+4")
        self._view.set_output = MagicMock()
        self._model.input_tokenize = MagicMock(
            return_value=[CalculatorToken("Digit", "2"), CalculatorToken("Operator", "+"),
                          CalculatorToken("Digit", "4")])
        self._model.sort_machine_algo = MagicMock(
            return_value=[CalculatorToken("Digit", "2"), CalculatorToken("Digit", "4"),
                          CalculatorToken("Operator", "+")])
        self._model.evaluate = MagicMock(return_value=6)

        self._presenter.execute()

        self._model.input_tokenize.assert_called_once_with("2+4")
        self._model.sort_machine_algo.assert_called_once_with(
            [CalculatorToken("Digit", "2"), CalculatorToken("Operator", "+"), CalculatorToken("Digit", "4")])
        self._model.evaluate.assert_called_once_with(
            [CalculatorToken("Digit", "2"), CalculatorToken("Digit", "4"), CalculatorToken("Operator", "+")])
        self._view.set_output.assert_has_calls([call("Результат вычисления"), call("6")])

    # def test_execute_divide_zero_error(self):
    #     """
    #     Testing execute function of presenter with ZeroDivisionError
    #     """
    #     self._view.display_error = MagicMock()
    #     self._view.get_input = MagicMock(return_value="2/0")
    #     self._model.calculate = MagicMock(side_effect=ZeroDivisionError("ZeroDivisionError"))
    #
    #     self._presenter.execute()
    #
    #     self._view.get_input.assert_called_once_with()
    #     self._view.display_error.assert_called_with("ZeroDivisionError")
    #
    # def test_execute_small_number_error(self):
    #     """
    #     Testing execute function of presenter with small number exception
    #     """
    #     self._view.display_error = MagicMock()
    #     self._view.get_input = MagicMock(return_value="0.000000008+1")
    #
    #     self._presenter.execute()
    #
    #     self._view.get_input.assert_called_once_with()
    #     self._view.display_error.assert_called_with("Small number exception!")


class TestView(unittest.TestCase):

    def setUp(self):
        self._view = View()
        self._model = Mock()
        self._presenter = Mock(self._view, self._model)
        self._presenter.execute = Mock()
        self._view.init_gui(self._presenter)  # Инициализация GUI для теста

    @patch('tkinter.messagebox.showerror')
    def test_display_error(self, mock_showerror):
        """
        Testing display_error function in view
        :param mock_showerror: tkinter.messagebox.showerror mock
        """
        error_message = "Произошла ошибка!"
        self._view.display_error(error_message)
        mock_showerror.assert_called_once_with("Ошибка!", error_message)

    def test_set_output(self):
        """
        Testing set_output function in view
        """
        message_to_output = "Message to output!"
        self._view.set_output(message_to_output)
        self.assertEqual(self._view.result_label.cget("text"), message_to_output)

    def test_init_gui(self):
        """
        Testing init_gui function in view
        """
        self.assertIsNotNone(self._view._presenter)
        self.assertIsNotNone(self._view.window)
        self.assertEqual(self._view.window.title(), "Калькулятор")
        self.assertIsNotNone(self._view.entry)
        self.assertIsNotNone(self._view.calculate_button)
        self.assertIsNotNone(self._view.result_label)

    def test_get_input(self):
        """
        Testing get_input function in view
        """
        message = "Message to get"
        self._view.entry.insert(0, message)
        self.assertEqual(self._view.get_input(), message)

    def tearDown(self):
        self._view.window.destroy()  # Очистка окна после каждого теста
