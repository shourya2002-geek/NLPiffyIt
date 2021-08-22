import streamlit as st 
import spacy_streamlit
import spacy
nlp = spacy.load('en_core_web_sm')
import spacy_streamlit
from spacy_streamlit import visualize_parser
import os
from PIL import Image

def print(doc):
    return 



def app():
    st.subheader("Tokenization")
    docx = nlp(st.session_state)
    spacy_streamlit.visualize_tokens(docx,attrs=['text','pos_','dep_','ent_type_'])

    if st.button("Visualize Dependencies"):
        doc = nlp(st.session_state)
        
        visualize_parser(doc)

    