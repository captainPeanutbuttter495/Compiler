def emit_program(program, output_path):
    with open(output_path, "w") as f:

        emit_function(program.function, f)

def emit_function(func, f):
    f.write(f".globl {func.name}\n")
    f.write(f"{func.name}:\n")

    for instruction in func.instructions:
            f.write(f"    {emit_instruction(instruction)}\n")
