"""
Step 1:
Download WEB page from rag_conf.WEB_PAGE_URL into local rag_conf.WEB_PAGE_FILE_NAME file
"""
import rag_conf
import requests

# #download WEB page
r = requests.get(rag_conf.WEB_PAGE_URL)
open(rag_conf.WEB_PAGE_FILE_NAME , 'wb').write(r.content)