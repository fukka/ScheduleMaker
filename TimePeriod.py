from MeetingSection import MeetingSection
#from datetime import datetime
class TimePeriod:
##    def __init__(self, start_time:'datetime.datetime', end_time:'datetime.datetime'):
##        self.start_time = start_time
##        self.end_time = end_time
    def __init__(self, day:str, start:int, end:int):
        self.day = day
        self.start = start
        self.end = end
        self.meeting_sections = []

    def add_meeting_section(self, meeting_section:'MeetingSection') -> None:
        self.meeting_sections.append(meeting_section)

    def __eq__(self, other:object) -> bool:
        if type(other) != type(self):
            return False
        if self.day == other.day and self.start == other.start and self.end == other.end:
            return True
        return False