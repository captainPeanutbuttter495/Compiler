class Program:
    def __init__(self, function):
        self.function = function

    def __repr__(self):
        return f"Program(\n {repr(self.function)}\n)"

class Function:
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def __repr__(self):
        return f"Function(\n name={repr(self.body)},\n body={repr(self.body)}\n"

class Return:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Return(\n value={repr(self.value)}\n)"

class Constant:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Constant({repr(self.value)})"

class Unary:
    def __init__(self, operator, expr):
        self.value = operator
        self.function = expr

    def __repr__(self):
        return f"Unary(\n operator={repr(self.operator)},\n expr={repr(self.expr)}\n)"
