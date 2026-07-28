# test_connection.py

import os
from dotenv import load_dotenv
from openai import AzureOpenAI


# Load .env
load_dotenv()


endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment = os.getenv("AZURE_CHAT_DEPLOYMENT")


print("=" * 50)
print("Azure OpenAI Connection Test")
print("=" * 50)

print("Endpoint :", endpoint)
print("Deployment :", deployment)
print("API Version :", api_version)
print()


# Check missing values

if not endpoint:
    raise Exception("Missing AZURE_OPENAI_ENDPOINT")

if not api_key:
    raise Exception("Missing AZURE_OPENAI_API_KEY")

if not deployment:
    raise Exception("Missing AZURE_CHAT_DEPLOYMENT")


# Create client

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version=api_version
)


try:

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {
                "role": "user",
                "content": "Say hello. Reply with only one sentence."
            }
        ],
        temperature=0
    )


    print("✅ CONNECTION SUCCESSFUL")
    print()
    print("Model response:")
    print(response.choices[0].message.content)


    if response.usage:
        print()
        print("Tokens used:")
        print(response.usage.total_tokens)


except Exception as e:

    print("❌ CONNECTION FAILED")
    print()
    print(type(e).__name__)
    print(e)