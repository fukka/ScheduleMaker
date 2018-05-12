from Course import Course
from MeetingSection import MeetingSection

class CourseManager:
    def __init__(self):
        self.courses = []

    def add_course(self, course:'Course'):
        self.courses.append(course)

    def remove_course(self, course:'Course'):
        if course in self.get_courses():
            self.courses.remove(course)
        else:
            print("course doesn't exist")

    def get_courses(self) -> 'list[Course]':
        return self.courses

    def get_meeting_sections(self) -> 'list[list[MeetingSection]]':
        result = []
        for course in self.get_courses():
            result.append(course.meeting_sections)
        return result
        
