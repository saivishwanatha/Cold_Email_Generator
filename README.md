# Cold Email Generator

An AI-powered Cold Email Generator that extracts job postings from company career pages and generates personalized outreach emails.

## Features

* Scrapes job descriptions directly from URLs
* Extracts structured job information using LLMs
* Matches relevant portfolio projects using ChromaDB vector search
* Generates personalized cold emails
* Streamlit-based user interface

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq LLM
* ChromaDB
* Pandas

## Setup

### Clone the repository

```bash
git clone https://github.com/saivishwanatha/Cold_Email_Generator.git
cd Cold_Email_Generator
```

### Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### Run the application

```bash
streamlit run app/main.py
```

## Project Structure

```text
app/
├── chains.py
├── main.py
├── portfolio.py
├── utils.py
└── resources/

vectorstore/
README.md
requirements.txt
```
