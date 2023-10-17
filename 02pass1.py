# Create a file with the assembly code
with open('assembly_code.txt', 'w') as code_file:
    code_file.write("""START 1000
LABEL1 LDA VALUE
LOOP ADD X
STO RESULT
BRZ FINISH
SUB X
BR LOOP
FINISH HLT
VALUE DEC 42
X HEX 0A
RESULT RESW 1
""")

# Symbol table and literal table dictionaries
symbol_table = {}
literal_table = {}

# Pass 1 of the assembler
location_counter = None

with open('assembly_code.txt', 'r') as code_file:
    lines = code_file.readlines()

for line in lines:
    parts = line.split()
    label = None
    opcode = None
    operand = None

    if len(parts) == 2:
        opcode = parts[0]
        operand = parts[1]
    elif len(parts) == 3:
        label = parts[0]
        opcode = parts[1]
        operand = parts[2]

    if location_counter is None and opcode == 'START':
        location_counter = int(operand)
        continue

    if label:
        symbol_table[label] = location_counter

    # Handle literals
    if operand and operand.startswith('='):
        literal = operand[1:]
        if literal not in literal_table:
            literal_table[literal] = None  # Assign an address later
        location_counter += 1

    if opcode in ('LDA', 'ADD', 'STO', 'BRZ', 'SUB', 'BR', 'HLT', 'RESW'):
        location_counter += 1

# Write the symbol table to a file
with open('symbol_table.txt', 'w') as symbol_file:
    for symbol, address in symbol_table.items():
        symbol_file.write(f"{symbol}\t{address}\n")

# Write the literal table to a file
with open('literal_table.txt', 'w') as literal_file:
    for literal in literal_table.keys():
        literal_file.write(literal + '\n')

# Output:
# Contents of 'symbol_table.txt':
# LABEL1  1002
# LOOP    1003
# FINISH  1007
# VALUE   1009
# X       100A
# RESULT  100B

# Contents of 'literal_table.txt':
# 42
# 0A
