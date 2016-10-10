"""
luff sensor verification script
compares python calculations to matlab calculations
"""

import csv
from collections import deque


dratios = deque('', 15)
dfav = deque('', 15)


def sailstate(a, b, ratio):
    """
    uses the last 15 ratios to determine whether the sail is luffing, and what tack it's on.
    returns a tuple
    the first digit is 1 if the boat is on a starboard tack and -1 if on a port tack
    the second digit is 1 if the sail is full and 0 if it is luffing.
    if luffing, the tack is probably inaccurate. idea: multiply the two.
    """

    average = float(sum(dratios)) / len(dratios)
    dfav.append(abs(average - dratios[-1]))  # this is the distace of the current ratio from the running average
    avdistfromav = float(sum(dfav)) / len(dfav)        # the average distance from average

    # determine tack based on running average
    tack = -1  # port tack
    if average < 1:
        tack = 1  # starboard tack

    # determine luffing based on average distance from average
    luff = 1  # not luffing
    if avdistfromav > 0.025:
        luff = 0  # luffing

    return(tack, luff)



datafile = "LuffRecords/luffrecord20160623_1257.csv"
outputfile = "LuffRecords/verif.csv"


with open(datafile, 'r') as d:
    with open(outputfile, 'w') as o:
        reader = csv.reader(d)
        writer = csv.writer(o)
        for row in reader:
            a = float(row[1])
            b = float(row[2])
            ratio = float(row[3])
            dratios.append(ratio)
            tack, luff = sailstate(a, b, ratio)
            writer.writerow([tack, luff])
