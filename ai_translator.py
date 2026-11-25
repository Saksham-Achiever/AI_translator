import streamlit as st 
import streamlit as st 
from google import genai
from dotenv import load_dotenv
load_dotenv()
client = genai.Client()
model_list=["gemini-3.1-flash-lite","gemini-3.5-flash-lite","gemini-4-hydrogen"]


st.set_page_config(page_title="ai translator",page_icon="🌎")

import streamlit as st

st.set_page_config(page_title="AI Translator", layout="wide")

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&family=Plus+Jakarta+Sans:wght@600&display=swap');

        .minimal-web-title {
            padding: 0.4rem 0 0.95rem 0;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid rgba(186, 230, 253, 0.25);
            position: relative;
        }

        .minimal-web-title::after {
            content: "";
            position: absolute;
            left: 0;
            bottom: -1px;
            width: 110px;
            height: 2px;
            background: linear-gradient(90deg, #93C5FD, #FFFFFF);
            box-shadow: 0 0 12px rgba(147, 197, 253, 0.8);
            border-radius: 999px;
        }

        .minimal-web-title h1 {
            margin: 0;
            line-height: 1.1;
            font-size: clamp(1.9rem, 3.8vw, 2.6rem);
        }

        .minimal-ai {
            font-family: 'Instrument Serif', serif;
            font-style: italic;
            font-weight: 400;
            color: #93C5FD;
            text-shadow: 0 0 16px rgba(147, 197, 253, 0.65);
            padding-right: 0.14em;
        }

        .minimal-word {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 600;
            letter-spacing: -0.03em;
            color: #FFFFFF;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.22);
        }
    </style>

    <header class="minimal-web-title">
        <h1><span class="minimal-ai">AI</span><span class="minimal-word">Translator</span></h1>
    </header>
    """,
    unsafe_allow_html=True,
)
col1 , col2 , col3 = st.columns([5,1,5])

#st.caption("total characters:"+ str(len(text)))
languages=[ "English","Marathi","Hindi", "Spanish", "French", "German", "Italian", "Portuguese", "Dutch", "Swedish", "Norwegian", "Danish" ]
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
        st.text_area("Translation",value=response.output_text,key=1,placeholder="Hello, how are you mate?",max_chars=200)
