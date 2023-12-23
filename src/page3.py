import streamlit as st
from openai import OpenAI
import logging
            
def page3():
    st.title("Image Generation")
    st.info("""NOTE: You can download the image by right clicking on it and selecting 'Save image.'""")

    logging.basicConfig(level=logging.DEBUG)

    with st.sidebar:
        st.title('OpenAI Chatbot: Peppa Pig GPT 🐷')
        api_key3 = st.text_input('Enter OpenAI API key:', type='password')
        if not (api_key3.startswith('sk-') and len(api_key3)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
            client = OpenAI(
                    api_key = api_key3
                    )
        
    with st.form(key='image_generation_form'):
        prompt = st.text_input("Enter a prompt for image generation:", key='page3_chat_input')
        generate_button = st.form_submit_button("Generate Image")

    if generate_button and prompt:
        img_response = client.images.generate(
                        model="dall-e-2",
                        prompt="{}".format(prompt),
                        quality="standard",
                        n=1,
                    )
        logging.debug(img_response)
            
        try:
            img_url = img_response.data[0].url
            logging.debug(f"Image URL: {img_url}")
            st.image(img_url, caption=f"Generated image")
    
        except (IndexError, KeyError, TypeError) as e:
            logging.error(f"Error retrieving image URL: {e}")
            st.warning("No image generated for the given prompt.")
        
    else:
        st.warning("Please enter a prompt to generate an image.")

