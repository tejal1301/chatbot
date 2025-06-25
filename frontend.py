import streamlit as st
import backend as bk

st.title("Gen AI Project")
input = st.text_input("INPUT")
go_button = st.button("Go")

if go_button:
 output = bk.get_text_stream_output(input)
 st.write(output)