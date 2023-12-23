import streamlit as st

introduction = """
About Peppa Pig GPT (3-in-1) Model 🐷:

### Use of OpenAI
Built using OpenAI APIs for text, image and speech generation, this model has been designed to:
1. Act as a conversational agent
2. Generate audio files from the responses it gives
3. Generate images from the prompts given to it

It has been built mainly using Streamlit Library, along with the OpenAI class from openai libary.
For accessing this this web application, you have to:
1. Visit https://platform.openai.com/api-keys  
2. Click on 'New Key' to generate an API key to enter into the prompt for the API key. 
Make an account on https://platform.openai.com before generating an API key, if not made yet. 
$5 credits will be given for free.

"""

def page1():
    st.title("Peppa Pig GPT")
    st.markdown(introduction)