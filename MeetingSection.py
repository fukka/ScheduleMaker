from Time import Time
class MeetingSection():
    def __init__(self, code:str, size:int, enrolment:int, times:'list[Time]', instructors:'list[str]'):
        self.code = code
        self.size = size
        self.enrolment = enrolment
        self.times = times
        self.instructors = instructors

    def __str__(self):
        result = self.code
        for time in self.times:
            result += str(time) + "    "
        return result

    def type(self) -> str:
       return self.code[0:3]