import sys

print("Anyways Compiler ===============\n")

acc = ""
mem = [""] * 100

skipCode = False
skipElseStatement = False

ended = False

debug = False
path = ""
index = 0
for arg in sys.argv:
	if arg == "-i" or arg == "--input":
		try:
			path = sys.argv[index + 1]
			print("Path provided: " + sys.argv[index + 1])
		except:
			print("-i flag but no input file!")

	if arg == "-d" or arg == "--debug":
		print("debug: ON")
		debug = True

	if arg == "-h" or arg == "--help":
		print("Usage:\n")
		print("-d / --debug: Show a LOT of output; only use if debugging interpreter!")
		print("-h / --help: This menu")
		print("-i / --input: Provide an input file")

		sys.exit()

	index += 1

if path == "":
	path = input("Path to file >>>")

print("Reading file...")
with open(path, 'r') as myfile:
    data=myfile.read().splitlines()

for line in data:
	if debug: print("line: " + line)

	if line == "Who's there?":
		if debug: print("else: detected")
		if skipElseStatement:
			skipCode = True

	if line == "Banana!":
		skipElseStatement = False
		skipCode = False

	if not skipCode:

		if line == '"Ow!" it said.':
			print(acc)

		if line[:26] == "There was this guy called ":
			if debug: print("detected: accumulator set")
			acc = line[26:]

		if line == '"What are you doing?" they said.':
			acc = input("Input to program: ")

		if line[:9] == "But then ":
			if line[-9:] == "happened!":
				acc = int(acc) - int(line[9:-9])
			else:
				print("*** Malform at line: '" + line + "'")

		if line[:6] == "Until ":
			if line[-9:] == "happened!":
				acc = int(acc) * int(line[6:-9])
			else:
				print("*** Malform at line: '" + line + "'")

		if line[:5] == "When ":
			if line[-9:] == "happened!":
				acc = int(acc) * int(line[5:-9])
			else:
				print("*** Malform at line: '" + line + "'")

		if line[:9] == "And then ":
			if line[-9:] == "happened!":
				acc = int(acc) + int(line[9:-9])
			else:
				print("*** Malform at line: '" + line + "'")

		if line[:13] == "Knock Knock, ":
			comp = line[13:]
			if debug: print("comp: " + comp + ", comp0: " + comp[0])
			operator = comp[0]
			operand = int(comp[1:])
			if operator == ">":
				if debug: print("if-type: gtr")
				if debug: print("result: " + str(acc > operand))
				if acc > operand:
					skipElseStatement = True
			if operator == "<":
				if debug: print("if-type: lss")
				if debug: print("result: " + str(acc < operand))
				if acc < operand:
					skipElseStatement = True
			if operator == "=":
				if debug: print("if-type: equ")
				if debug: print("result: " + str(acc == operand))
				if acc == operand:
					skipElseStatement = True

		if line[:15] == "Then I forgot, ":
			memLoc = line[15:-1]
			if line[-1:] == "!":
				mem[int(memLoc)] = acc
			else:
				print("*** Malform at line: '" + line + "'")

		if line[:19] == "Then I remembered, ":
			memLoc = line[19:-1]
			if line[-1:] == "!":
				acc = mem[int(memLoc)]
			else:
				print("*** Malform at line: '" + line + "'")

		if line == "That's all folks!":
			ended = True

	else:

		if debug: print("skip-code: true")


if debug: print("acc: " + str(acc))

if ended == False:
	print("Please end your program with a 'That's all folks!'")