
import os
import base64
import openai
from openai import AzureOpenAI

from dotenv import load_dotenv

load_dotenv()

# os.environ["OPENAI_API_TYPE"] = "azure"
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

# Initialize Azure OpenAI Service client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version=api_version,
)


# IMAGE_PATH = "YOUR_IMAGE_PATH"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')

#Prepare the chat prompt
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are an AI assistant that helps people find information."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Hello!"
            }
        ]
    }
]

# Include speech result if speech is enabled
messages = chat_prompt
# Generate the completion
completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(completion.to_json())

embeddings = client.embeddings.create(
    input = 'hello', model=os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT")
)

print(embeddings)
