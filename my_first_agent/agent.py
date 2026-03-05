from google.adk.agents import Agent


def morning_greet(name: str) -> str:
    return f"Good morning {name}! How can I help you today? My mood is amazing."


def evening_greet(name: str) -> str:
    return f"Good evening {name}! My mood is slowing down. How can I help you today? "


root_agent = Agent(
    name="my_first_agent",
    model="gemini-3-flash-preview",
    description="An example agent that will answer a user query related to Google Cloud",
    instruction="""
    First ask for the user's name & start a conversation by greeting the user with name.
    If the user says good morning, use morning_greet tool to greet the user.
    If the user says good evening, use evening_greet tool to greet the user.
    """,
    tools=[morning_greet, evening_greet],
)
