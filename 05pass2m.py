import re

# Sample source code with macros
source_code = """
START 100
MCR ADDMACRO X, Y
X EQU 10
Y EQU 20
LDA X
MCR SUBMACRO X, Y
STOP
ADDMACRO MACRO A, B
    ADD A, B
    MEND
SUBMACRO MACRO A, B
    SUB A, B
    MEND
"""

# Define the macro table
macro_table = {
    "ADDMACRO": {
        "parameters": ["A", "B"],
        "body": ["ADD A, B"]
    },
    "SUBMACRO": {
        "parameters": ["A", "B"],
        "body": ["SUB A, B"]
    }
}

# Define a dictionary for equates
equates = {}

# Pass 2: Expand macros and generate code
lines = source_code.split('\n')
output_code = []

for line in lines:
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    # Split the line into tokens
    tokens = re.split(r'[ ,]+', line)

    # Check if it's a macro call
    if tokens[0] in macro_table:
        macro_name = tokens[0]
        macro = macro_table[macro_name]

        # Check if the number of arguments matches
        if len(tokens[1:]) != len(macro["parameters"]):
            print(f"Error: Number of arguments in {macro_name} does not match the definition.")
            continue

        # Replace parameters in the macro body
        macro_body = macro["body"][:]
        for i in range(len(macro["parameters"])):
            macro_parameter = macro["parameters"][i]
            macro_body = [line.replace(macro_parameter, tokens[i + 1]) for line in macro_body]

        # Add the expanded macro to the output code
        output_code.extend(macro_body)
    else:
        # Handle equates
        for i in range(len(tokens)):
            if tokens[i] in equates:
                tokens[i] = equates[tokens[i]]
        output_code.append(" ".join(tokens))

# Print the expanded code
for line in output_code:
    print(line)
