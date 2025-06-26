
---

## 📙 LangGraph_AI_Agent_System

```markdown
# LangGraph AI Agent System

Un sistema multi-agente orchestrato tramite grafi con LangGraph.

## 🎯 Scopo
Coordinare più agenti specializzati che cooperano per task complessi tramite un grafo di flusso.

## 🛠 Tecnologie principali
- **LangGraph** per definire il grafo e la logica di orchestrazione
- **FastAPI** + Uvicorn per esporre le API
- **LLM** remoto: Google Gemini via API
- **Agent types**:
  - **Retrieval Agent**: interroga ChromaDB o altro retriever
  - **Classification Agent**: etichetta input/testo
  - **Persona Simulator Agent**: simula comportamenti/risposte di un utente

## 📦 Dipendenze
- `langgraph`
- `fastapi`, `uvicorn`
- `requests` (per chiamate a Gemini)
- `pytest`

## 🧭 Setup
```bash
git clone https://github.com/ZakDeveloperAI/LangGraph_AI_Agent_System.git
cd LangGraph_AI_Agent_System
pip install -r requirements.txt
export GEMINI_API_KEY="..."
uvicorn main:app --reload
