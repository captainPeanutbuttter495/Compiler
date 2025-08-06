A C compiler built in Python. This project walks through the early stages of compiler design, from lexing to code emission, generating valid x86 assembly from C source files.

🚀 Features Implemented

* Lexical analysis (tokenizer)

* Recursive descent parser for a simplified C grammar

* AST generation for valid C input

* Code generation into x86 assembly AST

* x86 assembly emission using AT&T syntax

* End-to-end driver pipeline to compile and execute C files with a return value

📁 File Structure


my_compiler.py         # Compiler driver 

lexer.py               # Tokenizer 

parser.py              # Parser that builds a C AST

assembly_nodes.py      # Data structures for assembly AST

assembly_generation.py # Generates assembly AST from C AST

code_emission.py       # Outputs x86 assembly to file

test.c                 # Sample input file to compile

💻 Example Input

Here is a simple C program the compiler accepts:

int main(void) {
    return 42;
}

⚙️ How to Use (Linux / WSL)

✅ 1. Install Prerequisites

You need:

Python 3.10+

GCC (for assembling and linking)

Ubuntu / WSL:

sudo apt update
sudo apt install build-essential python3

📥 2. Clone and Compile

git clone https://github.com/captainPeanutbuttter495/Compiler.git

cd Compiler

python3 my_compiler.py test.c

If successful:

Preprocessed file written to: /tmp/tmpabc123/output.i
[INFO] Done! Can now run executable

▶️ 3. Run the Output Program

./test
# Check return code
echo $?


Compilation

$ python3 my_compiler.py test.c

Preprocessed file written to: /tmp/tmpabc123/output.i

[INFO] Done! Can now run executable

Execution

$ ./test

$ echo $?

42

📌 Supported C Subset

Only supports int main(void)

Single return <constant>; statement inside main



This project demonstrates compiler fundamentals and shows how languages are parsed and translated. It covers: 

Compiler phases

ASTs

x86 assembly (AT&T syntax)

System-level programming

🛠️ Future Work

Add expression parsing

Add operator support (+, -, etc.)

Implement symbol tables and type checking

Extend to more complex C programs
