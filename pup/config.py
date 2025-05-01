"""Project shared settings.

NOTE: This module is meant to be standalone. It should not depend on other
modules in the project since it might cause circular dependency.
"""
import os
import pathlib

import dotenv

# Base Directory
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

dotenv.load_dotenv(BASE_DIR / ".env")

# General
REQUEST_TIMEOUT = int(os.environ["REQUEST_TIMEOUT"])

# OpenAI
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Azure OpenAI
AZURE_OPENAI_API_VERSION = os.environ["AZURE_OPENAI_API_VERSION"]
AZURE_OPENAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
AZURE_OPENAI_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]
AZURE_OPENAI_DEPLOYMENT = os.environ["AZURE_OPENAI_DEPLOYMENT"]
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT = os.environ["AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT"]
AZURE_OPENAI_EMBEDDINGS_API_VERSION = os.environ["AZURE_OPENAI_EMBEDDINGS_API_VERSION"]
AZURE_OPENAI_IMAGE_API_VERSION = os.environ["AZURE_OPENAI_IMAGE_API_VERSION"]
AZURE_OPENAI_IMAGE_DEPLOYMENT = os.environ["AZURE_OPENAI_IMAGE_DEPLOYMENT"]

# Hugging Face
HUGGING_FACE_API_KEY = os.environ["HUGGING_FACE_API_KEY"]

# Chapter Directories
CHAPTER_00_DIR = BASE_DIR / "00-course-setup"
assert CHAPTER_00_DIR.exists(), f"Directory not found: {CHAPTER_00_DIR}"
CHAPTER_01_DIR = BASE_DIR / "01-introduction-to-genai"
assert CHAPTER_01_DIR.exists(), f"Directory not found: {CHAPTER_01_DIR}"
CHAPTER_02_DIR = BASE_DIR / "02-exploring-and-comparing-different-llms"
assert CHAPTER_02_DIR.exists(), f"Directory not found: {CHAPTER_02_DIR}"
CHAPTER_03_DIR = BASE_DIR / "03-using-generative-ai-responsibly"
assert CHAPTER_03_DIR.exists(), f"Directory not found: {CHAPTER_03_DIR}"
CHAPTER_04_DIR = BASE_DIR / "04-prompt-engineering-fundamentals"
assert CHAPTER_04_DIR.exists(), f"Directory not found: {CHAPTER_04_DIR}"
CHAPTER_05_DIR = BASE_DIR / "05-advanced-prompts"
assert CHAPTER_05_DIR.exists(), f"Directory not found: {CHAPTER_05_DIR}"
CHAPTER_06_DIR = BASE_DIR / "06-text-generation-apps"
assert CHAPTER_06_DIR.exists(), f"Directory not found: {CHAPTER_06_DIR}"
CHAPTER_07_DIR = BASE_DIR / "07-building-chat-applications"
assert CHAPTER_07_DIR.exists(), f"Directory not found: {CHAPTER_07_DIR}"
CHAPTER_08_DIR = BASE_DIR / "08-building-search-applications"
assert CHAPTER_08_DIR.exists(), f"Directory not found: {CHAPTER_08_DIR}"
CHAPTER_09_DIR = BASE_DIR / "09-building-image-applications"
assert CHAPTER_09_DIR.exists(), f"Directory not found: {CHAPTER_09_DIR}"
CHAPTER_10_DIR = BASE_DIR / "10-building-low-code-ai-applications"
assert CHAPTER_10_DIR.exists(), f"Directory not found: {CHAPTER_10_DIR}"
CHAPTER_11_DIR = BASE_DIR / "11-integrating-with-function-calling"
assert CHAPTER_11_DIR.exists(), f"Directory not found: {CHAPTER_11_DIR}"
CHAPTER_12_DIR = BASE_DIR / "12-designing-ux-for-ai-applications"
assert CHAPTER_12_DIR.exists(), f"Directory not found: {CHAPTER_12_DIR}"
CHAPTER_13_DIR = BASE_DIR / "13-securing-ai-applications"
assert CHAPTER_13_DIR.exists(), f"Directory not found: {CHAPTER_13_DIR}"
CHAPTER_14_DIR = BASE_DIR / "14-the-generative-ai-application-lifecycle"
assert CHAPTER_14_DIR.exists(), f"Directory not found: {CHAPTER_14_DIR}"
CHAPTER_15_DIR = BASE_DIR / "15-rag-and-vector-databases"
assert CHAPTER_15_DIR.exists(), f"Directory not found: {CHAPTER_15_DIR}"
CHAPTER_16_DIR = BASE_DIR / "16-open-source-models"
assert CHAPTER_16_DIR.exists(), f"Directory not found: {CHAPTER_16_DIR}"
CHAPTER_17_DIR = BASE_DIR / "17-ai-agents"
assert CHAPTER_17_DIR.exists(), f"Directory not found: {CHAPTER_17_DIR}"
CHAPTER_18_DIR = BASE_DIR / "18-fine-tuning"
assert CHAPTER_18_DIR.exists(), f"Directory not found: {CHAPTER_18_DIR}"
CHAPTER_19_DIR = BASE_DIR / "19-slm"
assert CHAPTER_19_DIR.exists(), f"Directory not found: {CHAPTER_19_DIR}"
CHAPTER_20_DIR = BASE_DIR / "20-mistral"
assert CHAPTER_20_DIR.exists(), f"Directory not found: {CHAPTER_20_DIR}"
CHAPTER_21_DIR = BASE_DIR / "21-meta"
assert CHAPTER_21_DIR.exists(), f"Directory not found: {CHAPTER_21_DIR}"
