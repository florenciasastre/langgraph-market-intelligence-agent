LangGraph Market Intelligence Agent
The Business Context: Automated OSINT
In fast-paced industries (Tech, iGaming, Finance), staying updated with competitor moves and regulatory shifts requires countless hours of manual OSINT (Open Source Intelligence) gathering. Standard LLMs cannot solve this due to their knowledge cut-offs and hallucination risks.

This repository demonstrates a stateful, Agentic Workflow using LangGraph to automate market research. It guarantees real-time accuracy by forcing the LLM to synthesize data strictly from live web searches, creating rapid, auditable executive briefings.

Architecture (The State Graph)
Built with LangChain and LangGraph, the system operates as a deterministic multi-step agent:

State Management: Utilizes a strictly typed dictionary (AgentState) to carry the query, search context, and final output across nodes.

Research Node (Tavily): Executes a targeted web search to gather real-time, objective data, bypassing LLM knowledge limitations.

Synthesis Node (Gemini 2.5 Flash): Ingests the raw search data and compiles an executive briefing tailored for C-level readability.

Traceability: Includes a source-inspection UI, essential for AI Governance and verifying the exact URLs used for the briefing.

Tech Stack
Orchestration: LangGraph, LangChain

LLM: Google Gemini 2.5 Flash

Tools: Tavily Search API

Frontend: Streamlit

Operational Value
Efficiency: Reduces the time to compile a market event briefing from hours to seconds.

Accuracy: Mitigates hallucinations by grounding the generation strictly in retrieved Tavily search results.

Scalability: The modular Graph architecture allows for easy insertion of new nodes (e.g., adding a "Compliance Checker" node before the final output).
