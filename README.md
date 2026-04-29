# Skip
==Sikp Ver 0.1==<br>
Skip Language Engine
Skip is a lightweight, YAML-based scripting engine powered by Python. It's designed to be intuitive, readable, and highly extensible, making it perfect for rapid prototyping, CLI tools, and text-based adventures.
Key Features
YAML-Native: Write your logic using clean, structured YAML syntax.
Dynamic Evaluation: Support for f-string style variable expansion (e.g., {var_name}) <br>
Built-in Coloring: Easily add flair to your console output with ANSI color constants.
Modular Design: Define reusable blocks with def and execute them with call.
Persistence: Save and load your session variables effortlessly using the .skp format.
Getting Started
Prerequisites
Python 3.x
PyYAML (pip install pyyaml)
Installation
Clone this repository and ensure skip.py (or the compiled skip.pyc) is in your working directory.
Running a Script
Execute your .skp files using the Skip interpreter:
bash
python skip.py your_script.skp
Syntax Example (demo.skp)
# Define a reusable function
- def:<br>
    name: "greet"<br>
    do:<br>
      - println: "{C.Y}--------------------{C.END}"<br>
      - println: "  Hello, {name}!"<br>
      - println: "{C.Y}--------------------{C.END}"<br>

# Set a variable and call the function
- var: { name: "Explorer" }<br>
- call: "greet"<br>

# Perform a calculation
- clc: "10 * 5 + 5"
- println: "{C.G}Calculation Result: {res}{C.END}"
# Command
| Command | Description | Example |
| :--- | :--- | :--- |
| `println` | Print to console | `println: "Hi {user}"` |
| `typetext` | Animated typing effect | `typetext: "Loading..."` |
| `var` | Define/Update variables | `var: { hp: 100 }` |
| `clc` | Evaluate math | `clc: "hp - 10"` |
| `def` | Define a function | `def: { name: "f", do: [] }` |
| `call` | Invoke a function | `call: "f"` |
| `adopt` | Import another .skp | `adopt: "lib_module"` |
| `save` | Save variables | `save: { file: "save1", vars: ["hp"] }` |
| `exit` | Terminate script | `exit: ""` |
| `input` | Get user input and store in variable | `input: "user_name"` |
