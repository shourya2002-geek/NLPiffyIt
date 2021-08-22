from deep_translator import GoogleTranslator
import streamlit as st


def app():

    st.header('Translate')
    option = st.selectbox('Choose the Target Language',("English","Hindi","Spanish","French","German","Chinese"))
    st.subheader('Translated Text')

    if option == "English":
        translated = GoogleTranslator(source='auto', target='en').translate(st.session_state) 
        st.write(translated)

    if option == "Hindi":
        translated = GoogleTranslator(source='auto', target='hi').translate(st.session_state) 
        st.write(translated)

    if option == "Spanish":
        translated = GoogleTranslator(source='auto', target='es').translate(st.session_state) 
        st.write(translated)
    if option == "French":
        translated = GoogleTranslator(source='auto', target='fr').translate(st.session_state) 
        st.write(translated)
    if option == "German":
        translated = GoogleTranslator(source='auto', target='de').translate(st.session_state) 
        st.write(translated)
    if option == "Chinese":
        translated = GoogleTranslator(source='auto', target='zh').translate(st.session_state) 
        st.write(translated)            
    if option == "Italian":
        translated = GoogleTranslator(source='auto', target='it').translate(st.session_state) 
        st.write(translated) 
    
    