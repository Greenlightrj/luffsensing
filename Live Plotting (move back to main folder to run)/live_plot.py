"""
live plotting of data from luff sensors
or from a csv generated by flex_testing.py
python3

hasn't been tested since a few changes in flex_testing.py, may not work
switching between reading a csv file and plotting live data requires some commenting-out 
"""


import csv
from time import sleep
import matplotlib.pyplot as plt
from flex_sensor import FlexSensor

#comment out when running on computer
F = FlexSensor()

def read(fileobj=None):
    # either reads the next value from the CSV or grabs current flex sensor data
    if fileobj:
            reader = csv.reader(fileobj)
            row = next(reader)
            return(row[1], row[2], row[3])
    else:
        return F.readsensors()

def liveplot(filename=0):
    """
    Produces a matplotlib plot of the ratio between the sensors.
    If running from a csv file, pass the name of the file to this function.
    If no filename is provided, will attempt to read data live from sensors.
    A lot of the plotting code is magic from various tutorials.
    """
    ratio = None
    if filename:    # if plotting from CSV
        with open(filename) as f:
            for i in range(0, 480): # number of slightly-more-than-quarter-seconds to run for
                oldratio = ratio
                a, b, ratio = read(f)
                print(ratio)

                if oldratio is not None:
                    plt.plot([i - 1, i], [oldratio, ratio], hold=True, color='black')  # plots a line connecting the last 2 points
                    plt.axis([i - 20, i + 2, .8, 1.2])  # axes shift with data
                # magic
                plt.show(block=False)
                plt.pause(0.05)
                # run approximately every quarter second to mimic the data collection
                sleep(0.25)


    else:  # no file provided, plotting live data from sensors
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

                # no quarter second sleep because plotting takes significant amounts of time
                # probably doesn't run at the right speed for actual luff sensing because the algorithm 
                # parameters depend on the frequency of sensor reading.


if __name__ == "__main__":
    
    # computer test
    #liveplot('LuffRecords/luffrecord20161025_2142.csv')
    
    # pi test
    liveplot()