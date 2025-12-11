from flask import Flask, render_template, request, jsonify
from src.helper import download_huggingface_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import CahtOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import google.generativeai as genai
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
genai.api_key = os.getenv("GEMINI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
#os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
embeddings = download_huggingface_embeddings()

index_name = "medical-chatbot"
#embed each chunk and upsert the embeddings into your pinecone index
docsearch = PineconeVectorStore.from_existing_index(
    embedding=embeddings,
    index_name=index_name,
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

chatmodel = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
prompt = ChatPromptTemplate.from_messages(
    [
    ("system", system_prompt),
    ("user", "{input}"),
    ]
    )

question_answering_chain = create_retrieval_chain(chatmodel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answering_chain)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=["GET","POST"])
def chat():
    msg = request.form.get('msg')
    input = msg
    response = rag_chain.invoke({"input" :msg})
    print("Response :", response["answer"])
    return str(response["answer"])
                        

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000, debug=True)
