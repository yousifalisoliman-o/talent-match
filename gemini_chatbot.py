from google import genai
from google.genai import types
from PIL import Image


client = genai.Client(api_key="AQ.Ab8RN6IaWEsxykXziOyZ-pKkxHVVa89l18agC6nNbCeFEPcB-w")


image = Image.open("As.png")
history=[]
while True:
    user = input("Enter your question: ")
    if user=="exit":
        break
    history.append(user)
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[user, image, history],
        config=types.GenerateContentConfig(
            temperature=2.0,
            system_instruction="be funny throw a joke every 10 words , response must be under 50 words"
        )
    )
    print(response.text)
    history.append(response.text)

