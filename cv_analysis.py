from google import genai
from google.genai import types
import os
history=[] # i made this variable so it can give gemini the full history so it dont forget the context
cv=[] # i made this so i upload all cvs at ones

client= genai.Client(api_key="AQ.Ab8RN6IZ-Pzl6IQEpaRQjnd9uRsswS4KjizvFrNeEnbqbOPxLA")# api key
folder=r"C:\Users\yousi\Downloads\cv's" # the path for the folder


while True: # the loop that will keep it continuing


    for file in os.listdir(folder): #os.listdir list everything inside that and  loop over it
        path = os.path.join(folder, file) # here where we join the full path for gemini not just name x.pdf

        pdf = client.files.upload(file=path)# here is where we upload it to gemini
        cv.append(pdf)# we append to cv to make a list and upload it ones to cv not 50 upload
        history.append(pdf)# adding to history


    #normal part for  asking  gemini
    ask=input("what is your question?")
    history.append(ask)
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[ask,history,cv],
        config=types.GenerateContentConfig(
            temperature=0,
            system_instruction="no asterisk + tell me at the bottom how many cv you got and the exact time you took to analyze your question"
        )

    )
    print(response.text)
    history.append(response.text)


