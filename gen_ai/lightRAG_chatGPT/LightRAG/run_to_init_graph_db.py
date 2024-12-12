import os
from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete, gpt_4o_complete

"""
This script initializes a LightRAG instance and populates its graph representation 
with knowledge extracted from the content of a text file ('book.txt').

Modules:
    os: Provides functions for interacting with the operating system.
    lightrag: A library for lightweight retrieval-augmented generation (RAG) systems.
    lightrag.llm: Contains functions for large language model integration.

Usage:
    Execute the script to initialize a graph database and populate it with the
    knowledge contained in the 'book.txt' file.
"""

# Uncomment the following lines if running in a Jupyter notebook to handle async nature of rag.insert()
# import nest_asyncio
# nest_asyncio.apply()

WORKING_DIR = "./dickens"

# Ensure the working directory exists
if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

# Initialize the LightRAG instance with a specified LLM model function
rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=gpt_4o_mini_complete  # Use gpt_4o_mini_complete LLM model
    # llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
)

# Read the content of 'book.txt' and populate the LightRAG graph representation
with open("./book.txt") as f:
    rag.insert(f.read())
