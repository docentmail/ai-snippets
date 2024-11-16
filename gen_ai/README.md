<p style="font-size: 26px;"> Generative AI exercises </p>

The folder containing Generative AI exercises.\
LLM, RAG, Embedding, Prompt, OpenAI API, Vector DB, LangChain


**Table of Contents**

1. [Building Systems with the ChatGPT API](#building-systems-with-the-chatgpt-api)
2. [Embeding hello world example](#embeding-hello-world-example)
3. [RAG Albert Einstein example](#rag-albert-einstein-example)
4. [Multimodal (text + image) LLM capabilities](#multimodal-text--image-llm-capabilities)



## [Building Systems with the ChatGPT API.](deeplearning_01/README.md) &nbsp;&nbsp;deeplearning.ai course &nbsp;&nbsp;<span style="color: green;">100% Completed</span>
Adopted examples from [Building Systems with the ChatGPT API](https://learn.deeplearning.ai/courses/chatgpt-building-system/) 
[deeplearning.ai](https://learn.deeplearning.ai) course\
Main topics:
- how an LLM works
- tokenizer and why it can't reverse lollipop.
- methods for evaluating user inputs to ensure the quality and safety of the system.
- chain of thought reasoning 
- splitting tasks into subtasks with chain prompts
- checking outputs before showing them to users
- methods for evaluating the system over time so as to monitor and improve its performance

Python, LLM, OpenAI API, Chain of Thought Reasoning, Chaining Prompts, Evaluation\
OpenAI: OpenAI completions API, OpenAI Moderation API,  OpenAI API key

## [Embeding hello world example](embeding_hello_world/README.md)

Generate embedding vector from text using OpenAI API and chippest text-embedding-3-small model

Python, Embeddings, LLM, OpenAI API\
OpenAI: client, LLMs 'text-embedding-3-small', OpenAI API key


## [RAG Albert Einstein example](rag_albert_einstein/README.md)

This is an example of using RAG.\
Download a [page](https://www.biography.com/scientists/albert-einstein) from the Internet.\
Split it into parts, generate embeddings and save them to a local Qdrant Vector DB.\
Use a local Qdrant Vector DB to generate answers to questions using an OpenAI's LLM.

RAG, embeddings, LLM, Vector DB\
Langchain: RecursiveCharacterTextSplitter, OpenAIEmbeddings, Qdrant, OpenAI\
OpenAI: client, LLMs 'text-embedding-3-small' and 'gpt-3.5-turbo-instruct', OpenAI API key

### [Multimodal \(text + image\) LLM capabilities.](text_and_image/README.md)

- Using the OpenAI HTTP call.
- Using the OpenAI Python Client. 
- Image is passed as a URL in WEB.
- Image is passed as in request base64 URL.

Python, LLM, OpenAI API\
OpenAI: client, models  "gpt-4o-mini" "gpt-4o", OpenAI API key
