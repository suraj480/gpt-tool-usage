from openai import AzureOpenAI
from config.settings import (
    AZURE_ENDPOINT,
    AZURE_API_KEY,
    AZURE_API_VERSION,
    CHAT_DEPLOYMENT,
)
print("Endpoint:", AZURE_ENDPOINT)
print("Deployment:", CHAT_DEPLOYMENT)
print("API Version:", AZURE_API_VERSION)
# Create Azure OpenAI client
chat_client = AzureOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=AZURE_API_KEY,
    api_version=AZURE_API_VERSION,
)

def ask(system: str, user: str) -> str:
    """Simple helper function for Chat Completions."""

    response = chat_client.chat.completions.create(
        model=CHAT_DEPLOYMENT,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )

    return response.choices[0].message.content