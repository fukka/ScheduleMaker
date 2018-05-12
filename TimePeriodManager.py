from MeetingSection import MeetingSection
from TimePeriod import TimePeriod
weekdays = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

class TimePeriodManager():
    def __init__(self):
        self.time_period = [[], [], [], [], [], [], []]

    def record_meeting_section(self, meeting_section:'MeetingSection') -> None:
        for time in meeting_section.times:
            time_period = TimePeriod(time.day, time.start, time.end)
            day_list = self.time_period[weekdays.index(time.day)]
            if time_period in day_list:
                existing_time_period = day_list[day_list.index(time_period)]
                existing_time_period.add_meeting_section(meeting_section)
            else:
                time_period.add_meeting_section(meeting_section)
                day_list.append(time_period)

    def has_time_conflict(self) -> bool:
        for day_list in self.time_period:
            for time_period in day_list:
                if len(time_period.meeting_sections) > 1:
                    return True
        return False