duck = []
monet = []
with open('results_duck.txt') as fp:
	line = fp.readline()
	while line:
		line = fp.readline()
		duck.append(line.split(',')[0][1:])
with open('results_monet.txt') as fp:
	line = fp.readline()
	while line:
		line = fp.readline()
		monet.append(line.split(',')[0][1:])

for i in range(len(duck)):
	if duck[i] != monet[i]:
		print(str(duck[i]) + "  " +str(monet[i]) + " " + str(i)) 
