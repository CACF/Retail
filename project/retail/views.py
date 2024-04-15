from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
import streamlit as st
import tiktoken
from llama_index.legacy import LLMPredictor, OpenAIEmbedding, PromptHelper
from llama_index.llms.openai import OpenAI
from llama_index.core import service_context 
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler
from sqlalchemy import create_engine, text
from llama_index.core import SQLDatabase,ServiceContext
from llama_index.core.query_engine.sql_join_query_engine import NLSQLTableQueryEngine
import os
import openai
import logging
import sys

from .serializer import customer_serializer
openai.api_key = os.getenv("OPENAI_API_KEY")
 
 
logging.basicConfig(stream=sys.stdout, level=logging.INFO, force=True)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
from IPython.display import Markdown, display
# Your existing code for database connection and LLMPredictor setup
db_user = "root"
db_password = "kashif"
db_host = "localhost"
db_name = "retail"
# Construct the connection string
connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
 
# Create an engine instance
engine = create_engine(connection_string)
table_details = {
    "customer": "stores customer’s data.",
    "product": "stores a list of scale model cars.",
    "order": "stores sales orders placed by customers.",
    "employee": "stores all employee information as well as the organization structure such as who reports to whom.",
    "distribution_center": "stores  Distribution Centers details data.",
    "order_product":"this table is for many to many relationship between order and product tables",
    "supplier": "stores all supplier related data."
}
from llama_index.core import SQLDatabase
tables = ["customers","orders"]
sql_database = SQLDatabase(engine, sample_rows_in_table_info=2)
 
token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode
)
 
callback_manager = CallbackManager([token_counter])
 
llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo")
 
service_context = ServiceContext.from_defaults(
    llm=llm, callback_manager=callback_manager
)
 
query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    service_context=service_context
)
@api_view(["POST"])
def run_llm(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')

        # Query the database
        response = query_engine.query(prompt)

        # Prepare response data
        result = {
            'response': response.response,
            'sql_query': response.metadata.get('sql_query', '')
        }
        return Response(result)

@api_view(["POST"])
def create_customer(request):
    serializer =customer_serializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        query = f"insert the data in to  Customer table {serializer.validated_data}" 
        # data = serializer.validated_data['name']+serializer.validated_data['contact_information']+serializer.validated_data['address']
        response = query_engine.query(query)
        result = {
            'response': serializer.data,
            'sql_query': response.metadata.get('sql_query', '')
        }
        return Response(result)