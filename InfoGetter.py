import requests
import json

from Course import Course
from Location import Location
from MeetingSection import MeetingSection
from Time import Time

API_KEY = "kkzDO0EXFmfAHD7ApPP7HIrZvpPaDcKw"


def object_decoder(obj):
    meeting_sections = []
    for meeting_section in obj["meeting_sections"]:
        times = []
        for time in meeting_section["times"]:
            times.append(Time(day=time["day"], start=time["start"], end=time["end"], duration=time["duration"], location=Location(time["location"])))
        meeting_sections.append(MeetingSection(code=meeting_section["code"], size=meeting_section["size"],
                                               enrolment=meeting_section["enrolment"], times=times,
                                               instructors=meeting_section["instructors"]))

    # code: str, size: int, enrolment: int, times: 'list[Time]', instructors: 'list[str]'):
    if True:  # '__type__' in obj and obj['__type__'] == 'Course':
        return Course(ID=obj["id"], code=obj["code"], name=obj["name"], description=obj["description"],
                      division=obj["division"], department=obj["department"], prerequisites=obj["prerequisites"],
                      exclusions=obj["exclusions"], level=obj["level"], campus=obj["campus"], term=obj["term"],
                      meeting_sections=meeting_sections, breadths=obj["breadths"])



def get_course(course_id: str) -> 'Course':
    r = requests.get("https://cobalt.qas.im/api/1.0/courses/" + course_id + "/?key=" + API_KEY)
    return object_decoder(r.json())



if __name__ == "__main__":
    course_id = "ABP100Y1Y20169"
    course = get_course("ABP100Y1Y20169")

