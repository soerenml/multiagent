from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

"""
State(TypedDict): Think of State as a special box where we store all the
messages in the conversation. These messages can come from you or the robot.
Whenever someone says something, it gets added to this box.
"""
class State(TypedDict):
    """
    Annotated[list, add_messages]: This tells the robot that whenever a new
    message arrives, it doesn't throw away the old ones. Instead, it adds the
    new message to the list of all the messages we've seen so far. It’s like
    writing all the conversation down in one big notebook.
    """
    messages: Annotated[list, add_messages]

"""
StateGraph(State): This is like a map that guides how the chatbot moves
through the conversation. It starts at a certain point, does something,
and eventually reaches an end. The StateGraph helps keep track of where we
are in the conversation.
"""
graph_builder = StateGraph(State)