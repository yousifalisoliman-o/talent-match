from google import genai
from google.genai import types

api_key   = 'AQ.Ab8RN6IaWEsxykXziOyZ-pKkxHVVa89l18agC6nNbCeFEPcB-w'
llm_model = "gemini-3.5-flash"
query="tell me the root of  50394"

# Connect to Gemini API
client=genai.Client(api_key=api_key)

# Get the response using the llm model
response=client.models.generate_content(
    model=llm_model,
    contents=query
)
print(response.text)
