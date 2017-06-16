"""
Runs a flex sensor test that prints the outputs and ratio of the sensors
and plots them with matplotlib.
python3

I don't remember whether this method or live_plot.py worked most recently.
"""

from flex_sensor import FlexSensor
from time import sleep, time

F = FlexSensor()
starttime = time()

for i in range(0, 100):
    F.readsensors()
    F.plot(starttime)
    #sleep(0.25)
