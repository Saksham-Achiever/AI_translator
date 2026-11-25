import streamlit as st 
import streamlit as st 
from google import genai
from dotenv import load_dotenv


client = genai.Client()
model_list=["gemini-3.1-flash-lite","gemini-3.5-flash-lite","gemini-4-hydrogen"]


st.set_page_config(page_title="ai translator",page_icon="🌎")

import streamlit as st

st.set_page_config(page_title="AI Translator", layout="wide")

import streamlit as st

import streamlit as st

import streamlit as st

    
import streamlit as st

st.markdown("""
<div style="text-align:center; padding:24px 0;">
<pre style="
    font-family: 'Courier New', monospace;
    font-size: 2rem;
    font-weight: bold;
    line-height: 1.2;
    display: inline-block;
    color: #c9956b;
">
  ██╗  ██╗   ██████╗   █████╗
  ██║  ██║  ██╔═══██╗ ██╔══██╗
  ███████║  ██║   ██║ ███████║
  ██╔══██║  ██║   ██║ ██╔══██║
  ██║  ██║  ╚██████╔╝ ██║  ██║
  ╚═╝  ╚═╝   ╚═════╝  ╚═╝  ╚═╝
</pre>
<h1 style="
    font-size: 2.6rem; font-weight: 900; margin: 10px 0 4px;
    color: #e8c9a0;
    letter-spacing: 2px;
">AI TRANSLATOR</h1>
<p style="
    color: #8b7355; font-size: 1rem; letter-spacing: 2px;
    margin-bottom: 20px; font-family: monospace;
">Translate in any language</p>

<p style="
    color: #6b5b4a; font-size: 0.9rem; margin: 0;
    letter-spacing: 0.5px;
">
    Made by ChammChamm· FY Student, YCCE CSE
</p>
</div>
""", unsafe_allow_html=True)       
col1 , col2 , col3 = st.columns([5,1,5])

#st.caption("total characters:"+ str(len(text)))
languages=[ "English", "Mandarin Chinese", "Hindi", "Spanish", "French",
    "Arabic", "Bengali", "Russian", "Portuguese", "Urdu",
    "Indonesian", "German", "Japanese", "Swahili", "Turkish",
    "Marathi", "Telugu", "Tamil", "Punjabi", "Italian",
    "Korean", "Vietnamese", "Persian Farsi", "Hausa", "Thai",
    "Gujarati", "Kannada", "Malay", "Dutch", "Greek",
    "Hebrew", "Polish", "Czech", "Romanian", "Hungarian",
    "Zulu", "Xhosa", "Amharic", "Pashto", "Sinhala",
    "Burmese", "Nepali", "Serbian", "Croatian", "Bulgarian",
    "Slovak", "Ukrainian ", "Kazakh", "Mongolian", "Armenian"]
with col1:
    source_language=st.selectbox("From:",languages)
with col2:
    st.write(" ")
    st.write(" ")
    swap=st.button("🔄")
with col3:
    Target_language=st.selectbox("To:",languages, index=1)
left,right =st.columns(2)
with left:

    text=st.text_area(" ",placeholder="Hello, how are you mate?",max_chars=200)
    

system_prompt=f"""you are a experienced translator withover 
15 years of experience. your sole job is to translate in a 
language that user selects, pay close attention to grammar 
and punctuation the target language is {Target_language} do not act like generative ai give only translation and nothing else"""
model=st.radio("choose model",model_list)
if st.button("Translate"):
    with st.spinner("Translating..."):
        response = client.interactions.create(
            model=model,
            system_instruction=system_prompt,
            input=text
        )
    with right:
        st.text_area("Translation",value=response.output_text,key=2,placeholder="Hello, how are you mate?",max_chars=200)
