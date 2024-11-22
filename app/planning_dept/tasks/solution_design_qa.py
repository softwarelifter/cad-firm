from crewai import Task
from app.planning_dept.workers.lead_architect import lead_architect
from app.planning_dept.responses.building_plan import BuildingPlan
from app.utils.plan_number import PlanNumber

plan_number = PlanNumber()

solution_qa_review = Task(
    description=(
        "Review the response drafted by the Design Architect for {customer}'s inquiry:\n"
        "{inquiry}"
        "Ensure that the plan is comprehensive, accurate, and adheres to the "
        "high-quality standards expected for building architect.\n"
    ),
    expected_output=(
        "A final, detailed markdown document, building's design plan."
        "Check if the design contains proper measurements of all the building spaces/areas/zones, "
        "the components are properly placed, and the design meets the {customer}'s needs. "
        "The plan adheres to the high-quality standards expected for building architect."
    ),
    agent=lead_architect,
    output_file=f"building-plans/plan-{plan_number.number}/prd.md",
)

create_plan_json = Task(
    description=("Create a json file for the building plan."),
    expected_output=("A json file containing the building plan."),
    agent=lead_architect,
    output_json=BuildingPlan,
    output_file=f"building-plans/plan-{plan_number.number}/prd.json",
)
