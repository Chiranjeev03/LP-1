# Initialize symbol table
symbol_table = {}

# Read the symbol table created in Pass 1
with open("symbol_table.txt", "r") as symbol_file:
    for line in symbol_file:
        if ":" in line:
            symbol, address = line.strip().split(": ")
            symbol_table[symbol] = int(address)

# Sample assembly code with references to symbols
assembly_code = [
    "LDA X",
    "ADD Y",
    "STA Z",
    "HLT",
]

# Initialize output machine code
machine_code = []

# Pass 2: Generate machine code
for line in assembly_code:
    tokens = line.split()

    if tokens[0] == "LDA":
        opcode = "00"
        operand = str(symbol_table[tokens[1]])
    elif tokens[0] == "ADD":
        opcode = "01"
        operand = str(symbol_table[tokens[1]])
    elif tokens[0] == "STA":
        opcode = "02"
        operand = str(symbol_table[tokens[1]])
    elif tokens[0] == "HLT":
        opcode = "03"
        operand = "000"

    # Combine opcode and operand to create machine code instruction
    machine_instruction = opcode + operand

    # Add the machine instruction to the output
    machine_code.append(machine_instruction)

# Display the generated machine code
print("Machine Code:")
for instruction in machine_code:
    print(instruction)

