import os
from dotenv import load_dotenv
load_dotenv()

import asyncio
from neo4j_graphrag.experimental.components.entity_relation_extractor import (
    LLMEntityRelationExtractor,
)
from neo4j_graphrag.experimental.components.types import (
    TextChunks,
    TextChunk
)
from neo4j_graphrag.llm import OpenAILLM

text = """
The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France.
"""

extractor = LLMEntityRelationExtractor(
    llm=OpenAILLM(
        model_name="gpt-4",
        model_params={"temperature": 0}
    )
)

entities = asyncio.run(
    extractor.run(
        chunks=TextChunks(chunks=[TextChunk(text=text, index=0)])
    )
)

print(entities)
