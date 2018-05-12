from SchedulePlanner import SchedulePlanner
from CourseManager import CourseManager
import InfoGetter
import sys
# course_id = "ABP100Y1Y20169"
#
# course = InfoGetter.get_course(course_id = "ABP100Y1Y20169")
# print(course)
# print("\n\n\n\n\n")
course_manager = CourseManager()
# course_manager.add_course(course)
# course = InfoGetter.get_course("AER372H1S20181")
#
# print(course)
# print("\n\n\n\n\n")
# course_manager.add_course(course)
##
#course = InfoGetter.get_course("MAT135H1S20181")
#course_manager.add_course(InfoGetter.get_course("MAT135H1S20181"))
course_manager.add_course(InfoGetter.get_course("CSC207H1F20179"))
course_manager.add_course(InfoGetter.get_course("CSC258H1F20179"))
course_manager.add_course(InfoGetter.get_course("MAT244H1F20179"))
course_manager.add_course(InfoGetter.get_course("ABP100Y1Y20169"))
#course = InfoGetter.get_course("MAT135H1S20181")
#course_manager.add_course(InfoGetter.get_course("MAT223H1S20181"))
#course_manager.add_course(InfoGetter.get_course("CSC148H1S20181"))
#course_manager.add_course(InfoGetter.get_course("ECO102H1S20181"))
#course_manager.add_course(InfoGetter.get_course("CSC209H1S20181"))
##
schedule_planner = SchedulePlanner(course_manager)
list_of_schedule = schedule_planner.make_nonconflicting_schedule()
#list_of_schedule = schedule_planner.make_schedule()
print(list_of_schedule)
i = 0
for schedule in list_of_schedule:
    print("schedule"  +" " + str(i) +"\n   " + str(schedule))
    i += 1
print(sys.getsizeof(list_of_schedule))