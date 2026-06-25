# LangGraph Market Intelligence Agent

## Automated OSINT for Executive Decision-Making

`LangGraph Market Intelligence Agent` is a stateful agentic workflow designed to automate real-time market research and generate concise executive briefings from live web data.

The system combines **LangGraph**, **LangChain**, **Tavily Search**, **Gemini 2.5 Flash**, and **Streamlit** to transform open-source intelligence into structured, C-level insights.

---

## The Business Context: Automated OSINT

In fast-moving industries such as **technology, iGaming, finance, and regulated digital markets**, staying updated on competitor moves, regulatory shifts, product launches, and market signals requires constant monitoring.

Traditional manual OSINT workflows are time-consuming, fragmented, and difficult to scale.

Standard LLMs also introduce limitations:

* Knowledge cut-offs
* Hallucination risk
* Lack of source traceability
* Limited suitability for time-sensitive market intelligence

This project explores how agentic workflows can reduce manual research time by grounding executive summaries in real-time search results.

---

## The Solution

This repository demonstrates a **stateful market intelligence agent** built with LangGraph.

The agent performs two core functions:

1. Retrieves real-time market data through Tavily Search.
2. Synthesizes the retrieved information into a concise executive briefing using Gemini 2.5 Flash.

The goal is to support faster, more reliable business analysis by ensuring the LLM generates its output from live search context rather than static model memory.

---

## Architecture: The State Graph

The system is built as a deterministic multi-step workflow using **LangGraph**.

Each step in the process is represented as a node in the graph.

### 1. State Management

The workflow uses a strictly typed `AgentState` dictionary to carry information across nodes.

The state includes:

* User query
* Search results
* Final executive briefing

This makes the agent easier to inspect, debug, and extend.

### 2. Market Research Node

The research node uses **Tavily Search API** to retrieve real-time information from the web.

This step helps bypass LLM knowledge cut-offs and provides external context for the final briefing.

### 3. Executive Briefing Node

The synthesis node uses **Gemini 2.5 Flash** to transform raw search results into a structured executive briefing.

The output is designed for C-level readability and includes:

* Executive summary
* Key market signals
* Strategic implications
* Risks to monitor
* Recommended next steps

### 4. Source Traceability

The Streamlit interface includes a source-inspection section showing the raw Tavily search results used by the agent.

This supports:

* AI governance
* Output verification
* Source inspection
* Auditability
* Trust in AI-assisted research

---

## Technical Stack

**Agent Orchestration**
LangGraph · LangChain

**LLM**
Google Gemini 2.5 Flash

**Search / OSINT Layer**
Tavily Search API

**Frontend**
Streamlit

**Language**
Python

---

## Operational Value

### Research Efficiency

Reduces the time required to compile a market event briefing from manual research cycles to an automated workflow.

### Real-Time Awareness

Uses live web search to support time-sensitive analysis of competitors, regulations, product launches, and market movements.

### Hallucination Mitigation

Grounds the final briefing in retrieved search context rather than relying only on model memory.

### Executive Readability

Transforms raw search data into concise, structured insights suitable for strategic decision-making.

### Scalable Architecture

The modular graph architecture allows new nodes to be added easily, such as:

* Compliance checker
* Risk scoring layer
* Source ranking node
* Sentiment analysis node
* Competitor comparison node
* Human approval checkpoint

---

## Business Use Cases

This type of agent can support:

* Competitive intelligence
* Regulatory monitoring
* iGaming market analysis
* Technology trend tracking
* Financial market research
* Product launch monitoring
* Executive brief generation
* Strategic planning workflows

---

## Why It Matters

Organizations do not only need access to information.

They need fast, reliable, structured intelligence that helps leaders understand what changed, why it matters, and what risks or opportunities should be monitored next.

This project demonstrates how agentic workflows can turn open-source information into actionable business intelligence.

---

## Status

Proof of concept.

This project demonstrates how LangGraph-based workflows can automate real-time market research, improve source traceability, and generate executive-ready intelligence briefings.
