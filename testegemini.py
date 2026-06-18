import google.genai as genai

# Configure com sua chave
client = genai.Client(api_key="AIzaSyCSMNyij7Ez7Qi5OQqiZN9QJAINc_n6oIM")

# response = client.models.list(config={'page_size': 5, 'query_base': True})
client.models.list
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
