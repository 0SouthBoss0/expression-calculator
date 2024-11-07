import sys

sys.path.append("D:\pyprj\expression-calculator")

from model import Model
from view import View
from presenter import Presenter


def before_all(context):
    context.view = View()
    context.model = Model()
    context.presenter = Presenter(context.view, context.model)
    context.view.init_gui(context.presenter)
