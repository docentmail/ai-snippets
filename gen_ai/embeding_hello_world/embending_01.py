'''
Generate embedding vector from text using OpenAI API and chippest 
text-embedding-3-small model
'''

import os
from openai import OpenAI
import getpass

embedding_model = "text-embedding-3-small"

#Enter OpenAI key or use environment variable OPENAI_API_KEY instead
# export OPENAI_API_KEY="your-api-key" 
#os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding


the_text="hello world"
the_embending =  get_embedding(the_text, model=embedding_model)

print(the_embending)
