from CourseSelectionOption import CourseSelectionOption
from MeetingSection import MeetingSection

class CourseSelectionOptionManager:
    def __init__(self):
        self.courses = []

    def add_course(self, course: 'CourseSelectionOption'):
        self.courses.append(course)

    def remove_course(self, course: 'CourseSelectionOption'):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print("course doesn't exist")


    def get_meeting_sections(self) -> 'list[list[MeetingSection]]':
        result = []
        for course in self.courses:
            result.append(course.meeting_section)
        return result
