# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:19:00 2024

@author: giuga
"""

from tool_functions.imports_ import *

st.set_page_config(
    page_title="Giulio_Garnier_portfolio",
    page_icon="👋",
)

# Functions for animations
import json #because the lottie animation are in json format

import requests
from streamlit_lottie import st_lottie


def load_lottieur(url:str): #load animation from the web
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieur("https://lottie.host/817fbd08-7a7c-42ef-882f-b3b3e5b5e28d/cH5QdYoi4M.json")




def app():
    col_text_intro, col_image_hello = st.columns([1,1])

    with col_text_intro:
       st.title("Welcome to my portfolio 🎉")
       st.write("Hey there !:wave:")
       st.write("My name is Giulio Garnier and welcome to my portfolio ! The goal of this portfolio is to present my self and some of my informatic skills.Feel free to navigate in the differents pages in the sidebar or with the menu")

    
    with col_image_hello:
      st_lottie(lottie_hello,key="hello")
      
    st.markdown("""
                #### The librairies that i used to make this portfolio are:
                - [streamlit.io](https://streamlit.io)
                - [streamlit-lottie](https://github.com/andfanilo/streamlit-lottie)
                - [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu)
             """) #Faire attention que les # soit alignés avec les -
             
app()
    
