"""
Live test of tack sensing by flex sensors on sail

Solid white LED when ready
On button press, blinks slowly for five seconds then records two minutes of data (blinking rapidly) and saves to CSV file.
Solid white LED means ready for another reading. Press button again to begin. Runs indefinitely.
Pi must be shut down properly to save CSV files.

"""

from time import sleep
import datetime
import csv
from flex_sensor import FlexSensor
from gpiozero import Button, LED

F = FlexSensor()

# GPIOZero uses GPIO pin numbering rather than
button = Button(13, bounce_time=.025)  # initialize gpiozero button class with debounce
statLED = LED(19)  # white LED
portLED = LED(26)  # red LED
#stbdLED = LED(6)  # green/blue LED
luffLED = LED(6)  #changed because I don't have another LED


def runtest():

    button.wait_for_press()  # function is running, but wait for the button press to start recording data.

    print("Running Luff Sensing Test")

    # grab a timestamp
    filename = '/home/pi/luffsensing/LuffRecords/luffrecord' + datetime.datetime.strftime(datetime.datetime.today(), "%Y%m%d_%H%M") + ".csv"

    # blink light for five seconds
    for i in range(1, 10):
        statLED.toggle()
        sleep(0.5)

    # open file and write two minutes of record while blinking light and updating LEDs
    with open(filename, 'w') as f:
            writer = csv.writer(f)
            for i in range(0, 480):  # number of quarter-seconds to run
                # get data to write to file
                time = datetime.datetime.today()
                timestr = time.strftime("%X")
                a, b, ratio = F.readsensors()
                tack, luff = F.sailstate()
                print(a, b, ratio)
                # turn on LEDs
                # red (port) LED is tack
                if tack > 0:
                    #stbdLED.on()
                    portLED.off()
                elif tack < 0:
                    #stbdLED.off()
                    portLED.on()

                # stbd (blue) LED is luff:
                if luff:
                    luffLED.on()
                else:
                    luffLED.off()

                writer.writerow([timestr, a, b, ratio, tack, luff])  # record data
                statLED.toggle()

                sleep(.25)
    f.close()

# run and record data as many times in a row as you need
while True:
    statLED.on()  # turn on LED to tell user it's ready
    portLED.off()  # turn off other LEDs while waiting
    #stbdLED.off() # not currently initialized
    luffLED.off()
    runtest()  # runs runtest() which waits for button press
