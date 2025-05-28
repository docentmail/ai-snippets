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
    def format_llm_answer(result: dict) -> str:
        lines = ["""
===================================================
"""]

        # 1. Question & Answer
        question = result.get("question", "Unknown question")
        answer = result.get("answer", "No answer provided").strip()

        lines.append("📌 **Question:**")
        lines.append(question)
        lines.append("\n💡 **Answer:**")
        lines.append(answer)

        # 2. Sources
        sources = result.get("sources")
        if sources:
            lines.append("\n🔗 **Source(s):**")
            lines.append(f"- {sources}")

        # 3. Source Documents
        source_docs = result.get("source_documents", [])
        if source_docs:
            lines.append("\n📚 **Source Document Highlights:**")
            for i, doc in enumerate(source_docs, 1):
                title = doc.metadata.get("title", "Untitled")
                snippet = doc.page_content.strip()[:300].replace("\n", " ")
                lines.append(f"\n  {i}. **{title}**")
                lines.append(f"     {snippet}...")
        lines.append("""
===================================================
""")                

        return "\n".join(lines)



    print(f"{result}")
    print(f"{format_llm_answer(result)}")


