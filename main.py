import streamlit as st
from src.page1 import page1
from src.page2 import page2
from src.page3 import page3

pages = {
    "Home Page": page1,
    "Text and Audio Generation": page2,
    "Image Generation": page3,
}

page = st.sidebar.selectbox("Select a page", list(pages.keys()))
pages[page]()
