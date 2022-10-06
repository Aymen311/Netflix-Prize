import streamlit as st
import pandas as pd
import numpy as np
import time
import hashlib
import base64
import random

def add_bg_from_local(image_file):
  
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )    

def flag_verifyer(username, pswd):
  if (username and pswd ):
    with st.spinner('Please wait...'):
      time.sleep(random.randint(3,10))
      if username=="CyberErudites" and pswd==hashlib.md5(b"129349").hexdigest():
        st.write("CyberErudites{5t4ti5tic4l_d3an0nymiz4ti0n_4tt4ck5_4r3_4_r34l_thr34t}")
      else :
        st.warning("Login failed!")


def main():
  st.title("Welcome to Netflix")
  add_bg_from_local("/home/bert/GDG/GDG-CTF/challenges/Quantasmania/Netflix-Background.jpg")
  username = st.text_input("Username")
  pswd = st.text_input("MD5 of userId", type="password")
  st.button("Log in", on_click=flag_verifyer(username, pswd))
if __name__ == "__main__":
  main()