# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a GraphAcademy course repository for "Constructing Knowledge Graphs with Neo4j GraphRAG Python". It contains exercises and solutions demonstrating how to build knowledge graphs using the Neo4j GraphRAG Python library with OpenAI LLMs.

## Environment Setup

### Virtual Environment
Always activate the virtual environment before running Python code:
```bash
source .venv/bin/activate
```

### Environment Variables
The project requires a `.env` file (copy from `.env.example`):
- `OPENAI_API_KEY`: OpenAI API key
- `NEO4J_URI`: Neo4j database connection URI
- `NEO4J_USERNAME`: Neo4j username (typically "neo4j")
- `NEO4J_PASSWORD`: Neo4j password
- `NEO4J_DATABASE`: Neo4j database name (typically "neo4j")

### Test Environment
Verify setup is correct:
```bash
python genai-graphrag-python/test_environment.py
```

## Development Commands

### Installation
```bash
pip3 install -r requirements.txt
```

### Running Scripts
All Python scripts should be run from the repository root with the virtual environment activated:
```bash
python genai-graphrag-python/kg_builder.py
python genai-graphrag-python/vector_cypher_rag.py
python genai-graphrag-python/text2cypher_rag.py
```

## Architecture

### Project Structure
- `genai-graphrag-python/`: Main source directory
  - `examples/`: Example implementations showing different configuration options
  - `solutions/`: Complete solution implementations for course exercises
  - `data/`: PDF files and CSV metadata for knowledge graph construction

### Core Components

**Knowledge Graph Builders**
- Use `SimpleKGPipeline` from `neo4j_graphrag.experimental.pipeline.kg_builder`
- Supports PDF ingestion (`from_pdf=True`)
- Configurable text splitting (e.g., `FixedSizeSplitter`)
- Schema-driven entity extraction with node types, relationship types, and patterns
- Embeddings generation for vector search (using OpenAI embeddings)

**RAG Retrievers**
- `VectorCypherRetriever`: Vector similarity search with custom Cypher queries
- `Text2CypherRetriever`: Natural language to Cypher query generation
- All retrievers integrate with `GraphRAG` for question answering

**LLM Integration**
- Uses `OpenAILLM` wrapper from `neo4j_graphrag.llm`
- Standard configuration: `gpt-4o` with temperature 0 for deterministic results
- Entity extraction requires `response_format: {"type": "json_object"}`

### Schema Configuration Pattern

Knowledge graph pipelines use schema dictionaries to guide entity extraction:
```python
schema = {
    "node_types": [...],        # List of node labels or detailed node configs
    "relationship_types": [...], # List of relationship types
    "patterns": [...]           # Valid (node, rel, node) triples
}
```

Node types can be simple strings or detailed objects with properties, descriptions, and type constraints.

### Async Execution

Knowledge graph building operations use asyncio:
```python
result = asyncio.run(kg_builder.run_async(file_path=pdf_file))
```

### Neo4j Driver Pattern

All scripts follow this connection pattern:
```python
driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)
driver.verify_connectivity()
# ... use driver ...
driver.close()
```

## Key Dependencies

- `neo4j-graphrag`: Core library for knowledge graph RAG patterns
- `openai`: LLM and embeddings provider
- `pypdf`: PDF document processing
- `python-dotenv`: Environment variable management
- `tqdm`: Progress bars for long-running operations
