from crewai import Task
from app.sketching_dept.workers.sketch_artist import sketch_artist
from app.utils.plan_number import PlanNumber

plan_number = PlanNumber()

sketch_css = Task(
    description=(
        "Create detailed line diagram sketch and drawings of the building design based on the "
        "specifications provided by the Design Architect as follows.\n"
        "{building_plan}"
        "Ensure that the sketches are accurate, detailed with proper labeling of "
        "the elements of the buildings, and capture the essence of the design."
    ),
    expected_output=("Provide a detailed line diagram as css file."),
    agent=sketch_artist,
    output_file=f"building-plans/plan-{plan_number.number}/sketch.css",
)

sketch_html = Task(
    description=(
        "Create html file with following css for bulding drawing.\n"
        "{drawing_css}"
        "Ensure that the html sketch is accurate and uses the css provided."
    ),
    expected_output=("Provide a detailed line diagram as html file."),
    agent=sketch_artist,
    output_file=f"building-plans/plan-{plan_number.number}/sketch.html",
)
