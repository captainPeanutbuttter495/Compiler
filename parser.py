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

# parse C program structure
# build a function node and a body
# generate formal grammer line by line
def parse_function(tokens):
    expect(tokens, "KEYWORD", "int")
    name_token = expect(tokens, "IDENT")
    expect(tokens, "LPAREN")
    expect(tokens, "KEYWORD", "void")
    expect(tokens, "RPAREN")
    expect(tokens, "LBRACE")

    body = parse_statement(tokens)

    expect(tokens, "RBRACE")
    expect(tokens, "BITWISE")
    expect(tokens, "NEGATE")

    return Function(name_token.value, body)

def expect(tokens, expected_type, expected_value=None):
    # checks that a token exists
    if not tokens:
        raise SyntaxError(f"Unexpected end of input")

    token = tokens[0]

    # checks its type and match expectatoin
    if token.type != expected_type:
        raise SyntaxError(f"Expected {expected_type}, but got {token.type}")

    if expected_value is not None and token.value != expected_value:
        raise SyntaxError(f"Expected {expected_value!r}, but got {token.value!r}")


    # removes token from the list and returns it
    return tokens.pop(0)

# implement grammer rule
def parse_statement(tokens):

    # expect "return" keyword
    expect(tokens, "KEYWORD", "return")

    # parse the expression
    expr = parse_exp(tokens)

    # expect semicolon
    expect(tokens, "SEMICOLON")

    # return a Return AST node wrapping the expression
    return Return(expr)

def parse_exp(tokens):
    next_token = peek(tokens)

    if next_token.type == "CONSTANT":
        token = take_token(tokens) # remove from token list
        value = int(token.value) # convert string -> integer
        return Constant(value) # return AST node

    # checks for negation or bitwise operators
    elif next_token.type == "NEGATION" or next_token.type == "BITWISE":
        # removes operator token from token list
        token = take_token(tokens) 

        # stores operator type as string
        operator = token.type

        # recursively parses operand
        parse_exp(token)

        # creates and returns Unary AST node
        return Unary(operator, expr)

    elif next_token.type == "LPAREN":
        # takens in Left parenthesis
        take_token(tokens)
        parse_exp(token)
        expect(tokens, "RPAREN")
        return expr

    # reject inputs such as --2
    elif next_token.type == "DECREMENT":
        raise SyntaxError("Unsupported operator '--'")

    # if token doesn't match any valid form of <exp> give an error
    else:
        raise SyntaxError("Malformed expression")


