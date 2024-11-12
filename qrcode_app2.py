import streamlit as st
from qrcode_generator_page import generate_qrcode_page
from decode_qrcode_page import decode_qrcode

st.set_page_config(page_title="My QR Code App",
                   page_icon=":white_check_mark:")

options = ['Create QR Code', 'Decode QR Code', 'About Me']
page_selection = st.sidebar.selectbox("Menu", options)

st.write(page_selection)

if page_selection == 'Create QR Code':
    generate_qrcode_page()
elif page_selection == 'Decode QR Code':
    decode_qrcode()
elif page_selection == 'About Me':
    st.write("Hi, I am a cat")
