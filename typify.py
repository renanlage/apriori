def typify(path):
	inputData = open(path, 'r')
	data = inputData.readlines()
	attrName = data.pop(0).strip().split(",")
	ans = []
	#getting the biggest, smallest and mean values for attributes...
	for x in xrange(5,21):
		ans.append(attrCounter(data,x))
	#creating a new file
	writeNewFile(attrName,data,ans)		

	inputData.close()
	

def attrCounter(data, col_num):
	lines_num = len(data)
	biggest=0
	smallest=999999
	mean = 0
	for line in data:
		player = line.strip().split(',')
		num = float(player[col_num])
		mean += num
		if num > biggest:
			biggest = num
		if num < smallest:
			smallest = num
	mean = mean/float(lines_num)
	return [biggest,smallest,mean]


def writeNewFile(attrName,data,values):

	modifiedData = ""

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

			elif value >= mean :
				#'b'
				player[x] = attrName[x]+"-b"

			elif value >= ((smallest + mean) / 2.0):
				#'r'
				player[x] = attrName[x] + "-r"				

			else:
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
	output_file = open('mod_input.csv', 'w')
	output_file.writelines(modifiedData) 
	output_file.close()  

typify("input.csv")