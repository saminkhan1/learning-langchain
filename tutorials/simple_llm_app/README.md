## LangChain Translation Application

This repository contains code for building a simple language translation application using LangChain. It includes functionality for translating text from English into various languages using OpenAI's GPT-3.5 model.

### Setup Instructions

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory and add your OpenAI API key and LangChain tracing information:

OPENAI_API_KEY=your_openai_api_key  
LANGCHAIN_TRACING_V2=your_langchain_tracing_v2_key  
LANGCHAIN_API_KEY=your_langchain_api_key  


Make sure to replace `your_openai_api_key`, `your_langchain_tracing_v2_key`, and `your_langchain_api_key` with your actual API keys.

### Usage

#### 1. Building the LangChain Application

- The main functionality of the application is in the `English_to_Language_Translation.ipynb` notebook.
- It demonstrates how to use LangChain to translate text from English into various languages using the GPT-3.5 model.
- The notebook provides code examples for defining the translation chain, using prompt templates, and invoking the translation process.

#### 2. Serving with LangServe

- To deploy the application as an API server, use the `serve.py` script.
- This script sets up a FastAPI app and defines a route for serving the LangChain translation functionality.
- It includes the definition of the translation chain, creation of prompt templates, and setting up the FastAPI server.

### Running the Server

To run the server, execute the following command in your terminal:

python serve.py


The server will start running locally on `http://localhost:8000`.

### API Endpoints

- `/chain`: Endpoint for translating text from English into other languages. Accepts POST requests with JSON payloads containing the language and text to translate.

### Contributing

Contributions are welcome! If you have any ideas for improvements or feature requests, feel free to open an issue or submit a pull request.

