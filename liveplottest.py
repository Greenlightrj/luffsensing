"""
Runs a flex sensor test that prints the outputs and ratio of the sensors
and plots them with matplotlib.
python3
"""

from flex_sensor import FlexSensor
from time import sleep

F = FlexSensor()

for i in range(0, 100):
    print('reading')
    F.readsensors()
    print('plotting')
    F.plot()
    print('sleeping')
    sleep(0.25)
