import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('text-davinci-003')  # Consider a model trained on educational content

def kalvi_chat(question):
  """
  Processes user questions and retrieves responses from the Kalvi chatbot model.
  """
  chat = model.start_chat(history=[])
  response = chat.send_message(question)
  return response.text

st.title("கல்வி (Kalvi) - உங்கள் தமிழ் கல்விக்கான துணை (Your Tamil Learning Companion)")

user_input = st.text_input("உங்கள் கேள்வியைக் கேளுங்கள் (Ask your question)", key="user_input")

if user_input:
  response = kalvi_chat(user_input)
  st.write(f"கல்வி (Kalvi): {response}")

