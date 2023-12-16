import math
import random

class Calculator:
    def __init__(self, first_operand, second_operand):
        self.first_operand = first_operand
        self.second_operand = second_operand

    def add(self):
        return self.first_operand + self.second_operand

    def subtract(self):
        return self.first_operand - self.second_operand

    def multiply(self):
        return self.first_operand * self.second_operand

    def divide(self):
        if self.second_operand != 0:
            return self.first_operand / self.second_operand
        else:
            return "Ділення на 0 неможливе"

    def power(self):
        return math.pow(self.first_operand, self.second_operand)

    @staticmethod
    def random_number(a, b):
        return random.uniform(a, b)