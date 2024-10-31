import unittest
from unittest.mock import patch, MagicMock, Mock

from model import Model
from presenter import Presenter
from view import View


class TestModel(unittest.TestCase):
    def setUp(self):
        self._model = Model()

    def test_sum(self):
        self.assertEqual(self._model.sum_func(1, 2), 3)

    def test_sub(self):
        self.assertEqual(self._model.sub_func(3, 2), 1)

    def test_mul(self):
        self.assertEqual(self._model.mul_func(2, 3), 6)

    def test_div(self):
        self.assertEqual(self._model.div_func(6, 3), 2)

    def test_pow(self):
        self.assertEqual(self._model.pow_func(2, 3), 8)

    def test_rem_div(self):
        self.assertEqual(self._model.rem_div_func(6, 4), 2)

    def test_calculate(self):
        self.assertEqual(self._model.calculate(1, self._model.sum_func, 2), 3)
        self.assertEqual(self._model.calculate(3, self._model.sub_func, 2), 1)
        self.assertEqual(self._model.calculate(2, self._model.mul_func, 3), 6)
        self.assertEqual(self._model.calculate(4, self._model.div_func, 2), 2)
        self.assertEqual(self._model.calculate(2, self._model.pow_func, 3), 8)
        self.assertEqual(self._model.calculate(6, self._model.rem_div_func, 4), 2)


class TestPresenter(unittest.TestCase):
    def setUp(self):
        self._view = Mock()
        self._model = Mock()
        self._presenter = Presenter(self._view, self._model)

        self._model.sum_func = lambda a, b: a + b
        self._model.div_func = lambda a, b: a / b
        self._model.operations = {"+": self._model.sum_func,
                                  "/": self._model.div_func}

    def test_execute(self):
        """
        Testing execute function of presenter with no errors
        """
        self._view.get_input = MagicMock(return_value="2+4")
        self._view.set_output = MagicMock()
        self._model.calculate = MagicMock(return_value=6)

        self._presenter.execute()

        self._view.get_input.assert_called_once_with()
        self._model.calculate.assert_called_once_with(2, self._model.sum_func, 4)
        self._view.set_output.assert_called_with("6\n")

    def test_execute_divide_zero_error(self):
        """
        Testing execute function of presenter with ZeroDivisionError
        """
        self._view.display_error = MagicMock()
        self._view.get_input = MagicMock(return_value="2/0")
        self._model.calculate = MagicMock(side_effect=ZeroDivisionError("ZeroDivisionError"))

        self._presenter.execute()

        self._view.get_input.assert_called_once_with()
        self._view.display_error.assert_called_with("ZeroDivisionError")

    def test_execute_small_number_error(self):
        """
        Testing execute function of presenter with small number exception
        """
        self._view.display_error = MagicMock()
        self._view.get_input = MagicMock(return_value="0.000000008+1")

        self._presenter.execute()

        self._view.get_input.assert_called_once_with()
        self._view.display_error.assert_called_with("Small number exception!")


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
