from google import genai
from google.genai import types
import os
history=[] # i made this variable so it can give gemini the full history so it dont forget the context
# cv=[] # i made this so i upload all cvs at ones

client= genai.Client(api_key="AQ.Ab8RN6KhjxKUCdp4gEHQ-kdxQrDAMpKNKYFZLXpy453KKc1hFQ")# api key
folder=r"C:\Users\yousi\Downloads\cv's" # the path for the folder




for file in os.listdir(folder): #os.listdir list everything inside that and  loop over it
        path = os.path.join(folder, file) # here where we join the full path for gemini not just name x.pdf

        pdf = client.files.upload(file=path, config=types.UploadFileConfig(
            display_name=file))  # here is where we upload it to gemini
        # cv.append(pdf)# we append to cv to make a list and upload it ones to cv not 50 upload
        history.append(f"The following resume file is named: {file}")
        history.append(pdf)# adding to history


    #normal part for  asking  gemini
ask=input("what is your question?")
history.append(ask)
with open("questions.txt", "w") as file:
    file.write(ask)
response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=history,
        config=types.GenerateContentConfig(
            temperature=0,
            system_instruction="if i asked you to give me the best fit  then (Choose 3 candidates and give a brief introduction of each. Refer to each candidate by their file's display name, not by job title or position) else if i asked you any other question answer that question and dont give me three candite"
        )

    )
print(response.text)
history.append(response.text)





