import streamlit as st
from openai import OpenAI
import time
import json   

def page2():
    st.title("Text and Audio Generation")
    st.info("""NOTE: You can converse with the chatbot here and have audio files generated for the response simultaneously. The audio files will be visible only until the next prompt is provided. To access it later, you can donwlowd it. You can also set the playback speed accordingly.""")

    with st.sidebar:
        st.title('OpenAI Chatbot: Peppa Pig GPT 🐷')
        if 'OPENAI_API_KEY' in st.secrets:
            st.success('API key already provided!', icon='✅')
            api_key2 = st.secrets['OPENAI_API_KEY']
            client = OpenAI(
                    api_key = api_key2
                    )

        else:
            api_key2 = st.text_input('Enter OpenAI API key:', type='password')
            if not (api_key2.startswith('sk-') and len(api_key2)==51):
                st.warning('Please enter your credentials!', icon='⚠️')
            else:
                st.success('Proceed to entering your prompt message!', icon='👉')
                client = OpenAI(
                    api_key = api_key2
                    )

    def load_conversation_history():
        try:
            with open("conversation_history.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_conversation_history(history):
        with open("conversation_history.json", "w") as file:
            json.dump(history, file)

    conversation_history = load_conversation_history()

    for message in conversation_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"]) 

    if prompt := st.chat_input("What's up?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        conversation_history.append({"role": "user", "content": prompt})
    
        if prompt:
            response = client.chat.completions.create(model="gpt-3.5-turbo",
                            messages=[
                                {
                                    "role": m["role"], 
                                    "content": m["content"]
                                } 
                                for m in conversation_history],
                            stream=True, 
                            temperature=1, 
                            max_tokens=1000, 
                            top_p=1, 
                            frequency_penalty=0, 
                            presence_penalty=0)
        
            chatbot_responses = []

            for msg in response:
                if msg.choices and msg.choices[0].delta and msg.choices[0].delta.content:
                    chatbot_responses.append(msg.choices[0].delta.content)

            full_chatbot_response = ' '.join(chatbot_responses)
            conversation_history.append({"role": "assistant", "content": full_chatbot_response})

            if full_chatbot_response:
                with st.chat_message("assistant"):
                    st.markdown(full_chatbot_response)  
                    if len(full_chatbot_response)>0:
                        timestamp = str(int(time.time()))
                        speech_response = client.audio.speech.create(
                            model="tts-1",
                            voice="shimmer",
                            input=full_chatbot_response
                            )   
                    
                        audio_file_path = f"speech_output_{timestamp}.mp3"
                        speech_response.stream_to_file(audio_file_path)
                        st.audio(audio_file_path, format='audio/mp3')

            save_conversation_history(conversation_history)
