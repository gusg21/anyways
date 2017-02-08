import sys

print("Anyways Compiler ===============\n")

acc = ""
mem = [""] * 100

skipCode = False
skipElseStatement = False

ended = False

try:
	sys.argv[1]
except:
	path = input("Path to file >>> ")
else:
	path = sys.argv[1]

with open(path, 'r') as myfile:
    data=myfile.read().splitlines()

for line in data:
	print("line: " + line)

	if line == "Who's there?":
		print("else: detected")
		if skipElseStatement:
			skipCode = True

	if line == "Banana!":
		skipElseStatement = False
		skipCode = False

	if not skipCode:

		if line == '"Ow!" it said.':
			print(acc)

		if line[:26] == "There was this guy called ":
			print("detected: accumulator set")
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
			print("comp: " + comp + ", comp0: " + comp[0])
			operator = comp[0]
			operand = int(comp[1:])
			if operator == ">":
				print("if-type: gtr")
				print("result: " + str(acc > operand))
				if acc > operand:
					skipElseStatement = True
			if operator == "<":
				print("if-type: lss")
				print("result: " + str(acc < operand))
				if acc < operand:
					skipElseStatement = True
			if operator == "=":
				print("if-type: equ")
				print("result: " + str(acc == operand))
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

		print("skip-code: true")


print("acc: " + str(acc))

if ended == False:
	print("Please end your program with a 'That's all folks!'")