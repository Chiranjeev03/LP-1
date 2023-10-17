# Initialize symbol table
symbol_table = {}

# Initialize intermediate code
intermediate_code = []

# Read macro definitions from a file
with open("macro_definitions.txt", "r") as macro_file:
    macro_definitions = {}
    current_macro = None

    for line in macro_file:
        line = line.strip()
        if line.startswith("MACRO"):
            current_macro = line.split()[1]
            macro_definitions[current_macro] = {"parameters": [], "body": []}
        elif current_macro:
            if line.startswith("MEND"):
                current_macro = None
            else:
                if line:
                    macro_definitions[current_macro]["body"].append(line)
        elif line:
            # Handle non-macro symbol definitions (if any)
            symbol, address = line.split()
            symbol_table[symbol] = address

# Read assembly code from another file
with open("assembly_code.txt", "r") as assembly_file:
    assembly_code = assembly_file.readlines()

# Pass 1: Expand macros, build symbol table, and generate intermediate code
for line in assembly_code:
    line = line.strip()
    tokens = line.split()

    if tokens[0] in macro_definitions:
        macro_name = tokens[0]
        parameters = tokens[1].split(',')
        macro_body = macro_definitions[macro_name]["body"]

        # Replace macro parameters with actual values
        for i, parameter in enumerate(parameters):
            macro_body = [instruction.replace(macro_definitions[macro_name]["parameters"][i], parameter) for instruction in macro_body]

        intermediate_code.extend(macro_body)
    else:
        # Handle non-macro instructions
        intermediate_code.append(line)

# Display intermediate code
print("Intermediate Code:")
for instruction in intermediate_code:
    print(instruction)
