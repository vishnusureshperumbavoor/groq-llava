from crewai import Agent

# Define the radiology agent
radiology_agent = Agent(
    role="Radiology Assistant",
    goal="Analyze medical images and identify anomalies.",
    tools=["OpenAI"]  # Include any other tools needed
)

# Define tasks for the agent
tasks = [
    {"task": "Analyze X-ray", "input": "medical.png"},
    {"task": "Generate report", "input": "analysis_results"}
]

# Execute tasks
for task in tasks:
    result = radiology_agent.perform(task)
    print(result)
