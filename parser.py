from ast_nodes import Program, Function, Return, Constant
from lexer import Token  

# call parse_function
# returns a Program AST node wrapping the result
# Entry point of parser to parse a C program
def parse_program(tokens):
    # parse the only function in the program
    function_node = parse_function(tokens)

    # after parsing function, no tokens should be left
    # if any tokens remain, give error message
    if tokens:
        raise SyntaxError(f"Unexpected token: { tokens[0]}")

    # wrap function node in a Program node and return the AST root
    return Program(function_node)
