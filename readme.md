# Privacera QA Chatbot by Vipul Munot

This project is a QA chatbot designed to answer questions about Privacera using information extracted from provided PDF documents. The chatbot is built using Streamlit, LangChain, and OpenAI API, with data storage managed by AstraDB.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)

## Features
- Ingests PDF documents to create a searchable knowledge base.
- Uses LangChain for retrieval-augmented generation.
- Integrates OpenAI API for generating responses.
- Provides a simple and interactive UI using Streamlit.

## Prerequisites
- Python 3.8 or later
- AstraDB account and credentials
- OpenAI API key

## Installation

1. **Clone the repository:**
   ```bash
   git clone this repo
   cd into the repo

2. **Set up a virtual environment::**
    ```bash
    python3 -m venv venv
    source venv/bin/activate


3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    

4. **Set up environment variables:**
    ```bash
    Create a .env file in the project root and add the following variables:
    OPENAI_API_KEY=your_openai_api_key
    ASTRA_DB_API_ENDPOINT=your_astra_db_api_endpoint
    ASTRA_DB_APPLICATION_TOKEN=your_astra_db_application_token
    ASTRA_DB_KEYSPACE=your_astra_db_keyspace


5. ** Ingest PDF data::**
    ```bash
    Ensure your PDF files are placed in the data directory and run the ingestion process:
    python src/data_ingestion.py

## Usage


1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py

2. **Interact with the chatbot:**
    ```bash
    Open your web browser and go to http://localhost:8501 to interact with the chatbot.



