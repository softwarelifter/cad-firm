from crewai import Agent

autolisp_tester = Agent(
    role="Autolisp reviewer",
    goal="Review the generated autolisp by the draft person for {inquiry}. "
    " and ensure that the autolisp script is valid, it doesn't ask for any input from user in the script\n"
    "the final autolisp script should be in the form of a function, it should be"
    "executable, and adheres to the high-quality standards expected for an architect.",
    backstory=(
        "You are very experienced in reviewing of autolisp scripts."
        "you know how to identify errors and provide feedback to improve the script."
    ),
    Verbose=True,
)
