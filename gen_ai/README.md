# gen_ai
The folder containing examples for the generative AI.
LLM, RAG, Embedding, Prompt, OpenAI API, Vector DB, LangChain


## content

### embeding_hello_world

Embeding hello world example.

Generate embedding vector from text using OpenAI API and chippest text-embedding-3-small model

Python, Embeddings, LLM, OpenAI API\
OpenAI: client, LLMs 'text-embedding-3-small', OpenAI API key


### rag_albert_einstein**

RAG Albert Einstein example

This is an example of using RAG.\
Download a [page](https://www.biography.com/scientists/albert-einstein) from the Internet.\
Split it into parts, generate embeddings and save them to a local Qdrant Vector DB.\
Use a local Qdrant Vector DB to generate answers to questions using an OpenAI's LLM.

RAG, embeddings, LLM, Vector DB\
Langchain: RecursiveCharacterTextSplitter, OpenAIEmbeddings, Qdrant, OpenAI\
OpenAI: client, LLMs 'text-embedding-3-small' and 'gpt-3.5-turbo-instruct', OpenAI API key
