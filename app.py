import openai

openai.api_key = "YOUR_API_KEY"

prompt = "What are the symptoms of COVID-19?"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024
)

print(response["choices"][0]["text"])
