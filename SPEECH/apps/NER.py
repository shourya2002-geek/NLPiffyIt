import streamlit as st
import spacy_streamlit
import nltk
from nltk.corpus import stopwords
import spacy
import os
from PIL import Image
from gensim.summarization import summarize
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from spacy import displacy
nlp = spacy.load('en_core_web_sm')




def text_analyzer(my_text):
	
	docx = nlp(my_text)
	# tokens = [ token.text for token in docx]
	allData = [('"Token":{},\n"Lemma":{}'.format(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop))for token in docx ]
	return allData

def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result
	



def app():

	st.subheader("Named Entity Recognition")
	
	docx = nlp(st.session_state)
	spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)


	

	

	
	


	
			

	