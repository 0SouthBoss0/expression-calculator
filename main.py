from model import Model
from presenter import Presenter
from view import View

if __name__ == "__main__":
    view = View()
    model = Model()
    presenter = Presenter(view, model)

    # view.init_gui(presenter)
    # view.set_output("calculate>")
    # view.window.mainloop()
    # in_str = input()

    # tokens = presenter.input_tokenize(in_str)
    # print([item.t_type for item in tokens], sep=" ")
    # print([item.t_value for item in tokens], sep=" ")
    # print()
    #
    # parsed = presenter.sort_machine_algo(tokens)
    # print([item.t_type for item in parsed], sep=" ")
    # print(" ".join([item.t_value for item in parsed]))
    #
    # print()
    # print(presenter.evaluate(parsed))

    print(presenter.solve(input()))

# todo: add expression to calculator
# todo: number buttons for calculator
# todo: expression parser to calculator
# todo: saving expression when fails
# todo: user-friendly errors
# todo: calculator ui rework
# todo: lab 4
