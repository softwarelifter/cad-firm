import warnings
from dotenv import load_dotenv

load_dotenv()
import os

openai_model = os.getenv("OPENAI_MODEL_NAME")
openai_key = os.getenv("OPENAI_API_KEY")


warnings.filterwarnings("ignore")
from crewai import Crew

# from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool


from app.planning_dept.workers.lead_architect import lead_architect
from app.planning_dept.workers.design_architect import design_architect
from app.sketching_dept.workers.sketch_artist import sketch_artist
from app.lisp_dept.workers.drafts_person import drafts_person
from app.lisp_dept.workers.autolisp_qa import autolisp_tester
from app.planning_dept.tasks.solution_design import solution_designing
from app.planning_dept.tasks.solution_design_qa import (
    solution_qa_review,
    create_plan_json,
)
from app.lisp_dept.tasks.generate_autolisp import autolisp_generation
from app.lisp_dept.tasks.autolisp_qa import autolisp_qa_review
from app.sketching_dept.tasks.sketch import sketch_css, sketch_html
from app.utils.plan_number import PlanNumber


planner_crew = Crew(
    agents=[lead_architect, design_architect],
    tasks=[
        solution_designing,
        solution_qa_review,
    ],
    verbose=2,
)
sketch_css_crew = Crew(
    agents=[sketch_artist],
    tasks=[sketch_css],
    verbose=2,
)
sketch_html_crew = Crew(
    agents=[sketch_artist],
    tasks=[sketch_html],
    verbose=2,
)

# generation_crew = Crew(
#     agents=[
#         drafts_person,
#         autolisp_tester,
#     ],
#     tasks=[autolisp_generation, autolisp_qa_review],
#     verbose=2,
# )
planner_inputs = {
    "plan_number": "1",
    "customer": "yadav&yadav.ai",
    "person": "Suraj Yadav",
    "project": "Building Design",
    "inquiry": "I need help with my building design."
    "The plot size is 40 feet by 60 feet. It is a single floor building."
    "I want 3 master bedroom with attached bathroom and 1 guest with common bathroom. "
    "Leave remaining area for parking space\n"
    "Can you provide me with design plan in detail for this house?",
}


# inputs = {
#     "customer": "yadav&yadav.ai",
#     "person": "Suraj Yadav",
#     "project": "Building Design",
#     "inquiry": "I need help creating an autolisp script for autocad. for my building design. "
#     "The plot size is 40 feet by 60 feet. "
#     "I want 3 master bedroom with attached bathroom and 1 guest with common bathroom. "
#     "I also need a kitchen, living room, and drawing room."
#     "The building should be 1 floor with a parking space for 2 cars."
#     "The rooms should be around the living room. kitchen should be near the drawing room and it is open kitchen. "
#     "Can you provide me with a detailed autolisp script for this house?",
# }
plan_number = PlanNumber()
plan_number.number = 1
plan_result = planner_crew.kickoff(inputs=planner_inputs)
sketch_css_res = sketch_css_crew.kickoff(inputs={"building_plan": plan_result})
sketch_html = sketch_html_crew.kickoff(
    inputs={
        "drawing_css": sketch_css_res,
    }
)
# create_lisp_file(filename="buildinghouse-plan-doc-2", content=plan_result)
# script_result = generation_crew.kickoff(inputs={"inquiry": plan_result})
# create_lisp_file(filename="buildinghouse-plan-script-2", content=script_result)
