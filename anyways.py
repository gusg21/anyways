import sys

print("Anyways Compiler ===============\n")

acc = ""
mem = [""] * 100

append = 0 # The amount of extra program loops

skipCode = False
skipElseStatement = False
skipThenStatement = False

ended = False

debug = False
path = ""
index = 0
for arg in sys.argv:

	# Input file argument
	if arg == "-i" or arg == "--input":
		try:
			path = sys.argv[index + 1]
			print("Path provided: " + sys.argv[index + 1])
		except:
			print("-i flag but no input file!")

	# Debug argument
	if arg == "-d" or arg == "--debug":
		print("debug: ON")
		debug = True

	# Help menu
	if arg == "-h" or arg == "--help":
		print("Usage:\n")
		print("-d / --debug: Show a LOT of output; only use if debugging interpreter!")
		print("-h / --help: This menu")
		print("-i / --input: Provide an input file")

		sys.exit()

	index += 1

# If we weren't given the path, prompt for it
while path == "":
	path = input("Path to file >>>")

# Read file and split at newlines
print("Reading file...")
with open(path, 'r') as myfile:
    program=myfile.read().splitlines() # program is the initial code

data = program

for line in data:
	if debug: print("line: " + line)

	if line == "Who's there?": # Else statement
		if debug: print("else: detected")
		if skipElseStatement:
			skipCode = True
		if skipThenStatement:
			skipCode = False

	if line == "Banana!": # Close if statement
		skipElseStatement = False
		skipThenStatement = False
		skipCode = False

	if not skipCode:

		# ACCUMULATOR FUNCTIONS

		if line == '"Ow!" it said.': # Print accumulator
			print(acc)

		if line[:26] == "There was this guy called ": # Set the acumulator
			if debug: print("detected: accumulator set")
			acc = line[26:]

		if line == '"What are you doing?" they said.': # Input to the accmulator
			acc = input("Input to program: ")

		# ARITHMETIC

		if line[:9] == "And then ": # Add passed variable to acc
			if line[-9:] == "happened!":
				acc = int(acc) + int(line[9:-9])
			else:
				print("*** Malform at line: '" + line + "'")

		if line[:9] == "But then ": # Subtract passed variable from acc
			if line[-9:] == "happened!":
				acc = int(acc) - int(line[9:-9])
			else:
				print("*** Malform at line: '" + line + "'")

		if line[:5] == "When ": # Multiply passed variable by acc
			if line[-9:] == "happened!":
				acc = int(acc) * int(line[5:-9])
			else:
				print("*** Malform at line: '" + line + "'")

		if line[:6] == "Until ": # Divide acc by passed variable
			if line[-9:] == "happened!":
				acc = int(acc) / int(line[6:-9])
			else:
				print("*** Malform at line: '" + line + "'")

		# IF STATEMENT

		if line[:13] == "Knock Knock, ": # If condition (opening statement)
			comp = line[13:] # Condition
			if debug: print("comp: " + comp + ", comp0: " + comp[0])
			operator = comp[0] # The >, <, =
			operand = int(comp[1:]) # Number to compare to
			if operator == ">":
				if debug: print("if-type: gtr")
				if debug: print("result: " + str(int(acc) > int(operand)))
				if int(acc) > int(operand):
					skipElseStatement = True # Skip the else statement because it returned true
				else:
					skipThenStatement = True
			if operator == "<":
				if debug: print("if-type: lss")
				if debug: print("result: " + str(int(acc) < int(operand)))
				if int(acc) < int(operand):
					skipElseStatement = True # Skip the else statement because it returned true
				else:
					skipThenStatement = True
			if operator == "=":
				if debug: print("if-type: equ")
				if debug: print("result: " + str(int(acc) == int(operand)))
				if int(acc) == int(operand):
					skipElseStatement = True # Skip the else statement because it returned true
				else:
					skipThenStatement = True

			if skipThenStatement:
				skipCode = True

		# MEMORY STORE AND LOAD

		if line[:15] == "Then I forgot, ": # Store acc to mem slot provided
			memLoc = line[15:-1]
			if line[-1:] == "!":
				mem[int(memLoc)] = acc
			else:
				print("*** Malform at line: '" + line + "'")

		if line[:19] == "Then I remembered, ": # Read from mem slot provided into the acc
			memLoc = line[19:-1]
			if line[-1:] == "!":
				acc = mem[int(memLoc)]
			else:
				print("*** Malform at line: '" + line + "'")

		if line == "Ha, ha, ha!": # Add the program to the end of the program
			append += 1
			if append % 20 == 0: # If append is a multiple of 5
				data = [] # Some rudimentary memory saving
			data += program

		if line == "That's all folks!": # End the program
			sys.exit()

	else:

		if debug: print("skip-code: true")


if debug: print("acc: " + str(acc))

if ended == False:
	print("Please end your program with a 'That's all folks!'")