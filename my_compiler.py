#!/usr/bin/env python3
import sys
import shutil
import tempfile
import os
import subprocess
from lexer import tokenize, Token, TOKEN_PATTERNS
from assembly_generation import generate_program
from code_emission import emit_program
from parser import parse_program

def preprocesses(input_file, tmp_dir):
    i_path = os.path.join(tmp_dir, "output.i")

    # Run the preprocessor
    try:
        subprocess.run(
                ["gcc", "-E", "-P", input_file, "-o", i_path],
                check=True
                )
    except subprocess.CalledProcessError:
        print("[Error] Preprocessing failed.")
        sys.exit(1)

    print(f"Preprocessed file written to: {i_path}")
    return i_path


def compile(preprocessed_file, tmp_dir):
    s_path = os.path.join(tmp_dir, "output.s")

    try:
        shutil.copyfile("hello.s", s_path)

    except FileNotFoundError:
        print("[Error] Missing hello.s placeholder.")
        sys.exit(1)


    print(f"[OK] Simulated assembly written to: {s_path}")
    return s_path


def assemble_link(s_file, output_file):
    try:
        subprocess.run(
                ["gcc", s_file, "-o", output_file],
                check=True
                )
    except subprocess.CalledProcessError:
        print("[Error] Assembly/linking failed.")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: my_compiler.py [--lex] <source_file.c>")
        sys.exit(1)

    flags = [arg for arg in sys.argv[1:] if arg.startswith("--")]
    input_files = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if len(input_files) != 1:
        print("Error: Provide only one input .c file")
        sys.exit(1)

    input_file = input_files[0]

    with tempfile.TemporaryDirectory() as tmp_dir:
        preprocessed_file = preprocesses(input_file, tmp_dir)

        if "--lex" in flags:
            with open(preprocessed_file) as f:
                source = f.read()

            try:
                tokens = tokenize(source)
            except SyntaxError as e:
                print(f"[Error] {e}", file=sys.stderr)
                sys.exit(1)

            for token in tokens:
                print(token)
            sys.exit(0)


        if "--parse" in flags:
            with open(preprocessed_file) as f:
                source = f.read()

            try:
                tokens = tokenize(source)
                parse_program(tokens)
            except (SyntaxError, Exception) as e:
                print(f"[Error] {e}", file=sys.stderr)
                sys.exit(1)

            sys.exit(0)


        if "--codegen" in flags:
            with open(preprocessed_file) as f:
                source = f.read()

            try:
                tokens = tokenize(source)
                c_ast = parse_program(tokens)
                asm_ast = generate_program(c_ast)
                output_path = os.path.splitext(input_file)[0] + ".s"
                emit_program(asm_ast, output_path)
                print(f"[OK] Assembly written to {output_path}")
                sys.exit(0)

            except (SyntaxError, Exception) as e:
                print(f"[Error] {e}", file=sys.stderr)
                sys.exit(1)


        try:
            tokens = tokenize(open(preprocessed_file).read())
            c_ast = parse_program(tokens)
            asm_ast = generate_program(c_ast)

            s_file = os.path.join(tmp_dir, "output.s")
            emit_program(asm_ast, s_file)

            output_file = os.path.splitext(input_file)[0]
            assemble_link(s_file, output_file)

            print("[INFO] Done! Can now run executable")
            sys.exit(0)

        except (SyntaxError, Exception) as e:
            print(f"[Error] {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
