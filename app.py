from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie


# Place to get emoji: https://www.webfx.com/tools/emoji-cheat-sheet/

# Set page title and icon
st.set_page_config(page_title="Streamlit practice", page_icon=":white_heart:", layout="wide")


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# LOAD ASSETS
lottie_coding = load_lottie_url("https://lottie.host/62013d2e-48d1-4ef4-bc3e-0321fd4b79a5/UtvKT2CFVx.json")
img_anime = Image.open("images/anime.jpg")
img_anime2 = Image.open("images/anime2.jpg")

# Text input
title = st.text_input('Movie title', '')
st.write('The current movie title is', title)

# Header Section
with st.container():
    st.subheader("Hi, I am a Subheader :wave:")
    st.title("Streamlit Practice")
    st.write("This is a practice app to learn Streamlit")
    st.write("[Learn More >](https://streamlit.io)")

# What I Do
with st.container():
    st.write("---")  # dashed line break
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do :smile:")
        st.write("##")  # Spacing
        st.write(
            """
            Hey man, My name is wasif nadeem and I am a Data Science student. I am learning Streamlit to create web apps.
            - I am a Data Science student
            - I am learning Streamlit
            - I am creating web apps
            - I am learning to deploy web apps

            Haha That's it for now. I will update this section later.
            """
        )
        st.write("[To Know More >](https://wasif-portfolio.netlify.app/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# Projects
with st.container():
    st.write("---")  # dashed line break
    st.header("My Projects :computer:")
    st.write("##")  # Spacing
    image_column, text_column = st.columns((1, 2)) # Text column get more space
    with image_column:
        st.image(img_anime)
    with text_column:
        st.subheader("Project 1")
        st.write("""
        This is a project 1. I am learning to create web apps using Streamlit. 
        I will update this section later.
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        """
        )
        st.markdown("[YouTube Link >](https://www.youtube.com/watch?v=VqgUkExPvLY)")

with st.container():
    st.write("---")  # dashed line break
    st.header("My Projects :computer:")
    st.write("##")  # Spacing
    image_column, text_column = st.columns((1, 2)) # Text column get more space
    with image_column:
        st.image(img_anime2)
    with text_column:
        st.subheader("Project 2")
        st.write("""
        This is a project 2. I am learning to create web apps using Streamlit. 
        I will update this section later.
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        """
        )
        st.markdown("[YouTube Link >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
