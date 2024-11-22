from crewai import Task

from app.lisp_dept.workers.drafts_person import drafts_person

autolisp_generation = Task(
    description=("Create a precise autolisp script for the 2d layout for {inquiry}. "),
    expected_output=(
        "A valid autolisp script that can be executed in autocad."
        "The response script must be formatted such that it has main function to run the whole script"
    ),
    agent=drafts_person,
)
