def typify(path):
	inputData = open(path, 'r')
	data = inputData.readlines()
<<<<<<< HEAD
	attrName = data.pop(0).strip().split(",")
=======
	col_names = data.pop(0)
>>>>>>> f78c9494632cf728d9139d95fc6f521c7bb40ee4
	ans = []
	#getting the biggest, smallest and mean values for attributes...
	for x in xrange(5,21):
		ans.append(attrCounter(data,x))
	#creating a new file
<<<<<<< HEAD
	writeNewFile(attrName,data,ans)		
=======
	writeNewFile(col_names,data,ans)			
>>>>>>> f78c9494632cf728d9139d95fc6f521c7bb40ee4

	inputData.close()
	

def attrCounter(data, col_num):
	lines_num = len(data)
	biggest=0
<<<<<<< HEAD
	smallest=999999
=======
	smallest=999
>>>>>>> f78c9494632cf728d9139d95fc6f521c7bb40ee4
	mean = 0
	for line in data:
		player = line.strip().split(',')
		num = float(player[col_num])
		mean += num
		if num > biggest:
			biggest = num
<<<<<<< HEAD
		if num < smallest:
=======
		elif num < smallest:
>>>>>>> f78c9494632cf728d9139d95fc6f521c7bb40ee4
			smallest = num
	mean = mean/float(lines_num)
	return [biggest,smallest,mean]


<<<<<<< HEAD
def writeNewFile(attrName,data,values):

	modifiedData = ""
=======
def writeNewFile(col_names,data,values):

	modifiedData = ""
	attrName = col_names.strip().split(",")
>>>>>>> f78c9494632cf728d9139d95fc6f521c7bb40ee4

	for line in data:
		player = line.strip().split(',')
		stringLine = ""
		
		for x in xrange(5,21):
			#compares with the attr counted before
			value = float(player[x])
			biggest = values[x-5][0]
			smallest = values[x-5][1]
			mean = values[x-5][2]
			if value >=  ((biggest + mean) / 2.0) :
				#'mb'
				player[x] = attrName[x]+"-mb"

<<<<<<< HEAD
			elif value >= mean :
				#'b'
				player[x] = attrName[x]+"-b"

			elif value >= ((smallest + mean) / 2.0):
				#'r'
				player[x] = attrName[x] + "-r"				

			else:
=======
			elif value < ((biggest + mean) / 2.0) and value > mean :
				#'b'
				player[x] = attrName[x]+"-b"

			elif value < ((smallest + mean) / 2.0) and value <= mean :
				#'r'
				player[x] = attrName[x] + "-r"				

			elif value <= ((smallest + mean) / 2.0):
>>>>>>> f78c9494632cf728d9139d95fc6f521c7bb40ee4
				#'mr'
				player[x] = attrName[x]+"-mr"
		#create new txt line
		for i in range(len(player)):
			if i < len(player) - 1:
				stringLine+= player[i] + ","
			else:
				stringLine+= player[i] + "\n"
		modifiedData+=stringLine

	# write on output file and close program
<<<<<<< HEAD
	output_file = open('mod_input.csv', 'w')
	output_file.writelines(modifiedData) 
	output_file.close()  

typify("input.csv")
=======
	output_file = open('output2.csv', 'w')
	output_file.writelines(modifiedData) 
	output_file.close()  
>>>>>>> f78c9494632cf728d9139d95fc6f521c7bb40ee4
