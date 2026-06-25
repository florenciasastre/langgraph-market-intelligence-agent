```python
import streamlit as st
import os
from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import StateGraph, END


# 1. Page Configuration
st.set_page_config(
    page_title="Enterprise Market Intelligence Agent",
    layout="wide"
)

st.title("Enterprise Market Intelligence Agent")
st.markdown(
    "Real-time market intelligence powered by LangGraph, Gemini, and Tavily."
)


# 2. Sidebar: API Key Configuration
with st.sidebar:
    st.header("API Configuration")

    google_key = st.text_input("Google API Key", type="password")
    tavily_key = st.text_input("Tavily API Key", type="password")

    if google_key and tavily_key:
        os.environ["GOOGLE_API_KEY"] = google_key
        os.environ["TAVILY_API_KEY"] = tavily_key
        st.success("APIs configured successfully")


# 3. Agent State Definition
class AgentState(TypedDict):
    question: str
    search_results: str
    executive_brief: str


# 4. LangGraph Nodes
def market_research_node(state: AgentState):
    """
    Performs real-time market research using Tavily.
    """
    search = TavilySearchResults(max_results=5)
    results = search.invoke(state["question"])

    return {"search_results": str(results)}


def executive_brief_node(state: AgentState):
    """
    Converts real-time search results into a concise executive briefing.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    prompt = f"""
You are an expert Market Intelligence Analyst.

Based on the real-time search context provided, generate a concise Executive Briefing for a C-level audience.

Highlight:
- Key events
- Market implications
- Strategic risks
- Potential opportunities
- Recommended executive considerations

Maintain a highly professional, objective tone.

SEARCH CONTEXT:
{state["search_results"]}

BUSINESS QUESTION:
{state["question"]}

OUTPUT FORMAT:
1. Executive Summary
2. Key Market Signals
3. Strategic Implications
4. Risks to Monitor
5. Recommended Next Steps
"""

    response = llm.invoke(prompt)

    return {"executive_brief": response.content}


# 5. Workflow Construction
workflow = StateGraph(AgentState)

workflow.add_node("market_research", market_research_node)
workflow.add_node("executive_brief", executive_brief_node)

workflow.set_entry_point("market_research")
workflow.add_edge("market_research", "executive_brief")
workflow.add_edge("executive_brief", END)

app_graph = workflow.compile()


# 6. User Interface
if google_key and tavily_key:
    user_question = st.text_input(
        "Market intelligence request",
        placeholder="Example: What are the latest strategic moves in generative AI for enterprise software?"
    )

    if user_question:
        with st.spinner("Running market research and generating executive briefing..."):
            try:
                inputs = {"question": user_question}
                result = app_graph.invoke(inputs)

                st.markdown("---")
                st.subheader("Executive Briefing")
                st.write(result["executive_brief"])

                with st.expander("Source Data: Tavily Search Results"):
                    st.code(result["search_results"], language="text")

            except Exception as e:
                st.error(f"An error occurred while generating the briefing: {str(e)}")
                st.info("Please verify that your API keys are valid and have available credits.")

else:
    st.warning("Enter your Google and Tavily API keys in the sidebar to start.")
```
