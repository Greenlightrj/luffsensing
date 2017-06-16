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
        self.dtimes = deque('', 15)  # deque, which is like a list but for queueing
        self.dratios = deque('', 15) 
        self.dfav = deque('', 15)

    def test(self):
        """
        simple test that prints the values from the two inputs every quarter-second
        change the second number in range to the desired number of quarter-seconds (240 is 1 minute)
        """
        for i in range(0, 240):
            print("A:", end=" ")
            print(self.a.value)
            print("B:", end=" ")
            print(self.b.value)

            print(self.a.value / self.b.value)

    def readsensors(self):
        """
        returns a tuple of the two current values and the ratio between them
        and appends the ratio to the deque used to calculate running average
        meant to be run every quarter-second
        """
        a = self.a.value  # method that checks current value 
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
        Buggy. Raspberry Pi has trouble handling this amount of graphics processing.
        """

        self.figure = plt.figure(1)       
        times = [x - starttime for x in self.dtimes]  # scrolls time, only shows last 15 readings

        plt.figure(1) # return to same figure plotted before
        if len(self.dratios) > 1: # can't plot a line on the first iteration
            # this matplotlib function plots a line/vector based on two endpoints.
            plt.plot([times[-1], times[-2]], [self.dratios[-1], self.dratios[-2]], hold=True, color='black')
        plt.axis([times[0], times[-1] + 1, .8, 1.2])

        # some sort of magic that makes it work, hopefully.
        plt.show(block=False)
        plt.pause(0.05)

    def sailstate(self):
        """
        important: call readsensors first
        uses the last 15 ratios to determine whether the sail is luffing, and what tack it's on.
        returns a tuple:
          the first digit is 1 if the boat is on a starboard tack and -1 if on a port tack
          the second digit is 1 if the sail is full and 0 if it is luffing.
        if luffing, the tack is probably inaccurate. idea: multiply the two.

        INCOMPLETE
        Use the method in algorithmplotter.m to determine luffing. 
        I meant to port it to Python but ran out of time. 
        """

        # determine tack based on running average
        tack = -1  # default is port tack
        if average < 1:
            tack = 1

        # determine luffing based on average distance from average
        # FILL THIS IN FROM ALGORITHMPLOTTER.M
        luff = 0
        
        return(tack, luff)
