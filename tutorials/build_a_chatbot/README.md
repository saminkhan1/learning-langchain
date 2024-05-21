Chatbot With Langchain Framework
===========================

This repository contains code for building chatbots using LangChain, a framework designed to streamline interactions with language models. It enables the creation of intelligent conversational agents using various models, such as OpenAI's GPT-3.5 Turbo.

Setup Instructions
------------------

1.  Clone this repository to your local machine.
2.  Install the required dependencies by running `pip install -r requirements.txt`.
3.  Create a `.env` file in the root directory and add your API keys:

plaintext

Copy code

`OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_TRACING_V2=your_langchain_tracing_v2_key
LANGCHAIN_API_KEY=your_langchain_api_key`

Ensure to replace `your_openai_api_key`, `your_langchain_tracing_v2_key`, and `your_langchain_api_key` with your actual keys.

Usage
-----

### 1\. Basic Interaction

-   To interact with the language model directly, use the `model.invoke` method in the notebook.
-   This demonstrates how to initiate conversations and receive responses from the model without maintaining state.

### 2\. Stateful Conversations

-   For stateful interactions and conversation history management, use the `RunnableWithMessageHistory` class.
-   This class wraps the model and maintains context across turns, providing a more coherent chatbot experience.

### 3\. Prompt Templates

-   Utilize prompt templates to structure user inputs and provide additional context to the model.
-   This enhances the model's understanding and improves response quality.

### 4\. Managing Conversation History

-   Implement message history management to prevent memory overflow and maintain context relevance.
-   LangChain provides utilities for filtering and limiting message history, ensuring efficient conversation flow.

### 5\. Streaming Responses

-   Enable streaming responses for a better user experience, allowing users to see progress as the model generates each token.
-   LangChain supports streaming responses through the `.stream` method.

Contributing
------------

Contributions to this repository are welcome! If you have ideas for improvements or feature requests, feel free to open an issue or submit a pull request.