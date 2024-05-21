Build Agent with LangChain
==========================



This repository contains code for building an intelligent agent using the LangChain framework. This agent uses a language model (LLM) as a reasoning engine to determine and execute actions based on the inputs provided. The results of these actions can be fed back into the agent to decide whether further actions are necessary or if the task is complete.

Setup Instructions
------------------

* * * * *

1.  Clone this repository to your local machine.
2.  Install the required dependencies by running `pip install -r requirements.txt`.
3.  Create a `.env` file in the root directory and add your API keys:


```
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_TRACING_V2=your_langchain_tracing_v2_key
LANGCHAIN_API_KEY=your_langchain_api_key
TAVILY_API_KEY=your_tavily_api_key`
```

Ensure to replace `your_openai_api_key`, `your_langchain_tracing_v2_key`, `your_langchain_api_key`, and `your_tavily_api_key` with your actual keys.

Usage
-----

* * * * *

### 1\. Define Tools

-   Create the tools the agent will use, such as Tavily for online searches and a retriever over a local index.

```python

from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults(max_results=2)
search.invoke("what is the latest projects related to ai agents?")
```

### 2\. Setup Retriever

-   Create a retriever over your own data to search within a specific dataset.



```python
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()
documents = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200
).split_documents(docs)
vector = FAISS.from_documents(documents, OpenAIEmbeddings())
retriever = vector.as_retriever()
retriever.invoke("how to upload a dataset")[0]
```

### 3\. Create Tools List

-   Combine the created tools into a list for use by the agent.


```python
from langchain.tools.retriever import create_retriever_tool

retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
)
tools = [search, retriever_tool]
```

### 4\. Using Language Models

-   Initialize and bind tools to the language model to enable tool calling.



```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")
model_with_tools = model.bind_tools(tools)
```

### 5\. Create and Run the Agent

-   Create the agent using LangGraph and execute queries.

```python
from langgraph.prebuilt import chat_agent_executor

agent_executor = chat_agent_executor.create_tool_calling_executor(model, tools)
response = agent_executor.invoke({"messages": [HumanMessage(content="hi!")]})
response["messages"]
```

### 6\. Streaming Messages

-   Stream messages to show intermediate progress during multi-step execution.

```python
for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="whats the weather in Queens, NY?")]}
):
    print(chunk)
    print("----")
```

### 7\. Adding Memory

-   Incorporate memory to maintain context across interactions using a checkpointer.



```python
from langgraph.checkpoint.sqlite import SqliteSaver

memory = SqliteSaver.from_conn_string(":memory:")

agent_executor = chat_agent_executor.create_tool_calling_executor(
    model, tools, checkpointer=memory
)

config = {"configurable": {"thread_id": "abc123"}}

for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="hi im bob!")]}, config
):
    print(chunk)
    print("----")

for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="whats my name?")]}, config
):
    print(chunk)
    print("----")
```

Contributing
------------

* * * * *

Contributions to this repository are welcome! If you have ideas for improvements or feature requests, feel free to open an issue or submit a pull request.