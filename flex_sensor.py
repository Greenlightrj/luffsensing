""""
Code for reading from two flex sensors with an MCP3302 analog digital converter
python3
"""
from time import sleep, time
from datetime import timedelta
from gpiozero import MCP3008
from collections import deque
import matplotlib as m
import matplotlib.pyplot as plt


class FlexSensor():

    def __init__(self):
        self.a = MCP3008(channel=0)  # objects that access the flex sensor values through the adc
        self.b = MCP3008(channel=1)
        self.dtimes = deque('', 15)
        self.dratios = deque('', 15)  # deque, which is like a list but for queueing
        self.dfav = deque('', 15)

    def test(self):
        """
        simple test that prints the values from the two inputs every quarter-second for a minute
        """
        for i in range(0, 240):
            print("A:", end=" ")
            print(self.a.value)
            print("B:", end=" ")
            print(self.b.value)

            print(self.a.value / self.b.value)

            sleep(.25)

    def readsensors(self):
        """
        returns a tuple of the two current values and the ratio between them
        and appends the ratio to the deque used to calculate running average
        """
        a = self.a.value
        b = self.b.value
        ratio = a / b

        self.dtimes.append(time())
        self.dratios.append(ratio)
        return(a, b, ratio)

    def plot(self, starttime):
        """
        plots a line representing the last 15 recorded using matplotlib.
        does not check for new data--call readsensors() first.
        automatically scrolls sideways. time displayed is time elapsed since starttime
        (in format given by time.time(), seconds.)
        """

        self.figure = plt.figure(1)       
        times = [x - starttime for x in self.dtimes]

        plt.figure(1) # return to same figure plotted before
        if len(self.dratios) > 1: # can't plot a line on the first iteration
            plt.plot([times[-1], times[-2]], [self.dratios[-1], self.dratios[-2]], hold=True, color='black')
        plt.axis([times[0], times[-1] + 1, .8, 1.2])

        plt.show(block=False)
        plt.pause(0.05)

    def sailstate(self):
        """
        uses the last 15 ratios to determine whether the sail is luffing, and what tack it's on.
        returns a tuple
        the first digit is 1 if the boat is on a starboard tack and -1 if on a port tack
        the second digit is 1 if the sail is full and 0 if it is luffing.
        if luffing, the tack is probably inaccurate. idea: multiply the two.
        """
        self.readsensors()  # important to get new ratio value. it is automatically added to self.dratios.
        average = float(sum(self.dratios)) / len(self.dratios)  # find the running average of the flex sensor ratio
        self.dfav.append(abs(average - self.dratios[-1]))  # this is the distace of the current ratio from the running average
        avdistfromav = float(sum(self.dfav)) / len(self.dfav)        # the average distance from average

        # determine tack based on running average
        tack = -1  # default is port tack
        if average < 1:
            tack = 1

        # determine luffing based on average distance from average
        #luff = 1  # default is no luffing
        #if avdistfromav > 0.025:
        #    luff = 0
        luff = 0
        
        return(tack, luff)
