from fastapi import FastAPI, HTTPException, status
from uuid import UUID
from typing import Union, Optional
from multipart import multipart
from pydantic import BaseModel, validator
from enum import Enum 
import datetime



starter = FastAPI()

class level(Enum):
    Beginner = 1,
    Intermediate = 2,
    Advanced = 3

class Course(BaseModel):
    title: str 
    level: int 
    teacher: str 
    students: Optional[list[str]] = []

class Student(BaseModel):
    first_name: str
    last_name: str 
    age : int
    date_joined: datetime.date 
    level: Optional[level]

    @validator("age")
    def validate_age(cls, v):
       if v < 0:
            raise ValueError("Age cannot be negative")
       return v
    
    @validator("level")
    def validate_level(cls, level, values):
        if level != None:
            if level is level.Beginner and( values["age"] < 9 or values["age"] > 12):
                raise ValueError("You have to be between 9 and 12 years old to join this class")
            print(values)
        return level


students = [
    Student(
        first_name = "Jane",
        last_name = "Smith",
        age = 11,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Beginner
    ),
    Student(
        first_name = "Ade",
        last_name = "Ola",
        age = 15,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Intermediate
    ),
    Student(
        first_name = "Grace",
        last_name = "Akoh",
        age = 13,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Intermediate
    ),
    Student(
        first_name = "Balkis",
        last_name = "Audu",
        age = 9,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Beginner
    ),
    Student(
        first_name = "Peter",
        last_name = "Jones",
        age = 17,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Advanced
    ),
    Student(
        first_name = "John",
        last_name = "Abraham",
        age = 16,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Advanced
    ), 
    Student(
        first_name = "Babajide",
        last_name = "Cole",
        age = 18,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Advanced
    ),
    Student(
        first_name = "Jane",
        last_name = "Smith",
        age = 11,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Beginner
    ),
    Student(
        first_name = "Ashabi",
        last_name = "Dollar",
        age = 16,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Advanced
    ),
    Student(
        first_name = "Rebecca",
        last_name = "Smith",
        age = 14,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Intermediate
    ),
    Student(
        first_name = "Femi",
        last_name = "Johnson",
        age = 15,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Intermediate
    ),
    Student(
        first_name = "Loveth",
        last_name = "Paul",
        age = 10,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Beginner
    ),
    Student(
        first_name = "Beatrice",
        last_name = "Olowu",
        age = 12,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Beginner
    ),
    Student(
        first_name = "Ibukun",
        last_name = "Branaid",
        age = 14,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Intermediate
    ),
    Student(
        first_name = "Josephine",
        last_name = "Peters",
        age = 15,
        date_joined = datetime.date(2020, 9, 5),
        level = level.Intermediate
    )
]
    


def beginner():   
    beginner_students = []
    for s in students:
        if s.level == level.Beginner:
            beginner_students.append(f"{s.first_name} {s.last_name}")
            return beginner_students
        
def intermediate(): 
    intermediate_students = []  
    for s in students:
        if s.level == level.Intermediate:
            intermediate_students.append(f"{s.first_name} {s.last_name}")
            return intermediate_students
        
def advanced(): 
    advanced_students = []  
    for s in students:
        if s.level == level.Advanced:
            advanced_students.append(f"{s.first_name} {s.last_name}")
            return advanced_students
        





courses = {
    1: {
        "title": "English Language",
        "level": level.Beginner,
        "teacher": "Ms. Simbi",
        "students": beginner()
    },
    2: {
        "title": "English Language",
        "level": level.Intermediate,
        "teacher": "Mr. Wright",
        "students": [intermediate()]
    },
    3: {
        "title": "English Language",
        "level": level.Advanced,
        "teacher": "Ms. Gladys",
        "students": [advanced()]
    },
    4: {
        "title": "Mathematics",
        "level": level.Beginner,
        "teacher": "Ms. Aliyu",
        "students": beginner()
    },
    5: {
        "title": "Mathematics",
        "level": level.Intermediate,
        "teacher": "Mr. John",
        "students": intermediate()
    },
    6: {
        "title": "Mathematics",
        "level": level.Advanced,
        "teacher": "Mr. Brown",
        "students": advanced()
    },
    7: {
        "title": "Science",
        "level": level.Beginner,
        "teacher": "Mr. James",
        "students": beginner()
    },
    8: {
        "title": "Science",
        "level": level.Intermediate,
        "teacher": "Mr. James",
        "students": intermediate()
    },
    9: {
        "title": "Science",
        "level": level.Advanced,
        "teacher": "Mr. Greg",
        "students": advanced()
    },
    10: {
        "title": "Computer",
        "level": level.Beginner,
        "teacher": "Ms. Silvia",
        "students": beginner()
    },
    11: {
        "title": "Computer",
        "level": level.Intermediate,
        "teacher": "Ms. Silvia",
        "students": intermediate()
    },
    12: {
    "title": "Computer",
    "level": level.Advanced,
    "teacher": "Ms. Silvia",
    "students": advanced()
    }
}



@starter.get("/")
def index():
    return{"message": "Welcome to Nora School Listing App!"}

@starter.get("/courses")
def get_courses(level: Union[int, None] = None):
    if level:
        level_course = []
        for y in courses.keys():
            if courses[y] ["level"] == level:
                level_course.append(courses[y])
        return level_course
    return courses

@starter.get("/courses/course/{id}")
def get_course(id:int):
    try:
        course = courses.get(id)
        return {"data": course}
    
    except KeyError:
        raise HTTPException(status_code = 404, detail = f"Course is not available!")
 
    
@starter.delete("/course/{id}")
def delete_course(id:int):

    try:
        del courses[id]
        return {"Message":f"Course with id: {id} has been deleted successfuly.", "data": courses}
    
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Course with id '{id}' is not available.")


@starter.post("/courses", status_code=status.HTTP_201_CREATED)
def create_course(new_course: Course):
    # new_course["id"] = len(courses) + 1
    id = max(courses.keys()) + 1
    courses[id] = new_course.dict()
    return {"Message": "New course created!", "data": courses[id]}


@starter.put("/courses/course/{id}")
def update_course(id:int, updated_course: Course):
    # course = courses.copy()
    # if id not in courses:
    #     raise HTTPException(status_code=404, detail = f"Course with id '{id}' is not available")      
    
    # course_id = list(courses)[id] - 1
    # return {"Message": f"Course with id '{course_id}' has been updated successfuly", "data": updated_course}

   
    try:
        course = courses[id]
        course["title"] = updated_course.title
        course["level"] = updated_course.level
        course["teacher"] = updated_course.teacher
        course[students] = updated_course.students
        return {"Message": f"Course with id '{id}' has been updated successfuly", "data": course}
    
    except KeyError:
        raise HTTPException(status_code=404, detail = f"Course is not available") 
    
