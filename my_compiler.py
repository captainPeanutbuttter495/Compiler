#!/usr/bin/env python3
import sys
import shutil
import tempfile
import os
import subprocess
from lexer import tokenize, Token, TOKEN_PATTERNS
from parser import parse_program
from assembly_generation import generate_program


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

            tokens = tokenize(source)
            for token in tokens:
                print(token)
            sys.exit(0)

        if "--parse" in flags:
            with open(preprocessed_file) as f:
                source = f.read()

            tokens = tokenize(source)
            parse_program(tokens)
            sys.exit(0)

        if "--codegen" in flags:
            with open(preprocessed_file) as f:
                source = f.read()

            tokens = tokenize(source)
            c_ast = parse_program(tokens)
            asm_ast = generate_program(c_ast)
            sys.exit(0)


        s_file = compile(preprocessed_file, tmp_dir)
        output_file = os.path.splitext(input_file)[0]
        assemble_link(s_file, output_file)
        print("[INFO] Done! Can now run executable")

if __name__ == "__main__":
    main()
