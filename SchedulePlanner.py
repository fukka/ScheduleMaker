from CourseManager import CourseManager
from Schedule import Schedule

class SchedulePlanner():
    def __init__(self, course_manager:'CourseManager'):
        self.course_manager = course_manager

    def make_schedule(self) -> 'list[Schedule]':
        schedule = Schedule()
        schedule_list = []
        if len(self.course_manager.courses) > 0:
            new_schedule_list = []
            schedule_list = schedule.add_course(self.course_manager.courses[0])
            for course in self.course_manager.get_courses()[1:]:
                for schedule in schedule_list:
                    new_schedule_list += schedule.add_course(course)
                schedule_list = new_schedule_list
                new_schedule_list = []
        return schedule_list

    def make_nonconflicting_schedule(self) -> 'list[Schedule]':
        schedule = Schedule()
        schedule_list = []
        if len(self.course_manager.courses) > 0:
            new_schedule_list = []
            schedule_list = schedule.add_course(self.course_manager.courses[0])
            for course in self.course_manager.get_courses()[1:]:
                for schedule in schedule_list:
                    schedule.sort_by_time_period_manager()
                    #if schedule.has_time_conflict():
                     #   print(schedule)
                    if not schedule.has_time_conflict():
                        #print(course.code)
                        new_schedule_list += schedule.add_course(course)
                schedule_list = new_schedule_list[::]
                new_schedule_list = []
        return schedule_list