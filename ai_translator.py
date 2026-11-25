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

st.markdown("""
<div style="text-align:center; padding:20px 0;">
<pre style="
    font-family: 'Courier New', monospace;
    font-size: 1.8rem;
    line-height: 1.4;
    display: inline-block;
    background: linear-gradient(180deg, #1a0a00, #0d0d0d);
    border-radius: 14px;
    padding: 22px 30px;
    border: 3px double #ff6a00;
">
<span style="color:#ff6a00;"> ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ </span>
<span style="color:#ffffff;">  █   █     █     </span>
<span style="color:#ffffff;">  █   █     █     </span>
<span style="color:#ffffff;">  █   █     █     </span>
<span style="color:#ffffff;">  █   █     █     </span>
<span style="color:#ffffff;"> ▀▀▀▀▀ ▀▀▀▀▀ ▀▀▀▀▀ </span>
</pre>
<h1 style="
    font-size: 2.4rem; font-weight: 900; margin: 12px 0 4px;
    background: linear-gradient(90deg, #ff6a00, #fff, #ff6a00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 4px;
">AI TRANSLATOR</h1>
<p style="color:#888; font-size:1rem;">~ Breaking Language Barriers ~</p>
</div>
""", unsafe_allow_html=True)
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
