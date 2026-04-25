# Skip
==Sikp Ver Beta0.1==
Skip Language Engine
Skip is a lightweight, YAML-based scripting engine powered by Python. It's designed to be intuitive, readable, and highly extensible, making it perfect for rapid prototyping, CLI tools, and text-based adventures.
Key Features
YAML-Native: Write your logic using clean, structured YAML syntax.
Dynamic Evaluation: Support for f-string style variable expansion (e.g., {var_name}).
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
- def:
    name: "greet"
    do:
      - println: "{C.Y}--------------------{C.END}"
      - println: "  Hello, {name}!"
      - println: "{C.Y}--------------------{C.END}"

# Set a variable and call the function
- var: { name: "Explorer" }
- call: "greet"

# Perform a calculation
- clc: "10 * 5 + 5"
- println: "{C.G}Calculation Result: {res}{C.END}"
Command Reference
Command	Description	Example
println	Print to console (supports {vars})	println: "Hi {user}"
typetext	Animated typing effect	typetext: "Loading..."
var	Define/Update variables	var: { hp: 100 }
clc	Evaluate math (stores result in res)	clc: "hp - 10"
def	Define a function	def: { name: "f", do: [] }
call	Invoke a function	call: "f"
adopt	Import another .skp file	adopt: "lib_module"
save	Save variables to a file	save: { file: "save1", vars: ["hp"] }
exit	Terminate the script	exit: ""
Color Constants
Use these inside println or typetext:
{C.R}: Red
{C.G}: Green
{C.Y}: Yellow
{C.B}: Blue
{C.END}: Reset color
License
This project is licensed under the MIT License.
