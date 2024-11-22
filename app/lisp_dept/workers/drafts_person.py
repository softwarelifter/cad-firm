from crewai import Agent

drafts_person = Agent(
    role="Technical Drawing Specialist",
    goal="Create precise autolisp script for 2d layout for {inquiry}.",
    backstory=(
        "You are a autocad professional with experience in converting 2d layout plans "
        "into executable executable, valid autolisp scripts."
    ),
    allow_delegation=False,
    Verbose=True,
)
