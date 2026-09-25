class Calculator:
    def __init__(self):
        self.operators = '+-*/'
    def calc(self, data: str):
        data = self.input(data)

        if data[1] == self.operators[0]:
            return data[0] + data[2]

        elif data[1] == self.operators[1]:
            return data[0] - data[2]

        elif data[1] == self.operators[2]:
            return data[0] * data[2]

        elif data[1] == self.operators[3]:
            return data[0] / data[2]

    def input(self, data: str):
        data = data.split(" ")

        if len(data) != 3:
            raise ValueError
        if data[1] not in self.operators:
            raise ValueError

        return [int(data[0]), data[1], int(data[2])]




