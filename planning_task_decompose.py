import json
from llm_client import ask

goal = "Launch a new product page: write the copy, design a banner, and publish it."

#linear plan

linear_plan = ask(
    "Break this goal into a simple numbered list of steps, in the order they should happen.",
    goal
)
print("Linear plan")
print(linear_plan)

#dag-style plan

dag_pompt=f"""Break this goal into steps as JSON. 
Each step has an id, a description, and a list of "depends_on" step ids(empty list if it can start immediately).
Return ONLY JSON in this shape:
[{{"id":1, "description":"...", "depends_on":[]}}, ...]

Goal:{goal}"""

dag_plan_raw = ask("You are a project planner.", dag_pompt)
print("dag_plan_raw")


try:
    dag_plan =json.loads(dag_plan_raw)
    print("Parsed step ehich can start right now - no dependencies")
    for step in dag_plan:
        if not step["depends_on"]:
            print(f" Step {step['id']}: {step['description']}")
except json.JSONDecodeError:
    print("(Model didn't return clean JSON this time -- tru again or add stricter formatting instructions)")



#dynamic replan

original_step = "Design a banner using the in-house desgin tool."
failure = "The i-house design tool is down for maintenance."

replan = ask(
    "A planned step failed. Suggest ONE alternative way to achieve the"
    "same underlying goal, given the failure reason.",
    f"Original step: {original_step}\nFailure:{failure}"
)
print("Replanned step:", replan)