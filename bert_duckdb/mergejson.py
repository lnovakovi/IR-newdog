import json
import glob

def mangle(s):
    return s.strip()[1:-1]

def cat_json(output_filename, input_filenames):
    with open(output_filename, "w") as outfile:
        first = True
        for infile_name in input_filenames:
            with open(infile_name) as infile:
                if first:
                    outfile.write('[')
                    first = False
                else:
                    outfile.write(',')
                outfile.write(mangle(infile.read()))
        outfile.write(']')

filenames = glob.glob("./raww/*.json")

input_filenames = []
for file in filenames:
    input_filenames.append(file)

cat_json("all.json",input_filenames)



'''
import json
import glob

def mangle(s):
	return s.strip()[1:-1]

def cat_json(output_filename, input_filenames):
    with open(output_filename, "w") as outfile:
        first = True
        for infile_name in input_filenames:
            with open(infile_name) as infile:
                if first:
                    outfile.write('[')
                    first = False
                else:
                    outfile.write(',')
                outfile.write(mangle(infile.read()))
        outfile.write(']')

filenames = glob.glob("./raww/*.json")

input_filenames_latimes = [] 
input_filenames_fr94 = [] 
input_filenames_fbis = [] 
input_filenames_ft = [] 
for file in filenames:
	if "latimes" in file:
		input_filenames_latimes.append(file)
	elif "fr94" in file:
		input_filenames_fr94.append(file)
	elif "fbis" in file:
		input_filenames_fbis.append(file)
	else:
		input_filenames_ft.append(file)

cat_json("latimes.json",input_filenames_latimes)
cat_json("fr94.json",input_filenames_fr94)
cat_json("fbis.json",input_filenames_fbis)
cat_json("ft.json",input_filenames_ft)
'''