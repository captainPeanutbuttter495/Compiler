from assembly_nodes import Program
from assembly_nodes import Imm, Register, Mov, Ret, Function, Program

# entry point for code gen phase
# takes C AST root node from ast_node class
def generate_program(c_ast_program):
    # extracts C AST function node
    c_function = c_ast_program.function

    # calls next codegen function and passes in the C AST function node
    asm_function = generate_function(c_function)

    # return new assembly AST Programe node
    # this is the root of assembly program
    return Program(asm_function)

# takes C AST Function node
def generate_function(c_func):

    # extracts a string
    name = c_func.name

    # extracts a Return node
    body = c_func.body

    # converts return statement into a list of assembly instructions
    instructions = generate_statement(body)

    # returns an assembly_nodes. Function node
    return Function(name, instructions)

# Converts a Return AST node into assembly instructions
# Emits a mov from expression into %eax, followed by ret
def generate_statement(stmt):
    expression = stmt.value
    src_operand = generate_exp(expression)
    dst_operand = Register()

    mov_instr = Mov(src_operand, dst_operand)
    ret_instr = Ret()

    return [mov_instr, ret_instr]

# converts a Constant expression into an Imm operand for assembly
def generate_exp(exp):
    return Imm(exp.value)
