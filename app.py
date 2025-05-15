import streamlit as st
from main import process_user_query

st.title("AI Crypto Assistant")
query = st.text_input("Enter your question:")

if st.button("Ask"):
    with st.spinner("Generating response..."):
        answer = process_user_query(query)
        st.success(answer)
