from google import genai
from google.genai import types

# from learning.d import model

client=genai.Client(api_key='AQ.Ab8RN6IaWEsxykXziOyZ-pKkxHVVa89l18agC6nNbCeFEPcB-w')
response=client.models.generate_content(
    model="gemini-3.5-flash",
    contents="tell me the root of  50394"



)
print(response.text)





# there is something else if yo are interested which is streaming or chunking
# for big answers you do  generate_content_streaming+
# you hide the print respone and do for x in response print x  or x.text









#