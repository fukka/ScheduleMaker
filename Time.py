class Time():
    def __init__(self, day:str, start:int, end:int, duration:int, location:'Location'):
        self.day = day
        self.start = start
        self.end = end
        self.duration = duration
        self.location = location

    def __str__(self):
        return "starting at " + str(self.day) + "   " + str(self.start) + " ending at " + str(self.end)