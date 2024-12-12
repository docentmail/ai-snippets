import os
from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete, gpt_4o_complete

"""
This script initializes a LightRAG instance and performs various types of queries 
(naive, local, global, and hybrid) on the data extracted from a text file.

Modules:
    os: Provides functions for interacting with the operating system.
    lightrag: A library for lightweight retrieval-augmented generation (RAG) systems.
    lightrag.llm: Contains functions for large language model integration.

Usage:
    Execute this script to:
    1. Initialize a LightRAG graph database.
    2. Perform different search modes (naive, local, global, hybrid) on the data.

Script Variables:
    WORKING_DIR: Directory where LightRAG will store its data.

Search Modes:
    - Naive: Basic search functionality.
    - Local: Limited to local context.
    - Global: Broad, across the entire knowledge base.
    - Hybrid: Combines local and global search.

Note:
    If running in a Jupyter notebook, uncomment the lines importing and applying `nest_asyncio` 
    to handle asynchronous operations in `rag.insert()`.
"""

# Uncomment the following lines if running in a Jupyter notebook to handle async nature of rag.insert()
# import nest_asyncio
# nest_asyncio.apply()

WORKING_DIR = "./dickens"

# Check the working directory exists
if not os.path.exists(WORKING_DIR):
    exit(f"Error: The working directory '{WORKING_DIR}' does not exist.")
    

# Initialize the LightRAG instance with a specified LLM model function
rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=gpt_4o_mini_complete  # Use gpt_4o_mini_complete LLM model
    # llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
)

# Perform naive search
print("\n\n ----------- Naive Search: ----------- ")
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="naive")))

# Perform local search
print("\n\n ----------- Local Search: ----------- ")
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="local")))

# Perform global search
print("\n\n ----------- Global Search: ----------- ")
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="global")))

# Perform hybrid search
print("\n\n ----------- Hybrid Search: ----------- ")
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="hybrid")))
