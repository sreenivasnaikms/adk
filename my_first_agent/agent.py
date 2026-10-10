from google.adk.agents.llm_agent import Agent

# Why root_agent?
# ADK command-line tools and the Agent Platform runtime look for a
# Python variable named root_agent as the entry point to your agent system.
#  This is a convention that allows ADK and deployment runtimes to discover, run, and deploy your agent
# “The agent.py file contains a root_agent definition, which is the only required element of an ADK agent.”
# root_agent = Agent(
# model='gemini-3.8-flash',
# name='root_agent',
#  description='A helpful assistant for user questions.',
#   instruction='Answer user questions to the best of your knowledge',
# )
root_agent = Agent(
    model='gemini-3.8-flash',
    name="math_tutor_agent",
    description="Helps students learn algebra by guiding them through problem-solving steps.",
    instruction="You are a patient math tutor. Help students with algebra problems."
)
