from crewai import Task

from app.planning_dept.workers.design_architect import design_architect

solution_designing = Task(
    description=(
        "{customer} just reached out for a building design plan as following:\n"
        "{inquiry}\n"
        "{person} from {customer} is the one that reached out. "
        "Provide a detailed structural design plan for the building.\n"
        "Ask as many questions as needed to understand the requirements.\n"
    ),
    expected_output=(
        "A detailed  design plan that meets the customer's needs."
        "The design must contain proper measurements of all the building spaces/areas/zones."
        "The design must include the tentative location of all the building elements such "
        "that all the elements fit properly in the given plot as per the plan."
    ),
    agent=design_architect,
)
