class Program:
    # root of assembly AST
    # wraps a single Function node
    # returns a Program node from generate_program() function
    def __init__(self, function):
        self.function = function

    def __repr__(self):
        return f"Program(\n {repr(self.function)}\n)"

# single assembly function definition
class Function:
    # stores function name and a list of assembly instructions
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

    def __repr__(self):
        return f"Function(\n name={repr(self.name)}\n instructions={repr(self.instructions)}\n)"
