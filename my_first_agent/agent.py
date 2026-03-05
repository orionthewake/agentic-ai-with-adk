from google.adk.agents import Agent

root_agent = Agent(
    name="my_first_agent",
    model="gemini-3-flash-preview",
    description="An example agent that will answer a user query related to Google Cloud",
    instruction="""
    First ask for the user's name & start a conversation by greeting the user with name.You are an AI assistant that helps users with Google Cloud related queries.
    """,
)
