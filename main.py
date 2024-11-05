from model import Model
from presenter import Presenter
from view import View

if __name__ == "__main__":
    view = View()
    model = Model()
    presenter = Presenter(view, model)

    view.init_gui(presenter)
    #view.set_output("calculate>")
    view.window.mainloop()
# todo: add expression to calculator
# todo: number buttons for calculator
# todo: expression parser to calculator
# todo: saving expression when fails
# todo: user-friendly errors
# todo: calculator ui rework
# todo: lab 4
