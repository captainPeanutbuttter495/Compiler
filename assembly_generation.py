from assembly_nodes import Program

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
