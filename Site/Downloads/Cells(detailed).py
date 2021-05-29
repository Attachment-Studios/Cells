# cells
codeline = "" # just starts as nothing
while codeline != ">exit0>": # until codeline is not exit line program stays on
	codeline = input(":::") # takes input
	if ">exit0>" == codeline: # turns off program
		break # stops the execution
	code = [] # store code as commands and items, which will be followed item after item
	iterated_code = "0skip " # code that is currently being read
	push_to_next_line = ":" # character that will push code to next item
	# iterate over codeline
	for character in codeline: # iterate for cells
		# checks if iteration says next line or not
		if character == push_to_next_line: # if character is push to next line character
			code.append(iterated_code) # adds iterated code to code
			iterated_code = "0skip " # resets iterated code
		else: # if character is any other character
			if iterated_code == "0skip ": # change iterator to empty
				iterated_code = "" # updates iterator to be empty
			iterated_code = iterated_code + character # iterated text is updated
	skip_lines = [] # contains indices of cells to skip
	variables_name = [] # list of names of variables declared
	variables_value = [] # list of values of variables declared
	# variables require separate iterations
	for cell in code: # iterates per cell to find if there is any variable declaration
		if " < " in cell: # " < " will set value of variable
			variable_name = "" # variable to be set the value
			for character in cell.replace("nomenclate ", ""): # iterates for all data in cell
				if character == " ": # if space then break
					break # stops the process of naming the variable
				else: # if not space then
					variable_name = variable_name + character # updates name
			variable_value = cell.replace("nomenclate ", "") # removes syntax
			variable_value = variable_value.replace(variable_name, "") # removes variable name
			variable_value = variable_value.replace(" < ", "") # removes syntax
			if "nomenclate " in cell: # if the syntax that says variable is new is present
				variables_name.append(variable_name) # adds variable name to all variables names
				variables_value.append("") # gives the value of variable to nothing
			variables_value[variables_name.index(variable_name)] = variable_value # substitutes value of variable from old value or nothing to new value
			skip_lines.append(int(code.index(cell))) # the cell will not be processed in the main process
	remove_lines = [] # lines to remove when extra execution is done
	# iterate over code
	line = -1 # iterator variable for main code processing
	while line < len(code) - 1: # loops once through all commands of code
		# commands and iteration variables and updation
		line += 1 # updates iterator
		pure_command = str(code[line]) # real command for indices comparisons while processing
		command = pure_command # formatted command that will help for variables
		
		# skipping
		skip_this_line = False # if line to be skipped
		if code.index(pure_command) in skip_lines: # checks if index of cell is there in indices to skip
			skip_this_line = True # sets that cell needs to be skipped
			skip_lines.remove(code.index(pure_command)) # removes skipped line when once skipped
		
		# variables
		for name in variables_name: # runs a loop to check if there is any variable in cell
			if " " + name in command and not skip_this_line: # if variable is in the cell
				if "endocytosis " not in command and "grow " not in command and "exosmosis " not in command and "multinucleate " not in command and "mitosis " not in command and "meiosis " not in command and "fuse " not in command: # leaves cells using variables to return and change their value
					command = command.replace(" " + name, " " + str(variables_value[variables_name.index(name)])) # replaces variable name with it's value
		
		# errors
		cell_contains_error = False # initially assuming no error
		
		if not(skip_this_line): # if not skipping this line
			# code processing and outputs
			if "exocytosis " in command: # exocytosis for display on console
				output = command.replace("exocytosis ", "") # sets the output to be everything but "dispc"
				print(output) # prints output
			elif "endocytosis " in command: # endocytosis for taking inputs
				variable_name = command.replace("endocytosis ", "") # removes syntax to get variable name
				if variable_name in variables_name: # if variable name is present in all variable names and not nothing
					variables_value[variables_name.index(variable_name)] = input() # takes input and sets value of variable to be input value
				else: # in all other cases
					cell_contains_error = True # will return error
			elif "skip " in command: # skip for skipping given amount cells after current cell
				skip_amount = (command.replace("skip ", "")) # sets skip amount to a number
				try: # if skip amount is a number
					for after_index in range(1, int(skip_amount)+1): # loops for how many indices to skip
						index = code.index(pure_command) + after_index # index to skip with respect to code
						skip_lines.append(index) # appends index to skip to skip_lines
				except: # if skip amount is not a number
					cell_contains_error = True # there is some error in code
			elif "regulate ^ " in command: # skip for skipping given amount cells after current cell
				try: # with all valid cases
					cell_number = int(command.replace("regulate ^ ", "")) # goes to cell according to instructions
					line = cell_number - 2 # goes to given line
					if line < -1: # in case line is less than zero, so need to prevent problems
						line = -1 # restarts the code
				except: # in case error drops
					cell_contains_error = True # declares error in cell
			elif ">" in command or ">" == command: # exit cell
				break # breaks the loop, this means operation ended
			elif "eject " in command: # subtraction of variable with number
				try: # if cell is valid
					variable_name = command.replace("eject ", "") # name of variable to add a value
					temporary_iterator = "" # temporary iterator
					for character in variable_name: # check for separator syntax
						if character == ",": # when correct separator syntax charater is recieved
							break # stops process of finding variable
						else: # if not such indication of syntax
							temporary_iterator = temporary_iterator + character # updates temporary iterator
					variable_name = temporary_iterator # updates variable name
					add_value = command.replace("eject ", "") # gets value to reduce
					add_value = add_value.replace(variable_name + ",", "") # gets value to reduce
					try: # for numerical values
						variables_value[variables_name.index(variable_name)] = int(variables_value[variables_name.index(variable_name)]) # converts variable value to integer
						variables_value[variables_name.index(variable_name)] -= int(add_value) # subtracts value from variable value
					except: # for string cases
						variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)]) # converts variable value to string
						variables_value[variables_name.index(variable_name)] = variables_value[variables_name.index(variable_name)].replace(str(add_value), "") # removes value from variable value
				except: # if cell is invalid
					cell_contains_error = True # cell contains error
			elif "mitosis " in command: # division of variable with number
				try: # if cell is valid
					variable_name = command.replace("mitosis ", "") # name of variable to add a value
					temporary_iterator = "" # temporary iterator
					for character in variable_name: # check for separator syntax
						if character == ",": # when correct separator syntax charater is recieved
							break # stops process of finding variable
						else: # if not such indication of syntax
							temporary_iterator = temporary_iterator + character # updates temporary iterator
					variable_name = temporary_iterator # updates variable name
					add_value = command.replace("mitosis ", "") # gets value to divide
					add_value = add_value.replace(variable_name + ",", "") # gets value to divide
					try: # for numerical values
						variables_value[variables_name.index(variable_name)] = int(variables_value[variables_name.index(variable_name)]) # converts variable value to integer
						variables_value[variables_name.index(variable_name)] /= int(add_value) # divides value from variable value
					except: # for string cases
						variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)]) # converts variable value to string
						variables_value[variables_name.index(variable_name)] = variables_value[variables_name.index(variable_name)].replace(str(add_value), "") # removes value from variable value
				except: # if cell is invalid
					cell_contains_error = True # cell contains error
			elif "grow " in command: # addition of variable with number
				try: # if cell is valid
					variable_name = command.replace("grow ", "") # name of variable to reduce value
					temporary_iterator = "" # temporary iterator
					for character in variable_name: # check for separator syntax
						if character == ",": # when correct separator syntax charater is recieved
							break # stops process of finding variable
						else: # if not such indication of syntax
							temporary_iterator = temporary_iterator + character # updates temporary iterator
					variable_name = temporary_iterator # updates variable name
					add_value = command.replace("grow ", "") # gets value to add
					add_value = add_value.replace(variable_name + ",", "") # gets value to add
					try: # for numerical values
						variables_value[variables_name.index(variable_name)] = int(variables_value[variables_name.index(variable_name)]) # converts variable value to integer
						variables_value[variables_name.index(variable_name)] += int(add_value) # adds add value to variable value
					except: # for string cases
						variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)]) # converts variable value to string
						variables_value[variables_name.index(variable_name)] += str(add_value) # concatenates add value to variable value
				except: # if cell is invalid
					cell_contains_error = True # cell contains error
			elif "multinucleate " in command: # multiplication of variable with number
				try: # if cell is valid
					variable_name = command.replace("multinucleate ", "") # name of variable to reduce value
					temporary_iterator = "" # temporary iterator
					for character in variable_name: # check for separator syntax
						if character == ",": # when correct separator syntax charater is recieved
							break # stops process of finding variable
						else: # if not such indication of syntax
							temporary_iterator = temporary_iterator + character # updates temporary iterator
					variable_name = temporary_iterator # updates variable name
					add_value = command.replace("multinucleate ", "") # gets value to multiply
					add_value = add_value.replace(variable_name + ",", "") # gets value to multiply
					try: # for numerical values
						variables_value[variables_name.index(variable_name)] = int(variables_value[variables_name.index(variable_name)]) # converts variable value to integer
						variables_value[variables_name.index(variable_name)] *= int(add_value) # multiplies value to variable value
					except: # for string cases
						variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)]) # converts variable value to string
						variables_value[variables_name.index(variable_name)] += str(add_value) # concatenates value to variable value
				except: # if cell is invalid
					cell_contains_error = True # cell contains error
			elif "fuse " in command: # float multiplication of variable with number
				try: # if cell is valid
					variable_name = command.replace("fuse ", "") # name of variable to reduce value
					temporary_iterator = "" # temporary iterator
					for character in variable_name: # check for separator syntax
						if character == ",": # when correct separator syntax charater is recieved
							break # stops process of finding variable
						else: # if not such indication of syntax
							temporary_iterator = temporary_iterator + character # updates temporary iterator
					variable_name = temporary_iterator # updates variable name
					add_value = command.replace("fuse ", "") # gets value to multiply
					add_value = add_value.replace(variable_name + ",", "") # gets value to multiply
					try: # for numerical values
						variables_value[variables_name.index(variable_name)] = float(variables_value[variables_name.index(variable_name)]) # converts variable value to integer
						variables_value[variables_name.index(variable_name)] *= float(add_value) # multiplies value to variable value
					except: # for string cases
						variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)]) # converts variable value to string
						variables_value[variables_name.index(variable_name)] += str(add_value) # concatenates value to variable value
				except: # if cell is invalid
					cell_contains_error = True # cell contains error
			elif "meiosis " in command: # float division of variable with number
				try: # if cell is valid
					variable_name = command.replace("meiosis ", "") # name of variable to add a value
					temporary_iterator = "" # temporary iterator
					for character in variable_name: # check for separator syntax
						if character == ",": # when correct separator syntax charater is recieved
							break # stops process of finding variable
						else: # if not such indication of syntax
							temporary_iterator = temporary_iterator + character # updates temporary iterator
					variable_name = temporary_iterator # updates variable name
					add_value = command.replace("meiosis ", "") # gets value to divide
					add_value = add_value.replace(variable_name + ",", "") # gets value to divide
					try: # for numerical values
						variables_value[variables_name.index(variable_name)] = float(variables_value[variables_name.index(variable_name)]) # converts variable value to integer
						variables_value[variables_name.index(variable_name)] /= float(add_value) # divides value from variable value
					except: # for string cases
						variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)]) # converts variable value to string
						variables_value[variables_name.index(variable_name)] = variables_value[variables_name.index(variable_name)].replace(str(add_value), "") # removes value from variable value
				except: # if cell is invalid
					cell_contains_error = True # cell contains error
			else: # in cases where no instructions given
				cell_contains_error = True # cell contains error
			
			if cell_contains_error: # in cases of error
				print("Error in cell::" + str(code.index(pure_command) + 1) + "::" + pure_command) # prints error
				break # stop the process after iteration and finding error