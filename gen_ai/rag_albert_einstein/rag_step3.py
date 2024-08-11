"""
Step 3:
Initialize the Qdrant vector DB from rag_conf.QDRANT_PATH folder
Ask questions to the RAG model
"""

import rag_conf
import getpass
from langchain_community.vectorstores import Qdrant
from langchain_openai import OpenAIEmbeddings 
from langchain_community.llms import OpenAI


#Enter OpenAI key
# os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

#Load Vector DB from the local folder
embeddings = OpenAIEmbeddings(model=rag_conf.EBEDINGS_MODEL)
doc_store = Qdrant.from_existing_collection(    
    embedding=embeddings,
    path=rag_conf.QDRANT_PATH,
    collection_name=rag_conf.QDRANT_COLLECTION_NAME
)


# ask questions
llm = OpenAI(model_name='gpt-3.5-turbo-instruct')

while True:

    question = input('Your question: ') #  When was Albert Einstein born?

    from langchain.chains import RetrievalQAWithSourcesChain
    qa = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=doc_store.as_retriever(),
        return_source_documents=True,
        
        reduce_k_below_max_tokens=True,
        max_tokens_limit=3000,
        verbose=True
    )

    result = qa(question)
    print(f"Answer: {result}")


