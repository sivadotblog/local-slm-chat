# local-slm-chat

This repo will demo a Local SLM chat bot for knowledgebase chat bot. It will use a rag design and a small Language Model microsoft phi3.5 medium.

The idea is ,

1) We have a /docs knowledge base with markdown files on a subject.
2) We use NLP libraries such as nltk and or spacy and or scikit to tokenize the docs into a local vector FAISS
3) use microsoft phi3.5 medium and fast api to create a conversational api.
4) use streamlit to demo the interface.
5) the streamlit app has multiple pages and based on wher the user is, the page meta will be sent to the fast api along with the chat query so that the rag model is able to get more accurate response
