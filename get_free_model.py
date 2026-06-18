import requests
import json

response = requests.get("https://openrouter.ai/api/v1/models")
data = response.json()

free_models = []
for m in data.get("data", []):
    pricing = m.get("pricing", {})
    if pricing.get("prompt") == "0" and pricing.get("completion") == "0":
        free_models.append(m["id"])

print("Found free models:", free_models[:20])
