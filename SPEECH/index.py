import streamlit as st
from multiapp import MultiApp
from apps import main,NER,translate,token,sentiment

app = MultiApp()   

app.add_app("Upload", main.app)
app.add_app("Translate", translate.app)
app.add_app("NER", NER.app)
app.add_app("Tokenization and Lemmatization", token.app)





app.run() 