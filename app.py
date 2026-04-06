import streamlit as st
from realtime_voice import start_voice_agent
from ingest import ingest_document

st.title("Voice AI Knowledge Assistant")

uploaded_file = st.file_uploader("Upload Knowledge PDF")

if uploaded_file:

    path = f"documents/{uploaded_file.name}"

    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    ingest_document(path)

    st.success("Document indexed successfully")

if st.button("Start Voice Assistant"):

    st.write("Assistant running in terminal")

    start_voice_agent()
