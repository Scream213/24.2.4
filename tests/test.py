from app.calculator import Calculator


class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_multiply(self):
        # Позитивный тест для умножения
        assert self.calc.multiply(2, 3) == 6

    def test_division(self):
        # Позитивный тест для деления
        assert self.calc.division(6, 3) == 2

    def test_subtraction(self):
        # Позитивный тест для вычитания
        assert self.calc.subtraction(5, 3) == 2

    def test_adding(self):
        # Позитивный тест для сложения
        assert self.calc.adding(2, 3) == 5
