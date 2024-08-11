"""
Step 2:
Load rag_conf.WEB_PAGE_FILE_NAME local file into Qdrant vector DB 
Generate embeddings with rag_conf.EBEDINGS_MODEL 
persist the DB in rag_conf.QDRANT_PATH folder
"""
import rag_conf
import getpass
from langchain_community.vectorstores import Qdrant
from langchain_openai import OpenAIEmbeddings 
from langchain_community.llms import OpenAI
from langchain_community.document_loaders import BSHTMLLoader
from langchain.chains import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter


#load text from html
loader = BSHTMLLoader(rag_conf.WEB_PAGE_FILE_NAME, rag_conf.OPEN_ENCODING)

# initialize TextSplitter to split the 26k page_content into documents by 1 
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1000,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
)
the_document = loader.load_and_split(text_splitter)


# Write the page_content and metadata into the files
docs_page_content =''
docs_metadata =''
for doc in the_document:
    docs_page_content += '\n===================\n'+doc.page_content
    docs_metadata += '\n===================\n'+str(doc.metadata)
with open('text_'+rag_conf.WEB_PAGE_FILE_NAME, 'w') as f:
    f.write(docs_page_content)
with open('meta_'+rag_conf.WEB_PAGE_FILE_NAME, 'w') as f:
    f.write(docs_metadata)

# print the_document stats
print('The document stats:')
print('Number of documets:', len(the_document))
print('Total length of the page_content-s:', sum([len(doc.page_content) for doc in the_document]))

#Enter OpenAI key or use environment variable OPENAI_API_KEY instead
# export OPENAI_API_KEY="your-api-key" 
#os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

#init Vector DB
embeddings = OpenAIEmbeddings(model=rag_conf.EBEDINGS_MODEL)

# Create and persist Qdrant
doc_store = Qdrant.from_documents(
    the_document,
    embeddings,
    path=rag_conf.QDRANT_PATH,
    collection_name=rag_conf.QDRANT_COLLECTION_NAME
)