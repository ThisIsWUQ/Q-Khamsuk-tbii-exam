import streamlit as st
import datetime
import pandas as pd
from helpers import connect_to_collection

def registration_page():
    placeholder = st.empty()

    with placeholder.form("Registration"):
        username = st.text_input("User Name")
        password = st.text_input("Password", type="password")
        repeat_password = st.text_input("Repeat Password", type="password")
        age = st.number_input("Enter Age", min_value=18, step=1)
        pet = st.text_input("What is Your Favorite Pet?")
        button_submit = st.form_submit_button("Register")

    if button_submit:
        # connect to collection
        db = 'streamlit'
        collection_name = 'user'  # a collection can also be created from here
        collection = connect_to_collection(db, collection_name)

        # get data from MongoDB as a dataframe
        user_data = pd.DataFrame(list(collection.find()))
        users = list(user_data.user_name)

        if password != repeat_password:
            st.warning("PASSWORDS DON'T MATCH", icon="!")
        elif len(username) < 1 and len(password) < 1:
            st.error("ENTER USERNAME AND PASSWORD")
        elif username in users:
            st.error("THIS USER NAME EXIST!")
        else:
            # create a document with the data
            document = {
                "user_name": username,
                "password": password,
                "age": age,
                "pet": pet,
                "created_at": datetime.datetime.now()
            }

            # write this document to the collection
            collection.insert_one(document)

            # clear the widgets
            placeholder.empty()
            # option 2,
            st.title(f"Welcome New User")
            # place an image
            st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGpubGNsZnI5cXJicjNpcXBkNGFzNWFjNW1rdHJ4ZnJmbWpkeDhicCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/NTsD5QdhUOrEyU3TGC/giphy.gif")
