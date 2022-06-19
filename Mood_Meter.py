import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

def main():
    inputData()
    input()
    userInput = input("Show graph? y/n \n")
    if userInput == 'y':
        plotData(getDate(getData()), getData())
    else:
        exit

def plotData(x, y):
    plt.style.use('fivethirtyeight')
    plt.plot(x, y, marker='.')
    plt.xlabel('Date')
    plt.ylabel('Mental Score')
    plt.title('Mood Meter')
    plt.show()

def inputData():
    dataFile = open('data.txt', 'a')
    newData = input("Rate your existence 1-10 \n")
    dataFile.write(newData + "\n")
    dataFile.close()

def getData():
    dataFile = open('data.txt', 'r')
    data = [int(x) for x in dataFile.readlines()]
    dataFile.close()
    return data

def getDate(data):
    list = []
    index = 1
    for i in data:
        list.append(index)
        index += 1 
    return list

main()
input()
