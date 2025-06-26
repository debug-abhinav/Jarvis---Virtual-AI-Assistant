from google import genai

client = genai.Client(api_key="GEMINI API KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="What is Coding?"
)
print(response.text)