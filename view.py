import tkinter as tk
import tkinter.messagebox


class View:
    def __init__(self):
        self.result_label = None
        self.calculate_button = None
        self.entry = None
        self.window = None
        self._presenter = None

    def init_gui(self, presenter):
        self._presenter = presenter
        # Создаем главное окно
        self.window = tk.Tk()
        self.window.title("Калькулятор")

        # Создаем строку ввода
        self.entry = tk.Entry(self.window, width=25)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Создаем кнопки цифр
        button_list = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]
        row = 1
        col = 0
        for button_text in button_list:
            button = tk.Button(self.window, text=button_text, width=5,
                               command=lambda text=button_text: self.entry.insert(tk.END, text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 4:
                row += 1
                col = 0

        # Создаем кнопку "Вычислить"
        self.calculate_button = tk.Button(self.window, text="Вычислить", command=self._presenter.execute)
        self.calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Создаем кнопку "Очистить"
        self.clear_button = tk.Button(self.window, text="Очистить", command=self.entry.delete, width=5)
        self.clear_button.grid(row=5, column=2, columnspan=2, padx=10, pady=10)

        # Создаем кнопки тригонометрических функций
        trig_button_list = ["sin(", "cos(", "tg(", "ctg("]
        row = 6
        col = 0
        for button_text in trig_button_list:
            button = tk.Button(self.window, text=button_text, width=5,
                               command=lambda text=button_text: self.entry.insert(tk.END, text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 4:
                row += 1
                col = 0

        # Создаем метку для вывода результата
        self.result_label = tk.Label(self.window, text="", font=("Arial", 16))
        self.result_label.grid(row=7, column=0, columnspan=5, padx=10, pady=10)

        # Создаем кнопки арифметических операций
        button_list = ["+", "-", "*", "/", "^", "%"]
        row = 2
        col = 4
        for button_text in button_list:
            button = tk.Button(self.window, text=button_text, width=5,
                               command=lambda text=button_text: self.entry.insert(tk.END, text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 8:
                row += 1
                col = 4

        self.window.resizable(False, False)

    def set_output(self, output):
        self.result_label.config(text=output)

    def get_input(self):
        return self.entry.get()

    def display_error(self, error):
        tkinter.messagebox.showerror("Ошибка!", error)
