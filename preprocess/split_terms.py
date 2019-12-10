import pandas as pd
import numpy as py



df2 = pd.read_csv("terms.csv",sep='|',header = None)

indices = []
for i in range(0,99600000,100000):
    indices.append(i)


for i in range(1,len(indices)):
    df2[indices[i-1]:indices[i]].to_csv("terms" + str(i) + ".csv",sep='|',index=False, header=None)
    print("created between " + str(indices[i-1]) + " and " + str(indices[i]))

