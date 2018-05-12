import copy
from CourseSelectionOptionManager import CourseSelectionOptionManager
from CourseSelectionOption import CourseSelectionOption
from Course import Course
from TimePeriodManager import TimePeriodManager
class Schedule():
    def __init__(self):
        self.course_selection_option_manager = CourseSelectionOptionManager()
        self.time_period_manager = TimePeriodManager()
        self.sorted = True

    def add_course(self, course:'Course') -> 'list[Schedule]':
        new_schedules = []
        for course_selection_option in course.get_course_selection_options():
            new_schedules.append(self.add_course_selection_option(course_selection_option))
        self.sorted = False
        return new_schedules

    def add_course_selection_option(self, course_selection_option:'CourseSelectionOption') -> 'Schedule':
        new_schedule = copy.deepcopy(self)
        new_schedule.course_selection_option_manager.add_course(course_selection_option)
        return new_schedule

    def sort_by_time_period_manager(self) -> None:
        if self.sorted:
            return None
        for course_selection_option in self.course_selection_option_manager.courses:
            if course_selection_option.lec != None:
                self.time_period_manager.record_meeting_section(course_selection_option.lec)
            if course_selection_option.tut != None:
                self.time_period_manager.record_meeting_section(course_selection_option.tut)
            if course_selection_option.pra != None:
                self.time_period_manager.record_meeting_section(course_selection_option.pra)
        self.sorted = True

    def has_time_conflict(self) -> bool:
        return self.time_period_manager.has_time_conflict()

    def __str__(self) -> str:
        result = ''
        i = 0
        for course in self.course_selection_option_manager.courses:
            result += "     "+"course " + str(i) + ":\n     "
            result += str(course)
            i += 1
            result += "\n"
        return result