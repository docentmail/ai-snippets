# RAG Albert Einstein example

- [What is in this example?](#what-is-in-this-example)
- [Preparing the environment](#preparing-the-environment)
- [The main flow](#the-main-flow)
   * [bin/python rag_step1.py			](#binpython-rag_step1py)
   * [bin/python rag_step2.py		](#binpython-rag_step2py)
   * [bin/python rag_step3.py](#binpython-rag_step3py)
- [Files in the project](#files-in-the-project)
- [Useful links to visit and questions to ask ChatGPT ](#useful-links-to-visit-and-questions-to-ask-chatgpt)
   * [Links ](#links)
   * [Questions to ask ChatGPT ](#questions-to-ask-chatgpt)
- [Things to pay attention to](#things-to-pay-attention-to)
   * [Your question: When was Albert Einstein born?](#your-question-when-was-albert-einstein-born)
   * [Your question: What is the connection between Albert Einstein and GPS?     ](#your-question-what-is-the-connection-between-albert-einstein-and-gps)
   * [Your question: Who is Agatha Christie?](#your-question-who-is-agatha-christie)
   * [Explore Qdrant content](#explore-qdrant-content)

## What is in this example?
**This is an example of using RAG.**\
Download a [page](https://www.biography.com/scientists/albert-einstein) from the Internet.\
Split it into parts, generate embeddings and save them to a local Qdrant Vector DB.\
Use a local Qdrant Vector DB to generate answers to questions using an OpenAI's LLM.

**Technologies and frameworks used:**

RAG, embeddings, LLM, Vector DB\
Langchain: RecursiveCharacterTextSplitter, OpenAIEmbeddings, Qdrant, OpenAI\
OpenAI: client, LLMs 'text-embedding-3-small' and 'gpt-3.5-turbo-instruct', OpenAI API key


## Preparing the environment
Get your [OpenAI API key](https://platform.openai.com/api-keys)

Create python's Virtual Environment\
`python3 -m venv rag_albert_einstein`

Check OPENAI_API_KEY environment variable\
`printenv`\
`export OPENAI_API_KEY="your-api-key"`

Installation of Pyhon modules\
`cd rag_albert_einstein`\
`bin/pip install requests langchain_community langchain_openai beautifulsoup4 lxml qdrant-client`

## The main flow
Execute one by one:
```
bin/python rag_step1.py			
bin/python rag_step2.py		
bin/python rag_step3.py
```

### bin/python rag_step1.py			
Step 1:Download WEB page from rag_conf.WEB_PAGE_URL into local rag_conf.WEB_PAGE_FILE_NAME file

### bin/python rag_step2.py		
Step 2:\
Load rag_conf.WEB_PAGE_FILE_NAME local file into Qdrant vector DB \
Generate embeddings with rag_conf.EBEDINGS_MODEL \
persist the DB in rag_conf.QDRANT_PATH folder

### bin/python rag_step3.py
Step 3:\
Initialize the Qdrant vector DB from rag_conf.QDRANT_PATH folder\
Ask questions to the RAG model

## Files in the project

**rag_conf.py**\
Configurtation parameters. Impotred by each step.

**rag_step1.py**\
Step 1: Python file.

**rag_step2.py**\
Step 2: Python file.

**rag_step3.py**\
Step 3: Python file.

**albert-einstein**\
Downloaded WEB page. Created during step2.\
**text_albert-einstein**\
Text of chunks after TextSplitter. Created during step2.\
**meta_albert-einstein**\
Metadata of chunks after TextSplitter. Created during step2.

**qdrant**\
folder with persisted Qdrant vector DB. Created during Step 2. Used in Step 3.


## Useful links to visit and questions to ask ChatGPT 

### Links 
[How to load HTML](https://python.langchain.com/v0.2/docs/how_to/document_loader_html/)\
[langchain_community.document_loaders.html_bs.BSHTMLLoader](https://api.python.langchain.com/en/latest/document_loaders/langchain_community.document_loaders.html_bs.BSHTMLLoader.html)\
[Examples using BSHTMLLoader](https://api.python.langchain.com/en/latest/document_loaders/langchain_community.document_loaders.html_bs.BSHTMLLoader.html#langchain_community.document_loaders.html_bs.BSHTMLLoader.load_and_split)\
[LangChain: Text Splitters](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/)\
[ChunkViz v0.1 - This is an tool to understand different chunking/splitting strategies.](https://chunkviz.up.railway.app/)\
[OpenAIEmbeddings](https://api.python.langchain.com/en/latest/embeddings/langchain_community.embeddings.openai.OpenAIEmbeddings.html#langchain_community.embeddings.openai.OpenAIEmbeddings)\
[Qdrant.from_documents and  from_existing_collection](https://api.python.langchain.com/en/latest/vectorstores/langchain_community.vectorstores.qdrant.Qdrant.html#langchain_community.vectorstores.qdrant.Qdrant.from_documents)\
[Qdrant. Local mode](https://github.com/qdrant/qdrant-client#local-mode)\
[OpenAIEmbeddings[source]](https://api.python.langchain.com/en/latest/embeddings/langchain_community.embeddings.openai.OpenAIEmbeddings.html#langchain_community.embeddings.openai.OpenAIEmbeddings)\
[langchain_community.llms.openai.OpenAI](https://api.python.langchain.com/en/latest/llms/langchain_community.llms.openai.OpenAI.html#langchain_community.llms.openai.OpenAI)\
[langchain.chains.retrieval_qa.base.RetrievalQA](https://api.python.langchain.com/en/latest/chains/langchain.chains.retrieval_qa.base.RetrievalQA.html#)\
[langchain.chains.qa_with_sources.retrieval.RetrievalQAWithSourcesChain.from_chain_type](https://api.python.langchain.com/en/latest/chains/langchain.chains.qa_with_sources.retrieval.RetrievalQAWithSourcesChain.html#langchain.chains.qa_with_sources.retrieval.RetrievalQAWithSourcesChain.from_chain_type)\
[How RetrievalQAWithSourcesChain uses LLM?](https://stackoverflow.com/questions/76482024/how-to-get-more-detailed-results-sources-with-langchain)\
[OpenAIEmbeddings](# https://api.python.langchain.com/en/latest/embeddings/langchain_community.embeddings.openai.OpenAIEmbeddings.html#langchain-community-embeddings-openai-openaiembeddings()
### Questions to ask ChatGPT 
What types of Retrieving Documents techniques are there?\
What Retrieving Documents techniques does Qdrant use?\
What Retrieving Documents techniques does RetrievalQAWithSourcesChain use?


## Things to pay attention to

### Your question: When was Albert Einstein born?
'answer': ' Albert Einstein was born on March 14, 1879.\n'

**Note:** Retrieving Documents mechanizm is good. The chunk with date of birth is the first.

```
Answer: {'question': 'When was Albert Einstein born?', 'answer': ' Albert Einstein was born on March 14, 1879.\n', 'sources': 'albert-einstein', 'source_documents': [Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': 'a5737af9d30940278fb1ad0315ef2240', '_collection_name': 'docs'}, page_content='EducationAlbert Einstein was born on March 14, 1879, in Ulm, Württemberg, Germany. He grew up in a secular Jewish family. His father, Hermann Einstein, was a salesman and engineer who, with his brother, founded Elektrotechnische Fabrik J. Einstein & Cie, a Munich-based company that mass-produced electrical equipment. Einstein’s mother, the former Pauline Koch, ran the family household. Einstein had one sister, Maja, born two years after him.Einstein attended elementary school at the Luitpold Gymnasium in Munich. However, he felt alienated there and struggled with the institution’s rigid pedagogical style. He also had what were considered speech challenges. However, he developed a passion for classical music and playing the violin, which would stay with him into his later years. Most significantly, Einstein’s youth was marked by deep inquisitiveness and inquiry. Toward the end of the 1880s, Max Talmud, a Polish medical student who sometimes dined with the Einstein family, became an'), Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': '69f11f9b73234fdd8f29c00efb4a9041', '_collection_name': 'docs'}, page_content='1879-1955Who Was Albert Einstein?Albert Einstein was a German mathematician and physicist who developed the special and general theories of relativity. In 1921, he won the Nobel Prize in Physics for his explanation of the photoelectric effect. In the following decade, he immigrated to the United States after being targeted by the German Nazi Party. His work also had a major impact on the development of atomic energy. In his later years, Einstein focused on unified field theory. He died in April 1955 at age 76. With his passion for inquiry, Einstein is generally considered the most influential physicist of the 20th century.Quick FactsFULL NAME: Albert EinsteinBORN: March 14, 1879DIED: April 18, 1955BIRTHPLACE: Ulm, Württemberg, GermanySPOUSES: Mileva Einstein-Maric (1903-1919) and Elsa Einstein (1919-1936)CHILDREN: Lieserl, Hans, and EduardASTROLOGICAL SIGN: PiscesEarly Life, Family, and EducationAlbert Einstein was born on March 14, 1879, in Ulm, Württemberg, Germany. He grew up in a'), Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': 'bf726c0a6f0442a68008ea14e1201d0c', '_collection_name': 'docs'}, page_content='prospects as a school dropout and draft dodger. Einstein was eventually able to gain admission into the Swiss Federal Institute of Technology in Zurich, specifically due to his superb mathematics and physics scores on the entrance exam. He was still required to complete his pre-university education first and thus attended a high school in Aarau, Switzerland, helmed by Jost Winteler. Einstein lived with the schoolmaster’s family and fell in love with Winteler’s daughter Marie. Einstein later renounced his German citizenship and became a Swiss citizen at the dawn of the new century.Einstein’s IQEinstein’s intelligence quotient was estimated to be around 160, but there are no indications he was ever actually tested.Related StoryWhat Was Albert Einstein’s IQ?Psychologist David Wechsler didn’t release the first edition of the WAIS cognitive test, which evolved into the WAIS-IV test commonly used today, until 1955—shortly before Einstein’s death. The maximum score of the current version is'), Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': '453458c5d30346479e0474d21c0fe8e8', '_collection_name': 'docs'}, page_content='before becoming director of the Kaiser Wilhelm Institute for Physics (today is known as the Max Planck Institute for Physics) from 1917 to 1933. Nobel Prize in PhysicsIn 1921, Einstein won the Nobel Prize in Physics for his explanation of the photoelectric effect, since his ideas on relativity were still considered questionable. He wasn’t actually given the award until the following year due to a bureaucratic ruling, and during his acceptance speech, he still opted to speak about relativity.Wives and ChildrenGetty ImagesAlbert Einstein with his second wife, ElsaEinstein married Mileva Maric on January 6, 1903. While attending school in Zurich, Einstein met Maric, a Serbian physics student. Einstein continued to grow closer to Maric, but his parents were strongly against the relationship due to her ethnic background.Nonetheless, Einstein continued to see her, with the two developing a correspondence via letters in which he expressed many of his scientific ideas. Einstein’s father')]}
```

### Your question: What is the connection between Albert Einstein and GPS?     
'answer': " Albert Einstein's theories of relativity underpin the accuracy of GPS technology. \n"

**Note:** Vector Search (not Keyword Search) Retrieving Documents mechanizm is surprisingly good. The chunk with GPS is the first. How can it find a piece of text with three fixed letters GPS  by imbedding vector is unclear.

```
> Entering new RetrievalQAWithSourcesChain chain...

> Finished chain.
Answer: {'question': 'What is the connection between Albert Einstein and GPS?', 'answer': " Albert Einstein's theories of relativity underpin the accuracy of GPS technology. \n", 'sources': 'albert-einstein', 'source_documents': [Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': '5a067056f5294ccd9632289b275ca07f', '_collection_name': 'docs'}, page_content='science icon was born. Today, the theories of relativity underpin the accuracy of GPS technology, among other phenomena.Even so, Einstein did make one mistake when developing his general theory, which naturally predicted the universe is either expanding or contracting. Einstein didn’t believe this prediction initially, instead holding onto the belief that the universe was a fixed, static entity. To account for, this he factored in a “cosmological constant” to his equation. His later theories directly contracted this idea and asserted that the universe could be in a state of flux. Then, astronomer Edwin Hubble deduced that we indeed inhabit an expanding universe. Hubble and Einstein met at the Mount Wilson Observatory near Los Angeles in 1931. Decades after Einstein’s death, in 2018, a team of scientists confirmed one aspect of Einstein’s general theory of relativity: that the light from a star passing close to a black hole would be stretched to longer wavelengths by the overwhelming'), Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': '4ef3f9203d9344b9b919313c0b081552', '_collection_name': 'docs'}, page_content='relativity in 1905 in his paper “On the Electrodynamics of Moving Bodies,” which took physics in an electrifying new direction. The theory explains that space and time are actually connected, and Einstein called this joint structure space-time. By November 1915, Einstein completed the general theory of relativity, which accounted for gravity’s relationship to space-time. Einstein considered this theory the culmination of his life research. He was convinced of the merits of general relativity because it allowed for a more accurate prediction of planetary orbits around the sun, which fell short in Isaac Newton’s theory. It also offered a more expansive, nuanced explanation of how gravitational forces worked. Einstein’s assertions were affirmed via observations and measurements by British astronomers Sir Frank Dyson and Sir Arthur Eddington during the 1919 solar eclipse, and thus a global science icon was born. Today, the theories of relativity underpin the accuracy of GPS technology,'), Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': '69f11f9b73234fdd8f29c00efb4a9041', '_collection_name': 'docs'}, page_content='1879-1955Who Was Albert Einstein?Albert Einstein was a German mathematician and physicist who developed the special and general theories of relativity. In 1921, he won the Nobel Prize in Physics for his explanation of the photoelectric effect. In the following decade, he immigrated to the United States after being targeted by the German Nazi Party. His work also had a major impact on the development of atomic energy. In his later years, Einstein focused on unified field theory. He died in April 1955 at age 76. With his passion for inquiry, Einstein is generally considered the most influential physicist of the 20th century.Quick FactsFULL NAME: Albert EinsteinBORN: March 14, 1879DIED: April 18, 1955BIRTHPLACE: Ulm, Württemberg, GermanySPOUSES: Mileva Einstein-Maric (1903-1919) and Elsa Einstein (1919-1936)CHILDREN: Lieserl, Hans, and EduardASTROLOGICAL SIGN: PiscesEarly Life, Family, and EducationAlbert Einstein was born on March 14, 1879, in Ulm, Württemberg, Germany. He grew up in a'), Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': 'a5737af9d30940278fb1ad0315ef2240', '_collection_name': 'docs'}, page_content='EducationAlbert Einstein was born on March 14, 1879, in Ulm, Württemberg, Germany. He grew up in a secular Jewish family. His father, Hermann Einstein, was a salesman and engineer who, with his brother, founded Elektrotechnische Fabrik J. Einstein & Cie, a Munich-based company that mass-produced electrical equipment. Einstein’s mother, the former Pauline Koch, ran the family household. Einstein had one sister, Maja, born two years after him.Einstein attended elementary school at the Luitpold Gymnasium in Munich. However, he felt alienated there and struggled with the institution’s rigid pedagogical style. He also had what were considered speech challenges. However, he developed a passion for classical music and playing the violin, which would stay with him into his later years. Most significantly, Einstein’s youth was marked by deep inquisitiveness and inquiry. Toward the end of the 1880s, Max Talmud, a Polish medical student who sometimes dined with the Einstein family, became an')]}

```


### Your question: Who is Agatha Christie?
'answer': ' Agatha Christie was not mentioned in the given content.\n'

**Note:** The LLM iside itself knows who is Agatha Christie but unswered about provided documents. See [how RetrievalQAWithSourcesChain uses LLM?](https://stackoverflow.com/questions/76482024/how-to-get-more-detailed-results-sources-with-langchain)

```
Answer: {'question': 'Who is Agatha Christie?', 'answer': ' Agatha Christie was not mentioned in the given content.\n', 'sources': '', 'source_documents': [Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': '384f434683f347c5b6470479e08b84c4', '_collection_name': 'docs'}, page_content="editor. He is a graduate of Syracuse University. When he's not writing and researching his next story, you can find him at the nearest amusement park, catching the latest movie, or cheering on his favorite sports teams.Advertisement - Continue Reading BelowNobel Prize WinnersAlice MunroChien-Shiung WuThe Solar Eclipse That Made Albert Einstein a Star14 Hispanic Women Who Have Made HistoryAdvertisement - Continue Reading BelowMarie CurieMartin Luther King Jr.Henry KissingerMalala YousafzaiJimmy Carter10 Famous Poets Whose Enduring Works We Still Read22 Famous Scientists You Should KnowWole SoyinkaAdvertisement - Continue Reading BelowAbout Biography.comNewsletterContact UsOther Hearst SubscriptionsA Part of Hearst Digital MediaWe may earn commission from links on this page, but we only recommend products we back.©2024 Hearst Magazine Media, Inc. Site contains certain content that is owned A&E Television Networks, LLC. All Rights Reserved. Biography and associated logos are trademarks"), Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': '69f11f9b73234fdd8f29c00efb4a9041', '_collection_name': 'docs'}, page_content='1879-1955Who Was Albert Einstein?Albert Einstein was a German mathematician and physicist who developed the special and general theories of relativity. In 1921, he won the Nobel Prize in Physics for his explanation of the photoelectric effect. In the following decade, he immigrated to the United States after being targeted by the German Nazi Party. His work also had a major impact on the development of atomic energy. In his later years, Einstein focused on unified field theory. He died in April 1955 at age 76. With his passion for inquiry, Einstein is generally considered the most influential physicist of the 20th century.Quick FactsFULL NAME: Albert EinsteinBORN: March 14, 1879DIED: April 18, 1955BIRTHPLACE: Ulm, Württemberg, GermanySPOUSES: Mileva Einstein-Maric (1903-1919) and Elsa Einstein (1919-1936)CHILDREN: Lieserl, Hans, and EduardASTROLOGICAL SIGN: PiscesEarly Life, Family, and EducationAlbert Einstein was born on March 14, 1879, in Ulm, Württemberg, Germany. He grew up in a'), Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': '8647f278f2764ca389ed14a7c644ff5a', '_collection_name': 'docs'}, page_content='stuck his tongue out at the crowd for a moment before turning away. UPI photographer Arthur Sasse captured the shot.Einstein was amused by the picture and ordered several prints to give to his friends. He also signed a copy of the photo that sold for $125,000 at a 2017 auction.Death and Final WordsEinstein died on April 18, 1955, at age 76 at the University Medical Center at Princeton. The previous day, while working on a speech to honor Israel’s seventh anniversary, Einstein suffered an abdominal aortic aneurysm. He was taken to the hospital for treatment but refused surgery, believing that he had lived his life and was content to accept his fate. “I want to go when I want,” he stated at the time. “It is tasteless to prolong life artificially. I have done my share, it is time to go. I will do it elegantly.”According to the BBC, Einstein muttered a few words in German at the moment of his death. However, the nurse on duty didn’t speak German so their translation was lost forever.In a'), Document(metadata={'source': 'albert-einstein', 'title': 'Albert Einstein: Biography, Physicist, Nobel Prize Winner', '_id': '87abd2c8467944389cda55153caa6da7', '_collection_name': 'docs'}, page_content='death. However, the nurse on duty didn’t speak German so their translation was lost forever.In a 2014 interview, Life magazine photographer Ralph Morse said the hospital was swarmed by journalists, photographers, and onlookers once word of Einstein’s death spread. Morse decided to travel to Einstein’s office at the Institute for Advanced Studies, offering the superintendent alcohol to gain access. He was able to photograph the office just as Einstein left it.After an autopsy, Einstein’s corpse was moved to a Princeton funeral home later that afternoon and then taken to Trenton, New Jersey, for a cremation ceremony. Morse said he was the only photographer present for the cremation, but Life managing editor Ed Thompson decided not to publish an exclusive story at the request of Einstein’s son Hans. Einstein’s BrainDuring Einstein’s autopsy, pathologist Thomas Stoltz Harvey had removed his brain, reportedly without his family’s consent, for preservation and future study by doctors of')]}
```


### Explore Qdrant content
`sqlite3 qdrant/collection/docs/storage.sqlite`

`.tables`\
points

`PRAGMA table_info(points);`\
0|id|TEXT|0||1\
1|point|BLOB|0||0

`select count() from points;`
31

`select length(point) from points;`
15195\
14428\
15192\
15194\
...

