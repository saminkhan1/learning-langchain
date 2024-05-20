# Serving with LangServe

"""
To create a server for our application we'll make a serve.py file. This will contain our logic for serving our application. It consists of three things:

1. The definition of our chain that we just built (English_to_Language_Translation.ipynb)
2. Our FastAPI app
3. A definition of a route from which to serve the chain, which is done with langserve.add_routes
"""

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
# Accessing the variables
os.getenv("OPENAI_API_KEY")
os.getenv("LANGCHAIN_TRACING_V2")
os.getenv("LANGCHAIN_API_KEY")

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

# 2. Create model
model = ChatOpenAI(model="gpt-3.5-turbo-0125")

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser

# 4. App definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces for english to other language translation",
)

# 5. Adding chain route
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
