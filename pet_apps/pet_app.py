import streamlit as st
import time # for more control of the app's sequence
import requests


def get_cat_image():
    url = "https://cataas.com//cat"
    contents = requests.get(url)

    return contents.content


def get_dog_image_url():
    url = "https://random.dog/woof.json"
    contents = requests.get(url).json()
    dog_image_url = contents['url']

    return dog_image_url

st.header("Welcome to My Pet App", divider="rainbow")

c1, c2 = st.columns(2)

with c1:
    button_cat = st.button("Click Here to See My Cat")

    if button_cat:
        image_cat = get_cat_image()
        st.image(image_cat, width=300, caption="This is my cat :)")
        #st.write("place a cat image")


with c2:
    button_dog = st.button("Click Here to See My Dog")

    if button_dog:
        image_dog_url = get_dog_image_url()

        while image_dog_url[-4:] == ".mp4":
            image_dog_url = get_dog_image_url()
        st.image(image_dog_url, width=300, caption="This is my dog :)")