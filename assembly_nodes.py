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
        return f"Function(\n name={repr(self.name)},\n instructions={repr(self.instructions)}\n)"

# 'mov' instruction in x64 assembly
# copies a value from src to dist
class Mov:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __repr__(self):
        return f"Mov(\n src={repr(self.src)},\n dst={repr(self.dst)}\n)"

# represents a constant operand
# used as the source in 'mov' instruction
class Ret:
    def __init__(self):
        pass

    def __repr__(self):
        return "Ret()"

class Imm:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Imm({repr(self.value)})"

# represents the %eax register in x64 assembly
# used as the destination in 'mov' instructions
class Register:
    def __init__(self):
        pass

    def __repr__(self):
        return "Register()"
