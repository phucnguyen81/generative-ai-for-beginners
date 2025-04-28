"""Azure OpenAI wrapper code"""
from typing import Iterable

from openai import AzureOpenAI
from openai.types.chat import ChatCompletion
from openai._types import NOT_GIVEN

from pup import config


def aoai_complete(message: str = "Hello!", functions: list[dict] = None) -> ChatCompletion:
    """Return the chat completion result for a single user message"""
    return AzureOpenAI(
        azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
        api_key=config.AZURE_OPENAI_API_KEY,
        api_version=config.AZURE_OPENAI_API_VERSION,
    ).chat.completions.create(
        model=config.AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are a helpful AI assistant.",
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": message,
                    }
                ]
            },
        ],
        functions=functions or NOT_GIVEN,
        function_call="auto" if functions else NOT_GIVEN,
        max_tokens=1024,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )


def aoai_function(
    name: str,
    description: str,
    params: Iterable[tuple] = None,
    required_params=None,
) -> dict:
    """Create a dict to pass as function to the API"""
    return {
        "name": name,
        "description": description,
        "parameters": {
            "type": "object",
            "required": required_params or NOT_GIVEN,
            "properties": {
                parm_name: {
                    "type": parm_type,
                    "description": parm_description,
                }
                for parm_name, parm_type, parm_description in params
            }
        } if params else NOT_GIVEN
    }


if __name__ == "__main__":
    response: ChatCompletion = aoai_complete("Tell me a joke")
    print(response.choices[0].message.content)

    response2: ChatCompletion = aoai_complete(
        "What is two plus two?", functions=[
            aoai_function(
                "sum", "Sum of two numbers",
                params=[
                    ("operand1", "number", "The first operand of the sum"),
                    ("operand2", "number", "The second operand of the sum"),
                ],
                required_params=["operand1", "operand2"],
            )
        ])
    print(response2.choices[0].message.function_call)
