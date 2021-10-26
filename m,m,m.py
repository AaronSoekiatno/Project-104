import statistics
import pandas as pd

df = pd.read_csv(r"weight.csv")
weightList = df["Weight(Pounds)"].tolist()

'''
sumList = []
x=0
for i in weightList:
    num = i+weightList[x]
    x = x+1
n = len(weightList)
mean = x/n
print(mean)
'''

def mean():
    totalMean = statistics.mean(weightList)
    print(totalMean)

def median():
    totalMedian = statistics.median(weightList)
    print(totalMedian)

def mode():
    totalMode = statistics.mode(weightList)
    print(totalMode)
    
mean()
median()
mode()