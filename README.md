# Medical Chatbot with RAG

A sophisticated medical chatbot built using Retrieval Augmented Generation (RAG) that provides accurate medical information by combining Large Language Models (LLMs) with a vector database for knowledge retrieval.

## 🚀 Features

- **RAG Architecture**: Combines LLM with vector database for accurate, context-aware responses
- **HuggingFace Embeddings**: Uses `sentence-transformers/all-MiniLM-L6-v2` for text embeddings
- **Pinecone Vector Database**: Fast and scalable vector storage for medical knowledge
- **Google Gemini 2.5 Flash**: Powered by Google's latest Gemini model
- **LangChain Integration**: Seamless integration with LangChain for RAG pipeline
- **Flask Web Interface**: Clean, modern web UI for interacting with the chatbot
- **PDF Document Processing**: Automatically processes and chunks PDF documents

## 📋 Prerequisites

- Python 3.8 or higher
- Pinecone account (free tier available)
- Google Gemini API key
- Medical documents in PDF format

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd MedicalChatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
PINECONE_API_KEY=your_pinecone_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

**How to get API keys:**
- **Pinecone**: Sign up at [https://app.pinecone.io/](https://app.pinecone.io/) and get your API key from the dashboard
- **Gemini**: Get your API key from [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

### 5. Prepare your medical documents

Place your PDF medical documents in the `data/` directory:
```
MedicalChatbot/
  └── data/
      ├── medical_document1.pdf
      ├── medical_document2.pdf
      └── ...
```

## 📚 Setup and Usage

### Step 1: Process and Upload Documents to Pinecone

Run the script to process your PDF documents and upload them to Pinecone:

```bash
python store-index.py
```

This script will:
- Load all PDF files from the `data/` directory
- Split them into chunks (500 characters with 20 character overlap)
- Generate embeddings using HuggingFace model
- Create a Pinecone index (if it doesn't exist)
- Upload all document chunks to Pinecone

**Note**: The first run will create the index. Subsequent runs will add/update documents.

### Step 2: Run the Flask Application

Start the Flask server:

```bash
python app.py
```

The application will start on `http://localhost:8000`

### Step 3: Access the Web Interface

Open your browser and navigate to:
```
http://localhost:8000
```

You can now start chatting with the medical chatbot!

## 🏗️ Project Structure

```
MedicalChatbot/
├── app.py                 # Main Flask application
├── store-index.py         # Script to process and upload documents to Pinecone
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── data/                  # Place your PDF documents here
│   └── dataset.pdf
├── src/
│   ├── __init__.py
│   ├── helper.py         # Utility functions for PDF loading and embeddings
│   └── prompt.py         # System prompt for the chatbot
├── templates/
│   └── index.html        # Frontend HTML
└── static/
    └── style.css         # CSS styling
```

## 🔧 Configuration

### Adjusting Chunk Size

Edit `src/helper.py` to modify chunk size and overlap:

```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Adjust chunk size
    chunk_overlap=20,    # Adjust overlap
)
```

### Changing the LLM Model

Edit `app.py` to use a different Gemini model:

```python
chatModel = ChatGoogleGenerativeAI(
    model="gemini-pro",  # Change model here (options: gemini-pro, gemini-1.5-pro, etc.)
    google_api_key=GEMINI_API_KEY,
    temperature=0.7
)
```

### Adjusting Retrieval Parameters

Edit `app.py` to change the number of retrieved documents:

```python
retriever = docsearch.as_retriever(
    search_type="similarity", 
    search_kwargs={"k": 3}  # Change number of retrieved chunks
)
```

## 🐛 Troubleshooting

### Issue: "PINECONE_API_KEY not found"
- Make sure you've created a `.env` file in the root directory
- Verify the API key is correct and has no extra spaces

### Issue: "Index not found"
- Run `store-index.py` first to create the index and upload documents
- Check that the index name matches in both `store-index.py` and `app.py`

### Issue: "No documents found"
- Ensure PDF files are in the `data/` directory
- Check that PDF files are not corrupted

### Issue: Import errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're using the correct Python version (3.8+)

## 📝 Notes

- **Medical Disclaimer**: This chatbot provides general medical information only. It should not replace professional medical advice, diagnosis, or treatment. Always consult qualified healthcare providers for personal medical concerns.

- **API Costs**: Be aware of API usage costs for both Pinecone and Google Gemini, especially with large document sets.

- **Data Privacy**: Ensure compliance with healthcare data regulations (HIPAA, GDPR, etc.) when handling medical documents.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

See LICENSE file for details.

## 👤 Author

sadafsoomro53@gmail.com

---

**Happy Chatting! 🏥💬**