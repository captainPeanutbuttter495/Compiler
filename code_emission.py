from assembly_nodes import Mov, Ret, Imm, Register

def emit_program(program, output_path):
    with open(output_path, "w") as f:

        emit_function(program.function, f)
        f.write('.section .note.GNU-stack,"",@progbits\n')

def emit_function(func, f):
    f.write(f".globl {func.name}\n")
    f.write(f"{func.name}:\n")

    for instruction in func.instructions:
        f.write(f"    {emit_instruction(instruction)}\n")

def emit_instruction(instr):
    if isinstance(instr, Mov):
        src_text = emit_operand(instr.src)
        dst_text = emit_operand(instr.dst)
        return f"movl {src_text}, {dst_text}"
    if isinstance(instr, Ret):
        return "ret"

def emit_operand(op):
    if isinstance(op, Imm):
        return "$" + str(op.value)

    if isinstance(op, Register):
        return "%eax"
