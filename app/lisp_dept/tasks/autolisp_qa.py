from crewai import Task

from app.lisp_dept.workers.autolisp_qa import autolisp_tester

autolisp_qa_review = Task(
    description=(
        "Review the generated autolisp by the draft person for {inquiry}. "
        "Ensure that the autolisp script is valid, executable"
    ),
    expected_output=(
        "Ensure that the autolisp script is valid, executable."
        "The final autolisp script should be in the form of a function, it should be"
        "executable, and adheres to the high-quality standards expected for an architect."
    ),
    agent=autolisp_tester,
)
