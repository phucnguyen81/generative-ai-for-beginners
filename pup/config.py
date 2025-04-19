"""Project shared settings"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# OpenAI
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Azure OpenAI
AZURE_OPENAI_API_VERSION = os.environ["AZURE_OPENAI_API_VERSION"]
AZURE_OPENAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
AZURE_OPENAI_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]
AZURE_OPENAI_DEPLOYMENT = os.environ["AZURE_OPENAI_DEPLOYMENT"]
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT = os.environ["AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT"]
AZURE_OPENAI_EMBEDDINGS_API_VERSION = os.environ["AZURE_OPENAI_EMBEDDINGS_API_VERSION"]

# Hugging Face
HUGGING_FACE_API_KEY = os.environ["HUGGING_FACE_API_KEY"]

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent
