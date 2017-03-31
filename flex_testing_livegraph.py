"""
Live test of tack sensing by flex sensors on sail
"""

from time import sleep, time
import datetime
import csv
from flex_sensor import FlexSensor
from gpiozero import Button, LED

F = FlexSensor()

button = Button(13, bounce_time=.025)  # initialize gpiozero button class with debounce
statLED = LED(19)
portLED = LED(26)
stbdLED = LED(6)
#luffLED = LED(20)


def runtest():

    button.wait_for_press()  # function is running, but wait for the button press to start recording data.

    print("Running Live Graph Test")

    # grab a timestamp
    filename = '/home/pi/luffsensing/LuffRecords/luffrecord' + datetime.datetime.strftime(datetime.datetime.today(), "%Y%m%d_%H%M") + ".csv"

    # blink light for five seconds
    for i in range(1, 10):
        statLED.toggle()
        sleep(0.5)

    # define start time of recording (in seconds)
    t = time()

    # open file and write one minute of record while blinking light and updating LEDs
    with open(filename, 'w') as f:
            writer = csv.writer(f)
            for i in range(0, 20):  # number of quarter-seconds to run
                # get data to write to file
                dtime = datetime.datetime.today()
                timestr = dtime.strftime("%X")
                sec = time() - t
                a, b, ratio = F.readsensors()
                tack, luff = F.sailstate()

                # update plot
                F.plot(t)

                # turn on LEDs
                if tack > 0:
                    stbdLED.on()
                    portLED.off()
                elif tack < 0:
                    stbdLED.off()
                    portLED.on()

                #if luff:
                #    luffLED.on()
                #else:
                #    luffLED.off()

                writer.writerow([timestr, a, b, ratio, tack, luff, sec])  # record data
                statLED.toggle()

                #sleep(.25)
    f.close()

# run and record data as many times in a row as you need
while True:
    statLED.on()  # turn on LED to tell user it's ready
    portLED.off()  # turn off other LEDs while waiting
    stbdLED.off()
    #luffLED.off()
    runtest()  # runs runtest() which waits for button press
