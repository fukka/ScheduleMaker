from CourseSelectionOption import CourseSelectionOption
from MeetingSection import MeetingSection

class Course():
    def __init__(self, ID:str, code:str, name:str, description:str, division:str, department:str, prerequisites:str,
                 exclusions:str, level:int, campus: str, term:str, meeting_sections: 'list[MeeingSection]', breadths: 'list[int]'):
        self.ID = ID
        self.code = code
        self.name = name
        self.description = description
        self.division = division
        self.department = department
        self.prerequisites = prerequisites
        self.exclusions = exclusions
        self.level = level
        self.campus = campus
        self.term = term
        self.breadths = breadths
        self.meeting_sections = meeting_sections

    def get_course_selection_options(self) -> 'list[CourseSelectionOption]':
        course_selection_options = []
        lec_meeting_sections = self.get_lec_meeting_section()
        tut_meeting_sections = self.get_tut_meeting_section()
        pra_meeting_sections = self.get_pra_meeting_section()
        if len(lec_meeting_sections) > 0:
            for lec_meeting_section in lec_meeting_sections:
                if len(tut_meeting_sections) > 0:
                    for tut_meeting_section in tut_meeting_sections:
                        if len(pra_meeting_sections) > 0:
                            for pra_meeting_section in pra_meeting_sections:
                                course_selection_option = CourseSelectionOption(self.ID)
                                course_selection_option.add_meeting_section(lec_meeting_section)
                                course_selection_option.add_meeting_section(tut_meeting_section)
                                course_selection_option.add_meeting_section(pra_meeting_section)
                                course_selection_options.append(course_selection_option)
                        else:
                            course_selection_option = CourseSelectionOption(self.ID)
                            course_selection_option.add_meeting_section(lec_meeting_section)
                            course_selection_option.add_meeting_section(tut_meeting_section)
                            course_selection_options.append(course_selection_option)
                else:
                    if len(pra_meeting_sections) > 0:
                        for pra_meeting_section in pra_meeting_sections:
                            course_selection_option = CourseSelectionOption(self.ID)
                            course_selection_option.add_meeting_section(lec_meeting_section)
                            course_selection_option.add_meeting_section(pra_meeting_section)
                            course_selection_options.append(course_selection_option)
                    else:
                        course_selection_option = CourseSelectionOption(self.ID)
                        course_selection_option.add_meeting_section(lec_meeting_section)
                        course_selection_options.append(course_selection_option)
        else:
            if len(tut_meeting_sections) > 0:
                for tut_meeting_section in tut_meeting_sections:
                    if len(pra_meeting_sections) > 0:
                        for pra_meeting_section in pra_meeting_sections:
                            course_selection_option = CourseSelectionOption(self.ID)
                            course_selection_option.add_meeting_section(tut_meeting_section)
                            course_selection_option.add_meeting_section(pra_meeting_section)
                            course_selection_options.append(course_selection_option)
                    else:
                        course_selection_option = CourseSelectionOption(self.ID)
                        course_selection_option.add_meeting_section(tut_meeting_section)
                        course_selection_options.append(course_selection_option)
            else:
                if len(pra_meeting_sections) > 0:
                    for pra_meeting_section in pra_meeting_sections:
                        course_selection_option = CourseSelectionOption(self.ID)
                        course_selection_option.add_meeting_section(pra_meeting_section)
                        course_selection_options.append(course_selection_option)
        return course_selection_options

    def get_lec_meeting_section(self) -> 'list[MeetingSection]':
        lec_meeting_sections = []
        for meeting_section in self.meeting_sections:
            if meeting_section.code[0] == 'L':
                lec_meeting_sections.append(meeting_section)
        return lec_meeting_sections

    def get_tut_meeting_section(self) -> 'list[MeetingSection]':
        tut_meeting_sections = []
        for meeting_section in self.meeting_sections:
            if meeting_section.code[0] == 'T':
                tut_meeting_sections.append(meeting_section)
        return tut_meeting_sections

    def get_pra_meeting_section(self) -> 'list[MeetingSection]':
        pra_meeting_sections = []
        for meeting_section in self.meeting_sections:
            if meeting_section.code[0] == 'R':
                pra_meeting_sections.append(meeting_section)
        return pra_meeting_sections

    def __str__(self):
        result = ""
        result += str(self.ID) + "\n    "
        for meeting_section in self.meeting_sections:
            result += str(meeting_section) + "\n    "
        return result