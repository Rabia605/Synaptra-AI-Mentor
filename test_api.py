import toml
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

secrets = toml.load(".streamlit/secrets.toml")
api_key = secrets["OPENROUTER_API_KEY"]
base_url = secrets.get("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")

chat = ChatOpenAI(
    model="openrouter/free",
    temperature=0.5,
    api_key=api_key,
    base_url=base_url
)

messages = [
    SystemMessage(content="You are an AI Mentor."),
    HumanMessage(content="Hi, what should I learn to become an AI engineer?")
]

print("Sending request to OpenRouter...")
response = chat.invoke(messages)
print("SUCCESS!")
print("Response:", response.content)
