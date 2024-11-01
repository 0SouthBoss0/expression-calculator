import unittest
import presenter, model, view


class TestSolver(unittest.TestCase):
    def setUp(self) -> None:
        self.model = model.Model()
        self.view = view.View()
        self.presenter = presenter.Presenter(self.view, self.model)

    def test_ordinary(self):
        self.assertEqual(self.presenter.solve("2+2"), 4.0)

    def test_long(self):
        self.assertAlmostEqual(self.presenter.solve(
            "15/(7-(1+1))*3-(2+(1+1))*15/(7-(200+1))*3-(2+(1+1))*(15/(7-(1+1))*3-(2+(1+1))+15/(7-(1+1))*3-(2+(1+1)))"),
            -30.0721649)

        self.assertAlmostEqual(self.presenter.solve(
            "15/(7-(1+1))*3-(2+(1+1))*15/(7-(200+1))*3-(2+(1+1))(15/(7-(1+1))*3-(2+(1+1))+15/(7-(1+1))*3-(2+(1+1)))"),
            -30.0721649)

    def test_triginometric(self):
        self.assertAlmostEqual(self.presenter.solve(
            "(sin(2π * (3 + (4 / (5 - 2)))) ^ 2) / (1 + (sin(π / 4)) ^ 3)"), 0.55409709)
        self.assertAlmostEqual(self.presenter.solve(
            "(sin(3 * (2^3 - 5))) ^ (1 / 2) + (sin(π / 6) ^ (1 / 3))"), 1.43566507737)
        self.assertAlmostEqual(self.presenter.solve(
            "(sin(π / 2) * (1 + (sin(π / 3)) ^ 2)) / ((sin(π / 4)) ^ 2 + (sin(π / 6)) ^ 2)"), 2.33333333333)
        self.assertAlmostEqual(self.presenter.solve(
            "((2^3 - 5) ^ (1 / 2) * (sin(π / 4) + sin(π / 6))) / (1 + (sin(π / 2)) ^ 2)"), 1.04538513)
        self.assertAlmostEqual(self.presenter.solve(
            "(sin((2 + (3 * (sin(π / 3)) ^ 2)) / (4 + (sin(π / 4)) ^ 2))) ^ 3"), 0.531778430)
