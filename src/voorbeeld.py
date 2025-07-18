
from typing import TypedDict, Annotated, Dict, Any
from langgraph.graph import add_messages, StateGraph, END
from langchain_core.messages import AIMessage, HumanMessage, AnyMessage, SystemMessage
from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode
from langchain_openai import AzureChatOpenAI
from langchain_ollama import ChatOllama
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
import aiosqlite
from pydantic import BaseModel
import uuid
import asyncio
from rich import print
from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import StreamingResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os
from contextlib import asynccontextmanager
from langchain_core.prompts import ChatPromptTemplate


llm = AzureChatOpenAI(
    deployment_name="gpt-4o-mini",
    model="gpt-4o-mini",
    temperature=0.0,
    openai_api_version="2024-02-15-preview",
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

# llm = ChatOllama(
#     model="qwen3:8b"
# )

def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


tools = [multiply] 
llm_with_tools = llm.bind_tools(tools)


result = llm.invoke("Wat is de hoofdstad van Nederland?")
# print(result.content)

result = llm_with_tools.invoke("wat is 5 * 4)")
print(result)