class SimpleCalc:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1/value2

    def percentage(self, value1, value2):
        return (value1/value2)*100

    def convert_cm_to_m(self, value1):
        return value1 * 0.01

    def dob(self, age):
        year = 2022 - age
        return year