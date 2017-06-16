#python3


class LuffAlgorithms():
    """
    Potential algorithms for detecting luffing. Designed for use in flex_sensor.py's sailstate()
    take the most recent 1-15 quarter-second readings (deq)
    and return a 1 if the sail is full and 0 if luffing
    """

    def __init__(self):
        pass

    def running_av(self, deq):
        """
        
        """
        average = float(sum(deq)) / len(deq)

        pass

    def avdistfromav(self, deq, avdeq):
        """
    
        """
        pass

    def variance(self, deq):
        """
        uses numpy's variance function to tell how spread out the data is from its average
        """
        pass
