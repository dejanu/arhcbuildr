# General

* LangChain is a framework for developing applications powered by language models. One of the main use cases for LangChain currently is to build chat-based applications on top of LLMs (especially ChatGPT).

* LangChain allows you to connect an LLM to your sources of data. You can put your data into documents which will be sliced into chunks that will be stored as embeddings in a Vector Database.

* More exactly embeddings  are vector representations of words or tokens in a text corpus. For GPT-3, embeddings play a crucial role in representing the input text and enabling the model to understand and generate coherent and contextually relevant responses.

## LangChain proposes Components and Chains.

* Components represent abstractions for working with large language models e.g. LLM Wrappers, Prompt Templates, Indexes for information retrieval.
* Chains represent a sequence of components combined in a particular way to accomplish an end-to-end use case.
* Agents represent the language model that drives decision-making


# Doc

* [API reference](https://api.python.langchain.com/en/latest/api_reference.html)
* [chat-langchain](https://github.com/langchain-ai/chat-langchain)