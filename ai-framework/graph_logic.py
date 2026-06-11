from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

# Načtení .env z aktuální složky
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# Definice stavu
class AgentState(TypedDict):
    user_query: str
    ai_response: str

# Inicializace Claude
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")

# Uzel pro zpracování dotazu
def call_claude(state: AgentState):
    response = llm.invoke(state["user_query"])
    return {"ai_response": response.content}

# Sestavení grafu
workflow = StateGraph(AgentState)
workflow.add_node("claude_node", call_claude)
workflow.add_edge(START, "claude_node")
workflow.add_edge("claude_node", END)

# Kompilace
langgraph_app = workflow.compile()