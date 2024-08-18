from decouple import config
import os
import google.generativeai as genai

G_API_KEY= config('G_API_KEY')
genai.configure(api_key=G_API_KEY)

# function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question)
    return response.text


# get_gemini_response("Good morning")