from MeetingSection import MeetingSection
class CourseSelectionOption():
    def __init__(self, ID:str):
        self.ID = ID
        self.lec = None
        self.tut = None
        self.pra = None

    def add_meeting_section(self, meeting_section: 'MeetingSection'):
        if meeting_section.code[0] == 'L':
            self.lec = meeting_section
        elif meeting_section.code[0] == 'T':
            self.tut = meeting_section
        else:
            self.pra = meeting_section

    def __str__(self):
        result = ""
        result += str(self.ID) + str(self.lec) + str(self.tut) + str(self.pra)
        return result