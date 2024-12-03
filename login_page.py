
import streamlit as st
import pandas as pd
from registration_page import registration_page
from helpers import connect_to_collection

placeholder = st.empty()
# Do not move to the next section until credential check flag becomes true
credentials_check = False

with placeholder.form("Login"):
    username = st.text_input("User Name", placeholder="Please enter your user name")
    password = st.text_input("Password", placeholder="Please enter your password", type="password")

    button_login = st.form_submit_button("login")
    button_register = st.form_submit_button("register")

if button_login:
    # define the database and the collection
    db_name = 'streamlit'
    collection_name = 'user'
    # connect to collection
    collection = connect_to_collection(db_name, collection_name)

    # check username
    # read the data from the collection and identify usernames
    user_data = pd.DataFrame(list(collection.find()))
    user_names = list(user_data.user_name)

    # check password
    if username in user_names:
        # this selects the password of the user that is entering information
        registered_password = list(user_data[user_data.user_name == username].password)[0]

        if password == registered_password:
            credentials_check = True
        else:
            st.error("The username/password is not correct")
    else:
        st.error("Please provide correct user name or click on register as new user")

if button_register:
    placeholder.empty()
    registration_page()


