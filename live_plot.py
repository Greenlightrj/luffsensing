"""
live plotting of data from luff sensors
or from a csv generated by flex_testing.py
python3
"""


import csv
from time import sleep
import matplotlib.pyplot as plt
from flex_sensor import FlexSensor

#comment out when running on computer
F = FlexSensor()

def read(fileobj=None):
    if fileobj:
            reader = csv.reader(fileobj)
            row = next(reader)
            return(row[1], row[2], row[3])
    else:
        return F.readsensors()

def liveplot(filename=0):
    ratio = None
    if filename:
        with open(filename) as f:
            for i in range(0, 480):
                oldratio = ratio
                a, b, ratio = read(f)
                print(ratio)

                if oldratio is not None:
                    plt.plot([i - 1, i], [oldratio, ratio], hold=True, color='black')
                    plt.axis([i - 20, i + 2, .8, 1.2])
                #plt.scatter(i, ratio, hold=True)
                plt.show(block=False)
                plt.pause(0.05)
                sleep(0.25)

                #while True:
                #    plt.pause(0.05)

    else:
        print("Live Sensing begun")
        for i in range(0, 100):
                oldratio = ratio
                a, b, ratio = read()
                print(ratio)

                if oldratio is not None:
                    plt.plot([i - 1, i], [oldratio, ratio], hold=True, color='black')
                    plt.axis([i - 20, i + 2, .8, 1.2])
                #plt.scatter(i, ratio, hold=True)
                plt.show(block=False)
                plt.pause(0.05)
                sleep(0.25)


if __name__ == "__main__":
    
    #computer test
    #liveplot('LuffRecords/luffrecord20161025_2142.csv')
    
    #pi test
    liveplot()