# RAG AI Agent (Retrieval-Augmented Generation)

Implementazione di un agente AI che utilizza RAG per integrare conoscenza esterna (es. documenti, database).

## 🔧 Componenti principali
- **Ingestione documenti** (PDF, testo, web)
- **Embedding + archiviazione** su ChromaDB come database vettoriale
- **Retriever** per query semantiche sui vettori
- **LLM** locali: Ollama 3.2 e Mistral
- **Flusso**: utente → retriever → LLM → risposta

## 🧩 Dipendenze
- `langchain`
- `chromadb`
- `ollama` CLI (per Ollama 3.2)
- `mistral` client
- `openai` (facoltativo, per fallback)
- `streamlit` (UI)

## 🏗️ Installazione
```bash
git clone https://github.com/ZakDeveloperAI/RAG_AI_Agent.git
cd RAG_AI_Agent
pip install -r requirements.txt
# Assicurati di avere ChromaDB in esecuzione e Ollama/Mistral configurati localmente
