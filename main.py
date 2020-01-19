from alberta import*
from novascotia import*
import csv
import matplotlib.pyplot as plt


frames =[df, df1]
result = pd.concat(frames, sort=True)
result.to_csv('merge.csv',index=False,encoding='cp1252')

time = []
demand = []
supply = []

with open('merge.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        demand.append(row[0])
        supply.append(row[1])
        time.append(row[2])



del time[0]
del demand[0]
del supply[0]



x = [demand[0],demand[0]]
y = [supply[0], supply[0]]
plt.plot(x,y, 'ro', color='blue', label= "ALBERTA "+ time[0])
plt.ylabel('SUPPLY(MW)')
plt.xlabel('DEMAND(MW)')

a = [demand[1],demand[1]]
b = [supply[1], supply[1]]
plt.plot(a,b, 'ro', color='red', label= "NOVA SCOTIA "+ time[1])
plt.legend()
plt.show()


