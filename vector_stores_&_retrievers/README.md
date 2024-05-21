
# Vector Stores and Retrievers with LangChain
===========================

This repository provides a comprehensive guide on using LangChain's vector store and retriever abstractions. These tools support data retrieval from vector databases and other sources for integration with large language model (LLM) workflows, which is essential for applications like retrieval-augmented generation (RAG).

## Setup Instructions
------------------

1. **Clone this repository to your local machine:**

    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Create a `.env` file in the root directory and add your API keys:**

    ```plaintext
    LANGCHAIN_TRACING_V2=your_langchain_tracing_v2_key
    LANGCHAIN_API_KEY=your_langchain_api_key
    ```

    Ensure to replace `your_langchain_tracing_v2_key` and `your_langchain_api_key` with your actual keys.

## Usage
-----

### 1. Documents

LangChain uses a Document abstraction to represent a unit of text and its metadata. Each document has:

- `page_content`: A string representing the content.
- `metadata`: A dictionary containing arbitrary metadata.

Example:

```python
from langchain_core.documents import Document

documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Goldfish are popular pets for beginners, requiring relatively simple care.",
        metadata={"source": "fish-pets-doc"},
    ),
    Document(
        page_content="Parrots are intelligent birds capable of mimicking human speech.",
        metadata={"source": "bird-pets-doc"},
    ),
    Document(
        page_content="Rabbits are social animals that need plenty of space to hop around.",
        metadata={"source": "mammal-pets-doc"},
    ),
]
```

2. Vector Stores
Vector stores enable efficient search over unstructured data by storing numeric vectors associated with text. Here’s how to set up a vector store using Chroma and OpenAI embeddings:

```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

vectorstore = Chroma.from_documents(
    documents,
    embedding=OpenAIEmbeddings(),
)
```

3. Querying Vector Stores
You can query the vector store synchronously, asynchronously, by string query, by vector, with similarity scores, or using maximum marginal relevance (MMR).

Examples:

```python
# Synchronous similarity search
results = vectorstore.similarity_search("cat")

# Asynchronous similarity search
results_async = await vectorstore.asimilarity_search("cat")

# Similarity search with scores
results_with_score = vectorstore.similarity_search_with_score("cat")

# Similarity search by vector
embedding = OpenAIEmbeddings().embed_query("cat")
results_by_vector = vectorstore.similarity_search_by_vector(embedding)
```

4. Retrievers
LangChain Retrievers are designed for integration into LangChain Expression Language (LCEL) chains. They implement standard methods for synchronous and asynchronous invocation and batch operations.

Creating a simple retriever:

```python
from typing import List
from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda

retriever = RunnableLambda(vectorstore.similarity_search).bind(k=1)  # select top result
retriever.batch(["cat", "shark"])
```
Using the as_retriever method:

```python
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1},
)
retriever.batch(["cat", "shark"])
```

5. Retrieval-Augmented Generation (RAG)
Integrate retrievers into more complex applications like RAG, which combines a question with retrieved context into a prompt for an LLM.

Example:

```python

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

llm = ChatOpenAI(model="gpt-3.5-turbo")

message = """
Answer this question using the provided context only.

{question}

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([("human", message)])

rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm

response = rag_chain.invoke("tell me about cats")

print(response.content)
```
## Contributing

Contributions are welcome! If you have ideas for improvements or feature requests, please open an issue or submit a pull request.